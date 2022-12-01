from os import makedirs
from shutil import copy



def do_extra(app):
    appid = app.appid
    content = 'opt/apps/' + appid + '/files/'
    icons_path = 'opt/apps/' + appid + '/entries/icons/hicolor/256x256/apps/'
    makedirs(icons_path)
    copy(content + "discord.png", icons_path)
