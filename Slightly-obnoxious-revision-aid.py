import tkinter as tk
import random
import time
import customtkinter as ctk
import os
from os import system as system
import json
import sys
import obxn

THEME_BG = "#f0f0f0"
THEME_FG = "#1a1a1a"
THEME_ACCENT = "#952ae1"
THEME_ACCENT_FG = "#bb1515"
THEME_FIELD_BG = "#e23232"
THEME_FONT_FAMILY = "Helvetica"
THEME_FONT_SIZE = 15

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

def setup_menu(self):
    def open_questionmenu():
        window(add_questions)

    self.root.title("Setup Menu")
    self.root.minsize(1000, 1500)

    label1 = tk.Label(text= "Please enter the name of a .obnx file, leave blank to use default questions", anchor="e").place(x=50, y=50)

    self.entry1 = tk.Entry()
    self.entry1.place(x=50, height=40, width=600, y=100)

    button1 = tk.Button(text="Add to or Create a new question pack", command=open_questionmenu).place(x=50, height=40, width=600, y=150)



def add_questions(self):

    def disable_button():
        self.button.config(state=tk.DISABLED)

    def enable_button():
        self.button.config(state=tk.NORMAL)

    def submit():
        entry1 = self.entry1.get()
        entry2 = self.entry2.get()
        entry3 = self.entry3.get()
        entry4 = self.entry4.get()
        entry5 = self.entry5.get()

        self.entry1.delete(0, tk.END)
        self.entry2.delete(0, tk.END)
        self.entry3.delete(0, tk.END)
        self.entry4.delete(0, tk.END)
        self.button.config(state="disabled")

        obxn.dump(entry5, entry1, entry2, entry3, entry4)


    def entry_fields(*args):
        x = self.entry1.get()
        y = self.entry2.get()
        z = self.entry3.get()
        w = self.entry4.get()
        v = self.entry5.get()
        if x and y and z and w and v:
            self.button.config(state="active")
        

    def printanswr(*args):
        toPrint = self.entry1.get()
        print(toPrint)

    self.root.title("Add Questions!")
    self.root.minsize(1000, 1500)

    self.tV1 = tk.StringVar()
    self.tV1.trace_add("write", printanswr)


    self.tV2 = tk.StringVar()
    self.tV2.trace_add("write", entry_fields)


    self.tV3 = tk.StringVar()
    self.tV3.trace_add("write", entry_fields)


    self.tV4 = tk.StringVar()
    self.tV4.trace_add("write", entry_fields)

    label1 = tk.Label(text= "Please enter a question to ask:", master=self.root)
    label1.place(x=50, y=50, width=800)
    self.entry1 = tk.Entry(self.root, textvariable=self.tV1)
    self.entry1.place(x=50, y=100, width=800)
    self.entry1.focus_set()
    self.entry1.bind("<KeyRelease>", entry_fields)

    label2 = tk.Label(text= "Please enter the correct answer:", master=self.root)
    label2.place(x=50, y=150, width=800)
    self.entry2 = tk.Entry(master=self.root, textvariable=self.tV2)
    self.entry2.place(x=50, y=200, width=800)
    self.entry2.focus_set()
    self.entry2.bind("<KeyRelease>", entry_fields)

    label3 = tk.Label(text= "Please enter an incorrect answer:", master=self.root)
    label3.place(x=50, y=250, width=800)
    self.entry3 = tk.Entry(master=self.root, textvariable=self.tV3)
    self.entry3.place(x=50, y=300, width=800)
    self.entry3.focus_set()
    self.entry3.bind("<KeyRelease>", entry_fields)

    label4 = tk.Label(text= "Please enter another incorrect answer:", master=self.root)
    label4.place(x=50, y=350, width=800)
    self.entry4 = tk.Entry(master=self.root, textvariable=self.tV4)
    self.entry4.place(x=50, y=400, width=800)
    self.entry4.focus_set()
    self.entry4.bind("<KeyRelease>", entry_fields)

    label5 = tk.Label(self.root, text="name and filepath of file to edit or create")
    label5.place(x=50, y=800, width=800)
    self.entry5 = tk.Entry(self.root)
    self.entry5.place(x=50, y=850, width=800)
    self.entry5.focus_set()
    self.entry5.bind("<KeyRelease>", entry_fields)

    self.button = tk.Button(master=self.root,state="disabled", text="Submit", command=submit)
    self.button.place(x=50, y=600, width=800)







setup = window(setup_menu)
#for i in range(20):
#    delay = random.randint(1, 20)
#    time.sleep(delay)
#    app1 = window(config_2)


print("done")