import os
import shutil


def do_extra(app):
    app_id = app.appid
    os.makedirs("opt/apps/" + app_id + "/entries/icons/hicolor/128x128/apps")
    os.makedirs("opt/apps/" + app_id + "/entries/icons/hicolor/scable/apps")
    shutil.copy("opt/apps/" + app_id + "/files/bin/mps.svg",
                    "opt/apps/" + app_id + "/entries/icons/hicolor/scable/apps/com.jetbrains.mps.svg")
