from tkinter import *
import tkinter as tk

root=tk.Tk()
root.iconbitmap(r'cal.ico')
root.title("simple calculator")
entry=tk.Entry(root,width=35,borderwidth=5)
entry.grid(row=0,column=0,columnspan=6,padx=10,pady=10)

def add_element(number):
    comman=entry.get()
    entry.delete(0,END)
    entry.insert(0, str(comman)+str(number))

def clear_function():
     entry.delete(0,END)

def add():
     first_number=entry.get()
     global f_num
     global math
     math="addition"
     f_num= int(first_number)   
     entry.delete(0,END)

def button_equal():
     second_number=entry.get()
     entry.delete(0,END)
     if math=="addition":
          entry.insert(0,f_num + int(second_number))
     if math=="substract":
          entry.insert(0,f_num - int(second_number))
     if math=="multiply":
          entry.insert(0,f_num * int(second_number))
     if math=="division":
          entry.insert(0,f_num / int(second_number))

def substract():
     first_number=entry.get()
     global f_num
     global math
     math="substract"
     f_num = int(first_number)   
     entry.delete(0,END)
     
def multiply():
     first_number=entry.get()
     global f_num
     global math
     math="multiply"
     f_num= int(first_number)   
     entry.delete(0,END)
def divide():
     first_number=entry.get()
     global f_num
     global math
     math="division"
     f_num= int(first_number)   
     entry.delete(0,END)

button1=tk.Button(root,text="1",padx=40,pady=20,bg="pink",command=lambda:add_element(1))
button1.grid(row=3,column=1)
button2=tk.Button(root,text="2",padx=40,pady=20,bg="pink",command=lambda:add_element(2))
button2.grid(row=3,column=2)
button3=tk.Button(root,text="3",padx=40,pady=20,bg="pink",command=lambda:add_element(3))
button3.grid(row=3,column=3)

button4=tk.Button(root,text="4",padx=40,pady=20,bg="pink",command=lambda:add_element(4))
button4.grid(row=2,column=1)
button5=tk.Button(root,text="5",padx=40,pady=20,bg="pink",command=lambda:add_element(5))
button5.grid(row=2,column=2)
button6=tk.Button(root,text="6",padx=40,pady=20,bg="pink",command=lambda:add_element(6))
button6.grid(row=2,column=3)

button7=tk.Button(root,text="7",padx=40,pady=20,bg="pink",command=lambda:add_element(7))
button7.grid(row=1,column=3)
button8=tk.Button(root,text="8",padx=40,pady=20,bg="pink",command=lambda:add_element(8))
button8.grid(row=1,column=2)
button9=tk.Button(root,text="9",padx=40,pady=20,bg="pink",command=lambda:add_element(9))
button9.grid(row=1,column=1)

button0=tk.Button(root,text="0",padx=40,pady=20,bg="pink",command=lambda:add_element(0))
button0.grid(row=4,column=2)

button_add=tk.Button(root,text="+",padx=40,pady=20,bg="skyblue",command=add)
button_add.grid(row=4,column=4)
button_sub=tk.Button(root,text="-",padx=40,pady=20,bg="skyblue",command=substract)
button_sub.grid(row=3,column=4)
button_mul=tk.Button(root,text="*",padx=40,pady=20,bg="skyblue",command=multiply)
button_mul.grid(row=2,column=4)
button_div=tk.Button(root,text="/",padx=40,pady=20,bg="skyblue",command=divide)
button_div.grid(row=1,column=4)

button_clear=tk.Button(root,text="clear",padx=30,pady=20,bg="lightgreen",command=clear_function)
button_clear.grid(row=4,column=1)
button_equal=tk.Button(root,text="=",padx=40,pady=20,bg="lightgreen",command=button_equal)
button_equal.grid(row=4,column=3)



root.mainloop()