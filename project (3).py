import tkinter
from tkinter import *
from test import *
from datetime import date, datetime

sri=Tk()
sri.geometry("1000x1000+0+0")
title=Label(sri,text="Market Billing System",font=('arial',50,'bold'),fg='green').pack(side=TOP)

_id=0
f=Frame(sri,width=800,height=800)
f.pack(side=LEFT)
ms=IntVar()
def show(e):
    global _id
    newcustomer = Customer(name=e.widget.get())
    session.add(newcustomer)
    session.commit()
    _id =newcustomer.id
#test
e = Entry(sri)
e.pack()
e.bind("<Return>", show)

text_Input=IntVar()
global bc
bc=IntVar()
global num1
global bagcount
bagcount=0
num1=0
def increment():
                    global num1
                    global bagcount
                    bagcount=bagcount+1
                    bc.set(bagcount)
                    num1+=1
                    text_Input.set(num1)
def decrement():
                    global num1
                    global bagcount
                    bagcount=bagcount-1
                    bc.set(bagcount)
                    num1-=1
                    text_Input.set(num1)

l=Label(f,padx=10,font=('arial',20,'bold'),text="Pasta",bd=10,anchor=W).grid(row=0,column=0)
lp=Label(f,padx=45,font=('arial','10','bold'),text="x10",bd=10).grid(row=0,column=4)
b=Button(f,bd=5,width=1,height=1,font=('arial',10,'bold'),text="+",padx=40,command=increment).grid(row=0,column=1)
e=Entry(f,width=4,bd=5,textvariable=text_Input,state='disabled').grid(row=0,column=2,padx=20)
b1=Button(f,bd=5,width=1,height=1,font=('arial',10,'bold'),text="-",padx=40,command=decrement).grid(row=0,column=3)




text_Input1=IntVar()
global num2
num2=0
def increment1():
                    global bagcount
                    bagcount=bagcount+1
                    bc.set(bagcount)
                    global num2
                    num2+=1
                    text_Input1.set(num2)
def decrement1():
                    global num2
                    num2-=1
                    global bagcount
                    bagcount=bagcount+1
                    bc.set(bagcount)
                    text_Input1.set(num2)

l1=Label(f,padx=10,font=('arial',20,'bold'),text="Noodles",bd=10,anchor=W).grid(row=1,column=0)
l1p=Label(f,padx=45,font=('arial','10','bold'),text="x20",bd=10).grid(row=1,column=4)
b2=Button(f,bd=5,width=1,height=1,font=('arial',10,'bold'),text="+",padx=40,command=increment1).grid(row=1,column=1)
e1=Entry(f,width=4,bd=5,textvariable=text_Input1,state='disabled').grid(row=1,column=2,padx=20)
b3=Button(f,bd=5,width=1,height=1,font=('arial',10,'bold'),text="-",padx=40,command=decrement1).grid(row=1,column=3)

text_Input2=IntVar()
global num3
num3=0

def increment2():
                   global num3
                   global bagcount
                   bagcount=bagcount+1
                   bc.set(bagcount)
                   num3+=1
                   text_Input2.set(num3)
def decrement2():
                   global num3
                   global bagcount
                   bagcount=bagcount-1
                   bc.set(bagcount)
                   num3-=1
                   text_Input2.set(num3)

l3=Label(f,padx=10,font=('arial',20,'bold'),text="Pizza",bd=10,anchor=W).grid(row=2,column=0)
l3p=Label(f,padx=45,font=('arial','10','bold'),text="x30",bd=10).grid(row=2,column=4)
b4=Button(f,bd=5,width=1,height=1,font=('arial',10,'bold'),text="+",padx=40,command=increment2).grid(row=2,column=1)
e2=Entry(f,width=4,bd=5,textvariable=text_Input2,state='disabled').grid(row=2,column=2,padx=20)
b5=Button(f,bd=5,width=1,height=1,font=('arial',10,'bold'),text="-",padx=40,command=decrement2).grid(row=2,column=3)


text_Input3=IntVar()
global num4
num4=0
def increment3():
                     global num4
                     global bagcount
                     bagcount=bagcount+1
                     bc.set(bagcount)
                     num4+=1
                     text_Input3.set(num4)
def decrement3():
                     global num4
                     global bagcount
                     bagcount=bagcount-1
                     bc.set(bagcount)
                     num4-=1
                     text_Input3.set(num4)                  
                   

