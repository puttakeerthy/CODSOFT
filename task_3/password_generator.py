import random
from tkinter import * 
from tkinter import messagebox
import tkinter as tk

root=Tk()
root.geometry("500x500")
root.title("PASSWORD_GENERATOR")
global a,b,c
def entred():
    entry_4.delete(0,END)
    global a,b,c
    a=entry_1.get()
    b=entry_2.get()
    c=entry_3.get()
        
    if (a=="" and b=="" and c==""):
        messagebox.showerror("wrong entry","you have to enter something")
        messagebox.showwarning("entry error","you must have to enter numbers 'ONLY'")
    entry_1.delete(0,END)
    entry_2.delete(0,END)
    entry_3.delete(0,END)

def password_generator(number1,number2,number3):
    entry_4.delete(0,END)
    letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    numbers=['1','2','3','4','5','6','7','8','9','0']
    symbols=['!','@','#','$','%','^','&','*','(',')']
    password=[]
    for i in range(1,int(number1)+1):
        password+=random.choice(letters)
    for i in range(1,int(number2)+1):
        password+=random.choice(numbers)
    for i in range(1,int(number3)+1):
        password+=random.choice(symbols)
    random.shuffle(password)
    pass_word=""
    for char in password:
        pass_word+=char
    entry_4.insert(0,pass_word)
    
    
label_1=tk.Label(root,text="HOW MANY LETTERS YOU WANT IN YOUR PASSWORD?",fg="brown",bg="yellow")
label_2=tk.Label(root,text="HOW MANY NUMBERS YOU WANT IN YOUR PASSWORD?",fg="brown",bg="yellow")
label_3=tk.Label(root,text="HOW MANY SYMBOLS YOU WANT IN YOUR PASSWORD?",fg="brown",bg="yellow")
label_1.grid(row=1,column=1,padx=10,pady=10)
label_2.grid(row=2,column=1,padx=10,pady=10)
label_3.grid(row=3,column=1,padx=10,pady=10)
label_4=tk.Label(root,text="THE GENERATED PASSWORD IS ",fg="brown",bg="lightgreen",padx=10,pady=10)
label_4.grid(row=4,column=1)
entry_1=tk.Entry(root)
entry_1.grid(row=1,column=2)
entry_2=tk.Entry(root)
entry_2.grid(row=2,column=2)
entry_3=tk.Entry(root)
entry_3.grid(row=3,column=2)
entry_4=tk.Entry(root)
entry_4.grid(row=4,column=2)
button_1=tk.Button(root,text="generate password",fg="white",bg="green",padx=10,pady=10,command=lambda:password_generator(a,b,c))
button_1.grid(row=5,column=2,columnspan=2,padx=100,pady=100)
button_2=tk.Button(root,text="entered",fg="white",bg="green",padx=10,pady=10,command=entred)
button_2.grid(row=5,column=1,padx=100,pady=100)
root.mainloop()