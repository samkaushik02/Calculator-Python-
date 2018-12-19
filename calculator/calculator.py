#made_by_sameer_kaushik
from tkinter import *
root=Tk()
root.title("CALCULATOR")
root.resizable(0,0)
from pynput.keyboard import Key, Controller

keyboard = Controller()

root.geometry("220x370")

e=Entry(root,font="20",bd=5)
e.grid(columnspan=4,row=0,ipadx=10,ipady=10,padx=5,pady=10)

n1=Button(text="1",font=("none","10","bold"),relief="raised",overrelief="ridge", bg="#6c6c62",fg="white",bd=2)
n1.grid(row=3,column=0,padx=2,pady=2,ipadx=10,ipady=10)
def no1(event):
        keyboard.press("1")
        keyboard.release("1")
n1.bind("<1>",no1)

n2=Button(text="2",font=("none","10","bold"),relief="raised",overrelief="ridge", bg="#6c6c62",fg="white",bd=2)
n2.grid(row=3,column=1,padx=5,pady=5,ipadx=12,ipady=12)
def no2(event):
        keyboard.press("2")
        keyboard.release("2")
n2.bind("<Button-1>",no2)

n3=Button(text="3",font=("none","10","bold"),relief="raised",overrelief="ridge", bg="#6c6c62",fg="white",bd=2)
n3.grid(row=3,column=2,padx=2,pady=2,ipadx=12,ipady=12)
def no3(event):
        keyboard.press("3")
        keyboard.release("3")
n3.bind("<Button-1>",no3)

n4=Button(text="4",font=("none","10","bold"),relief="raised",overrelief="ridge", bg="#6c6c62",fg="white",bd=2)
n4.grid(row=4,column=0,padx=2,pady=2,ipadx=12,ipady=12)
def no4(event):
        keyboard.press("4")
        keyboard.release("4")
n4.bind("<Button-1>",no4)

n5=Button(text="5",font=("none","10","bold"),relief="raised",overrelief="ridge", bg="#6c6c62",fg="white",bd=2)
n5.grid(row=4,column=1,padx=2,pady=2,ipadx=12,ipady=12)
def no5(event):
       keyboard.press("5")
       keyboard.release("5")
n5.bind("<Button-1>",no5)

n6=Button(text="6",font=("none","10","bold"),relief="raised",overrelief="ridge", bg="#6c6c62",fg="white",bd=2)
n6.grid(row=4,column=2,padx=2,pady=2,ipadx=12,ipady=12)
def no6(event):
        keyboard.press("6")
        keyboard.release("6")
n6.bind("<Button-1>",no6)

n7=Button(text="7",font=("none","10","bold"),relief="raised",overrelief="ridge", bg="#6c6c62",fg="white",bd=2)
n7.grid(row=5,column=0,padx=2,pady=2,ipadx=12,ipady=12)
def no7(event):
        keyboard.press("7")
        keyboard.release("7")
n7.bind("<Button-1>",no7)

n8=Button(text="8",font=("none","10","bold"),relief="raised",overrelief="ridge", bg="#6c6c62",fg="white",bd=2)
n8.grid(row=5,column=1,padx=2,pady=2,ipadx=12,ipady=12)
def no8(event):
        keyboard.press("8")
        keyboard.release("8")
n8.bind("<Button-1>",no8)

n9=Button(text="9",font=("none","10","bold"),relief="raised",overrelief="ridge", bg="#6c6c62",fg="white",bd=2)
n9.grid(row=5,column=2,padx=2,pady=2,ipadx=12,ipady=12)
def no9(event):
        keyboard.press("9")
        keyboard.release("9")
n9.bind("<Button-1>",no9)

n0=Button(text="0",font=("none","10","bold"),relief="raised",overrelief="ridge", bg="#6c6c62",fg="white",bd=2)
n0.grid(row=6,column=0,padx=2,pady=2,ipadx=12,ipady=12)
def no0(event):
        keyboard.press("0")
        keyboard.release("0")
n0.bind("<Button-1>",no0)

plus=Button(text="+",font=("none","10","bold"),relief="raised",overrelief="ridge", bg="#C1CDCD",fg="black",bd=2)
plus.grid(row=3,column=3,padx=2,pady=2,ipadx=12,ipady=12)
def oplus(event):
        keyboard.press("+")
        keyboard.release("+")
plus.bind("<Button-1>",oplus)

minus=Button(text="-",font=("none","12","bold"),relief="raised",overrelief="ridge", bg="#C1CDCD",fg="black",bd=2)
minus.grid(row=4,column=3,padx=2,pady=2,ipadx=12,ipady=12)
def ominus(event):
        keyboard.press("-")
        keyboard.release("-")
minus.bind("<Button-1>",ominus)

mult=Button(text="*",font=("none","10","bold"),relief="raised",overrelief="ridge", bg="#C1CDCD",fg="black",bd=2)
mult.grid(row=5,column=3,padx=2,pady=2,ipadx=12,ipady=12)
def omul(event):
       keyboard.press("*")
       keyboard.release("*")
mult.bind("<Button-1>",omul)

div=Button(text="/",font=("none","10","bold"),relief="raised",overrelief="ridge", bg="#C1CDCD",fg="black",bd=2)
div.grid(row=6,column=3,padx=2,pady=2,ipadx=12,ipady=12)
def odiv(event):
        keyboard.press("/")
        keyboard.release("/")
div.bind("<Button-1>",odiv)

rim=Button(text="%",font=("none","10","bold"),relief="raised",overrelief="ridge", bg="#C1CDCD",fg="black",bd=2)
rim.grid(row=6,column=2,padx=2,pady=2,ipadx=12,ipady=12)
def orim(event):
        keyboard.press("%")
        keyboard.release("%")
rim.bind("<Button-1>",orim)

pnt=Button(text=".",font=("none","10","bold"),relief="raised",overrelief="ridge", bg="#C1CDCD",fg="black",bd=2)
pnt.grid(row=6,column=1,padx=2,pady=2,ipadx=12,ipady=12)
def opnt(event):
        keyboard.press(".")
        keyboard.release(".")
pnt.bind("<Button-1>",opnt)

eq=Button(text="=",font=("none","10","bold"),relief="raised",overrelief="ridge", bg="#b9ffcb",fg="black",bd=2)
eq.grid(padx=2,pady=2,ipadx=12,ipady=12,row=2,column=0,sticky="W")
def oeq(event):
        data=e.get()
        ans.config(text=" Answer : "+str(eval(data)), fg="#000000" ,font=("Comic Sans MS","12"))
eq.bind("<Button-1>",oeq)

clr=Button(text="clr",font=("none","10","bold"),relief="raised",overrelief="ridge", bg="#f47b67",fg="black",bd=2)
clr.grid(padx=2,pady=2,ipadx=10,ipady=10,row=2,column=3,sticky="E")
def oclr(event):
        keyboard.press("\b")
        ans.config(text=" ", fg="#000000" ,font=("Comic Sans MS","12"))
clr.bind("<Button-1>",oclr)


ans=Label(root)
ans.grid(row=2,column=1,columnspan=2)

mainloop()
#made_by_sameer_kaushik
