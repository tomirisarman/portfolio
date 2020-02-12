
from tkinter import*
import requests
link="https://openexchangerates.org/api/latest.json?app_id=60da2bd9b3064714b2c5f2e8b00fbd40"
data=requests.get(link)
rates=data.json()["rates"]

def cT():
    tenge=float(varT.get())
    dollar=round(tenge/rates["KZT"], 5)
    varD.set(dollar)
    rubl=round(dollar*rates["RUB"], 5)
    varR.set(rubl)
    

def cR():
    rubl=float(varR.get())
    dollar=round(rubl/rates["RUB"], 5)
    varD.set(dollar)
    tenge=round(dollar*rates["KZT"], 5)
    varT.set(tenge)
    
def cD():
    dollar=float(varD.get())
    tenge=round(dollar*rates["KZT"], 5)
    varT.set(tenge)
    rubl=round(dollar*rates["RUB"], 5)
    varR.set(rubl)


wn=Tk()
wn.geometry("300x100")
wn.title("Exchange")
wn.config(bg="light blue")

t=Label(text="KZT:", bg="light blue", font=15)
t.grid(row=0, column=0)

r=Label(text="RUB:", bg="light blue", font=15)
r.grid(row=1, column=0)

d=Label(text="USD:", bg="light blue", font=15)
d.grid(row=2, column=0)

varT=StringVar()
enT=Entry(textvariable=varT)
enT.grid(row=0, column=1)

varR=StringVar()
enR=Entry(textvariable=varR)
enR.grid(row=1, column=1)

varD=StringVar()
enD=Entry(textvariable=varD)
enD.grid(row=2, column=1)

bT=Button(text="Convert", command=cT)
bT.grid(row=0, column=2)

bR=Button(text="Convert", command=cR)
bR.grid(row=1, column=2)

bD=Button(text="Convert", command=cD)
bD.grid(row=2, column=2)
