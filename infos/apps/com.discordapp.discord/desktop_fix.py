

from shutil import copy
from os import popen


def do_extra(app):
    appid = app.appid
    desktop = 'opt/apps/' + appid + '/entries/applications/discord.desktop'
    content_path = "opt/apps/" + appid + "/files/discord.desktop"
    copy(content_path, desktop)
    shell = "sed -i 's|Exec=/usr/share/discord/Discord|Exec=/opt/apps/com.discordapp.discord/files/Discord|g' " + desktop
    popen(shell).read()
