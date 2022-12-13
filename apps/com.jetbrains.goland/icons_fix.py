#!/usr/bin/env python3


import os
import shutil


def do_extra(app):
    app_id = app.appid
    os.makedirs("opt/apps/" + app_id + "/entries/icons/hicolor/128x128/apps")
    os.makedirs("opt/apps/" + app_id + "/entries/icons/hicolor/scable/apps")

    shutil.copy("opt/apps/" + app_id + "/files/bin/goland.svg",
                    "opt/apps/" + app_id + "/entries/icons/hicolor/scable/apps/com.jetbrains.goland.svg")
    shutil.copy("opt/apps/" + app_id + "/files/bin/goland.png",
                    "opt/apps/" + app_id + "/entries/icons/hicolor/128x128/apps/com.jetbrains.goland.png")
