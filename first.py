from tkinter import *
from tkinter import ttk
from googletrans import Translator,LANGUAGES

def change(text="type",src="English",dest="Hindi"):
    text1 = text
    src1 =src
    dest1 = dest
    trans = Translator()
    trans1 = trans.translate(text,src=src1,dest=dest1)
    return trans1.text

def data():
    s = combBox_sour.get()
    d = combBox_dest.get()
    masg = Sour_txt.get(1.0,END)
    textget = change(text=masg,src=s,dest=d)
    dest_txt.delete(1.0,END)
    dest_txt.insert(END,textget)


root = Tk()
root.title("Translator")
root.geometry("500x700")
root.config(bg='red')

lab_txt = Label(root,text="Translator",font=("Time New Roman",40,"bold"))
lab_txt.place(x=100,y=40,height=50,width=300)

fram = Frame(root).pack(side=BOTTOM)

lab_txt = Label(root,text="Source Text",font=("Comic Sans MS",17,"bold"),fg="Black",bg="Red")
lab_txt.place(x=100,y=100,height=20,width=300)

Sour_txt = Text(fram,font=("Time New Roman",20,"bold"),wrap=WORD)
Sour_txt.place(x=10,y=130,height=150,width=480)

list_text = list(LANGUAGES.values())
combBox_sour = ttk.Combobox(fram,values=list_text)
combBox_sour.place(x=10,y=300,height=40,width=150)
combBox_sour.set("English")

button_change = Button(fram,text="Translate",relief=RAISED,command=data)
button_change.place(x=170,y=300,height=40,width=150)

combBox_dest = ttk.Combobox(fram,values=list_text)
combBox_dest.place(x=330,y=300,height=40,width=150)
combBox_dest.set("English")

lab_txt = Label(root,text="Destination Text",font=("Comic Sans MS",17,"bold"),fg="Black",bg="Red")
lab_txt.place(x=100,y=360,height=20,width=300)

dest_txt = Text(fram,font=("Time New Roman",20,"bold"),wrap=WORD)
dest_txt.place(x=10,y=400,height=150,width=480)


root.mainloop()
