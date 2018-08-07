# coding: utf-8 
#
# Youtube reviewers Added my MrBlamo
#------------------------------------------------------------
#
#------------------------------------------------------------
#
#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Based on code from the YouTube addon
#
# Author: MrBlamo
#------------------------------------------------------------

import os
import sys
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon

addonID = 'plugin.video.squad'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

YOUTUBE_CHANNEL_ID_1 = "UCTYzvbIsyoHa_9NtHYhjFxg"
YOUTUBE_CHANNEL_ID_2 = "UChej9mYH1qjSnxTNSMl8hFA"
YOUTUBE_CHANNEL_ID_3 = "UC-jBkGiRokRd-B2ylx1VqJQ"
YOUTUBE_CHANNEL_ID_4 = "UCK64W1nGRL0aEZ3uhSxeRCw"
YOUTUBE_CHANNEL_ID_5 = "UC4E_esq81tDJqnazzod-Bmg"
YOUTUBE_CHANNEL_ID_6 = "UCwOfCDhGJwt2S9aroVm5d3Q"
YOUTUBE_CHANNEL_ID_7 = "UCikYLqVMy1wqpXZMqYyY3jA"
YOUTUBE_CHANNEL_ID_8 = "UC3OFPTgSjbex5P4TcL_XINA"
YOUTUBE_CHANNEL_ID_9 = "UCUmoHlZIkuEWZkg04DsNeSw"
YOUTUBE_CHANNEL_ID_10 = "UCe_mMF8PekuarK8OmtmUqsA"
YOUTUBE_CHANNEL_ID_11 = "UCWhumoxdhMORFToU0bFPrzQ"
YOUTUBE_CHANNEL_ID_12 = "UC_jjtvJiMqzZ4pj6KxzB_2A"
YOUTUBE_CHANNEL_ID_13 = "UC0QRG-gMqHhF5-BPdmJfs1w"
YOUTUBE_CHANNEL_ID_14 = "UCzDERZdP5DSWDGzn0M77LXA"
YOUTUBE_CHANNEL_ID_15 = "UCn9O8-AkpJZ9OCYzkyj3rFA"
YOUTUBE_CHANNEL_ID_16 = "UC9_mUAGFpEEsWqh7NOlh9_w"
YOUTUBE_CHANNEL_ID_17 = "PLU12uITxBEPHSMyieyaCTm3Tug3B1x0by"
YOUTUBE_CHANNEL_ID_18 = "UCKcXLkF2uTpUbcH_FrkJisQ"
YOUTUBE_CHANNEL_ID_19 = "UCkRdDqI8N1xSMX9GDFu3Hyw"
YOUTUBE_CHANNEL_ID_20 = "UCGEVFCOp9UCtDjwc7gIpTcQ"
YOUTUBE_CHANNEL_ID_21 = "UCBj6vHknwI4FQnZPM-9DVfw"
YOUTUBE_CHANNEL_ID_22 = "UCkX6dQihoolp88g4AEzxtng"
YOUTUBE_CHANNEL_ID_23 = "UCl-eGcrz6x88Xw37q2MWHyA"
YOUTUBE_CHANNEL_ID_24 = "UCvg1p5uER5gdFA2AWpNL_qQ"
YOUTUBE_CHANNEL_ID_25 = "UCFq5FJk4OY4j_VeL3wxSP3Q"
YOUTUBE_CHANNEL_ID_26 = "UCh0AhiuEhoCukIIsh5ZB3SQ"
YOUTUBE_CHANNEL_ID_27 = "UCNpGTnUm6xVUWxfOe3GEBVQ"
YOUTUBE_CHANNEL_ID_28 = "UCV_EOCb2sG-kjvJmVh18aUQ"
YOUTUBE_CHANNEL_ID_29 = "UCJsANtdMxPUdeNIxvcFeH_w"
YOUTUBE_CHANNEL_ID_30 = "UCzHA6WFM3WbkRfDZe1qniXQ"
YOUTUBE_CHANNEL_ID_31 = "UCUY5BYXIaZoa4-HclwnNWDA"
YOUTUBE_CHANNEL_ID_32 = "UCTj-2nCE8B_3AvEGAKVyn1g"
YOUTUBE_CHANNEL_ID_33 = "UCfiZzwbPTOw8MCQfyxES43A"
YOUTUBE_CHANNEL_ID_34 = "UC4t4DYJ34TZNFR3hKi-3TTg"
YOUTUBE_CHANNEL_ID_35 = "UCFOStcorp34JSwYTaTZB1oQ"
YOUTUBE_CHANNEL_ID_36 = "UCgTv3f2aLsOsgeaQ9MnS1wg"
YOUTUBE_CHANNEL_ID_37 = "UCzRJvnShKbJ8N8hfF94bX-A"
YOUTUBE_CHANNEL_ID_38 = "UCQZcmkkx7hc0ik4wjaAtINQ"
YOUTUBE_CHANNEL_ID_39 = "UCWhumoxdhMORFToU0bFPrzQ"
YOUTUBE_CHANNEL_ID_40 = "UCoN6fIDcZn-438ddCeEopCg"
YOUTUBE_CHANNEL_ID_41 = "UCaKZuTu78VRc94kymoX_ImQ"
YOUTUBE_CHANNEL_ID_42 = "UCFOStcorp34JSwYTaTZB1oQ"
YOUTUBE_CHANNEL_ID_43 = "UCs_Ci64Q3vz8h8rBhOkPMYw"
YOUTUBE_CHANNEL_ID_44 = "UCWJ3sjHCtaO240IYKueqkNw"





