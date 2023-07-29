from tkinter import *
from tkinter import messagebox
from random import randint,choice,shuffle
from pyperclip import copy
from json import dump,load

# ---------------------------- SEARCH PASSWORD ------------------------------- #
def sh():
    """Searches for password"""
    k1=e1.get()
    k2=e2.get()
    try:
        with open("data.json","r") as d:
            info=load(d)
            n1=info[k1]
            if k2==n1["Email"]:
                k3=n1["Password"]
    except FileNotFoundError:
        messagebox.showerror(title="Error",message="No Data File Found.")
    except KeyError:
        messagebox.showerror(title="Error",message=f"Credentials are not aviable\for the website {k1} with\n email {k2}")
    else:
        messagebox.showinfo(title=k1,message=f"Email: {k2}\nPassword: {k3}")
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gp():
    """Generate password"""
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
    inf={
        t1:{
            "Email":t2,
            "Password":t3
        }
    }
    if t1=="" or t1=="www." or t2=="" or t2=="@gmail.com" or t3=="":
        messagebox.showerror(title="Oops",message="Please don't leave any field empty!!")
    else:
        ok=messagebox.askokcancel(title=t1,message=f"These are actually your credentials\nEmail: {t2}\nPassword: {t3}\n\nAre these ok to save?")
        if ok:
            try:
                with open("data.json","r") as d:
                    info=load(d)
            except FileNotFoundError:
                with open("data.json","w") as d:
                    dump(inf,d,indent=4)
            else:
                info.update(inf)
                with open("data.json","w") as d:
                    dump(info,d,indent=4)
            finally:
                messagebox.showinfo(title="Success",message="Information has been\nsuccessfully saved\n😁😁😁😁😁")
                e1.delete(0,END)
                e2.delete(0,END)
                e3.delete(0,END)
                e1.insert(END,string="www.")
                e2.insert(0,string="tendongmohdeleoanangfac@gmail.com")
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
e1=Entry(width=31)
e1.insert(END,string="www.")
e1.focus()
e1.grid(row=1,column=1)
l2=Label(text="Email/Username:",font=('Arial',10))
l2.grid(row=2,column=0)
e2=Entry(width=49)
e2.insert(0,string="tendongmohdeleoanangfac@gmail.com")
e2.grid(row=2,column=1,columnspan=2)
l3=Label(text="Password:",font=('Arial',10))
l3.grid(row=3,column=0)
e3=Entry(width=31)
e3.grid(row=3,column=1)
b1=Button(text="Generate Password",padx=0,command=gp)
b1.grid(row=3,column=2)
b2=Button(text="Add",width=42,command=ad)
b2.grid(row=4,column=1,columnspan=2)
b3=Button(text="Search",width=14,command=sh)
b3.grid(row=1,column=2)
w.mainloop() 