l4=Label(f,padx=10,font=('arial',20,'bold'),text="Burger",bd=10,anchor=W).grid(row=3,column=0)
l4p=Label(f,padx=45,font=('arial','10','bold'),text="x40",bd=10).grid(row=3,column=4)
b6=Button(f,bd=5,width=1,height=1,font=('arial',10,'bold'),text="+",padx=40,command=increment3).grid(row=3,column=1)
e3=Entry(f,width=4,bd=5,textvariable=text_Input3,state='disabled').grid(row=3,column=2,padx=20)
b7=Button(f,bd=5,width=1,height=1,font=('arial',10,'bold'),text="-",padx=40,command=decrement3).grid(row=3,column=3)

text_Input4=IntVar()
global num5
num5=0
def increment4():
                    global  num5
                    global bagcount
                    bagcount=bagcount+1
                    bc.set(bagcount) 
                    num5+=1
                    text_Input4.set(num5)
def decrement4():
                    global num5
                    global bagcount
                    bagcount=bagcount-1
                    bc.set(bagcount) 
                    num5-=1
                    text_Input4.set(num5)


l5=Label(f,padx=10,font=('arial',20,'bold'),text="Sandwich",bd=10,anchor=W).grid(row=4,column=0)
l5p=Label(f,padx=45,font=('arial','10','bold'),text="x50",bd=10).grid(row=4,column=4)
b8=Button(f,bd=5,width=1,height=1,font=('arial',10,'bold'),text="+",padx=40,command=increment4).grid(row=4,column=1)
e4=Entry(f,width=4,bd=5,textvariable=text_Input4,state='disabled').grid(row=4,column=2,padx=20)
b9=Button(f,bd=5,width=1,height=1,font=('arial',10,'bold'),text="-",padx=40,command=decrement4).grid(row=4,column=3)

text_Input5=IntVar()
global num6
num6=0
def increment5():
                    global  num6
                    global bagcount
                    bagcount=bagcount+1
                    bc.set(bagcount) 
                    num6+=1
                    text_Input5.set(num6)
def decrement5():
                    global num6
                    global bagcount
                    bagcount=bagcount-1
                    bc.set(bagcount) 
                    num6-=1
                    text_Input5.set(num6)



l6=Label(f,padx=10,font=('arial',20,'bold'),text="KitKat",bd=10).grid(row=5,column=0)
l6p=Label(f,padx=45,font=('arial','10','bold'),text="x60",bd=10).grid(row=5,column=4)
b10=Button(f,bd=5,width=1,height=1,font=('arial',10,'bold'),text="+",padx=40,command=increment5).grid(row=5,column=1)
e5=Entry(f,width=4,bd=5,textvariable=text_Input5,state='disabled').grid(row=5,column=2,padx=20)
b11=Button(f,bd=5,width=1,height=1,font=('arial',10,'bold'),text="-",padx=40,command=decrement5).grid(row=5,column=3)

text_Input6=IntVar()
global num7
num7=0
def increment6():
                    global  num7
                    global bagcount
                    bagcount=bagcount+1
                    bc.set(bagcount) 
                    num7+=1
                    text_Input6.set(num7)
def decrement6():
                    global num7
                    global bagcount
                    bagcount=bagcount-1
                    bc.set(bagcount)
                    num7-=1
                    text_Input6.set(num7)

l7=Label(f,padx=10,font=('arial',20,'bold'),text="Biscuits",bd=10,anchor=W).grid(row=6,column=0)
l7p=Label(f,padx=45,font=('arial','10','bold'),text="x70",bd=10).grid(row=6,column=4)
b12=Button(f,bd=5,width=1,height=1,font=('arial',10,'bold'),text="+",padx=40,command=increment6).grid(row=6,column=1)
e6=Entry(f,width=4,bd=5,state='disabled',textvariable=text_Input6).grid(row=6,column=2,padx=20)
b13=Button(f,bd=5,width=1,height=1,font=('arial',10,'bold'),text="-",padx=40,command=decrement6).grid(row=6,column=3)

text_Input7=IntVar()
global num8
num8=0
def increment7():
                    global  num8
                    global bagcount
                    bagcount=bagcount+1
                    bc.set(bagcount) 
                    num8+=1
                    text_Input7.set(num8)
def decrement7():
                    global num8
                    global bagcount
                    bagcount=bagcount-1
                    bc.set(bagcount)
                    num8-=1
                    text_Input7.set(num8)

