#!/bin/env python3


import os
import shutil


def do_extra(app):
    app_id = app.appid
    icon_list = ["16x16", "32x32", "48x48", "64x64", "128x128"]
    for i in icon_list:
        os.makedirs("opt/apps/" + app_id + "/entries/icons/hicolor/" + i + "/apps")
        shutil.copy("opt/apps/" + app_id + "/files/browser/chrome/icons/default/default" + i.split('x')[0] + ".png",
                    "opt/apps/" + app_id + "/entries/icons/hicolor/" + i + "/apps/firefox-nal.png")