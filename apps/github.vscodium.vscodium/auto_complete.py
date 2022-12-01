from os import makedirs, popen

def do_extra(app):
    appid=app.appid
    makedirs('usr/share/bash-completion/completions')
    popen("ln -sf ../../../../opt/apps/" + appid + '/files/bash-completion/completions/codium usr/share/bash-completion/completions/codium').read()
    makedirs("usr/share/zsh/vendor-completions/")
    popen("ln -sf ../../../../opt/apps/" + appid + '/files/zsh/vendor-completions/_codium usr/share/zsh/vendor-completions/_codium').read()