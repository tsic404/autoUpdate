import os
import shutil

def do_extra(app):
    appid = app.appid
    dirname, filename = os.path.split(os.path.abspath(__file__))
    polkit_path ='opt/apps/' + appid + '/entries/polkit/actions'
    os.makedirs(polkit_path)
    shutil.copy(dirname + '/com.github.etcher.policy', polkit_path)
