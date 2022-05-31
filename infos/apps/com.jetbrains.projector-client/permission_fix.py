#!/bin/env python3
import os



def do_extra(app):
    os.chmod("opt/apps/" + app.appid +"/files/projector", 0o755)
    