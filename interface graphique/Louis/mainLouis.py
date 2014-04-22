# -*-coding:Latin-1 -*
import baseDonnee
import copy


"""Variables"""
listeEtudiants=[]

# Importe les étudiants du ficher txt
listeEtudiants=baseDonnee.importFichier(listeEtudiants, "liste_etudiants.txt")  

# Ajout de numéros étudiants
listeEtudiants=baseDonnee.ajoutNumCarte(listeEtudiants, "Velay", 1)
listeEtudiants=baseDonnee.ajoutNumCarte(listeEtudiants, "Lugand", 2)
listeEtudiants=baseDonnee.ajoutNumCarte(listeEtudiants, "Bortoli", 3)


# Ajout d'un non absent
listeAbsents = copy.deepcopy(listeEtudiants)
listeAbsents=baseDonnee.retraitAbsent(listeAbsents, 2)
listeAbsents=baseDonnee.retraitAbsent(listeAbsents, 1)


# Affichage des listes
print("Etudiants dans la base :")
for etu in listeEtudiants:
    print (etu.prenom, etu.nom, etu.numCarte)

print("Etudiants présents :")
for etu in listeAbsents:
    print (etu.prenom, etu.nom, etu.numCarte)


