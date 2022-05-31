#!/bin/env python3
import os
import shutil


def do_extra(app):
    os.makedirs("opt/apps/org.shotcut.shotcut/entries/icons/hicolor/64x64/apps/")
    shutil.move("opt/apps/org.shotcut.shotcut/files/shotcut.png",
                "opt/apps/org.shotcut.shotcut/entries/icons/hicolor/64x64/apps/shotcut.png")
