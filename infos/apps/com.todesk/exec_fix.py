import os

def do_extra(app):
    appid = app.appid
    shell = "sed -i 's|/opt/todesk/|/opt/apps/" + appid + "/files/|g' "
    os.popen(shell + " opt/apps/" + appid + "/entries/applications/todesk.desktop").read()
    