from tkinter import *
import os

def run():

    qualifying = 0
    gate = 0
    path = 0
    dice = 0
    fakeIsland = 0

    if v.get() == "Custom Run":
        if v1.get() == 1:
            gate = 1  
        else:
            gate = 0  

        if v2.get() == 1:
            path = 1   
        else:
            path = 0         
        
        if v3.get() == 1:
            dice = 1
        else:
            dice = 0
        
        if v4.get() == 1:
            fakeIsland = 1
        else:
            fakeIsland = 0
            
    elif v.get() == "Qualifying Run":
        qualifying = 1

    elif v.get() == "Full Run":
        qualifying = 0
        gate = 1
        path = 1
        dice = 1
        fakeIsland = 1

    elif v.get() == "Half Run":
        qualifying = 0
        gate = 1
        path = 1
        dice = 0
        fakeIsland = 0
    
    os.system("python " + os.path.dirname(__file__) + "/missionLogic.py " + str(qualifying) + " " + str(gate) + " " + str(path) + " " + str(dice) + " " + str(fakeIsland));
    
root = Tk()

MODES = [
        ("Qualifying Run", "Qualifying Run"),
        ("Full Run", "Full Run"),
        ("Half Run", "Half Run"),
        ("Custom Run", "Custom Run"),
    ]

v = StringVar()
v.set("1") # initialize

for text, mode in MODES:
    b = Radiobutton(root, text=text, variable=v, value=mode)
    b.pack(anchor=W)

v1 = IntVar()
v2 = IntVar()
v3 = IntVar()
v4 = IntVar()

c1 = Checkbutton(root, text="Gate 1", variable=v1).pack(anchor=W, padx=20)
c2 = Checkbutton(root, text="Follow Path", variable=v2).pack(anchor=W, padx=20)
c3 = Checkbutton(root, text="Dice", variable=v3).pack(anchor=W, padx=20)
c4 = Checkbutton(root, text="Island", variable=v4).pack(anchor=W, padx=20)

Button(root, 
       text='RUN', 
       fg="darkgreen", 
       command=run).pack(side=RIGHT, padx=10, pady=10)

mainloop()