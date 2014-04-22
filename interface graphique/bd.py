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



""" Ajout des étudiants du fichier à la liste """
def importFichier(liste, fichier):
    with open (fichier, "r") as f:  # Ouvre le fichier et le ferme proprement à la fin de la boucle

        # Récupère le fichier sous forme de string et la découpe (tous les blancs) en tableau 
        args=f.read().split()

        i=0
        while i < len(args):        # Ajoute les élts du tableau à la liste des étudiants
            liste+=[Etudiant(args[i],args[i+1])]
            i+=2
    # Fermeture fichier
    return liste


""" Ajout du numéro étudiant """
def ajoutNumCarte(liste, nom, numeroCarte):
    
    
    return liste
