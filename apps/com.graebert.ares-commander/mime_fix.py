from os import makedirs
from shutil import copyfile


def do_extra(app):
    appid = app.appid
    mime_entries = "opt/apps/" + appid + "/entries/mime/packages"
    makedirs(mime_entries)
    mime_path = "opt/apps/" + appid + "/files/Resources/"
    mimes = [
        "graebert-gmbh_ares-commander-dwg.xml",
        "graebert-gmbh_ares-commander-dwt.xml",
        "graebert-gmbh_ares-commander-dxf.xml"
    ]
    for i in mimes:
        copyfile(mime_path + i, mime_entries + i)
