import time
import keyboard
import pyautogui
from tkinter import *
import os
import sys


def resource_path(relative_path):

    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def typer():
    global sele
    speed = 0.003
    if sele.get() == "Normal":
        speed = 0.09
    elif sele.get() == "Fast":
        speed = 0.04
    else:
        speed = 0.005

    text = tex.get(1.0, "end")
    time.sleep(5)
    pyautogui.typewrite(text, interval=speed)


def typer1():
    text = tex.get(1.0, "end")
    time.sleep(2)
    pyautogui.typewrite(text, interval=0.003)


root = Tk()
root.title("Auto Typer")
root.geometry("820x830")
root.resizable(False, False)
raj=resource_path("autotyper.ico")
root.wm_iconbitmap(raj)
root.configure(bg="black")

f1 = Frame(root, bg="white", height=30)
f1.grid(sticky="w", columnspan=2)
weltext = Label(f1, text="Welcome to Autotyper                                                       ", bg="white",
                font=('Georgia bold', 16))
weltext.grid(sticky="w", columnspan=2)

tex = Text(root, background="white", font=("Tahoma", 11), padx=10, height=23, width=65, borderwidth=6)
tex.grid(row=1, column=0, columnspan=2)
warn = Label(root, text="By clicking button, typing will start in 5 seconds", bg="black", fg="white",
             font=('Arial bold', 12))
warn2 = Label(root, text="Or you can press Ctrl+d to start super fast typing", bg="black", fg="white",
              font=('Arial bold', 12))
btn = Button(root, text="GO", command=typer, padx=5, width=5, font=("Arial bold", 12), fg="white", bg="red")
btn.grid(row=2, column=1, sticky="e")
typ = ["Normal", "Fast", "Superfast"]
sele = StringVar()
sele.set("Speed")
drop = OptionMenu(root, sele, *typ)
drop.grid(row=2, column=0, sticky="w", padx=20)
warn.grid()
warn2.grid()
keyboard.add_hotkey('ctrl+d', typer1)
root.mainloop()
