

from requests import post
from scripts.appdev import get_all_systemStr, get_cookie, get_seach, submit
from yaml import safe_load
from os import environ
from os.path import split,abspath,join

dirname, _ = split(abspath(__file__))

with open(join(dirname,"appdev.yaml")) as f:
    account = safe_load(f)

def call(app):
    if environ.get("https_proxy"):
        del environ['https_proxy']
    if environ.get("http_proxy"):
        del environ['http_proxy']

    cookies = get_cookie(account['username'], account['password'])
    app_info = get_seach(cookies=cookies, app_id=app.id)

    if (app_info['pkg_version'].__eq__(app.version)):
        print("same version submit")
        return
    developer = app.meta_info.get("developer") if app.meta_info.get("developer") else "deepin-team"
    submit(app, app.packaged, account['username'], account['password'], developer_name=developer)
    app_info = get_seach(cookies=cookies, app_id=app.id)
    if (app_info['pkg_version'].__eq__(app.version)):
        print("submit successful")
        res = post(url=account['cooperation_url'], json={
            "package": app.appid,
            "detail": app.name,
            "version": app.version,
            "systemStr": get_all_systemStr(cookies=cookies, app_id=app.id),
            "appid": app.id
            }).json()
        if res['status'].__eq__(1):
            print(res['msg'])
        else:
            print("cooperation create record failed")
    else:
        print("submit file failed")
    
