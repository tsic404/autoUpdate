#!/bin/env python3
import os
import shutil

def do_extra(app):
    appid = app.appid
    dirname, filename = os.path.split(os.path.abspath(__file__))
    icons_path ='opt/apps/' + appid + '/entries/icons/'
    os.rmdir(icons_path)
    shutil.copytree(dirname + '/icons', icons_path)