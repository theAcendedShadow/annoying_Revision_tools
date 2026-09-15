import tkinter as tk
import random
import time
import customtkinter as ctk
import os
from os import system as system
import json
import sys

THEME_BG = "#f0f0f0"
THEME_FG = "#1a1a1a"
THEME_ACCENT = "#952ae1"
THEME_ACCENT_FG = "#bb1515"
THEME_FIELD_BG = "#e23232"
THEME_FONT_FAMILY = "Helvetica"
THEME_FONT_SIZE = 15


class ToolTip:
    """Small hover tooltip. tkinter has no built-in one."""

    def __init__(self, widget, text, delay=500):
        self.widget = widget
        self.text = text
        self.delay = delay
        self.tip = None
        self._job = None
        # add="+" so this never replaces bindings the widget already has.
        widget.bind("<Enter>", self._schedule, add="+")
        widget.bind("<Leave>", self._hide, add="+")
        widget.bind("<ButtonPress>", self._hide, add="+")

    def _schedule(self, _event=None):
        self._cancel()
        self._job = self.widget.after(self.delay, self._show)

    def _cancel(self):
        if self._job is not None:
            self.widget.after_cancel(self._job)
            self._job = None

    def _show(self):
        if self.tip is not None:
            return
        x = self.widget.winfo_rootx() + 12
        y = self.widget.winfo_rooty() + self.widget.winfo_height() + 6
        self.tip = tk.Toplevel(self.widget)
        # No title bar or border — it should look like a tooltip, not a window.
        self.tip.wm_overrideredirect(True)
        self.tip.wm_geometry(f"+{x}+{y}")
        tk.Label(
            self.tip,
            text=self.text,
            justify="left",
            background="#ffffe0",
            relief="solid",
            borderwidth=1,
            padx=6,
            pady=3,
        ).pack()

    def _hide(self, _event=None):
        self._cancel()
        if self.tip is not None:
            self.tip.destroy()
            self.tip = None



class window:
    def __init__(self, configure):
        self.root = ctk.CTk()
        self.configuration = configure
        self.configure()

        self.root.mainloop()

    def configure(self):
        self.configuration(self)

def config_1(self):
    self.root.title("Lazlo's App")
    self.root.geometry("1000x1000+2000+2000")
    self.root.minsize(750, 750)
    return(self.root)

def config_2(self):
    self.root.title("Do Some Work! D:")

    height = self.root.winfo_screenheight()
    width = self.root.winfo_screenwidth()

    height = random.randint(int(height / 3), int(height))
    width = random.randint(int(height / 3), int(height))

    height, width = int(height), int(width)
    randomOffset1 = random.randint(-3000, 3000)
    randomOffset2 = random.randint(-3000, 3000)

    self.root.geometry(f"{height}x{width}+{randomOffset1}+{randomOffset2}")
    self.root.minsize(width, height)

    questions = ["What is 5 squared", "When was slavery abolished within England?", "Find the Radius of: \n X squared + Y squared = 25", 
                 "What was the name of the largest death camp during WW2?"]
    answers = ["25", "1807", "5", "Auchwitz"]
    falseanswer1 = ["35", "1833", "6", "Poland"]
    falseanswer2 = ["20", "1901", "10", "Hitler"]
    num = random.randint(0, 3)
    answersCache = [answers[num], falseanswer1[num], falseanswer2[num]]
    print(answersCache)
    random.shuffle(answersCache)
    answersCache = ["Click to select answer"] + answersCache
    print(answersCache)

    def on_select(answer, correctanswer, self, command):
        correct = False
        command = command.get()
        print(command)
        if answer == correctanswer:
            correct = True
        self.root.destroy()
        if command == "adminroot":
            print(command)
            app = window(config_3)
            return
        if not correct:
            app = window(config_2)



    answer = None
    ctk.CTkLabel(self.root, text="Complete This Question To Continue About Your Work:", font=ctk.CTkFont(family=THEME_FONT_FAMILY, size=THEME_FONT_SIZE)).pack()
    ctk.CTkLabel(self.root, text=questions[num], font=ctk.CTkFont(family=THEME_FONT_FAMILY, size=THEME_FONT_SIZE)).pack()
    ctk.CTkComboBox(self.root, width=1000  ,values=answersCache, variable=answer, command=lambda answer: on_select(answer, answers[num], self, entry), font=ctk.CTkFont(family=THEME_FONT_FAMILY, size=THEME_FONT_SIZE)).pack()
    entry = ctk.CTkEntry(self.root, width=200, placeholder_text="Commandline")
    entry.pack()

    self.root.attributes("-topmost", True)


def config_3(self):
    def terminate():
        sys.exit("Admin Override")
    self.root.title("Admin Panel")
    self.root.minsize(500, 500)
    self.button1 = tk.Button(self.root, text="Terminate", command=terminate).pack()

for i in range(20):
    delay = random.randint(1, 20)
    time.sleep(delay)
    app1 = window(config_2)


print("done")