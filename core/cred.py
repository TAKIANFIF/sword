#!/usr/bin/python3

from prettytable import PrettyTable

class credential():
    def __init__(self):
        self.rhost = "\" \""
        self.rport = "5555"
        self.x = PrettyTable()
    def options(self,rhosts,rports):
        self.x.clear()
        self.x.add_column("Name",["RHOST","LPORT"])
        self.x.add_column("Current Setting",[rhosts,rports])
        self.x.add_column("Required",["yes","yes"])
        self.x.add_column("Description",["target ip","target port"])
        return self.x
