
from os import popen


def do_extra(app):
    appid = app.appid
    shell = "sed -i 's|Icon=/usr/share/icons/hicolor/512x512/apps/v2raya.png|Icon=v2raya|g'"
    popen(shell + " opt/apps/" + appid + "/entries/applications/v2raya.desktop").read()
