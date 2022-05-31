

from os import popen


def do_extra(info):
    appid = info['meta']['appid']
    desktop_path = 'opt/apps/' + appid + '/entries/applications/'
    desktops = ['skypeforlinux.desktop','skypeforlinux-share.desktop']
    for i in desktops:
        desktop = desktop_path + i
        shell = "sed -i 's/Exec=\/usr\/bin\/skypeforlinux/Exec=\/opt\/apps\/com.skype.www\/files\/skypeforlinux/g' " + desktop
        popen(shell).read()