# Entry point
def run():
    plugintools.log("docu.run")
    
    # Get params
    params = plugintools.get_params()
    
    if params.get("action") is None:
        main_list(params)
    else:
        action = params.get("action")
        exec action+"(params)"
    
    plugintools.close_item_list()

# Main menu
def main_list(params):
    plugintools.log("docu.main_list "+repr(params))

    plugintools.add_item( 
        #action="", 
        title="BO KNOWS",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_1+"/",
        thumbnail="https://ia601501.us.archive.org/32/items/urbankingz/bo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Blue's Tech and Tips",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_2+"/",
        thumbnail="https://ia601500.us.archive.org/1/items/livetube/blueshouse.jpg",
        folder=True )			
		
    plugintools.add_item( 
        #action="", 
        title="DaButcher",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_3+"/",
        thumbnail="https://ia601501.us.archive.org/32/items/urbankingz/dabutcher.jpg",
        folder=True )		
		
    plugintools.add_item( 
        #action="", 
        title="Doggmatic 71",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_4+"/",
        thumbnail="https://ia801501.us.archive.org/32/items/urbankingz/doggmatic.jpg",
        folder=True )		


    plugintools.add_item( 
        #action="", 
        title="Food Stamps UrbanKingz",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_5+"/",
        thumbnail="https://archive.org/download/urbankingz/urbankingz.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Istoit",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_6+"/",
        thumbnail="https://ia801501.us.archive.org/32/items/urbankingz/sweetistoit.jpg",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="MissKodi21",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_7+"/",
        thumbnail="https://ia601501.us.archive.org/32/items/urbankingz/misskodi.jpg",
        folder=True )
	
    plugintools.add_item( 
        #action="", 
        title="Muad'Dib",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_8+"/",
        thumbnail="https://ia601501.us.archive.org/32/items/urbankingz/muaddib.jpg",
        folder=True )
	
    plugintools.add_item( 
        #action="", 
        title="Rohas Tutorials",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_9+"/",
        thumbnail="https://ia601501.us.archive.org/32/items/urbankingz/rohas.jpg",
        folder=True )
	
    plugintools.add_item( 
        #action="", 
        title="SuperDell",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_10+"/",
        thumbnail="https://ia601501.us.archive.org/32/items/urbankingz/superdell.jpg",
        folder=True )
	
    plugintools.add_item( 
        #action="", 
        title="The Madd Mentor",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_11+"/",
        thumbnail="https://yt3.ggpht.com/-kxktkWIpvoE/AAAAAAAAAAI/AAAAAAAAAAA/JnlBxa4NI4c/s288-mo-c-c0xffffffff-rj-k-no/photo.jpg",
        folder=True )
	
    plugintools.add_item( 
        #action="", 
        title="TeverZ",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_12+"/",
        thumbnail="https://ia601501.us.archive.org/32/items/urbankingz/teverztheman.jpg",
        folder=True )
	
    plugintools.add_item( 
        #action="", 
        title="Top Tutorials",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_13+"/",
        thumbnail="https://ia801501.us.archive.org/32/items/urbankingz/toptuts.jpg",
        folder=True )
	
    plugintools.add_item( 
        #action="", 
        title="Ukodi1 Builds",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_14+"/",
        thumbnail="https://ia801501.us.archive.org/32/items/urbankingz/ukodi1.jpg",
        folder=True )
	
    plugintools.add_item( 
        #action="", 
        title="John Henderson",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_15+"/",
        thumbnail="https://ia801500.us.archive.org/1/items/livetube/johnhender.jpg",
        folder=True )
	
    plugintools.add_item( 
        #action="", 
        title="Skymashi TV",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_16+"/",
        thumbnail="https://ia601500.us.archive.org/1/items/livetube/skymashi.jpg",
        folder=True )
	
    plugintools.add_item( 
        #action="", 
        title="Live",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_17+"/",
        thumbnail="https://archive.org/download/livetube/livetube.jpg",
        folder=True )
	
    plugintools.add_item( 
        #action="", 
        title="Marcos Murillo",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_18+"/",
        thumbnail="https://ia801501.us.archive.org/23/items/photo_20180410/photo.jpg",
        folder=True )
	
    plugintools.add_item( 
        #action="", 
        title="NewDude167",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_19+"/",
        thumbnail="https://ia601501.us.archive.org/23/items/photo_20180410/photo%20(1).jpg",
        folder=True )
	
    plugintools.add_item( 
        #action="", 
        title="OndemandinternetTV",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_20+"/",
        thumbnail="https://ia801507.us.archive.org/3/items/Photo4_201804/photo.jpg",
        folder=True )
	
    plugintools.add_item( 
        #action="", 
        title="Stephen Cornelious",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_21+"/",
        thumbnail="https://ia801507.us.archive.org/3/items/Photo4_201804/photo%20(2).jpg",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Diamond Build",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_22+"/",
        thumbnail="https://ia801507.us.archive.org/3/items/Photo4_201804/photo%20(3).jpg",
        folder=True )
	
    plugintools.add_item( 
        #action="", 
        title="Terrorize Kodi",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_23+"/",
        thumbnail="https://ia801507.us.archive.org/3/items/Photo4_201804/photo%20(4).jpg",
        folder=True )
	
    plugintools.add_item( 
        #action="", 
        title="Fan Riffic",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_24+"/",
        thumbnail="https://ia801507.us.archive.org/3/items/Photo4_201804/photo%20(5).jpg",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="ReviewDork",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_25+"/",
        thumbnail="https://ia801507.us.archive.org/3/items/Photo4_201804/photo%20(6).jpg",
        folder=True )
	
    plugintools.add_item( 
        #action="", 
        title="TechReviews919",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_26+"/",
        thumbnail="https://ia801507.us.archive.org/3/items/Photo4_201804/photo%20(7).jpg",
        folder=True )
	
    plugintools.add_item( 
        #action="", 
        title="CSSC0DER",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_27+"/",
        thumbnail="https://ia601507.us.archive.org/3/items/Photo4_201804/photo%20(8).jpg",
        folder=True )	
	
    plugintools.add_item( 
        #action="", 
        title="darealwy",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_28+"/",
        thumbnail="https://ia601508.us.archive.org/16/items/Photo9_201804/photo%20(1).jpg",
        folder=True )
	
    plugintools.add_item( 
        #action="", 
        title="Supreme Builds",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_29+"/",
        thumbnail="https://ia601508.us.archive.org/16/items/Photo9_201804/photo%20(9).jpg",
        folder=True )
	
    plugintools.add_item( 
        #action="", 
        title="Jack Bower",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_30+"/",
        thumbnail="https://yt3.ggpht.com/-z3II_JhUBf4/AAAAAAAAAAI/AAAAAAAAAAA/ofor8ZjzWlw/s288-mo-c-c0xffffffff-rj-k-no/photo.jpg",
        folder=True )
	
    plugintools.add_item( 
        #action="", 
        title="Dimitrology",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_31+"/",
        thumbnail="https://yt3.ggpht.com/-gc8RvvduE-E/AAAAAAAAAAI/AAAAAAAAAAA/7YIGzK1cPME/s288-mo-c-c0xffffffff-rj-k-no/photo.jpg",
        folder=True )
	
    plugintools.add_item( 
        #action="", 
        title="TotalRevolution",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_32+"/",
        thumbnail="https://yt3.ggpht.com/-j-99Pz2bz2k/AAAAAAAAAAI/AAAAAAAAAAA/wm1dVKFr5tk/s288-mo-c-c0xffffffff-rj-k-no/photo.jpg",
        folder=True )
	
    plugintools.add_item( 
        #action="", 
        title="Triple M",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_33+"/",
        thumbnail="https://yt3.ggpht.com/-gc8RvvduE-E/AAAAAAAAAAI/AAAAAAAAAAA/7YIGzK1cPME/s288-mo-c-c0xffffffff-rj-k-no/photo.jpg",
        folder=True )
	
    plugintools.add_item( 
        #action="", 
        title="KODI NO LIMITS",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_33+"/",
        thumbnail="https://yt3.ggpht.com/-1BnZqH4y_YI/AAAAAAAAAAI/AAAAAAAAAAA/gOACD6u23sA/s288-mo-c-c0xffffffff-rj-k-no/photo.jpg",
        folder=True )
	
    plugintools.add_item( 
        #action="", 
        title="Kodi Best Build",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_34+"/",
        thumbnail="https://yt3.ggpht.com/-ppmp3LRcR0o/AAAAAAAAAAI/AAAAAAAAAAA/jeeW0ze1Rmw/s288-mo-c-c0xffffffff-rj-k-no/photo.jpg",
        folder=True )
	
    plugintools.add_item( 
        #action="", 
        title="Doc Squiffy",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_35+"/",
        thumbnail="https://yt3.ggpht.com/-nYgh3GLcdyc/AAAAAAAAAAI/AAAAAAAAAAA/eseha30N5uY/s288-mo-c-c0xffffffff-rj-k-no/photo.jpg",
        folder=True )
	
    plugintools.add_item( 
        #action="", 
        title="Mchanga",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_36+"/",
        thumbnail="https://yt3.ggpht.com/-3EcBegdu45I/AAAAAAAAAAI/AAAAAAAAAAA/ojcaItoFTqc/s288-mo-c-c0xffffffff-rj-k-no/photo.jpg",
        folder=True )
	
    plugintools.add_item( 
        #action="", 
        title="TROOPER 69",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_37+"/",
        thumbnail="https://yt3.ggpht.com/-T27_ouG_eJQ/AAAAAAAAAAI/AAAAAAAAAAA/UrNugeiRQZc/s288-mo-c-c0xffffffff-rj-k-no/photo.jpg",
        folder=True )
	
    plugintools.add_item( 
        #action="", 
        title="Peter Carcione",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_38+"/",
        thumbnail="https://yt3.ggpht.com/-ILSynlg95ME/AAAAAAAAAAI/AAAAAAAAAAA/NUXKGDZ9LA8/s288-mo-c-c0xffffffff-rj-k-no/photo.jpg",
        folder=True )
	
    plugintools.add_item( 
        #action="", 
        title="Everything Kodi",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_39+"/",
        thumbnail="https://yt3.ggpht.com/-7dzh8XZbMgY/AAAAAAAAAAI/AAAAAAAAAAA/ZxkMQe0xv-c/s288-mo-c-c0xffffffff-rj-k-no/photo.jpg",
        folder=True )
	
    plugintools.add_item( 
        #action="", 
        title="Optimum Bliss",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_40+"/",
        thumbnail="https://yt3.ggpht.com/-vbJI3xc3EgA/AAAAAAAAAAI/AAAAAAAAAAA/BHrKEdOu2eA/s288-mo-c-c0xffffffff-rj-k-no/photo.jpg",
        folder=True )
	
    plugintools.add_item( 
        #action="", 
        title="Your Kodi",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_41+"/",
        thumbnail="https://yt3.ggpht.com/-M_iQ8M7zz9g/AAAAAAAAAAI/AAAAAAAAAAA/olTarKFNkmo/s288-mo-c-c0xffffffff-rj-k-no/photo.jpg",
        folder=True )
	
    plugintools.add_item( 
        #action="", 
        title="Doc Squiffy",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_42+"/",
        thumbnail="https://yt3.ggpht.com/-nYgh3GLcdyc/AAAAAAAAAAI/AAAAAAAAAAA/eseha30N5uY/s288-mo-c-c0xffffffff-rj-k-no/photo.jpg",
        folder=True )
	
    plugintools.add_item( 
        #action="", 
        title="Tantrum Dev",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_43+"/",
        thumbnail="https://yt3.ggpht.com/-QBsJw5QH5dU/AAAAAAAAAAI/AAAAAAAAAAA/eAlPxL0b8WY/s288-mo-c-c0xffffffff-rj-k-no/photo.jpg",
        folder=True )
	
    plugintools.add_item( 
        #action="", 
        title="Kodi-Solutions",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_44+"/",
        thumbnail="https://yt3.ggpht.com/-EuxUdKKs8xI/AAAAAAAAAAI/AAAAAAAAAAA/NghEpit0kAk/s288-mo-c-c0xffffffff-rj-k-no/photo.jpg",
        folder=True )
	
run()
