# -*-coding:Latin-1 -*


"""Classe Etudiant"""
class Etudiant:
    # Attributs
    nom = ""
    prenom = ""
    numCarte = 0
    # constructeur
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom



""" Ajout des �tudiants du fichier � la liste """
def importFichier(liste, fichier):
    with open (fichier, "r") as f:  # Ouvre le fichier et le ferme proprement � la fin de la boucle

        # R�cup�re le fichier sous forme de string et la d�coupe (tous les blancs) en tableau 
        args=f.read().split()

        i=0
        while i < len(args):        # Ajoute les �lts du tableau � la liste des �tudiants
            liste+=[Etudiant(args[i],args[i+1])]
            i+=2
    # Fermeture fichier
    return liste


""" Ajout du num�ro �tudiant """
def ajoutNumCarte(liste, nom, numeroCarte):
    
    
    return liste
