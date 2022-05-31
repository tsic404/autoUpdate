from os import makedirs
from shutil import copy

def do_extra(app):
    appid = app.appid
    content = 'opt/apps/' + appid + '/files/'
    icons_path = 'opt/apps/' + appid + '/entries/icons/hicolor/'
    icons = ['1024']
    for i in icons:
        makedirs(icons_path + i + 'x' + i + '/apps/')
        copy(content + '/pixmaps/vscodium.png', icons_path + i + 'x' + i + '/apps/vscodium.png')
