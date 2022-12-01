from os import makedirs, mkdir, popen, symlink

def do_extra(app):
    appid = app.appid
    symlink("/lib/x86_64-linux-gnu/libudev.so.1", "opt/apps/" + appid + "/files/Libraries/libudev.so.0")
    mkdir("opt/apps/" + appid + "/files/udev")
    with open("opt/apps/" + appid + "/files/udev/ft-rockey.rules", "w+") as udev:
        udev.write("BUS==\"usb\", SYSFS{idVendor}==\"096e\", MODE==\"0666\"")
    makedirs("etc/udev/rules.d/")
    popen("ln -sf ../../../opt/apps/" + appid + "/files/udev/ft-rockey.rules etc/udev/rules.d/ft-rockey.rules").read()
