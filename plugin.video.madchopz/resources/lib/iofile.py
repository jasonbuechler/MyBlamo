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
import urllib2
from glo_var import *
#######################################################################

#######################################################################
# Handles getting contents of the menu file and returning them
def openMenuFile(menuFile):
    req = urllib2.Request(menuFile)
    req.add_header('User-Agent', USER_AGENT)
    response = urllib2.urlopen(req)
    link=response.read()
    response.close()
    return link
#######################################################################