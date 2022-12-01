#!/bin/env python3
import os
from os import listdir
from os.path import join,isfile
from shutil import copyfile, copytree

def do_extra(app):
    appid = app.appid
    dirname, filename = os.path.split(os.path.abspath(__file__))
    copy_content(dirname + "/icons", "opt/apps/" + appid + "/entries/icons")

def copy_content(src, dest):
    for content in listdir(src):
        origin = join(src, content)
        target = join(dest, content)
        if isfile(origin):
            try:
                copyfile(origin, target)
            except FileExistsError:
                pass
        else:
            copytree(origin, target)