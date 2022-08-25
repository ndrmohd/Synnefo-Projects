from tkinter import *

def pressOne():
    defOne=1
    view.set(defOne)

def pressTwo():
    defTwo=2
    view.set(defTwo)

def pressThree():
    defThree=3
    view.set(defThree)

def pressFour():
    defFour=4
    view.set(defFour)

def pressFive():
    defFive=5
    view.set(defFive)

def pressSix():
    defSix=6
    view.set(defSix)

def pressSeven():
    defSeven=7
    view.set(defSeven)

def pressEight():
    defEight=8
    view.set(defEight)

def pressNine():
    defNine=9
    view.set(defNine)

def pressZero():
    defZero=0
    view.set(defZero)

#def viewOperation():
    

#def isequalto():
    #print(operation)    


calculator=Tk()

view=StringVar()
result=StringVar()

calculator.title('Calculator')

f=Frame(calculator,width='320',height='570',bg='#D3D3D3')

Label(f,text="Standard",font="calibri 15 bold",bg='#D3D3D3').place(x=50,y=0)

Label(f,text="MC          MR",font="calibri 11 bold",fg='#A5A5A5',bg='#D3D3D3').place(x=15,y=145)
Label(f,text="Mˉ",font="calibri 11 bold",fg='#A5A5A5',bg='#D3D3D3').place(x=280,y=145)

btn=Button(f,text='M+',font='calibri 11 bold',width='4',height='1',border='0',bg='#D3D3D3').place(x=110,y=143)
btn2=Button(f,text='M-',font='calibri 11 bold',width='4',height='1',border='0',bg='#D3D3D3').place(x=170,y=143)
btn3=Button(f,text='MS',font='calibri 11 bold',width='4',height='1',border='0',bg='#D3D3D3').place(x=230,y=143)


getresult=Label(f,text='0=',font='calibri 12 bold',textvariable=result,fg='#A5A5A5',bg='#D3D3D3').place(x=280,y=40)
toview=Label(f,text='0',font='calibri 35 bold',textvariable=view,bg='#D3D3D3').place(x=280,y=65)


option=Button(f,text='☰',font='5',width='4',height='1',border='0',bg='#D3D3D3').place(x=0,y=0)
keeptop=Button(f,text='⌅',font='10',width='4',height='1',border='0',bg='#D3D3D3').place(x=140,y=0)
history=Button(f,text='⏲',font='10',width='4',height='1',border='0',bg='#D3D3D3').place(x=275,y=0)


percentage=Button(f,text='%',font='20',width='8',height='3',border='0',bg='#E1E1E1').place(x=0,y=175)
ce=Button(f,text='CE',font='15',width='8',height='3',border='0',bg='#E1E1E1').place(x=80,y=175)
clear=Button(f,text='C',font='15',width='8',height='3',border='0',bg='#E1E1E1').place(x=160,y=175)
delete=Button(f,text='⌫',font='20',width='8',height='3',border='0',bg='#E1E1E1').place(x=240,y=175)


decimal=Button(f,text='¹∕ₓ',font='20',width='8',height='3',border='0',bg='#E1E1E1').place(x=0,y=241)
power=Button(f,text='x²',font='20',width='8',height='3',border='0',bg='#E1E1E1').place(x=80,y=241)
root=Button(f,text='²√x',font='20',width='8',height='3',border='0',bg='#E1E1E1').place(x=160,y=241)
division=Button(f,text='➗',font='20',width='8',height='3',border='0',bg='#E1E1E1').place(x=240,y=241)

seven=Button(f,text='𝟳',font="20",width='8',height='3',border='0',bg='#F5F5F5',command=pressSeven).place(x=0,y=307)
eight=Button(f,text='𝟴',font='20',width='8',height='3',border='0',bg='#F5F5F5',command=pressEight).place(x=80,y=307)
nine=Button(f,text='𝟵',font='20',width='8',height='3',border='0',bg='#F5F5F5',command=pressNine).place(x=160,y=307)
multiplication=Button(f,text='✖',font='20',width='8',height='3',border='0',bg='#E1E1E1').place(x=240,y=307)

four=Button(f,text='𝟰',font='20',width='8',height='3',border='0',bg='#F5F5F5',command=pressFour).place(x=0,y=373)
five=Button(f,text='𝟱',font='20',width='8',height='3',border='0',bg='#F5F5F5',command=pressFive).place(x=80,y=373)
six=Button(f,text='𝟲',font='20',width='8',height='3',border='0',bg='#F5F5F5',command=pressSix).place(x=160,y=373)
substraction=Button(f,text='➖',font='20',width='8',height='3',border='0',bg='#E1E1E1').place(x=240,y=373)

one=Button(f,text='𝟭',font='20',width='8',height='3',border='0',bg='#F5F5F5',command=pressOne).place(x=0,y=439)
two=Button(f,text='𝟮',font='20',width='8',height='3',border='0',bg='#F5F5F5',command=pressTwo).place(x=80,y=439)
three=Button(f,text='𝟯',font='20',width='8',height='3',border='0',bg='#F5F5F5',command=pressThree).place(x=160,y=439)
addition=Button(f,text='➕',font='20',width='8',height='3',border='0',bg='#E1E1E1').place(x=240,y=439)

plusorminus=Button(f,text='±',font='50',width='8',height='3',border='0',bg='#F5F5F5').place(x=0,y=505)
zero=Button(f,text='𝟬',font='20',width='8',height='3',border='0',bg='#F5F5F5',command=pressZero).place(x=80,y=505)
dot=Button(f,text='•',font='20',width='8',height='3',border='0',bg='#F5F5F5').place(x=160,y=505)
equal=Button(f,text='＝',font='20',width='8',height='3',border='0',bg='#ADD8E6').place(x=240,y=505)



f.pack()

calculator.mainloop()
