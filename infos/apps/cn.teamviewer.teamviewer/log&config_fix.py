
from os import link, makedirs

def do_extra(app):
    appid = app.appid
    makedirs("etc/teamviewer/")
    makedirs("var/log/teamviewer15/")
    #link("etc/teamviewer/", "opt/apps/" + appid + "/files/config")
    #link("var/log/teamviewer15", "opt/apps/" + appid + "/files/logfiles")