l8=Label(f,padx=10,font=('arial',20,'bold'),text="Chocolates",bd=10,anchor=W).grid(row=7,column=0)
l8p=Label(f,padx=45,font=('arial','10','bold'),text="x80",bd=10).grid(row=7,column=4)
b14=Button(f,bd=5,width=1,height=1,font=('arial',10,'bold'),text="+",padx=40,command=increment7).grid(row=7,column=1)
e7=Entry(f,width=4,bd=5,state='disabled',textvariable=text_Input7).grid(row=7,column=2,padx=20)
b15=Button(f,bd=5,width=1,height=1,font=('arial',10,'bold'),text="-",padx=40,command=decrement7).grid(row=7,column=3)

bcount=Label(f,font=('arial',20,'bold'),textvariable=bc).grid(row=1,column=27)

#===============================================Bag Labels=====================================================#
global v
#global num7
v=IntVar()
s=IntVar()
r=IntVar()
a=IntVar()
b=IntVar()
d=IntVar()
o=IntVar()
j=IntVar()
k=IntVar()


Bag=Label(f,text="BAG",font=('arial',30,'bold'),anchor=N).grid(row=0,column=27,padx=100)
def total():
         
           if(num1>0):
                       #s=IntVar()
                       bagl=Label(f,font=('arial',10,'bold'),textvariable=s).grid(row=2,column=27)
                       a1='Pasta-',num1*10
                       s.set(a1)
         
           if(num2>0):
                        #r=IntVar()
                        bagl1=Label(f,font=('arial',10,'bold'),textvariable=r).grid(row=3,column=27)
                        a2='Noodles-',num2*20
                        r.set(a2)
           if(num3>0):
                        #a=IntVar()
                        bagl2=Label(f,font=('arial',10,'bold'),textvariable=a).grid(row=4,column=27)
                        a3='Pizza--',num3*30
                        a.set(a3)
           if(num4>0):
                      #b=IntVar()
                      bagl3=Label(f,font=('arial',10,'bold'),textvariable=b).grid(row=5,column=27)
                      a4='Burger--',num4*40
                      b.set(a4)
           if(num5>0):
                         #d=IntVar()
                         bagl4=Label(f,font=('arial',10,'bold'),textvariable=d).grid(row=6,column=27)
                         a5='Sandwich-',num5*50
                         d.set(a5)
           if(num6>0):
                        #o=IntVar()
                        bagl5=Label(f,font=('arial',10,'bold'),textvariable=o).grid(row=7,column=27)
                        a6='KitKat--',num6*60
                        o.set(a6)
                        
           if(num7>0):
                          #j=IntVar()
                          bagl6=Label(f,font=('arial',10,'bold'),textvariable=j).grid(row=8,column=27)
                          a7='Biscuits',num7*70
                          j.set(a7)
           if(num8>0):
                          #k=IntVar()
                          bagl7=Label(f,font=('arial',10,'bold'),textvariable=k).grid(row=9,column=27)
                          a8='Chocolates--',num8*80
                          k.set(a8)
            
           ntotal= num1*10+num2*20+num3*30+num4*40+num5*50+num6*60+num7*70+num8*80
           print(_id)
           newIteam = Iteam(customer_id=_id,time=date.today(),pasta=num1,noodles=num2,pizza=num3,burger=num4,sandwich=num5,kitkat=num6,biscuits=num7,chocolates=num8,total=ntotal)
           session.add(newIteam)
           session.commit()
           a9='Total Bill--',ntotal
           ms.set(a9)


bagtotal=Label(f,font=('arial',10,'bold'),textvariable=ms).grid(row=10,column=27)                                                                                                 




bTotal=Button(f,text="Total",bg="black",fg="white",bd=10,height=1,font=('arial',20,'bold'),command=total).grid(row=16,column=0)


def clear():
         global clear
         global num1
         global num2
         global num3
         global num4
         global num5
         global num6
         global num7
         global num8
         global ntotal
         global bagcount
         global ms
         clear=" "
         text_Input.set(" ")
         text_Input1.set(" ")
         text_Input2.set(" ")
         text_Input3.set(" ")
         text_Input4.set(" ")
         text_Input5.set(" ")
         text_Input6.set(" ")
         text_Input7.set(" ")
         v.set(" ")
         s.set(" ")
         r.set("  ")
         a.set(" ")
         b.set(" ")
         d.set(" ")
         o.set(" ")
         j.set(" ")
         k.set(" ")
         bc.set(" ")
         bagcount=0
         num1=0
         num2=0
         num3=0
         num4=0
         num5=0
         num6=0
         num7=0
         num8=0
         ntotal=0
         #operator=" "
         ms.set(" ")


