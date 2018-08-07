#######################################################################
#Import Modules Section
import xbmc
import xbmcgui
import xbmcaddon
import base64
#######################################################################

#######################################################################
# YouTube API Settings
DATA_API      = base64.b64decode(b'QUl6YVN5QTRrdENoN3RMQms0NjdBWWdQTXlrZ2R0TVo4SEw2OGhF')
DATA_CLIENT   = base64.b64decode(b'MTgzMTY1MzQzMjQ0LWJuZTBycmlkYTdndThkMnMyaGkxcjBrbWgzZzVjdWVhLmFwcHMuZ29vZ2xldXNlcmNvbnRlbnQuY29t')
DATA_SECRET   = base64.b64decode(b'MWN3c2stVm85bXRRMWhSdUlMLTdQdWdG')
#######################################################################

def Apply_API():
    __settings__ = xbmcaddon.Addon(id='plugin.video.youtube')
    __settings__.setSetting("youtube.api.enable", 'true')
    __settings__.setSetting("youtube.api.last.switch", 'own')
    __settings__.setSetting("youtube.api.key", DATA_API)
    __settings__.setSetting("youtube.api.id", DATA_CLIENT)
    __settings__.setSetting("youtube.api.secret", DATA_SECRET)
    ytDialog = xbmcgui.Dialog()
    ytDialog.ok('Jamzz', '[COLOR red]YouTube API Keys Set To Jamzz[/COLOR]')