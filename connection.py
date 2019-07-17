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
    
        subprocess.run(["openvpn", "--config", self.filePath])
    
    def disconnect(self):
        subprocess.run(["sudo", "killall", "openvpn"])


    
    

        
