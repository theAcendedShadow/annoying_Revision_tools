import tkinter as tk
from tkinter import ttk
import random
import time
import customtkinter as ctk
import os
from os import system as system
import json
import sys
import obnx

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
    def __init__(self, configure, imports=None):
        #if parent is None:
        self.imports=imports
        self.root = ctk.CTk()
        self.configuration = configure
        self.configure()


        #self.root.mainloop()


    def configure(self):
        self.configuration(self)

def config_1(self):
    self.root.title("Lazlo's App")
    self.root.geometry("1000x1000+2000+2000")
    self.root.minsize(750, 750)
    return(self.root)

def config_2(self):
    imports = self.imports
    questions = imports[0]
    answers = imports[1]
    falseanswer1 = imports[2]
    falseanswer2 = imports[3]
    self.root.title("Do Some Work! D:")

    height = self.root.winfo_screenheight()
    width = self.root.winfo_screenwidth()

    height = random.randint(int(height / 3), int(height))
    width = random.randint(int(height / 3), int(height))

    height, width = int(height), int(width)
    randomOffset1 = random.randint(-height, height)
    randomOffset2 = random.randint(-width, width)

    self.root.geometry(f"{height}x{width}+{randomOffset1}+{randomOffset2}")
    self.root.minsize(width, height)

    if questions is None:
        questions = ["What is 5 squared", "When was slavery abolished within England?", "Find the Radius of: \n X squared + Y squared = 25", 
                     "What was the name of the largest death camp during WW2?"]
        answers = ["25", "1807", "5", "Auchwitz"]
        falseanswer1 = ["35", "1833", "6", "Poland"]
        falseanswer2 = ["20", "1901", "10", "Hitler"]
    num = random.randint(0, 3)
    self.questionnum = num
    answersCache = [answers[num], falseanswer1[num], falseanswer2[num]]
    random.shuffle(answersCache)
    answersCache = ["Click to select answer"] + answersCache

    def on_select(answer, correctanswer, self, entry):
        correct = False
        entry = entry.get()
        print(entry)
        if answer == correctanswer:
            correct = True
        if entry == "adminroot":
            print(entry)
            app = window(config_3)
            return
        if not correct:
            app = window(config_2)
            self.root.destroy()
            app.root.mainloop()
            return
        self.root.destroy()

    #todo fix the question applying


    ctk.CTkLabel(self.root, text="Complete This Question To Continue About Your Work:", font=ctk.CTkFont(family=THEME_FONT_FAMILY, size=THEME_FONT_SIZE)).pack()
    ctk.CTkLabel(self.root, text=questions[num], font=ctk.CTkFont(family=THEME_FONT_FAMILY, size=THEME_FONT_SIZE)).pack()
    answer = tk.StringVar()
    entry = tk.Entry(self.root, width=20)
    cmb = ctk.CTkComboBox(self.root, 
                          width=200,
                          values=answersCache,
                          variable=answer,
                          command=lambda chosen: on_select(chosen, answers[num], self, entry), font=ctk.CTkFont(family=THEME_FONT_FAMILY, size=THEME_FONT_SIZE))
    cmb.pack()
    entry.pack()

    self.root.attributes("-topmost", True)


def config_3(self):
    def terminate():
        sys.exit("Admin Override")
    self.root.title("Admin Panel")
    self.root.minsize(500, 500)
    self.button1 = tk.Button(self.root, text="Terminate", command=terminate).pack()

def setup_menu(self):
    #total_questions, min_delay, max_delay, questions, answers, fA1, fA2
    def submit(total_questions, min_delay, max_delay, questions, answers, fA1, fA2):
        for i in range(total_questions):
            question = window(lambda root: config_2(root, answers=answers, questions=questions, falseanswer1=fA1, falseanswer2=fA2))
            if min_delay and max_delay:
                delay = random.randint(min_delay, max_delay)
            elif min_delay:
                delay = min_delay
            elif max_delay:
                delay = max_delay
            else:
                delay = 60
            time.sleep(delay)

    def entry_fields(*args):
        x = self.entry1.get()
        y = combobox1.get()
        z = combobox2.get()
        w = combobox3.get()
        if x and y and z and w:
            button2.config(state="active")


    def open_questionmenu():
        question_get = window(add_questions)

    def get_questions():

        try:
            questions, answers, wrong_answer1, wrong_answer2 = obnx.load(self.entry1.get())
        except FileNotFoundError:
            print("ERROR: file does not exist")
            return
        except PermissionError:
            print("ERROR: insufficient permissions to open file")
            return
        exports = [questions, answers, wrong_answer1, wrong_answer2]
        if questions and answers and wrong_answer1 and wrong_answer2:
            #submit(min_delay=int(combobox3.get()), max_delay=int(combobox2.get()), )
            self.min_del = int(combobox3.get())
            self.max_del = int(combobox2.get())
            self.total = int(combobox1.get())
            self.exports=exports
            self.root.destroy()
#            for i in range(total):
#                question = window(config_2, exports)
#                delay = random.randint(min_del, max_del)
#                time.sleep(delay)
            
        return
    


    self.root.title("Setup Menu")
    self.root.minsize(1350, 1500)

    label1 = tk.Label(text="Please select a studypack.obnx below:", anchor="c")
    label1.place(x=50, y=50, height=40, width=600)

    self.entry1 = tk.Entry()
    self.entry1.place(x=50, height=40, width=600, y=90)
    self.entry1.Tooltip = ToolTip(widget=self.entry1, text="e.g. user/folder/obnxpack.obxn", delay=10)

    button1 = tk.Button(text="Add to or Create a new question pack", command=open_questionmenu)
    button1.place(x=700, height=80, width=600, y=50)

    label2 = tk.Label(text="Or", anchor="e")
    label2.place(x=655, height=80, width=40, y=50)

    label3 = tk.Label(text="Select total questions to answer:", anchor="w")
    label3.place(y=150, x=50, height=80, width=600)

    combobox1 = tk.Entry(self.root)
    combobox1.place(y=150, x=700, height=80, width=600)

    label4 = tk.Label(text="Select max delay between questions (seconds):", anchor="w")
    label4.place(y=250, x=50, height=80, width=600)

    combobox2 = tk.Entry(self.root)
    combobox2.place(y=250, x=700, height=80, width=600)

    label5 = tk.Label(text="Select min delay between questions (seconds):", anchor="w")
    label5.place(y=350, x=50, height=80, width=600)

    combobox3 = tk.Entry(self.root)
    combobox3.place(y=350, x=700, height=80, width=600)

    self.entry1.bind("<KeyRelease>", entry_fields)
    combobox1.bind("<KeyRelease>", entry_fields)
    combobox2.bind("<KeyRelease>", entry_fields)
    combobox3.bind("<KeyRelease>", entry_fields)

    button2 = tk.Button(text="Submit", command=get_questions, state="disabled")
    button2.place(height=80, y=550, x=50, width=1250)


def add_questions(self):
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

        obnx.dump(entry5, entry1, entry2, entry3, entry4)


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

print()





setup = window(setup_menu)
setup.root.mainloop()
if len(setup.exports[0]) >= setup.total:
    remove_completed_questions = True
else:
    remove_completed_questions = False
for i in range(setup.total):
    delay = random.randint(setup.min_del, setup.max_del)
    time.sleep(delay)
    app1 = window(config_2, setup.exports)
#    if remove_completed_questions:
#        setup.exports.pop(app1.questionnum)
    app1.root.mainloop()


print("Well done, you finished your revision!")

