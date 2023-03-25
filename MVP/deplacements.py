# monopoly={'nom':{0:'APL',1:'Cafet Bréguet', 2: 'Interlocal', 3:'RU Eiffel', 4:'Local ViaRézo', 5:'Musée',6:'Amphi Michelin',7:'RU Bréguet'},
#  'possédé':{'Cafet Bréguet':0, 'Interlocal':0, 'RU Eiffel':0, 'Local ViaRézo':0, 'Musée':0, 'Amphi Michelin':0, 'RU Bréguet':0},
#  'prix_achat':{'Cafet Bréguet': 200, 'Interlocal': 250, 'RU Eiffel': 300, 'Local ViaRézo': 350, 'Musée': 400, 'Amphi Michelin': 450, 'RU Bréguet': 500},
#  'loyer':{'Cafet Bréguet': 5, 'Interlocal': 10, 'RU Eiffel': 15, 'Local ViaRézo': 20, 'Musée': 25, 'Amphi Michelin': 30, 'RU Bréguet': 35}}

# joueurs={'nom':{}, 'argent':{'1': 1000, '2': 1000}, 'position':{'1':0, '2':0}}
import random as rd

def lancer_de(ind_joueur, monopoly, joueurs):    #joueur est l'entier correspondant au numéro du joueur
    nb_de_cases=rd.randint(1,3)   # on lance un dé de 3 pour déterminer le nombre de cases dont le joueur va avancer
    print('Le joueur ' + str(ind_joueur) + ' avance de ' + str(nb_de_cases) +' cases.')
    placement=joueurs['position'][str(ind_joueur)]
    placement+=nb_de_cases

    if placement>8:             
        placement=placement-8                # pour repartir sur le bon numéro de case si c'est supérieur à 7
        print("Vous touchez 200€ d'APL :) ")
        joueurs['argent'][str(ind_joueur)]+=200
        print ("Vous avez actuellement " + str(joueurs['argent'][str(ind_joueur)]) + " euros.")
    elif placement == 8:
        placement = 0
        print("Vous touchez 400€d'APL :) ")
        joueurs['argent'][str(ind_joueur)] += 400
        print ("Vous avez actuellement " + str(joueurs['argent'][str(ind_joueur)]) + " euros.")

    joueurs['position'][str(ind_joueur)]=placement
