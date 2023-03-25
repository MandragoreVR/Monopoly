# monopoly={'nom':{0:'APL',1:'Cafet Bréguet', 2: 'Interlocal', 3:'RU Eiffel', 4:'Local ViaRézo', 5:'Musée',6:'Amphi Michelin',7:'RU Bréguet'},
#  'possédé':{'Cafet Bréguet':0, 'Interlocal':0, 'RU Eiffel':0, 'Local ViaRézo':0, 'Musée':0, 'Amphi Michelin':0, 'RU Bréguet':0},
#  'prix_achat':{'Cafet Bréguet': 200, 'Interlocal': 250, 'RU Eiffel': 300, 'Local ViaRézo': 350, 'Musée': 400, 'Amphi Michelin': 450, 'RU Bréguet': 500},
#  'loyer':{'Cafet Bréguet': 5, 'Interlocal': 10, 'RU Eiffel': 15, 'Local ViaRézo': 20, 'Musée': 25, 'Amphi Michelin': 30, 'RU Bréguet': 35}}
 
# joueurs={'nom':{}, 'argent':{'1': 1000, '2': 1000}, 'position':{'1':0, '2':0}}

from achat import achat
from loyer import loyer


def arrivee(indice_joueur, joueurs, monopoly):
    indice_case=joueurs['position'][str(indice_joueur)]
    N=monopoly['nom'][indice_case] #on appelle N le nom du lieu sur lequel arrive le joueur
    print('Vous êtes sur la case ' + N)
    if N == 'APL':
        print('Vous êtes sur la case APL')
        _ = input('Appuyez sur entrée pour continuer')
    elif monopoly['possédé'][N] != indice_joueur:        #si le joueur ne possède pas le lieu soit il l'achète soit il paie un loyer
        print('Cette propriété ne vous appartient pas')
        if monopoly['possédé'][N] == 0:
            achat(indice_joueur, monopoly, joueurs)
        else:
            print('Vous devez payer un loyer')
            loyer(monopoly, joueurs, joueurs['position'][str(indice_joueur)], indice_joueur)
            _ = input('Vous avez été débité. Appuyez sur la touche entrée pour continuer')
    else:
        print('Vous êtes chez vous !')
        _ = input("Appuyez sur entrée pour continuer")