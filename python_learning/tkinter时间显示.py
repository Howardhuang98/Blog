import tkinter
from tkinter import *
import datetime


def get_time():
    a = datetime.datetime.now()
    time_str = "{}:{}:{} \n {}/{}/{}".format(a.time().hour, a.time().minute, a.time().second, a.date().year,
                                             a.date().month, a.date().day)
    return time_str


def update_time(label: tkinter.Label):
    label.configure(text=get_time())
    label.after(100, update_time, label)


if __name__ == '__main__':
    # 窗口
    window = Tk()
    window.title("windows")
    window.geometry("500x500")
    # 时间显示
    time_str = get_time()
    lbl = Label(window, text=time_str, font=("微软雅黑:", 50))
    lbl.grid(column=1, row=0)
    update_time(lbl)
    # 图片
    tkinter.Image()

    window.mainloop()
