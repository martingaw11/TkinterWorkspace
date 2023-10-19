from tkinter import *
from tkinter import ttk
from Client import Client

class ControlPanel:

    def __init__(self, root):
        self.client = Client()
        root.title("Hyper Loop Chicago Control Pod")
        root.geometry("500x250")
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        # Binding keys for universal control
        root.bind("<space>", self.spaceToggle)
        root.bind("<Escape>", self.escapeToggle)
        root.bind("<Up>", self.accelerate)
        root.bind("<Down>", self.decelerate)       

        # Creating a Content Frame
        mainframe = ttk.Frame(root, padding="12", width=250, height=200)
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

        # Creating tracker for brake status
        self.brakeStatus = StringVar()
        self.brakeStatus.set("Brakes: OFF")

        self.speed = IntVar()
        self.speed.set(0)

        # Creating the Brake Label Widget
        ttk.Label(mainframe, textvariable=self.brakeStatus).grid(column=0, row=1, columnspan=1, sticky=(W, E))

        # Creating the Speed Label Widget
        ttk.Label(mainframe, text='Speed:').grid(column=0, row=2, sticky=(W, E))
        ttk.Label(mainframe, textvariable=self.speed).grid(column=1, row=2, sticky=(W, E))

        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)

    # On space key, toggle brakes
    def spaceToggle(self, *args):
        print("spaceToggle")
        if self.brakeStatus.get() == "Brakes: ON":
            self.brakeStatus.set("Brakes: OFF")
            self.client.send_command("Brakes: Off")
        else:
            self.brakeStatus.set("Brakes: ON")
            self.client.send_command("Brakes: On")

    '''
    BIG THING TO CONSIDER:
        THE CONTROL PANEL SHOULD NOT REFLECT CHANGES MADE TO
        CONTROL PANEL VARIABLES, INSTEAD IT SHOULD SEND THOSE
        CHANGE TO THE SERVER WHICH WILL PROCESS THE CHANGE, 
        THEN SEND BACK INFORMATION LEADING TO A VISIBLE CHANGE
        IN THE VALUE EFFECTED BY THE CHANGE.

        THIS IS THE ONLY WAY WE KNOW FOR SURE IF THE SPEED HAS 
        CHANGED, AND THE ONLY WAY TO KEEP THE CONTROL PANEL AND 
        THE SERVER IN SYNC. 

        PROCESS THESE CHANGES SOON, AND MAKE SURE TO UPDATE THE
        CONTROL PANEL TO REFLECT THE CHANGES MADE BY THE SERVER.
    '''

    # On up key, increase speed by 1
    def accelerate(self, *args):
        if (self.speed.get() < 100):
            self.speed.set(self.speed.get() + 1)
            self.client.send_command("Speed: " + str(self.speed.get()))
        else:
            pass

    # On down key, decrease speed by 1
    def decelerate(self, *args):
        if (self.speed.get() > 0):
            self.speed.set(self.speed.get() - 1)
            self.client.send_command("Speed: " + str(self.speed.get()))
        else:
            pass

    # On escape key, close the client and window
    def escapeToggle(self, *args):
        self.client.send_command("exit")
        self.client.close()
        root.quit()




root = Tk()

ControlPanel(root)

root.mainloop()
