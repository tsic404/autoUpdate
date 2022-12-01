from os import chmod

def do_extra(app):
    appid = app.appid
    chmod("opt/apps/" + appid + "/files/Leanote", 0o755)
    chmod("opt/apps/" + appid + "/files/chrome-sandbox", 0o4755)
