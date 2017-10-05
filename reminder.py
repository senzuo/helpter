#!/usr/bin/python  
# -*- coding: utf-8 -*-  

from tkinter import *


def show_reminder():
    reminder = Tk()
    reminder.withdraw()
    screenwidth = reminder.winfo_screenwidth()
    screenheight = reminder.winfo_screenheight() - 100
    reminder.resizable(False, False)
    reminder.title("reminder")
    frame = Frame(reminder, relief=RIDGE, borderwidth=3)
    frame.pack(fill=BOTH, expand=1)
    label = Label(frame, text="又学习1小时了，shuai 渣了，站起来休息一下吧!")
    label.pack(fill=BOTH, expand=1)
    button = Button(frame, text="确定", font="Futura", fg="black", command=reminder.destroy)
    button.pack(side=BOTTOM)
    reminder.update_idletasks()
    reminder.deiconify()
    reminder.withdraw()

    # root.geometry('%sx%s+%s+%s' % (root.winfo_width() + 10, root.winfo_height() + 10, (screenwidth - root.winfo_width())/2, (screenheight - root.winfo_height())/2))    #窗口所在位置以及大小，前两个字符串代表窗口宽高，后两个字符串代表左上角坐标  
    reminder.deiconify()
    reminder.lift(aboveThis=None)
    reminder.mainloop()


def show_update(title):
    reminder = Tk()
    reminder.withdraw()
    screenwidth = reminder.winfo_screenwidth()
    screenheight = reminder.winfo_screenheight() - 100
    reminder.resizable(False, False)
    reminder.title("reminder")
    frame = Frame(reminder, relief=RIDGE, borderwidth=3)
    frame.pack(fill=BOTH, expand=1)
    label = Label(frame, text="有新的公告，" + title, font="Monotype\ Corsiva -20 bold")
    label.pack(fill=BOTH, expand=1)
    button = Button(frame, text="确定", font="Futura", fg="black", command=reminder.destroy)
    button.pack(side=BOTTOM)
    reminder.update_idletasks()
    reminder.deiconify()
    reminder.withdraw()

    # root.geometry('%sx%s+%s+%s' % (root.winfo_width() + 10, root.winfo_height() + 10, (screenwidth - root.winfo_width())/2, (screenheight - root.winfo_height())/2))    #窗口所在位置以及大小，前两个字符串代表窗口宽高，后两个字符串代表左上角坐标
    reminder.deiconify()
    reminder.lift(aboveThis=None)
    reminder.mainloop()
