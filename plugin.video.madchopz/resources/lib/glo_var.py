#######################################################################
 # ----------------------------------------------------------------------------
 # "THE BEER-WARE LICENSE" (Revision 42):
 # @tantrumdev wrote this file.  As long as you retain this notice you
 # can do whatever you want with this stuff. If we meet some day, and you think
 # this stuff is worth it, you can buy me a beer in return. - Muad'Dib
 # ----------------------------------------------------------------------------
#######################################################################

# Addon Name: MaD ChopZ
# Addon id: plugin.video.madchopz
# Addon Provider: Rohas

#######################################################################
#Import Modules Section
import xbmc
import xbmcgui
import xbmcaddon
import xbmcplugin
import xbmcvfs
import os
import sys
#######################################################################

#######################################################################
# Primary Addon Variables 
AddonID             = xbmcaddon.Addon().getAddonInfo('id')
THISADDON           = xbmcaddon.Addon(id=AddonID)
ADDON_ID            = xbmcaddon.Addon().getAddonInfo('id')
URL                 = 'http://simplebuilds.net/tube/'
ADDONTITLE          = 'MaD ChopZ'
USER_AGENT          = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:18.0) Gecko/20100101 Firefox/18.0'
#######################################################################

#######################################################################
# Path Variables
HOMEPATH            = xbmc.translatePath('special://home/')
ADDONSPATH          = os.path.join(HOMEPATH, 'addons')
USERDATAPATH        = os.path.join(HOMEPATH, 'userdata')
ADDONDATAPATH       = xbmc.translatePath(os.path.join(USERDATAPATH, 'addon_data'))
LOGPATH             = xbmc.translatePath('special://logpath/')
IHADDONPATH         = os.path.join(ADDONSPATH, ADDON_ID)
IHDATAPATH          = os.path.join(ADDONDATAPATH, ADDON_ID)
YTADDONPATH         = os.path.join(ADDONSPATH, 'plugin.video.youtube')
YTADDONDATAPATH     = os.path.join(ADDONDATAPATH, 'plugin.video.youtube')
#######################################################################

#######################################################################
# Filename Variables 
BASEURL             = URL
MAINMENUFILE        = BASEURL + 'mainmenu.txt'
NEWSFILE            = BASEURL + 'news.xml'
#######################################################################

#######################################################################
# Artwork Variables 
DEFAULTICON         = os.path.join(IHADDONPATH, 'icon.png')
DEFAULTFANART       = os.path.join(IHADDONPATH, 'fanart.jpg')
DEFAULTBLANK        = os.path.join(IHADDONPATH, 'resources/art/pixel.png')
#######################################################################

#######################################################################
# Settings Variables 
DEBUGMODE           = THISADDON.getSetting('debug')
#######################################################################

artfolder           = os.path.join(IHADDONPATH,'resources','img')

def add_sort_methods():
    sort_methods = [xbmcplugin.SORT_METHOD_LABEL,xbmcplugin.SORT_METHOD_UNSORTED,xbmcplugin.SORT_METHOD_DATE,xbmcplugin.SORT_METHOD_DURATION,xbmcplugin.SORT_METHOD_EPISODE]
    for method in sort_methods:
        xbmcplugin.addSortMethod(int(sys.argv[1]), sortMethod=method)
    return
