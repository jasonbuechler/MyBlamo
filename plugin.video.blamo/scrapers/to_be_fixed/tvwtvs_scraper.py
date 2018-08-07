"""
    Death Streams Addon
    Copyright (C) 2014 Mr Blamo.Blamo

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
import re
import urlparse

import dom_parser
import kodi
import log_utils  # @UnusedImport
from deaths_lib import scraper_utils
from deaths_lib.constants import FORCE_NO_MATCH
from deaths_lib.constants import QUALITIES
from deaths_lib.constants import VIDEO_TYPES
import scraper


BASE_URL = 'http://series.tv'
LINK_URL = '/plugins/gkpluginsphp.php'

class TVWTVS_Scraper(scraper.Scraper):
    base_url = BASE_URL

    def __init__(self, timeout=scraper.DEFAULT_TIMEOUT):
        self.timeout = timeout
        self.base_url = kodi.get_setting('%s-base_url' % (self.get_name()))

    @classmethod
    def provides(cls):
        return frozenset([VIDEO_TYPES.TVSHOW, VIDEO_TYPES.EPISODE])

    @classmethod
    def get_name(cls):
        return 'TVWTVS'

    def resolve_link(self, link):
        return link

    def format_source_label(self, item):
        label = '[%s] %s' % (item['quality'], item['host'])
        return label

    def get_sources(self, video):
        source_url = self.get_url(video)
        hosters = []
        sources = {}
        if source_url and source_url != FORCE_NO_MATCH:
            page_url = urlparse.urljoin(self.base_url, source_url)
            html = self._http_get(page_url, cache_limit=.5)
            sources.update(self.__get_gk_links(html, page_url))
            sources.update(self.__get_iframe_links(html, page_url))
            
            for source in sources:
                host = self._get_direct_hostname(source)
                stream_url = source + '|User-Agent=%s' % (scraper_utils.get_ua())
                hoster = {'multi-part': False, 'host': host, 'class': self, 'quality': sources[source], 'views': None, 'rating': None, 'url': stream_url, 'direct': True}
                hosters.append(hoster)
    
        return hosters

    def __get_iframe_links(self, html, page_url):
        sources = {}
        urls = dom_parser.parse_dom(html, 'iframe', ret='data-lazy-src') + dom_parser.parse_dom(html, 'iframe', ret='src')
        for iframe_url in urls:
            headers = {'Referer': page_url}
            html = self._http_get(iframe_url, headers=headers, cache_limit=0)
            for match in re.finditer('"file"\s*:\s*"([^"]+)"\s*,\s*"label"\s*:\s*"([^"]+)', html, re.DOTALL):
                stream_url, height = match.groups()
                stream_url = re.sub('; .*', '', stream_url)
                if self._get_direct_hostname(stream_url) == 'gvideo':
                    quality = scraper_utils.gv_get_quality(stream_url)
                else:
                    quality = scraper_utils.height_get_quality(height)
                sources[stream_url] = quality
        return sources
    
    def __get_gk_links(self, html, page_url):
        sources = {}
        match = re.search('{link\s*:\s*"([^"]+)', html)
        if match:
            data = {'link': match.group(1)}
            url = urlparse.urljoin(self.base_url, LINK_URL)
            headers = {'Referer': page_url}
            html = self._http_get(url, data=data, headers=headers, cache_limit=.25)
            js_data = scraper_utils.parse_json(html, url)
            if 'link' in js_data:
                for link in js_data['link']:
                    if 'type' in link and link['type'] == 'mp4' and 'link' in link:
                        if self._get_direct_hostname(link['link']) == 'gvideo':
                            quality = scraper_utils.gv_get_quality(link['link'])
                        elif 'label' in link:
                            quality = scraper_utils.height_get_quality(link['label'])
                        else:
                            quality = QUALITIES.HIGH
                        sources[link['link']] = quality
        return sources
                            
    def get_url(self, video):
        return self._default_get_url(video)

    def _get_episode_url(self, show_url, video):
        results = self.__search(video.video_type, '', video.year)
        for result in results:
            if result['url'].startswith(show_url) and re.search('\s+season\s+%s( |$)' % (video.season), result['title'], re.I):
                return self.__find_episode(result['url'], video.episode)
                        
    def __find_episode(self, url, episode):
        url = urlparse.urljoin(self.base_url, url)
        html = self._http_get(url, cache_limit=2)
        fragment = dom_parser.parse_dom(html, 'ul', {'class': '[^"]*listing-videos[^"]*'})
        if fragment:
            for match in re.finditer('href="([^"]+)[^>]+>(.*?)</a>', fragment[0]):
                url, label = match.groups()
                label = re.sub('</?[^>]*>', '', label)
                if re.search('\s+Episode\s+%s( |$)' % (episode), label):
                    return scraper_utils.pathify_url(url)
                
    def __get_pages(self, url):
        pages = []
        url = urlparse.urljoin(self.base_url, url)
        html = self._http_get(url, cache_limit=2)
        fragment = dom_parser.parse_dom(html, 'div', {'class': 'pagination'})
        if fragment:
            pages = dom_parser.parse_dom(fragment[0], 'a', ret='href')
        return pages
    
    def search(self, video_type, title, year, season=''):
        results = self.__search(video_type, title, year)
        results = [result for result in results if not re.search('season[- ]\d+', result['url'], re.I)]
        return results

    def __search(self, video_type, title, year):
        url = urlparse.urljoin(self.base_url, '/categoryy')
        html = self._http_get(url, cache_limit=48)
        results = []
        norm_title = scraper_utils.normalize_title(title)
        fragment = dom_parser.parse_dom(html, 'div', {'class': 'tagindex'})
        if fragment:
            for match in re.finditer('href="([^"]+)[^>]+>(.*?)</a>', fragment[0]):
                url, match_title = match.groups()
                match_title = re.sub('\s+\(\d+\)$', '', match_title)
                match_title = match_title.replace('&amp;', '&')
                if norm_title in scraper_utils.normalize_title(match_title):
                    result = {'url': scraper_utils.pathify_url(url), 'title': match_title, 'year': ''}
                    results.append(result)

        return results