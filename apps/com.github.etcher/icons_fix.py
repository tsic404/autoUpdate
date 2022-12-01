from contextvars import copy_context

def do_extra(app):
    appid = app.appid
    content = 'opt/apps/' + appid + '/files/'
    icons_path = 'opt/apps/' + appid + '/entries/icons'
    copy_context(content + "/usr/share/icons", icons_path)
