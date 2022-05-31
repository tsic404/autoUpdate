
from os import makedirs
from shutil import copy

def do_extra(app):
    appid = app.appid
    services = [
        'com.teamviewer.TeamViewer.Desktop.service',
        'com.teamviewer.TeamViewer.service'
    ]
    service_deepin = "opt/apps/" + appid + "/entries/services/"
    service_pre = "opt/apps/" + appid + "/files/tv_bin/script/"
    makedirs(service_deepin)
    for i in services:
        copy(service_pre + i, service_deepin)
    