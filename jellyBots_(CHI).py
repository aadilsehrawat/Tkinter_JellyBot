import random
import subprocess
from tkinter import messagebox

from Module_2.PoseDetector.PoseModule import main_poseModule
from Module_3.DrownModule.DrownModule import main_drownModule

import tkinter as tk
from tkinter import *
from tkinter.constants import ANCHOR, BOTTOM, E, END, NW, SUNKEN, TRUE, W

# GUI Window
root = tk.Tk()
canvas = tk.Canvas(root, width=650, height=690)
canvas.pack(fill="both", expand=TRUE)
root.minsize(width=650, height=690)
root.maxsize(width=650, height=690)
root.iconbitmap('data/images/jellyfish.ico')
root.title("Jelly Bot Testing")

alert_delay=random.randint(5, 9)

def start(self):
    self.after(alert_delay,lambda:warning("Urgent"))

def comingSoon(function):
    messagebox.showinfo(function, "Application is still under build \nThis feature will be added soon !" )

def jellybot_details(function):
    messagebox.showinfo(function, "Team Members: \nMohammad Aadil Sehrawat\nKaran Allagh" )

def warning(function):
    messagebox.showerror(function, "Drown Alert")

def passit():
    pass

def main_rescuePlanning():
    from Module_4.PathPlanning.RRT_PathPlanningAlgorithm_ForJellyBot import main_pathPlanning
    main_pathPlanning()

def main_humanModule():
    try:
        import subprocess
        subprocess.call(['sh', 'data/shell_script/test.sh'])
    
    except: 
        main_drownModule("detect_human.mp4")

def README_File():
    subprocess.call('README.txt', shell=True)

background = tk.PhotoImage(file="data/images/background.png")
canvas.create_image(0,0, image=background, anchor=NW)


mainmenu = tk.Menu(root)
m1 = tk.Menu(mainmenu, tearoff=0)
m1.add_command(label="JELLY BOT", command= lambda: jellybot_details("Team Members"))
m1.add_separator()
m1.add_command(label="Exit", command=quit)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="Main", menu=m1)

m2 = tk.Menu(mainmenu, tearoff=0)
m2.add_command(label="READ-ME", command= lambda: README_File())
m2.add_separator()
m2.add_command(label="Exit", command=quit)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="Miscellaneous", menu=m2)

# displayResult=
canvas.create_text(317,80, text="Jelly Bot" , font="Times 50 bold", fill="#fafefe")
# canvas.create_window(180,20, anchor=NW, window=displayResult)

# Check Button which calls a funciton 
# Which further calls all the sub-modules of the main project
checkButton = tk.Button(root, text="Human Detection", command=lambda:main_humanModule(), font="Raleway", bg="#07858E", fg="white", border="5", height=2, width=15)
canvas.create_window(253,150, anchor=NW, window=checkButton)

checkButton = tk.Button(root, text="Pose Detector", command=lambda:main_poseModule(), font="Raleway", bg="#07858E", fg="white", border="5", height=2, width=15)
canvas.create_window(253,250, anchor=NW, window=checkButton)

checkButton = tk.Button(root, text="Drown Detection", command=lambda:main_drownModule("detect_drown.mp4"), font="Raleway", bg="#07858E", fg="white", border="5", height=2, width=15)
canvas.create_window(253,350, anchor=NW, window=checkButton)

checkButton = tk.Button(root, text="Rescue Planning", command=lambda:main_rescuePlanning(), font="Raleway", bg="#07858E", fg="white", border="5", height=2, width=15)
canvas.create_window(253,450, anchor=NW, window=checkButton)

checkButton = tk.Button(root, text="Exit", command=quit, font="Raleway", bg="#706353", fg="white", border="5", height=2, width=15)
canvas.create_window(253,550, anchor=NW, window=checkButton)

# Status Bar
statusvar = tk.StringVar()
statusvar.set(" Ready\t   |")
sbar = tk.Label(canvas, textvariable=statusvar, bd=1, relief=SUNKEN, anchor=W)
sbar.pack(side=BOTTOM, fill="x")

root.mainloop()