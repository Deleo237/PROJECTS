from tkinter import *
def cal():
    m=float(e.get())
    k=round(m*1.60934,2)
    l3.config(text=str(k))
w=Tk()
w.title("Mile to Km Converter")
w.minsize(width=250,height=100)
e=Entry(width=10)
e.grid(column=1,row=0)
b=Button(text="Calculate",command=cal)
b.grid(column=1,row=2)
l1=Label(text="  Miles",font=('Arial',15,"italic"))
l1.grid(column=2,row=0)
l2=Label(text="is equal to",font=('Arial',15,"italic"))
l2.grid(column=0,row=1)
l3=Label(text="0",font=('Arial',15,"italic"))
l3.grid(column=1,row=1)
l4=Label(text="Km",font=('Arial',15,"italic"))
l4.grid(column=2,row=1)
w.mainloop()