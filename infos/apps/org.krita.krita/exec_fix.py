#!/bin/env python3

import os

def do_extra(app):
    # os.remove("opt/apps/" + info['meta']['appid'] + '/files/AppRun')
    file = open("opt/apps/" + app.appid + '/files/bin/AppRun', "w+")
    os.chmod("opt/apps/" + app.appid + '/files/bin/AppRun', 0o755)
    content = """#!/bin/env bash
export LC_ALL=en_US.UTF-8
BINDIR=$(cd $(dirname $0);pwd)
export PYTHONPATH=/usr/lib/python3.7/
exec $BINDIR/krita $*

"""
    file.write(content)
    file.close()