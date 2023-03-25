## CHOSES A ACTUALISER DANS CE SCRIPT

# Remplacer le None par l'identifiant de la case du Local ViaRézo quand celui-ci sera définitif
# Vérifier qu'il y a bien toujours 42 cases sur le plateau, et si non, changer cela dans le elif ... == 4
# Importer la fonction prison depuis le script de Thomas
# Regarder comment fonctionne la carte "vous sortez de prison" d'après ce qu'a fait Thomas

import plateau_gestion_arrivee as ga
from deplacements_plateau_11 import *
from random import randint 
from payer import *

cartes_chance = {
    1 : "Allez à la case APL.",
    2 : "Allez au local ViaRézo.",
    3 : "Payez 200€ ou piochez une autre carte chance.",
    4 : "Reculez de trois cases.",
    5 : "Allez en prison, sans passer par la case APL.",
    6 : "Césal a prélevé trop d'argent sur votre dernier loyer, vous touchez 200€.",
    7 : "Vous êtes libérés de prison ! Cette carte peut être conservée.",
    8 : "Vous avez mis le feu à votre appartement, payez 200€ de réparations."
}

def verifier_format(config, min = 0): # Cette fonction vérifie que config est une chaîne de caractère contenant
    # un entier supérieur ou égal à min
    bool = True
    while bool: # Boucle pour s'assurer que l'on obtient un entier positif dans l'input
        try:
            if int(config) >= min: # Si config n'est pas de la forme str(n) avec n entier, il y a une erreur
                bool = False
            else:
                config = input("Veuillez entrer un entier supérieur ou égal à " + str(min) + " : ")
        except:
            config = input("La saisie ne convient pas : ")


def melanger_cartes_chance(cartes_chance):
    # Renvoie une liste mélangée des cartes chance
    n = len(cartes_chance)
    L = [i for i in range(1, n+1)]
    cartes = []
    while len(L) >= 1:
        i = randint(0, len(L) - 1)
        cartes.append(L.pop(i))
    return cartes



def piocher_carte_chance(monopoly, joueurs, id_joueur, liste_des_cartes_chance, cartes_chance):
    
    # La liste liste_ces_cartes_chance permet de représenter les cartes comme un paquet. Quand une carte est piochée,
    # retourne en bas du paquet
    position_actuelle = joueurs['position'][str(id_joueur)]
    id_carte =  liste_des_cartes_chance.pop(0)
    liste_des_cartes_chance.append(id_carte)
    print(cartes_chance[id_carte])
    if id_carte == 1:
        joueurs['position'][str(id_joueur)] = 0
        print("Vous touchez 400€ d'APL !")
        joueurs['argent'][str(id_joueur)] += 400
    elif id_carte == 2:
        joueurs['position'][str(id_joueur)] = 9 # En supposant que le Local ViaRézo soit la première des propriétés bleu clair
    elif id_carte == 3:
        choix=-1
        while choix!='0' and choix!='1':
            choix = input("Que choisissez-vous ? (0 = Payer 200€, 1 = Piocher une autre carte chance)")
        if int(choix) == 0:
            payer(200, id_joueur, monopoly, joueurs)
            print("Vous avez été débité de 200€")
        else:
            piocher_carte_chance(monopoly, joueurs, id_joueur, liste_des_cartes_chance, cartes_chance)
    elif id_carte == 4:
        joueurs['position'][str(id_joueur)] = (position_actuelle - 3) % 40
    elif id_carte == 5:
        print("Vous devez aller en prison")
        prison(id_joueur, monopoly, joueurs, cartes_chance, liste_des_cartes_chance)
    elif id_carte == 6:
        joueurs['argent'][str(id_joueur)] += 200
    elif id_carte == 7:
        joueurs['libere de prison'][str(id_joueur)] += 1
    else:
        payer(200, id_joueur, monopoly, joueurs)
    if joueurs['position'][str(id_joueur)] != position_actuelle: # si le joueur a changé de position
        ga.arrivee(id_joueur, joueurs, monopoly, cartes_chance, liste_des_cartes_chance)

