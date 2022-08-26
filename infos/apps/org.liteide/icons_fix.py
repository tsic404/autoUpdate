#!/bin/env python3


import os
import shutil


def do_extra(app):
    app_id = app.appid
    os.makedirs("opt/apps/" + app_id + "/entries/icons/hicolor/48x48/apps")

    shutil.copy("opt/apps/" + app_id + "/files/liteide.png",
                    "opt/apps/" + app_id + "/entries/icons/hicolor/48x48/apps/liteide.png")
