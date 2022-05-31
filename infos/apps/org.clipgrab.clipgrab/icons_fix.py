#!/bin/env python3

import shutil
import os


def do_extra(app):
    app_id = app.appid
    os.makedirs("opt/apps/" + app_id + "/entries/icons/hicolor/64x64/apps")
    shutil.copy("opt/apps/" + app_id + "/files/clipgrab.png",
                "opt/apps/" + app_id + "/entries/icons/hicolor/64x64/apps/clipgrab.png")
