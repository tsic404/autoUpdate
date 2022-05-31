

def call(app):
    db = app.config.get_db()
    appid = app.appid
    ver = app.version
    url = app.url
    db.set_ver_url(appid, ver, url)
    print(app.packaged)