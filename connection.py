#!/usr/bin/env python3
import subprocess
from tkinter import filedialog

class connection():
    def __init__(self):
        self.filePath = filedialog.askopenfilename(
            initialdir="/home/",
            title = "Open .ovpn file",
            filetypes = (("ovpn files", "*.ovpn"),
                         ("all files", ".*"))
        )

        proc = subprocess.Popen(['/usr/sbin/openvpn',
                                "--config",
                                self.filePath])
        out = proc.communicate()[0]

    def disconnect(self):
        subprocess.run(["sudo", "killall", "openvpn"])
