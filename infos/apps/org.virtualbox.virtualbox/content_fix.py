from os import popen

def do_extra(app):
    appid = app.appid
    popen("mv opt/apps/" + appid + "/files/* .").read()
