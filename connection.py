#!/usr/bin/env python3
import subprocess
from tkinter import filedialog
import threading 

class connection():
    def __init__(self):
        self.filePath = filedialog.askopenfilename(
            initialdir="/home/",
            title = "Open .ovpn file",
            filetypes = (("ovpn files", "*.ovpn"),
                         ("all files", ".*"))
        )
        self.ovpn_thread = threading.Thread(target=self.ovpn, args = (self.filePath,))
        self.ovpn_thread.start()


    def ovpn(self, filePath):
        proc = subprocess.Popen(['sudo',
                                'openvpn',
                                "--config",
                                filePath])
        proc.communicate()[0]        

    def disconnect(self):
        subprocess.run(["sudo", "killall", "openvpn"])