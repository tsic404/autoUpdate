import os
import shutil

def do_extra(info):
    appid = info['meta']['appid']
    dirname, filename = os.path.split(os.path.abspath(__file__))
    applications_path ='opt/apps/' + appid + '/entries/applications/'
    os.mkdir(applications_path)
    shutil.copy(dirname + '/' + appid + '.desktop', applications_path)
