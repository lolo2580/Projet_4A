# -*-coding:Latin-1 -*-
from tkinter import *
import toto

def duree():
    #création d'une fenetre au premier niveau
    fen_duree=Toplevel()

    #taille souhaite de la fenetre
    w = 120
    h = 200

    #position de la fenetre
    x = 100
    y = 20

    #application des paramettres
    fen_duree.geometry('%dx%d+%d+%d' % (w, h, x, y))
    
    bouton_type_1 = Button(fen_duree, text ='1 heure',command =fen_duree.destroy)
    bouton_type_1.pack(side =TOP, fill=X, padx =3, pady =3)
    
    bouton_type_2 = Button(fen_duree, text ='2 heures',command =fen_duree.destroy)
    bouton_type_2.pack(side =TOP, fill=X, padx =3, pady =3)
    
    bouton_type_3 = Button(fen_duree, text ='4 heures',command =toto.toto)
    bouton_type_3.pack(side =TOP, fill=X, padx =3, pady =3)
    
    bouton_type_4 = Button(fen_duree, text ='Autre',command =fen_duree.destroy)
    bouton_type_4.pack(side =TOP, fill=X, padx =3, pady =3)

    bouton_type_5 = Button(fen_duree, text ='Retour',command =fen_duree.destroy)
    bouton_type_5.pack(side =TOP, fill=X, padx =3, pady =3)
