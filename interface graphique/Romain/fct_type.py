# -*-coding:Latin-1 -*-
from tkinter import *
import param_cours
import toto

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
    
    bouton_type_1 = Button(fen_type, text ='Cours',command =return_type("Cours"), state=DISABLED)
    bouton_type_1.pack(side =TOP, fill=X, padx =3, pady =3)
    #print(bouton_type_1.state)
    bouton_type_2 = Button(fen_type, text ='Travaux Dirigés',command =return_type("Travaux Dirigés"))
    bouton_type_2.pack(side =TOP, fill=X, padx =3, pady =3)
    
    bouton_type_3 = Button(fen_type, text ='Travaux Pratique',command =return_type("Travaux Pratique"))
    bouton_type_3.pack(side =TOP, fill=X, padx =3, pady =3)
    
    bouton_type_4 = Button(fen_type, text ='Retour',command =fen_type.destroy)
    bouton_type_4.pack(side =TOP, fill=X, padx =3, pady =3)

def return_type(chaine):
    magie = param_cours.Cours(chaine)
    print(magie.type_cours)
