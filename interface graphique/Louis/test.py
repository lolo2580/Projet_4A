# -*-coding:Latin-1 -*

import baseDonnee


"""Variables"""
listeEtudiants=[]


# Importe les étudiants du ficher txt
listeEtudiants=baseDonnee.importFichier(listeEtudiants, "liste_etudiants.txt")  


"""Main"""
print("Etudiants dans la base :")
for etu in listeEtudiants:
    print (etu.prenom + " " + etu.nom)

