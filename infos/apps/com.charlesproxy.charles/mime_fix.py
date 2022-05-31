#!/bin/env python3
import os
import shutil


def do_extra(app):
    app_id = app.appid
    os.makedirs("opt/apps/" +app_id + "/entries/mime/packages/")
    shutil.move("opt/apps/" + app_id + "/files/etc/mime/charles-proxy.xml",
                "opt/apps/" +app_id + "/entries/mime/packages/")