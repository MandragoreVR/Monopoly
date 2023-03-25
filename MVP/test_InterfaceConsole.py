from InterfaceConsole import *


def test_ajout_ligne_proprietaire():

    ## Propriété libre

    monopoly_0={'nom':{0:'APL',1:'Cafet Bréguet', 2: 'Interlocal', 3:'RU Eiffel', 4:'Local ViaRézo', 5:'Musée',6:'Amphi Michelin',7:'RU Bréguet'},
    'possédé':{'Cafet Bréguet':0, 'Interlocal':0, 'RU Eiffel':0, 'Local ViaRézo':0, 'Musée':0, 'Amphi Michelin':0, 'RU Bréguet':0},
    'prix_achat':{'Cafet Bréguet': 200, 'Interlocal': 250, 'RU Eiffel': 300, 'Local ViaRézo': 350, 'Musée': 400, 'Amphi Michelin': 450, 'RU Bréguet': 500},
    'loyer':{'Cafet Bréguet': 5, 'Interlocal': 10, 'RU Eiffel': 15, 'Local ViaRézo': 20, 'Musée': 25, 'Amphi Michelin': 30, 'RU Bréguet': 35}}

    res=ajout_ligne_proprietaire(monopoly_0, 3)
    assert res== ' A vendre : 300'

    ## Propriété appartenante au joueur 1

    monopoly_1={'nom':{0:'APL',1:'Cafet Bréguet', 2: 'Interlocal', 3:'RU Eiffel', 4:'Local ViaRézo', 5:'Musée',6:'Amphi Michelin',7:'RU Bréguet'},
    'possédé':{'Cafet Bréguet':0, 'Interlocal':0, 'RU Eiffel':1, 'Local ViaRézo':0, 'Musée':0, 'Amphi Michelin':0, 'RU Bréguet':0},
    'prix_achat':{'Cafet Bréguet': 200, 'Interlocal': 250, 'RU Eiffel': 300, 'Local ViaRézo': 350, 'Musée': 400, 'Amphi Michelin': 450, 'RU Bréguet': 500},
    'loyer':{'Cafet Bréguet': 5, 'Interlocal': 10, 'RU Eiffel': 15, 'Local ViaRézo': 20, 'Musée': 25, 'Amphi Michelin': 30, 'RU Bréguet': 35}}

    res=ajout_ligne_proprietaire(monopoly_1, 3)
    assert res== ' Propriété de *'

    ## Propriété appartenante au joueur 2

    monopoly_2={'nom':{0:'APL',1:'Cafet Bréguet', 2: 'Interlocal', 3:'RU Eiffel', 4:'Local ViaRézo', 5:'Musée',6:'Amphi Michelin',7:'RU Bréguet'},
    'possédé':{'Cafet Bréguet':0, 'Interlocal':0, 'RU Eiffel':2, 'Local ViaRézo':0, 'Musée':0, 'Amphi Michelin':0, 'RU Bréguet':0},
    'prix_achat':{'Cafet Bréguet': 200, 'Interlocal': 250, 'RU Eiffel': 300, 'Local ViaRézo': 350, 'Musée': 400, 'Amphi Michelin': 450, 'RU Bréguet': 500},
    'loyer':{'Cafet Bréguet': 5, 'Interlocal': 10, 'RU Eiffel': 15, 'Local ViaRézo': 20, 'Musée': 25, 'Amphi Michelin': 30, 'RU Bréguet': 35}}

    res=ajout_ligne_proprietaire(monopoly_2, 3)
    assert res== ' Propriété de §'




def test_ajout_ligne_presence_1():
    joueurs_test_1={'nom':{}, 'argent':{'1': 1000, '2': 1000}, 'position':{'1':2, '2':0}, 'prison':{'1': False, '2':False}}
    res=ajout_ligne_presence_1(joueurs_test_1,2)
    assert res=='*'.center(15)

    joueurs_test_2={'nom':{}, 'argent':{'1': 1000, '2': 1000}, 'position':{'1':0, '2':0}, 'prison':{'1': False, '2':False}}
    res=ajout_ligne_presence_1(joueurs_test_2,2)
    assert res==' '.center(15)



def test_ajout_ligne_presence_2():
    joueurs_test_1={'nom':{}, 'argent':{'1': 1000, '2': 1000}, 'position':{'1':0, '2':2}, 'prison':{'1': False, '2':False}}
    res=ajout_ligne_presence_2(joueurs_test_1,2)
    assert res=='§'.center(15)

    joueurs_test_2={'nom':{}, 'argent':{'1': 1000, '2': 1000}, 'position':{'1':0, '2':0}, 'prison':{'1': False, '2':False}}
    res=ajout_ligne_presence_2(joueurs_test_2,2)
    assert res==' '.center(15)






def test_affichage():
    res=affichage(monopoly={'nom':{0:'APL',1:'Cafet Bréguet', 2: 'Interlocal', 3:'RU Eiffel', 4:'Local ViaRézo', 5:'Musée',6:'Amphi Michelin',7:'RU Bréguet'},
    'possédé':{'Cafet Bréguet':0, 'Interlocal':0, 'RU Eiffel':0, 'Local ViaRézo':0, 'Musée':0, 'Amphi Michelin':0, 'RU Bréguet':0},
    'prix_achat':{'Cafet Bréguet': 200, 'Interlocal': 250, 'RU Eiffel': 300, 'Local ViaRézo': 350, 'Musée': 400, 'Amphi Michelin': 450, 'RU Bréguet': 500},
    'loyer':{'Cafet Bréguet': 5, 'Interlocal': 10, 'RU Eiffel': 15, 'Local ViaRézo': 20, 'Musée': 25, 'Amphi Michelin': 30, 'RU Bréguet': 35}},joueurs={'nom':{}, 'argent':{'1': 1000, '2': 1000}, 'position':{'1':0, '2':0}, 'prison':{'1': False, '2':False}})
    assert res== None               ## Pas moyen de controler l'affichage de la grille
                                    ## Mais on voit que l'affichage dans la console correspond
    
 