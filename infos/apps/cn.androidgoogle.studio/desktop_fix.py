import os
import shutil

def do_extra(app):
    appid = app.appid
    dirname, filename = os.path.split(os.path.abspath(__file__))
    applications_path ='opt/apps/' + appid + '/entries/applications/'
    shutil.copy(dirname + '/cn.androidgoogle.studio.desktop', applications_path)