clear=Button(f,text="Clear",bg="black",fg="white",bd=10,height=1,font=('arial',20,'bold'),command=clear).grid(row=16,column=2)

def exit():
           sri.destroy()

exitbtn=Button(f,text="Exit",bg="black",fg="white",bd=10,height=1,font=('arial',20,'bold'),command=exit).grid(row=16,column=4)
            
#===================================================Calculator==================================================#

f1=Frame(sri,width=300,height=800,relief=SUNKEN)
f1.pack(side=RIGHT)

operator=" "
text_cal=IntVar()
def calclear():
             global opertor
             operator= " "
             text_cal.set(operator)
def btnclick(numbers):
             global operator
             operator = operator+str(numbers)
             text_cal.set(operator)
def equal():
              global operator
              sum=str(eval(operator))
              text_cal.set(sum)
              operator=""

textDisplay=Entry(f1,font=('arial',20,'bold'),textvariable=text_cal,bd=20,insertwidth=4,bg="white",justify='right')
textDisplay.grid(columnspan=4)

btn7=Button(f1,text="7",bd=5,font=('arial',20,'bold'),bg="black",fg="white",padx=16,pady=16,command=lambda:btnclick(7)).grid(row=1,column=0)
btn8=Button(f1,text="8",bd=5,font=('arial',20,'bold'),bg="black",fg="white",padx=16,pady=16,command=lambda:btnclick(8)).grid(row=1,column=1)
btn9=Button(f1,text="9",bd=5,font=('arial',20,'bold'),bg="black",fg="white",padx=16,pady=16,command=lambda:btnclick(9)).grid(row=1,column=2)
btnplus=Button(f1,text="+",bd=5,font=('arial',18,'bold'),bg="black",fg="white",padx=16,pady=16,command=lambda:btnclick("+")).grid(row=1,column=3)

btn4=Button(f1,text="4",bd=5,font=('arial',20,'bold'),bg="black",fg="white",padx=16,pady=16,command=lambda:btnclick(4)).grid(row=2,column=0)
btn5=Button(f1,text="5",bd=5,font=('arial',20,'bold'),bg="black",fg="white",padx=16,pady=16,command=lambda:btnclick(5)).grid(row=2,column=1)
btn6=Button(f1,text="6",bd=5,font=('arial',20,'bold'),bg="black",fg="white",padx=16,pady=16,command=lambda:btnclick(6)).grid(row=2,column=2)
btnsub=Button(f1,text="-",bd=5,font=('arial',20,'bold'),bg="black",fg="white",padx=16,pady=16,command=lambda:btnclick("-")).grid(row=2,column=3)

btn1=Button(f1,text="1",bd=5,font=('arial',20,'bold'),bg="black",fg="white",padx=16,pady=16,command=lambda:btnclick(1)).grid(row=3,column=0)
btn2=Button(f1,text="2",bd=5,font=('arial',20,'bold'),bg="black",fg="white",padx=16,pady=16,command=lambda:btnclick(2)).grid(row=3,column=1)
btn3=Button(f1,text="3",bd=5,font=('arial',20,'bold'),bg="black",fg="white",padx=16,pady=16,command=lambda:btnclick(3)).grid(row=3,column=2)
btnmul=Button(f1,text="*",bd=5,font=('arial',20,'bold'),bg="black",fg="white",padx=16,pady=16,command=lambda:btnclick("*")).grid(row=3,column=3)

btn0=Button(f1,text="0",bd=5,font=('arial',20,'bold'),bg="black",fg="white",padx=16,pady=16,command=lambda:btnclick(0)).grid(row=4,column=0)
btndiv=Button(f1,text="/",bd=5,font=('arial',20,'bold'),bg="black",fg="white",padx=16,pady=16,command=lambda:btnclick("/")).grid(row=4,column=1)
btnequal=Button(f1,text="=",bd=5,font=('arial',20,'bold'),bg="black",fg="white",padx=16,pady=16,command=equal).grid(row=4,column=2)
btncc=Button(f1,text="c",bd=5,font=('arial',19,'bold'),bg="black",fg="white",padx=16,pady=16,command=calclear).grid(row=4,column=3)
#============================================Calculator=========================================================#

sri.mainloop()




                                                                                                            
