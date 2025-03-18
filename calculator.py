from tkinter import*
x = Tk()
x.title("Calculator")
x.geometry("320x411")
x.resizable(False,False)

i = StringVar()
flag = False
# i.set("0")


def display(a):
     global x, flag
     val = i.get()
     if val == "0" and a not in [".", "+", "-", "*", "/"]:
          i.set(a)
     elif flag and a.isdigit():   
          x =a  
          flag = False
     elif val and val[-1] in "+-/*":
          if a in "+-/*":
               x = val[:-1]+a
          else:
               x = val+a
     else:
          x = val+a
     i.set(x)

def result():
     global x, flag
     if x:
          c = eval(x)
          i.set(c)
          x = str(c)
          flag = True
          
def clear():
     i.set("")
def backspace():
     global x
     x = x[:-1]
     i.set(x)

def bracket_sign():
     global x
     val = i.get()
     if val:
          if val[0] == "-":
               x = val[1:]
          else:
               x = "-" + val
          i.set(x)


e =Entry(x,width=29,textvariable=i,font="arial 15 bold ")
e.grid(columnspan=35,ipady=15)


b=Button(x,text="C",width=7,height=3,command=clear,font="arial 13 bold " )
b.grid(row=1,column=0)

b1=Button(x,text="<",width=7,height=3,command=backspace,font="arial 13 bold ")
b1.grid(row=1,column=1)

b2=Button(x,text="%",width=7,height=3,command= lambda:display("%"),font="arial 13 bold ")
b2.grid(row=1,column=2)

b3=Button(x,text="/",width=7,height=3,command= lambda:display("/"),font="arial 13 bold ")
b3.grid(row=1,column=3)

b4=Button(x,text="7",width=7,height=3,command= lambda:display("7"),font="arial 13 bold ")
b4.grid(row=2,column=0)

b5=Button(x,text="8",width=7,height=3,command= lambda:display("8"),font="arial 13 bold ")
b5.grid(row=2,column=1)

b6=Button(x,text="9",width=7,height=3,command= lambda:display("9"),font="arial 13 bold ")
b6.grid(row=2,column=2)

b7=Button(x,text="*",width=7,height=3,command= lambda:display("*"),font="arial 13 bold ")
b7.grid(row=2,column=3)

b8=Button(x,text="4",width=7,height=3,command= lambda:display("4"),font="arial 13 bold ")
b8.grid(row=3,column=0)

b9=Button(x,text="5",width=7,height=3,command= lambda:display("5"),font="arial 13 bold ")
b9.grid(row=3,column=1)

b10=Button(x,text="6",width=7,height=3,command= lambda:display("6"),font="arial 13 bold ")
b10.grid(row=3,column=2)

b11=Button(x,text="-",width=7,height=3,command= lambda:display("-"),font="arial 13 bold ")
b11.grid(row=3,column=3)

b12=Button(x,text="1",width=7,height=3,command= lambda:display("1"),font="arial 13 bold ")
b12.grid(row=4,column=0)

b13=Button(x,text="2",width=7,height=3,command= lambda:display("2"),font="arial 13 bold ")
b13.grid(row=4,column=1)

b14=Button(x,text="3",width=7,height=3,command= lambda:display("3"),font="arial 13 bold ")
b14.grid(row=4,column=2)

b15=Button(x,text="+",width=7,height=3,command= lambda:display("+"),font="arial 13 bold ")
b15.grid(row=4,column=3)

b16=Button(x,text="+/-",width=7,height=3,command= bracket_sign,font="arial 13 bold ")
b16.grid(row=5,column=0)

b17=Button(x,text="0",width=7,height=3,command= lambda:display("0"),font="arial 13 bold ")
b17.grid(row=5,column=1)

b18=Button(x,text=".",width=7,height=3,command= lambda:display("."),font="arial 13 bold ")
b18.grid(row=5,column=2)

b19=Button(x,text="=",width=7,height=3,command=result,font="arial 13 bold ")
b19.grid(row=5,column=3)

x.mainloop()
