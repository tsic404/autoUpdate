from os.path import exists
from os import remove

def do_extra(app):
    appid = app.appid
    configure_file = "opt/apps/" + appid + "/files/doublecmd.inf"
    if (exists(configure_file)):
        remove(configure_file)
