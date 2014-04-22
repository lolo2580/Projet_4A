# -*-coding:Latin-1 -*-
from tkinter import *
import fct_type
import fct_duree

application = Tk()                          #création d'une fenêtre
application.title("Fiche de présence")      #titre de la fenêtre
#application.attributes('-fullscreen', 1)   #fenêtre en fullscreen

#taille souhaite de la fenetre
w = 320
h = 240

#position de la fenetre
x = 0
y = 0

#application des paramettres
application.geometry('%dx%d+%d+%d' % (w, h, x, y))

frame1 = Frame(application, bg="yellow", padx=0, pady=0)
frame1.pack(side=BOTTOM,fill=X)

frame2 = Frame(application, bg="blue")
frame2.pack(side=RIGHT,fill=Y)

b1 = Button(frame2, text ='Quit',command =application.destroy)
b1.pack(side =TOP, padx =3, pady =3)

b2 = Button(frame1, text ='Type',command = fct_type.type)
b2.pack(side =LEFT, padx =3, pady =3)	#fill =X, expand=0

b3 = Button(frame1, text ='Durée',command = fct_duree.duree)
b3.pack(side =RIGHT, padx =3, pady =3)

####
scrollbar = Scrollbar(application)
scrollbar.pack(side=RIGHT, fill=Y)

Lb1 = Listbox(application)
Lb1.insert(1, "Python")
Lb1.insert(2, "Perl")
Lb1.insert(3, "C")
Lb1.insert(4, "PHP")
Lb1.insert(5, "JSP")
Lb1.insert(6, "Ruby")
Lb1.insert(7, "Python")
Lb1.insert(8, "Perl")
Lb1.insert(9, "C")
Lb1.insert(10, "PHP")
Lb1.insert(11, "JSP")
Lb1.insert(12, "Ruby")
Lb1.insert(13, "Python")
Lb1.insert(14, "Perl")
Lb1.insert(15, "C")
Lb1.insert(16, "PHP")
Lb1.insert(17, "JSP")
Lb1.insert(18, "Ruby")

Lb1.pack(side =LEFT,fill=X)

Lb1.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=Lb1.yview)
#### 

application.mainloop()
