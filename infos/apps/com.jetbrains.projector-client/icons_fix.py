#!/bin/env python3
import os
import shutil


def do_extra(app):
    os.makedirs("opt/apps/" + app.appid +"/entries/icons/hicolor/512x512/apps/")
    shutil.copy("opt/apps/" + app.appid +"/files/resources/app/assets/img/electron-icon.png",
                "opt/apps/" + app.appid +"/entries/icons/hicolor/512x512/apps/projector.png")
