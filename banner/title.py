#!/usr/bin/python3


class title:
    def __init__(self):
        self.author = "security007"
        self.version = "2.1"
        self.appname = "sword"
        self.country = "Indonesia"

    def ban(self):
        self.judul = """\033[1;34m
            /\=
/vvvvvvvvvvvv \--------------------------------------,
`^^^^^^^^^^^^ /====================================="
            \/=\033[0m"""+"""\033[1;32m
SWORD ( Android ADB Post Exploitation Framework )
[ Author : Security007 ]
[ Version : 2.1 ]
            \033[0m"""
        return self.judul

    def help(self):
        self.hl = """
SWORD HELP:

    help = show this help
    options = show options menu
    set = set options value
    run = run sword
    exit = exit sword framework
"""
        return self.hl

    def help1(self):
        self.hl = """
sword command:

    get_activity = get android get_activity
    sysinfo = get android info
    get_contact = get victim contact
    check_root = check if device is rooted
    download = download from remote host
    upload = upload to remote host
    shell = spawn android system shell
    adb_command = run adb command
    screenshot =  capture device screen
    open_url = open url from target browser
    get_apps = show installed apps on target device
    screen_mirror = open mirror device screen
"""

        return self.hl
