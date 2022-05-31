#!/bin/env python3


import os
import shutil


def do_extra(app):
    app_id = app.appid
    os.makedirs("opt/apps/" + app_id + "/entries/icons/hicolor/128x128/apps")
    os.makedirs("opt/apps/" + app_id + "/entries/icons/hicolor/scalable/apps")
    shutil.copy("opt/apps/" + app_id + "/files/bin/studio.svg",
                    "opt/apps/" + app_id + "/entries/icons/hicolor/scalable/apps/android-studio.svg")
    shutil.copy("opt/apps/" + app_id + "/files/bin/studio.png",
                    "opt/apps/" + app_id + "/entries/icons/hicolor/128x128/apps/android-studio.png")
