#!/bin/env python3
from os import popen

def do_extra(app):
    appid = app.appid
    bin_file = 'opt/apps/' + appid + '/files/bin/bcompare'
    shell = "sed -i 's|BC_LIB=/usr/lib/beyondcompare|BC_LIB=/opt/apps/" + appid + "/files/lib/beyondcompare|g' " + bin_file
    popen(shell).read()
