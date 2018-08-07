# -*- coding: utf-8 -*-
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Addon: Jamzz 
# Author: Team MadDogg


import os           
import xbmc         
import xbmcaddon    
import xbmcplugin  
import tools 

from koding import route, Addon_Setting, Add_Dir, Find_In_Text, Open_URL, OK_Dialog
from koding import Open_Settings, Play_Video, Run, Text_File

# Added by MuadDib
from koding import Keyboard
from ytpsearch import *

debug        = Addon_Setting(setting='debug')       
addon_id     = xbmcaddon.Addon().getAddonInfo('id') 


BASE  = "plugin://plugin.video.youtube/playlist/"

YOUTUBE_CHANNEL_ID_1 = "PLgJId4TlAszKtM-DHtrRWB3fvpiQ3ypBj"
YOUTUBE_CHANNEL_ID_2 = "PLgJId4TlAszIYcJS3sERFmB_pnn5CqWZk"
YOUTUBE_CHANNEL_ID_3 = "PLgJId4TlAszJU83qLfashqXWm1N6HxmRX"
YOUTUBE_CHANNEL_ID_4 = "PLgJId4TlAszJ_fiqrCBHIoS-GAiDoD-S_"

PLAYLISTS = [ YOUTUBE_CHANNEL_ID_1, YOUTUBE_CHANNEL_ID_2, YOUTUBE_CHANNEL_ID_3, YOUTUBE_CHANNEL_ID_4 ]

@route(mode='main_menu')
def Main_Menu():

	Add_Dir( 
        name="Heavy Metal", url=BASE+YOUTUBE_CHANNEL_ID_1+"/", folder=True,
        icon="http://repo.maddogg.ca/builds/metal1.jpg")
		
	Add_Dir( 
        name="Classic Rock", url=BASE+YOUTUBE_CHANNEL_ID_2+"/", folder=True,
        icon="http://repo.maddogg.ca/builds/classic1.jpg")
		
	Add_Dir( 
        name="Alternative", url=BASE+YOUTUBE_CHANNEL_ID_3+"/", folder=True,
        icon="http://repo.maddogg.ca/builds/alternative.jpg")

	Add_Dir( 
        name="Hair Bands", url=BASE+YOUTUBE_CHANNEL_ID_4+"/", folder=True,
        icon="http://repo.maddogg.ca/builds/hair-bands.jpg")

        # Added by MuadDib
	Add_Dir( 
        name="Search", url='plugin://plugin.video.jamzz?mode=search', folder=True,
        icon="http://repo.maddogg.ca/builds/search1.jpg")

        # Added by MuadDib
	Add_Dir( 
        name="Tools", url='plugin://plugin.video.jamzz?mode=tools', folder=True,
        icon="http://repo.maddogg.ca/builds/tools.jpg")

@route(mode='tools')
def Tools_Menu():
	Add_Dir( 
        name="Apply API for YouTube if Daily Limit is Shown", url='plugin://plugin.video.jamzz?mode=ytapi', folder=False,
        icon="http://www.free-icons-download.net/images/youtube-icons-67260.png")
		
@route(mode='koding_settings')
def Koding_Settings():
    Open_Settings()

@route(mode='simple_dialog', args=['title','msg'])
def Simple_Dialog(title,msg):
    OK_Dialog(title, msg)

#Added by MuadDib
@route(mode='search')
def Playlist_Search():
    search_term = Keyboard(default='', heading='Search Titles')
    if len(search_term) > 0:
        perform_search(search_term, PLAYLISTS)
    else:
        pass	

#Added by MuadDib	
@route(mode='ytapi')
def YTAPI():
    tools.Apply_API()

if __name__ == "__main__":
    Run(default='main_menu')
    xbmcplugin.endOfDirectory(int(sys.argv[1]))
