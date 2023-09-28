from tkinter import *
import tkinter as tk

wm=tk.Tk()
wm.iconbitmap(r'check.ico')
wm.geometry("500x500")
wm.title("to do list")
my_list=Listbox(wm,font=('arial',20),width=25,height=5)
my_list.grid(row=5,column=3)

def create():
    my_list.insert(END,a.get())
    a.delete(0,END)

def delete():
    my_list.delete(ANCHOR)
def cross_button():
    my_list.itemconfig(my_list.curselection(),fg="red")
    my_list.select_clear(0,END)

def uncross_button():
    my_list.itemconfig(my_list.curselection(),fg="green")
    my_list.select_clear(0,END)

label1=tk.Label(wm,text="ENTER YOUR TASK:",fg='green',font=('arial',15))
label1.grid(row=1,column=1)
a=tk.Entry(wm,bg='blue',fg='white',font=('arial',15))
a.grid(row=1,column=2)
bot2=tk.Button(wm,text="create",font=('arial',10),bg='pink',command=create)
bot2.grid(row=1,column=4)
bot3=tk.Button(wm,text="delete",font=('arial',10),bg='pink',command=delete)
bot3.grid(row=1,column=7)
bot4=tk.Button(wm,text="cross-button",font=('arial',10),bg='pink',command=cross_button)
bot4.grid(row=1,column=5)
bot5=tk.Button(wm,text="uncross-button",font=('arial',10),bg='pink',command=uncross_button)
bot5.grid(row=1,column=6)


wm.mainloop()
