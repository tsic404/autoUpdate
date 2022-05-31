
from os import popen

def do_extra(app):
    appid = app.appid
    popen("sed -i 's|/opt/emby-server|/opt/apps/" + appid +  "/files|g' opt/apps/media.emby.emby-server/files/bin/emby-server").read()