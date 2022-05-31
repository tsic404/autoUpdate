

from shutil import copy

from utils import mkdirs


def do_extra(info):
    appid = info['meta']['appid']
    content = 'opt/apps/' + appid + '/files/'
    icons_path = 'opt/apps/' + appid + '/entries/icons/hicolor/'
    icons = ['1024']
    for i in icons:
        mkdirs(icons_path + i + 'x' + i + '/apps/')
        copy(content + '/pixmaps/com.visualstudio.code.png', icons_path + i + 'x' + i + '/apps/com.visualstudio.code.png')

