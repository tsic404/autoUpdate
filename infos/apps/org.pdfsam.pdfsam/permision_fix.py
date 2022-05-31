#!/bin/env python3

import os

def do_extra(app):
    app_id = app.appid
    lib_path = "opt/apps/" + app_id + "/files/lib/"
    for i in os.listdir(lib_path):
        path = os.path.join(lib_path, i)
        os.chmod(path, 0o664)