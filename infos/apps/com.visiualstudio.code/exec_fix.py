

from os import popen

from package import App


def do_extra(app: App):
    appid = app.appid
    desktops = ['opt/apps/' + appid + '/entries/applications/code.desktop', 'opt/apps/' + appid + '/entries/applications/code-url-handler.desktop']
    for i in desktops:
        shell = "sed -i 's/Exec=\/usr\/share\/code\/code/Exec=\/opt\/apps\/com.visualstudio.code\/files\/code\/code/g' " + i
        popen(shell).read()
