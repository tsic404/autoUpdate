
from os import remove

def do_extra(info):
    appid = info['meta']['appid']
    remove("opt/apps/" + appid +"/files/Updater")