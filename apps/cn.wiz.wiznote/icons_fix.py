
import shutil

def do_extra(app):
    appid = app.appid
    shutil.rmtree('opt/apps/' + appid + '/entries/icons/hicolor/1024x1024/')
    shutil.rmtree('opt/apps/' + appid + '/files/usr/share/icons/hicolor/1024x1024/')
