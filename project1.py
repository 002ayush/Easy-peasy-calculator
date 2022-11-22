from tkinter import *
from functools import reduce
import math as m1
import speech_recognition as s

def add(l):
    return sum(l)

def sub(l):
    res = reduce(lambda n,m:n-m,l)

    return res
def pro(l):
    res = reduce(lambda p,q:p*q,l)
    return res

def div(l):
    return l[0] / l[1]

def mod(l):
    return l[0] % l[1];

def lcm(l):
    a,b=l[0],l[1]
    
    l1 = a if a>b else b
    while l1 <= a*b:
        if l1%a == 0 and l1%b == 0:
            return l1
        l1+=1

def hcf(l):
    a,b=l[0],l[1]
    l1 = a if a<b else b
    while l1 >= 1:
        if (a%l1 == 0 and b%l1 == 0):
            return l1;
        l1-=1
def fact(l):
    
    n=int(l[0])
    f=1
    for i in range(2,n+1):
        f=f*i
    return f
def extract_values(text):
    l = []
    for t in text.split():
        try:
            if t.upper() in op1: 
                l.append(t.upper())
            l.append(float(t))
        except:
            pass
    return l
def calculate():
    global textvar
    text = textvar.get()
    string = ""
    l = extract_values(text)
    if l[0] in op1:
        val=1
        flag=True
    else:
        val=0
        flag=False
    
    while(val < len(l)):
        if flag:
            if l[val] in op1:
                qw=op1[l[0]](l[1:val])
                del l[0:val-1]
                l[0]=qw
                l[0],l[1] = l[1],l[0]
                val=0
                print(l)
            val+=1
        else:
            if l[val] in op1:
                qw=op1[l[val]](l[0:val])
                del l[0:val]
                l[0]=qw
                #l[0],l[1] = l[1],l[0]
                val=0
                print(l)
            val+=1
            
    
  
     
    if len(l) > 1:
        try:
            qww = op1[l[0]](l[1:])
            l3.delete(0,END)
            l3.insert(END,qww)
        except:
            l3.delete(0,END)
            l3.insert(END,"KEHNA KYA CHAHTE HO")
    else:
        l3.delete(0,END)
        l3.insert(END,l)
def deg (p):
    return m1.degrees(p[0])
def rad(p):
    return m1.radians(p[0])
def sin(p):
    
    return m1.sin(rad(p))
def cos(p):
    return m1.cos(rad(p))
def tan(p):
    return m1.tan(rad(p))
def log(p):
    return m1.log10(p[0])
def ln(p):
    return m1.log(p[0])
def change_color(event):
    
    w1.configure(bg='black')
def clear():
    l3.delete(0,END)
def speaker():
    sr=s.Recognizer()
    with s.Microphone() as m:
        audio = sr.listen(m)
        query=sr.recognize_google(audio,language='eng-in')
        l3.insert(0,query)
        if 'calculate' in l3:
            calculate()
op1= {'ADD':add , 'ADDITION':add , 'SUM':add , 'PLUS':add ,
                'SUB':sub , 'DIFFERENCE':sub , 'MINUS':sub , 'SUBTRACT':sub,
                 'SUBTRACTION':sub,'LCM':lcm , 'HCF':hcf , 'PRODUCT': pro, 'MULTIPLICATION':pro,
                 'MULTIPLY':pro , 'DIVISION':pro , 'DIV':div ,'DIVIDE':div,
                  'DIVIDED':div,'REMAINDER':mod , 'MODULUS':mod,'MOD':mod,'+':add,'-':sub,
              '*':pro,'/':div,'%':mod,'FACTORIAL':fact,'!':fact,'SIN':sin,'COS':cos,
               'LOG':log,'LN':ln,'DEGREE':deg,'RADIANS':rad,'TAN':tan}

w1 = Tk()
w1.geometry('500x300')
w1.minsize(600,300)
w1.maxsize(1200,600)
w1.title('Calculator')
w1.configure(bg='chocolate1')
textvar = StringVar()
l2 = Label(w1 , text='EASY PEASY CALCULATOR' ,font="Helvetica 20 bold",width=30 ,borderwidth=6,fg="black",bg="orange",relief=SUNKEN, padx=3,pady=15)
l2.place(x=350,y=110)
l3 = Entry(w1  ,font="Helvetica 20 bold",width=40 ,borderwidth=6,fg="black",bg="maroon3",relief=SUNKEN, textvariable = textvar)
l3.place(x=300,y=250)
b1 = Button(w1 , text='Calculate' ,font="Helvetica 20 bold",width=10 ,borderwidth=6,fg="black",bg="orange",relief=SUNKEN,command=calculate)
b1.place(x=510,y=300)
b2 = Button(w1 , text='Clear' ,font="Helvetica 20 bold",width=8 ,borderwidth=6,fg="black",bg="orange",relief=SUNKEN,command=clear)
b2.place(x=520,y=370)
w1.bind('<Double-1>',change_color)
b3 = Button(w1 , text='Speak' ,font="Helvetica 20 bold",width=8 ,borderwidth=6,fg="black",bg="orange",relief=SUNKEN,command=speaker)
b3.place(x=900,y=250)

w1.mainloop()
