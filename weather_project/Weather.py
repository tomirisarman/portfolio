from tkinter import*
import requests

link1=("http://api.openweathermap.org/data/2.5/weather?q=")
link2=("&units=metric&APPID=6bab4d6713adbf3a428b1f2a7454395d")

def show():
    canvas.delete(ALL)
    city=en.get()
    link=link1+city+link2
    data=requests.get(link)
    temp=data.json()["main"]["temp"]
    canvas.create_text(300,100,text="Temp: "+str(temp)+" °C", font="Arial 15")             
    country=data.json()["sys"]["country"]
    canvas.create_text(20,20,text=country, font="Arial 20 bold")
    weather=data.json()["weather"][0]["main"]
    canvas.create_text(300,130,text="Sky: "+weather, font="Arial 15")
                           
    if weather=="Clouds":
        canvas.create_image(100,100, image=cloud)
    elif weather=="Clear":
        canvas.create_image(100,100, image=sun)
    elif weather=="Mist" or weather=="Smoke":
        canvas.create_image(100,100, image=fog)
    elif weather=="Rain":
        canvas.create_image(100,100, image=rain)

    
    x=int(temp)
    if x>=28:
        canvas.create_text(200,180, font="Calibri", fill="white", text="Damn! Your ass will surely sweat.")
    elif 20<x<28:
        canvas.create_text(200,180, font="Calibri", fill="white", text="It's warm. Continue to live your pitiful life.")
    elif 15<x<=20:
        canvas.create_text(200,180, font="Calibri", fill="white",  text="Perfect temperature. Not hot, not really cold. Like it, yep.")
    elif 10<x<=15:
        canvas.create_text(200,180, font="Calibri", fill="white", text="Nice chance to show your cool leather coat.")
    elif x<=10:
        canvas.create_text(200,180, font="Calibri", fill="white", text="As cold as my red pokerface.")


#сравнить если погода равно КЛАУДС, то сделать КРИЭЙТ ИМЕЙДЖ с картинкой облаков итд.


wn=Tk()
wn.title("Weather Forecast")
wn.geometry("500x300")

fr=Frame()
fr.pack()

lab=Label(fr, text="City: ")
lab.grid(row=0, column=0)

en=Entry(fr)
en.grid(row=0,column=1)

b=Button(fr, text="Get", command=show)
b.grid(row=0, column=2)

canvas=Canvas(width=400, height=200, bg="Cornflower Blue")
canvas.pack()

cloud=PhotoImage(file="cloud.png")
sun=PhotoImage(file="sun.png")
fog=PhotoImage(file="fog.png")
rain=PhotoImage(file="rain.png")




