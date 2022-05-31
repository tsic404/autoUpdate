#!/bin/env python3
import os
from scripts.utils import copy_content


def do_extra(app):
    appid = app.appid
    dirname, filename = os.path.split(os.path.abspath(__file__))
    copy_content(dirname + "/icons", "opt/apps/" + appid + "/entries/icons")
