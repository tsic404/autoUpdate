#!/bin/env python3


import os
import shutil


def do_extra(app):
    appid = app.appid
    os.makedirs("opt/apps/" + appid + "/entries/icons/hicolor/128x128/apps")
    os.makedirs("opt/apps/" + appid + "/entries/icons/hicolor/scable/apps")

    shutil.copy("opt/apps/" + appid + "/files/bin/clion.svg",
                    "opt/apps/" + appid + "/entries/icons/hicolor/scable/apps/com.jetbrains.clion.svg")
    shutil.copy("opt/apps/" + appid + "/files/bin/clion.png",
                    "opt/apps/" + appid + "/entries/icons/hicolor/128x128/apps/com.jetbrains.clion.png")