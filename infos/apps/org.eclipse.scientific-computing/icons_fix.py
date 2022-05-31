#!/bin/env python3
import os
import shutil


def do_extra(app):
    app_id = app.appid
    path, _ = os.path.split(os.path.abspath(__file__))
    os.makedirs("opt/apps/" + app_id + "/entries/icons/hicolor/36x36/apps/")
    shutil.copy(os.path.join(path, "parallel.png"),
                "opt/apps/" + app_id + "/entries/icons/hicolor/36x36/apps/eclipse-parallel.png")