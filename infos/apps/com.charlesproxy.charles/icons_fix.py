#!/bin/env python3
import os
import shutil


def do_extra(app):
    app_id = app.appid
    icons_path = "opt/apps/" + app_id + "/entries/icons/hicolor/"
    for size in os.listdir("opt/apps/" + app_id + "/files/icon"):
        shutil.move("opt/apps/" + app_id + "/files/icon/" + size, icons_path)
