#!/usr/bin/python3

import subprocess
from banner.color import *
import readline
import random
import string
import os

readline.parse_and_bind('tab: complete')

class com:
    def __init__(self):
        self.version = "2.1"
        self.warna = warna()

    def send(self,arg):
        self.cmd = subprocess.getoutput("adb {}".format(arg))
        return self.cmd.strip()

    def get_activity(self):
        self.ot = self.send("shell dumpsys activity")
        print(self.ot)

    def sysinfo(self):
        self.brand = self.send("shell getprop ro.product.brand")
        self.hostname = self.send("shell getprop net.hostname")
        self.username = self.send("shell getprop ro.product.name")
        self.version = self.send("shell getprop ro.build.version.release")
        self.architecture = self.send("shell getprop ro.product.cpu.abi")
        self.information = ""
        self.information += f"{self.warna.I}Brand: {self.brand}\n"
        self.information += f"{self.warna.I}Computer Hostname: {self.hostname}\n"
        self.information += f"{self.warna.I}Computer Username: {self.username}\n"
        self.information += f"{self.warna.I}Release Version: {self.version}\n"
        self.information += f"{self.warna.I}Processor Architecture: {self.architecture}"
        return self.information

    def get_contact(self):
        self.go = self.send("shell content query --uri content://contacts/phones/  --projection display_name:number")
        return self.go

    def upload(self,lfile,rfile):
        self.up = self.send("push "+lfile+" "+rfile)
        return self.up

    def download(self,rfile,lfile):
        self.dw = self.send("pull "+rfile+" "+lfile)
        return self.dw

    def spawn_shell(self):
        os.system("adb shell")

    def cek_root(self):
        self.cek = self.send("shell whoami")
        if self.cek == "root":
            print(self.warna.G+"Device is rooted")
        else:
            print(self.warna.W+"Device is not rooted")

    def adb_command(self):
        self.adb = str(input("ADB > "))
        return self.adb

    def get_random_string(self):
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for i in range(7))
        return result_str

    def screenshot(self):
        self.name = str(self.get_random_string())
        self.thispath = os.getcwd()+"/"+self.name+".png"
        self.screenshot_filename = "/sdcard/" + self.name  + ".png"
        print(self.warna.G + "Taking screenshot...")
        self.send("shell screencap " + self.screenshot_filename)
        print(self.warna.G + "Downloading "+self.name+".png")
        self.download(self.screenshot_filename,self.thispath)
        print(self.warna.G + "Saved to "+self.thispath)
        self.send("shell rm " + self.screenshot_filename)

    def open_url(self,args):
        if not args.startswith(("http://", "https://")):
            args = "http://" + args
        print(self.send("shell \"am start -a android.intent.action.VIEW -d "+args+"\""))

    def get_apps(self):
        print(self.send("shell 'pm list packages -f'"))

    def screen(self):
        cek = subprocess.getoutput("scrcpy -h")
        if "Usage: scrcpy [options]" in cek:
            os.system("xterm -e scrcpy &")
        else:
            print(warna.W+"scrcpy not installed")
            print(warna.I+"Download scrcpy here https://github.com/Genymobile/scrcpy")
