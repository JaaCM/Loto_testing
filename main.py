""""Tentative de creation d'un logiciel de LOTO / LOTERIE
    Necessité de la génération de 2 liste contenant les numéro + (concat) des Num Complementaire
    Une Fonction pour generer les deux liste, une autre pour choisir ses numéros.
"""
import random


liste_numeros = [n for n in range(1,31)] # la liste contient tout les chiffres de 1 à 31
#liste_compl = [nc for nc in range(1,6)]


def tirage_numeros(liste, nb_numeros):
    tirage = []
    while len(tirage)< nb_numeros :
        rand_numb = random.randint(min(liste)-1, max(liste)-1)
        if not liste_numeros[rand_numb] in tirage:
            tirage.append(liste[rand_numb])
    return tirage


def compare_numeros(liste_joueur):
    tirage_du_jour = tirage_numeros(liste_numeros, 5)
    nb_de_bon_numeros = 0
    jackpot = False
    #print(tirage_du_jour)
    for numeros in liste_joueur:
        if numeros in tirage_du_jour:
            nb_de_bon_numeros += 1
        if nb_de_bon_numeros == 4:
            jackpot = True
    return nb_de_bon_numeros, jackpot


liste_joueur_fixe = [11, 22, 31, 25, 9]
nb_bon_numeros, jackpot_state = compare_numeros(liste_joueur_fixe)
compteur_tirage = 0

while not jackpot_state:
    compteur_tirage += 1
    nb_bon_numeros, jackpot_state = compare_numeros(liste_joueur_fixe)
    if compteur_tirage == 1000000:
        print("1 milions de test")
    if compteur_tirage == 10000000:
        print("10 millions test")
    if compteur_tirage == 100000000:
        print("100 millions..")
    #print("Vous avez", nb_bon_numeros,"bon numéros")
    #print(compteur_tirage)

print("Whouuuu c'est le jackpot, il aura fallu:", compteur_tirage,"tentatives !")




