import subprocess
from tkinter import filedialog

class connection():
    def __init__(self):
        self.filePath = filedialog.askopenfilename(
            initialdir="/home/", 
            title = "Open .ovpn file",
            filetypes = (("ovpn files","*.ovpn"),
                         ("all files", ".*"))
        )

        proc = subprocess.Popen(['/usr/local/sbin/openvpn', 
                                "--config", 
                                self.filePath])
        proc.communicate()[0]
        
    
    def disconnect(self):
        subprocess.run(["sudo", "killall", "openvpn"])


    
    

        
