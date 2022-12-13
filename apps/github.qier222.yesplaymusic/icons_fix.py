#!/usr/bin/env python3
import shutil
import os

def do_extra(app):
    app_id = app.appid
    os.rmdir("opt/apps/" + app_id + "/entries/icons")
    shutil.copytree("opt/apps/" + app_id + "/files/usr/share/icons",
                "opt/apps/" + app_id + "/entries/icons")
    shutil.rmtree("opt/apps/github.qier222.yesplaymusic/entries/icons/hicolor/1024x1024/")