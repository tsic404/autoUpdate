from os import makedirs
from shutil import copy

def do_extra(app):
    appid = app.appid
    content = 'opt/apps/' + appid + '/files/'
    icons_path = 'opt/apps/' + appid + '/entries/icons/hicolor/'
    icons = ['16', '24', '32', '48', '128', '256']
    for i in icons:
        makedirs(icons_path + i + 'x' + i + '/apps/')
        copy(content + 'product_logo_' + i + '.png', icons_path + i + 'x' + i + '/apps/microsoft-edge.png')
