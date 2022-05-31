#!/bin/env python3
import os
import shutil


def do_extra(app):
    os.makedirs("opt/apps/github.popcorn-official.popcorn-time/entries/icons/hicolor/256x256/apps/")
    shutil.move("opt/apps/github.popcorn-official.popcorn-time/files/src/app/images/icon.png",
                "opt/apps/github.popcorn-official.popcorn-time/entries/icons/hicolor/256x256/apps/popcorn-time.png")
