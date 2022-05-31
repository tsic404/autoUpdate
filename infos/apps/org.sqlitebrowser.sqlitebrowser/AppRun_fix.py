#!/bin/env python3

import os
import shutil

def do_extra(app):
    app_id = app.appid
    AppRun = """#!/bin/env bash
APP_PATH=$(cd "$(dirname "$0")"; pwd) 
export LD_LIBRARY_PATH=$APP_PATH/usr/plugins/platforms:$LD_LIBRARY_PATH
exec $APP_PATH/usr/bin/sqlitebrowser.qt5run $*
    """
    shutil.copy("/usr/lib/x86_64-linux-gnu/libxcb-util.so.0.0.0", "opt/apps/" + app_id + "/files/usr/plugins/platforms/libxcb-util.so.1")
    os.remove("opt/apps/" + app_id + "/files/AppRun")
    with open("opt/apps/" + app_id + "/files/AppRun", "w+") as f:
        f.write(AppRun)
    os.chmod('opt/apps/' + app_id + "/files/AppRun", 0o755)

