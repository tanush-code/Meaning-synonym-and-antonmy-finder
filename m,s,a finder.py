from tkinter import *
import PyDictionary
from tkinter.messagebox import showinfo
root = Tk()
def Antonymns():
    b1.config(command=findantonyms)
    showinfo("Information","App is finally changed to antonymns")
def Synonmys():
    b1.config(command=findsynonmys)
    showinfo("Information", "App is finally changed to Synonmys")
def meaningfinder():
    a = t1.get(1.0,END)
    b = PyDictionary.PyDictionary.meaning(a)
    t2.insert(END,b)
def findantonyms():
    a = t1.get(1.0,END)
    b = PyDictionary.PyDictionary.antonym(a)
    t2.insert(END, b)
def findsynonmys():
    a = t1.get(1.0, END)
    b = PyDictionary.PyDictionary.synonym(a)
    t2.insert(END, b)
Mainmenu = Menu(root)
changemenu = Menu(Mainmenu)
Mainmenu.add_cascade(label="Change",menu=changemenu)
changemenu.add_command(label="Antonymns",command=Antonymns)
changemenu.add_command(label="Synonyms",command=Synonmys)
changemenu.add_command(label="Meaning",command=meaningfinder)
root.config(menu=Mainmenu)

root.maxsize(width=400,height=400)
root.title("Meaning finder")
l1 = Label(root,text="Word:",font=("Bold",20)).place(x=0,y=0)
t1 = Text(root)
t1.place(x=1,y=40,height=100,width=400)
t1value = t1.get(1.0,END)
global b1
b1 = Button(root,text="Find",command=meaningfinder)
l2 = Label(root,text="Answer:",font=("Bold",20)).place(x=1,y=180)
t2 = Text(root)
b1.place(x=1,y=150)
t2.place(x=1,y=220,height=100,width=400)
root.mainloop()