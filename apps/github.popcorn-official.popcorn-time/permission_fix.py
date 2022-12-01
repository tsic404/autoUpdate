#!/bin/env python3
import os
def do_extra(app):
    file_list = ["chromedriver", "minidump_stackwalk", "nacl_helper", "nacl_helper_bootstrap", "nacl_irt_x86_64.nexe", "nwjc", "payload", "Popcorn-Time"]
    for i in file_list:
        os.chmod("opt/apps/" + app.appid + "/files/" + i, 0o755)
