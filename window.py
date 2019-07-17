from tkinter import Tk, Label, Button, Text
from connection import *

class Window:
    def __init__(self, master):
        #Set a instance of command class to null for now
        self.con = None
        #set the window title
        master.title("OpenVPN-GUI")

        self.openButton = Button(
            master, 
            text="Open File",
            command = lambda: Window.Open(self))
        self.openButton.pack()

        self.disconnectButton = Button(
            master, 
            text = "Disconnect from Server",
            command = lambda: Window.disconnect(self),
            state = 'disabled')
        self.disconnectButton.pack()

        self.statusText = Label(
            master,
            height = 4,
            width = 25           
        )
        self.statusText.pack()
    

    def Open(self):
        self.con = connection()
        self.disconnectButton['state'] = 'normal'
    
    def disconnect(self):
        self.con.disconnect()

    







