
from tkinter import*
import requests, bs4
import urllib
import time

def on_configure(event):
    cn.configure(scrollregion=cn.bbox('all'))
    

def show():
    error.config(text="")
    global singers, varnames
    varnames = {}
    singers=[]
    r=0
    cn.pack(side=LEFT, fill=BOTH)
    scrollbar.pack(side = RIGHT, fill=Y)
    cn.config(yscrollcommand=scrollbar.set, scrollregion=cn.bbox(ALL))
    cn.bind('<Configure>', on_configure)
    cn.create_window(0, 0, window=cnframe, anchor=N)

    name=en.get()
    
    if name=="":
        error.config(text="The field is empty!")
    else:
        link ="http://www.similar-artist.com/similarto/artist/"+name+"/"
        data=requests.get(link)
        code=data.text
        html=bs4.BeautifulSoup(code, "html.parser")
        lst=html.find_all("h1")
        del lst[0:4]
            
         
        for i in range (0, len(lst)):
            string=str(lst[i])
            rep1=string.replace("</h1>", "")
            rep2=rep1.replace("<h1>", "")
            singers.append(rep2)

        for i in range (0, len(singers)):
            person=str(singers[i])
            if "amp;" in person:
                person=person.replace("amp;", "")
            else:
                pass
            
            space=Label(cnframe, width=15, height=6, bg="Dark Slate Gray")
            space.grid(row=r, column=0)
            """        
            face=Canvas(cnframe, width=50, height=50, bg="white")
            face.grid(row=r, column=1)
            """

            name=Label(cnframe, text=person, bg="Dark Slate Gray", fg="White", font="Arial 12")
            name.config(width=20, height=4)
            name.grid(row=r, column=1)
            
            bname = "button"+str(i)
            
            varnames[bname] = Button(cnframe, bg="Orange", text="Download", font="Aharoni 9", command=lambda i=i: download(i)) 
            varnames[bname].grid(row=r, column=2)

            #+str(i)

            r+=1


def download(index):

   
    
    ok=Tk()
    ok.geometry("200x80")
    ok.title("Downloading")

    hey=Label(ok, text="Please wait...")
    hey.pack()

    wn.update()

    print(index)
    person=str(singers[index])


    if " " in person:
        a=person.split()
        print(a)
        name1=a[0]
        name2=a[1]
        link ="http://pesni-tut.com/s.php?q="+name1+"+"+name2
    else:
        link ="http://pesni-tut.com/s.php?q="+person

    try:

        data=requests.get(link)
        code=data.text
        html=bs4.BeautifulSoup(code, "html.parser")
        lst=html.find(class_="songurl")
        r=str(lst).replace(">", " ")
        lst1=r.split()
        lst2=r.split('"')
        s=lst2[4]
        song=s.replace("</a ", "")
        print(lst1)


        load=lst1[2]
        numb=load.replace('href="/download_song-', "")
        numbers=numb.replace('.html"', "")
        loadlink="http://pesni-tut.com/dlsong"+numbers+".mp3"

                
        mp3file=urllib.request.urlopen(loadlink)
        audio=open(person+" -"+song+".mp3",'wb')
        audio.write(mp3file.read())
        audio.close()

        hey.config(text="DONE!")
        
    except:
        hey.config(text="Connection error!")




wn=Tk()
wn.title("MeLoady")
wn.geometry("500x500")
wn.config(bg="Dark Slate Gray")

wn.minsize(width=500, height=500)
wn.maxsize(width=500, height=500)

logo=Label(text="MeLoady", bg="Dark Slate Gray", fg="Orange", font=("Aharoni", 20, "bold"))
logo.pack()

lab=Label(text="Type the name of a singer:", bg="Dark Slate Gray", fg="White", font="Aharoni 15")
lab.pack()

sfr=Frame(bg="Dark Slate Gray")
sfr.pack()

en=Entry(sfr, width=50)
en.grid(row=0, column=0)

space=Label(sfr, text="   ", bg="Dark Slate Gray")
space.grid(row=0, column=1)

b=Button(sfr, text="Search", command=show)
b.grid(row=0, column=2)

error=Label(sfr, width=30, height=2, text="", bg="Dark Slate Gray", fg="red")
error.grid(row=1, column=0)

linefr=Frame(wn, bg="White", width=500)
linefr.pack()

cn=Canvas(wn, width=400, height=40, bg="Dark Slate Gray", highlightthickness=0)
scrollbar = Scrollbar(wn, command=cn.yview)
cnframe=Frame(cn, bg="Dark Slate Gray")











