#!/usr/bin/env python
# -*- coding: utf-8 -*-

# from tkinter import Tk, Scrollbar, Frame
import collegeInfo
import dean
import reminder
import yanghua
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Treeview
import sys
import webbrowser
import time
import _thread


def whileTrue():
    i = 1  # . an hour 60 min
    while True:
        time.sleep(2)
        i -= 1
        checkUpdate()
        if i==0:
            reminder.show_reminder()


def checkUpdate():
    reminder.show_update('关于2017年“国庆节”“中秋节”假期安排及安全注意事项的通知')


sys.path.append("libs")


def openbrowser(url):
    # url = 'http://www.baidu.com'
    webbrowser.open(url)


# 创建tkinter应用程序窗口
root = Tk()
w, h = root.maxsize()
root.geometry("{}x{}".format(w, h))
# 设置窗口大小和位置
# root.geometry('1000x600+200+300')

# 不允许改变窗口大小
# root.resizable(False, False)
root.resizable(True, True)

# 设置窗口标题
root.title('校内公告助手')

# lable
ttk.Label(root, text="选择新闻来源:").grid(column=0, row=0)  # 设置其在界面中出现的位置  column代表列   row 代表行
ttk.Label(root, text="选择时间范围").grid(column=1, row=0)  # 添加一个标签，并将其列设置为1，行设置为0


# ttk.Label(root, text="选择新闻来源:").pack()      # 设置其在界面中出现的位置  column代表列   row 代表行
# ttk.Label(root, text="选择时间范围").pack()    # 添加一个标签，并将其列设置为1，行设置为0

def clickMe():
    updateData()
    # print(name.get())
    # print(number.get())
    pass


# 按钮
action = ttk.Button(root, text="确定", command=clickMe)  # 创建一个按钮, text：显示按钮上面显示的文字, command：当这个按钮被点击之后会调用command函数
action.grid(column=2, row=1)  # 设置其在界面中出现的位置  column代表列   row 代表行
# action.pack()

# 创建一个下拉列表
name = StringVar()  # StringVar是Tk库内部定义的字符串变量类型，在这里用于管理部件上面的字符；不过一般用在按钮button上。改变StringVar，按钮上的文字也随之改变。
nameEntered = ttk.Combobox(root, width=12,
                           textvariable=name)  # 创建一个文本框，定义长度为12个字符长度，并且将文本框中的内容绑定到上一句定义的name变量上，方便clickMe调用
nameEntered.grid(column=0, row=1)  # 设置其在界面中出现的位置  column代表列   row 代表行
# nameEntered.pack()
nameEntered.focus()  # 当程序运行时,光标默认会出现在该文本框中
nameEntered['values'] = ('全部', '教务', '扬华', '信息学院')
nameEntered.current(0)

# 创建一个下拉列表
number = StringVar()
numberChosen = ttk.Combobox(root, width=12, textvariable=number)
numberChosen['values'] = ('最近一天', '最近三天', '最近一周', '最近一月')  # 设置下拉列表的值
# numberChosen['values'] = (1, 2, 3)     # 设置下拉列表的值
numberChosen.grid(column=1, row=1)  # 设置其在界面中出现的位置  column代表列   row 代表行
# numberChosen.pack()
numberChosen.current(0)  # 设置下拉列表默认显示的值，0为 numberChosen['values'] 的下标值

# 使用Treeview组件实现表格功能
frame = Frame(root)

# frame.place(x=0, y=10, width=900, height=700, relx = 0.05, rely = 0.)
frame.grid(column=0, row=2, rowspan=9, columnspan=9)
# frame.pack()
# 滚动条
scrollBar = Scrollbar(frame)
scrollBar.pack(side=RIGHT, fill=Y)

# Treeview组件，6列，显示表头，带垂直滚动条
tree = Treeview(frame, columns=('c1', 'c2', 'c3', 'c4'),
                show="headings",
                height=30,
                yscrollcommand=scrollBar.set)
w -= 25

# 设置每列宽度和对齐方式
tree.column('c1', width=int(w / 9), anchor='center')
tree.column('c2', width=int(w / 9), anchor='center')
tree.column('c3', width=int(w * 2 / 9), anchor='center')
tree.column('c4', width=int(5 * w / 9), anchor='w')

# 设置每列表头标题文本
tree.heading('c1', text='来源')
tree.heading('c2', text='标签')
tree.heading('c3', text='发布时间')
tree.heading('c4', text='标题')
tree.pack(side=LEFT, fill=Y)

# Treeview组件与垂直滚动条结合
scrollBar.config(command=tree.yview)


# 定义并绑定Treeview组件的鼠标单击事件
def treeviewClick(event):
    widget = event.widget
    # print (widget.identify_row(event.y))
    # print (widget.exists(widget.identify_row(event.y)))
    item = widget.item(widget.identify_row(event.y))

    # print (dir(widget.item(widget.identify_row(event.y))))
    # print (type(widget.item(widget.identify_row(event.y))))
    webbrowser.open(item['values'][4])




tree.bind('<Button-1>', treeviewClick)


def updateData():
    items = tree.get_children()
    [tree.delete(item) for item in items]

    data = collegeInfo.getInfo(number.get())
    # data = dean.getNewsFromDean(number.get()) + yanghua.getDefult()

    if name.get() == '全部':
        data = dean.getNewsFromDean(number.get()) + collegeInfo.getInfo(number.get())  + yanghua.getDefult()
    elif name.get() == '教务':
        data = dean.getNewsFromDean(number.get())
    elif name.get == '扬华':
        data = yanghua.getDefult()
    elif name.get() == '信息学院':
        data = collegeInfo.getInfo(number.get())

    data.sort(key=lambda obj: obj['time'], reverse=True)
    # 插入演示数据
    i = 0
    # print (number.get())
    for new in data:
        tree.insert('', i, values=[new['source'], new['tag'], new['time'][:16], new['title'], new['path']])
        i += 1



# 运行程序，启动事件循环
updateData()

try:
    _thread.start_new_thread(whileTrue, ())
except:
    print("Error: 无法启动线程")

root.mainloop()
