#!/bin/env python3
import os
import shutil


def do_extra(app):
    app_id = app.appid
    os.makedirs("opt/apps/" + app_id + "/entries/icons/hicolor/64x64/apps/")
    shutil.copy("opt/apps/" + app_id + "/files/data/flutter_assets/assets/images/logo_icon.png",
                "opt/apps/" + app_id + "/entries/icons/hicolor/64x64/apps/authpass.png")
