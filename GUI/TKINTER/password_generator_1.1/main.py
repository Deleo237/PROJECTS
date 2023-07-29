from tkinter import *
from tkinter import messagebox
from random import randint,choice,shuffle
from pyperclip import copy

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gp():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters= [choice(letters) for char in range(randint(8, 10))]
    password_symbols = [choice(symbols) for char in range(randint(2, 4))]
    password_numbers = [choice(numbers) for char in range(randint(2, 4))]
    password_list=password_letters+password_symbols+password_numbers
    shuffle(password_list)
    password = "".join(password_list)
    copy(password)
    e3.delete(0,END)
    e3.insert(0,string=password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def ad():
    t1=e1.get()
    t2=e2.get()
    t3=e3.get()
    if t1=="" or t1=="www." or t2=="" or t2=="@gmail.com" or t3=="":
        messagebox.showerror(title="Oops",message="Please don't leave any field empty!!")
    else:
        ok=messagebox.askokcancel(title=t1,message=f"These are actually your credentials\nEmail: {t2}\nPassword: {t3}\n\nAre these ok to save?")
        if ok:
            with open("data.txt","a") as d:
                d.write(f"Website:{t1}\nEmail:{t2}\nPassword:{t3}\n\n")
                messagebox.showinfo(title="Success",message="Information has been\nsuccessfully saved\n😁😁😁😁😁")
            e1.delete(0,END)
            e2.delete(0,END)
            e3.delete(0,END)
            e1.insert(END,string="www.")
            e2.insert(0,string="@gmail.com")
            e1.focus()
# ---------------------------- UI SETUP ------------------------------- # 
w=Tk()
w.title("PASSWORD MANAGER")
w.config(padx=50,pady=50)
im=PhotoImage(file="logo.png")
c=Canvas(width=200,height=200,highlightthickness=0)
c.create_image(100,100,image=im)
c.grid(row=0,column=1)
l1=Label(text="Website:",font=('Arial',10))
l1.grid(row=1,column=0)
e1=Entry(width=49)
e1.insert(END,string="www.")
e1.focus()
e1.grid(row=1,column=1,columnspan=2)
l2=Label(text="Email/Username:",font=('Arial',10))
l2.grid(row=2,column=0)
e2=Entry(width=49)
e2.insert(0,string="@gmail.com")
e2.grid(row=2,column=1,columnspan=2)
l3=Label(text="Password:",font=('Arial',10))
l3.grid(row=3,column=0)
e3=Entry(width=31)
e3.grid(row=3,column=1)
b1=Button(text="Generate Password",padx=0,command=gp)
b1.grid(row=3,column=2)
b2=Button(text="Add",width=42,command=ad)
b2.grid(row=4,column=1,columnspan=2)
w.mainloop() 