from os import makedirs, popen
from shutil import copy



def do_extra(app):
    appid = app.appid
    content = 'opt/apps/' + appid + '/files/'
    icons_path = 'opt/apps/' + appid + '/entries/icons/hicolor/256x256/apps/'
    makedirs(icons_path)
    copy(content + "/icon.png", icons_path + "freedownloadmanager.png" )
    desktop = 'opt/apps/' + appid + '/entries/applications/freedownloadmanager.desktop'
    shell = "sed -i 's|Icon=/opt/freedownloadmanager/icon.png|Icon=freedownloadmanager|g' " + desktop
    popen(shell).read()

