# -*-coding:Latin-1 -*-
from tkinter import *
from param_cours import *

""" Variable """


def type_cours():
    #création d'une fenetre au premier niveau
    fen_type=Toplevel()

    #taille souhaite de la fenetre
    w = 120
    h = 200

    #position de la fenetre
    x = 100
    y = 20

    #application des paramettres
    fen_type.geometry('%dx%d+%d+%d' % (w, h, x, y))
    
    bouton_type_1 = Button(fen_type, text ='Cours',command =return_type(1))
    bouton_type_1.pack(side =TOP, fill=X, padx =3, pady =3)
    
    bouton_type_2 = Button(fen_type, text ='Travaux Dirigés',command =return_type(2))
    bouton_type_2.pack(side =TOP, fill=X, padx =3, pady =3)
    
    bouton_type_3 = Button(fen_type, text ='Travaux Pratique',command =return_type(3))
    bouton_type_3.pack(side =TOP, fill=X, padx =3, pady =3)
    
    bouton_type_4 = Button(fen_type, text ='Retour',command =fen_type.destroy)
    bouton_type_4.pack(side =TOP, fill=X, padx =3, pady =3)

def return_type(choix):
    if choix == 1:
        magie.type_cours = "Cours"
    """if choix == 2:
        return "cours"
    if choix == 3:
        return "TP"""

magie = Cours("Cours")
#magie.type_cours = "Cours"
print(magie.type_cours)
