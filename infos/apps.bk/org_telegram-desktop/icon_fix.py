import os
import shutil

def do_extra(info):
    appid = info['meta']['appid']
    dirname, filename = os.path.split(os.path.abspath(__file__))
    icons_path ='opt/apps/' + appid + '/entries/icons/'
    shutil.copytree(dirname + '/icons', icons_path)
