#!/usr/bin/env python3
import os
def do_extra(app):
    file_list = ["chrome-sandbox"]
    for i in file_list:
        os.chmod("opt/apps/" + app.appid + "/files/" + i, 0o4755)