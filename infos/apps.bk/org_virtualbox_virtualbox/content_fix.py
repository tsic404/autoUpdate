from os import popen

def do_extra(info):
    appid = info['meta']['appid']
    popen("mv opt/apps/" + appid + "/files/* . ").read()
