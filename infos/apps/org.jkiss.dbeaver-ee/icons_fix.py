#!/bin/env python3


import os
import shutil


def do_extra(app):
    app_id = app.appid
    os.makedirs("opt/apps/" + app_id + "/entries/icons/hicolor/256x256/apps")

    shutil.copy("opt/apps/" + app_id + "/files/dbeaver.png",
                    "opt/apps/" + app_id + "/entries/icons/hicolor/256x256/apps/dbeaver-ee.png")
