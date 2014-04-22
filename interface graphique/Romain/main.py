# -*-coding:Latin-1 -*-
from tkinter import *
#from param_cours import *

import fct_type
import fct_duree
import param_cours
import toto


class MenuBar(Frame):
    """Barre de menus déroulants"""
    def __init__(self, boss =None):
        Frame.__init__(self, borderwidth =1)

        ##### Menu <Type> #####
        fileMenuType = Menubutton(self, text ='Type', relief=RAISED)
        fileMenuType.pack(side =LEFT)
        
        ##### Menu <Durée> #####
        fileMenuDuree = Menubutton(self, text ='Durée', relief=RAISED)
        fileMenuDuree.pack(side =BOTTOM)
        
        # Partie "déroulante" :
        me1 = Menu(fileMenuType)
        me1.add_command(label ='Cours', underline =0, command = boss.cours)
        me1.add_command(label ='Travaux Dirigés', underline =0, command = boss.travauxDiriges)
        me1.add_command(label ='Travaux Pratique', underline =0, command = boss.travauxPratique)

        me2 = Menu(fileMenuDuree)
        me2.add_command(label ='1h', underline =0, command = boss.duree1h)
        me2.add_command(label ='2h', underline =0, command = boss.duree2h)
        me2.add_command(label ='4h', underline =0, command = boss.duree4h)
        
        # Intégration du menu :
        fileMenuType.configure(menu = me1)
        fileMenuDuree.configure(menu = me2) 

class Application(Frame):
    """Application principale"""
    def __init__(self, boss =None):
        Frame.__init__(self)
        self.master.title('Fenêtre avec menus')
        self.master.geometry('%dx%d+%d+%d' % (320, 240, 0, 0))
        mBar = MenuBar(self)
        mBar.pack()
        #self.can = Canvas(self, bg='light grey', height=50, width=250, borderwidth =2)
        #self.can.pack()
        self.pack()

    def cours(self):
        print("Cours")
    def travauxDiriges(self):
        print("Travaux Dirigés")
    def travauxPratique(self):
        print("Travaux Pratique")
    def duree1h(self):
        print("Durée = 1h")
    def duree2h(self):
        print("Durée = 2h")
    def duree4h(self):
        print("Durée = 4h")
        
if __name__ == '__main__':
    app = Application()
    app.mainloop()



##fenetre_principale = Tk()                       # Création d'une fenêtre
##fenetre_principale.title("Fiche de présence")   # Titre de la fenêtre
#### application.attributes('-fullscreen', 1)     # Fenêtre en fullscreen
##
### Taille souhaite de la fenetre
##w = 320
##h = 240
##
### Position de la fenetre
##x = 0
##y = 0
##
### Application des paramettres
##fenetre_principale.geometry('%dx%d+%d+%d' % (w, h, x, y))
##
### Création de la frame 1
##frame1 = Frame(fenetre_principale, bg="yellow", padx=0, pady=0)
##frame1.pack(side=BOTTOM,fill=X)
##
### Création de la frame 2
##frame2 = Frame(fenetre_principale, bg="blue")
##frame2.pack(side=RIGHT,fill=Y)
##
##b1 = Button(frame2, text ="Quit",command =fenetre_principale.destroy)
##b1.pack(side =TOP, padx =3, pady =3)






















### Menu type cours
####mb = Menubutton(frame1, text="Type", relief=RAISED, direction='above')
####mb.grid()
####mb.menu  =  Menu ( mb, tearoff = 0 )
####mb["Menu type cours"]  =  mb.menu
####
####cours_var  = IntVar()
####TD_var = IntVar()
####TP_var = IntVar()
####
####mb.menu.add_checkbutton (label="Cours", variable=cours_var)
####mb.menu.add_checkbutton (label="Travaux Dirigés", variable=TD_var)
####mb.menu.add_checkbutton (label="Travaux Pratique", variable=TP_var)
####mb.pack(side =LEFT, padx =3, pady =3)
##
### Menu durée
##mb1 = Menubutton(frame1, text="Durée", relief=RAISED, direction='above')
###mb1.grid()
##mb1.menu  =  Menu ( mb1, tearoff = 0 )
##mb1["Menu durée"]  =  mb1.menu
##    
##unh_var = IntVar()
##deuxh_var = IntVar()
##quatreh_var = IntVar()
##
##mb1.menu.add_checkbutton (label="1h", variable=unh_var)
##mb1.menu.add_checkbutton (label="2h", variable=deuxh_var)
##mb1.menu.add_checkbutton (label="4h", variable=quatreh_var)
##mb1.pack(side =RIGHT, padx =3, pady =3)
##
###b2 = Button(frame1, text ='Type',command = fct_type.type_cours)
###b2.pack(side =LEFT, padx =3, pady =3)	#fill =X, expand=0
##
###b3 = Button(frame1, text ='Durée',command = fct_duree.duree)
###b3.pack(side =RIGHT, padx =3, pady =3)
##
######
##scrollbar = Scrollbar(fenetre_principale)
##scrollbar.pack(side=RIGHT, fill=Y)
##
##Lb1 = Listbox(application)
##Lb1.insert(1, "Python")
##Lb1.insert(2, "Perl")
##Lb1.insert(3, "C")
##Lb1.insert(4, "PHP")
##Lb1.insert(5, "JSP")
##Lb1.insert(6, "Ruby")
##Lb1.insert(7, "Python")
##Lb1.insert(8, "Perl")
##Lb1.insert(9, "C")
##Lb1.insert(10, "PHP")
##Lb1.insert(11, "JSP")
##Lb1.insert(12, "Ruby")
##Lb1.insert(13, "Python")
##Lb1.insert(14, "Perl")
##Lb1.insert(15, "C")
##Lb1.insert(16, "PHP")
##Lb1.insert(17, "JSP")
##Lb1.insert(18, "Ruby")
##
##Lb1.pack(side =LEFT,fill=X)
##
##Lb1.config(yscrollcommand=scrollbar.set)
##scrollbar.config(command=Lb1.yview)
###### 
##
##fenetre_principale.mainloop()
##
###magie = param_cours.Cours("Cours")
###magie.type_cours = "Cours"
###print(magie.type_cours)
###print(magie.type_cours)
