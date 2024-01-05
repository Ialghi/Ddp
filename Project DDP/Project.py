import tkinter as tk
from tkinter import *
from tkinter import ttk

root=Tk()
root.title("Calculator")
root.geometry("485x570+100+200")
root.resizable(False,False)
root.configure(bg="#17161b")

persamaan = ""

def show(value):
    global persamaan
    persamaan+=value
    label_hasil.config(text=persamaan)

def clear():
    global persamaan
    persamaan = ""
    label_hasil.config(text=persamaan)

def calculate():
    global persamaan
    hasil =""
    if persamaan !="":
        try:
            hasil= eval(persamaan)
        except:
            hasil ="Error"
            persamaan = ""
    label_hasil.config(text=hasil)
            

label_hasil= Label(root,width=20,height=2,text="",font=("arial",30,))
label_hasil.pack()

Button(root,text="C", width=4, height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#67605C",cursor="hand2",command=lambda: clear()).place(x=10,y=110)
Button(root,text="/", width=4, height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#181b45",cursor="hand2",command=lambda: show("/")).place(x=130,y=110)
Button(root,text="%", width=4, height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#181b45",cursor="hand2",command=lambda: show("%")).place(x=250,y=110)
Button(root,text="x", width=4, height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#181b45",cursor="hand2",command=lambda: show("*")).place(x=370,y=110)

Button(root,text="7", width=4, height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#2A2A2A",cursor="hand2",command=lambda: show("7")).place(x=10,y=203)
Button(root,text="8", width=4, height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#2A2A2A",cursor="hand2",command=lambda: show("8")).place(x=130,y=203)
Button(root,text="9", width=4, height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#2A2A2A",cursor="hand2",command=lambda: show("9")).place(x=250,y=203)
Button(root,text="-", width=4, height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#181b45",cursor="hand2",command=lambda: show("-")).place(x=370,y=203)

Button(root,text="4", width=4, height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#2A2A2A",cursor="hand2",command=lambda: show("4")).place(x=10,y=296)
Button(root,text="5", width=4, height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#2A2A2A",cursor="hand2",command=lambda: show("5")).place(x=130,y=296)
Button(root,text="6", width=4, height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#2A2A2A",cursor="hand2",command=lambda: show("6")).place(x=250,y=296)
Button(root,text="+", width=4, height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#181b45",cursor="hand2",command=lambda: show("+")).place(x=370,y=296)

Button(root,text="1", width=4, height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#2A2A2A",cursor="hand2",command=lambda: show("1")).place(x=10,y=389)
Button(root,text="2", width=4, height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#2A2A2A",cursor="hand2",command=lambda: show("2")).place(x=130,y=389)
Button(root,text="3", width=4, height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#2A2A2A",cursor="hand2",command=lambda: show("3")).place(x=250,y=389)
Button(root,text="0", width=9, height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#2A2A2A",cursor="hand2",command=lambda: show("0")).place(x=10,y=482)

Button(root,text=".", width=4, height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#2A2A2A",cursor="hand2",command=lambda: show(".")).place(x=250,y=482)
Button(root,text="=", width=4, height=3, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#67605C",cursor="hand2",command=lambda: calculate()).place(x=370,y=389)


root.mainloop()
