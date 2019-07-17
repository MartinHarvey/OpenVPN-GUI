from tkinter import Tk, Label, Button

class Window:
    def __init__(self, master):
        #set the window 
        master.title("OpenVPN-GUI")

        self.openButton = Button(master, text="Open File"
                                )
        self.openButton.pack()

        self.disconnectButton = Button(master, text = "Disconnect from Server",
                                        )
        self.disconnectButton.pack()





