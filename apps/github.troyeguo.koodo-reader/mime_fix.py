from os import makedirs
from shutil import copyfile

def do_extra(app):
    appid = app.appid
    makedirs("opt/apps/" + appid + "/entries/mime/packages")
    copyfile("opt/apps/" + appid + "/files/usr/share/mime/koodo-reader.xml",
                "opt/apps/" + appid + "/entries/mime/packages/koodo-reader.xml")
