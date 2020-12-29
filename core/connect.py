#!/usr/bin/python3

import subprocess
from core.command import *
from banner.color import *

class conn:
    def __init__(self):
        self.version = "2.1"
        self.konek = False
        self.ip = []
        self.port = []
        self.perintah = com()
        self.warna = warna()

    def net(self,ip,port):
        self.out = self.perintah.send("connect {}:{}".format(ip,port))
        self.ip.append(ip)
        self.port.append(port)
        return self.out

    def start_server(self):
        self.st = self.perintah.send("start-server")
        return "{}Server Start".format(self.warna.S,)

    def stop_server(self):
        self.stop = self.perintah.send("kill-server")
        return "{}Server Stop".format(self.warna.E,)

    def cek_con(self):
        self.cn = self.perintah.send("devices")
        if self.ip[0] in self.cn:
            self.konek = True
        else:
            self.konek = False
        return self.konek
