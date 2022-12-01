from shutil import move
from os import popen

def do_extra(app):
    appid = app.appid
    move("opt/apps/" + appid + "/entries/icons/hicolor/48x48/apps/vncviewer48x48.png",
         "opt/apps/" + appid + "/entries/icons/hicolor/48x48/apps/vncviewer.png")
    
    desktop = 'opt/apps/' + appid + '/entries/applications/realvnc-vncviewer.desktop'
    shell = "sed -i 's|Icon=/usr/share/icons/hicolor/48x48/apps/vncviewer48x48.png|Icon=vncviewer|g' " + desktop
    popen(shell).read()