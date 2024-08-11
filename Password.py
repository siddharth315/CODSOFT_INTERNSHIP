# TASK-2) PASSWORD GENERATOR --->
import random
from tkinter import *

root = Tk()
root.geometry("450x300")
root.title("Password Generator")

alpha = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
num = '0123456789'
symbols = '!@#$%^&*_-+='
characters = alpha + num + symbols

def click():
    x = lengthentry.get()
    password = "".join(random.sample(characters,int(x)))
    showpassword.config(text='Your new password: ' + password)
    print("Successful!")
    
# Heading
Label(root,text="Password Generator",font="arial 15 bold").grid(row=0,column=3)

# Field Names
username = Label(root,text="Enter Username: ")
length = Label(root,text="Enter Password Length: ")
showpassword = Label(root,font="arial 10 bold")

# Packing Fields
username.grid(row=1,column=2)
length.grid(row=2,column=2)
showpassword.grid(row=4,column=3)

# Variable for storing data
usernamevalue = StringVar
lengthvalue = StringVar

# Entry Field
usernameentry = Entry(root,textvariable_=usernamevalue,borderwidth=2)
lengthentry = Entry(root,textvariable_=lengthvalue,borderwidth=2)

# Packing Entry Fields
usernameentry.grid(row=1,column=3)
lengthentry.grid(row=2,column=3)

# Generate Button
Button(root,text="Generate",command=click,borderwidth=2).grid(row=3,column=3)

root.mainloop()
