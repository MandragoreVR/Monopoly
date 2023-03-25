from achat import *
import sys
from io import StringIO

def mock_return_0(_):
    return '0'

def mock_return_1(_):
    return '1'

def test_achat(monkeypatch):

    ## Le joueur a assez d'argent et il achète

    monopoly_1={'nom':{0:'APL',1:'Cafet Bréguet', 2: 'Interlocal', 3:'RU Eiffel', 4:'Local ViaRézo', 5:'Musée',6:'Amphi Michelin',7:'RU Bréguet'},
    'possédé':{'Cafet Bréguet':0, 'Interlocal':0, 'RU Eiffel':0, 'Local ViaRézo':0, 'Musée':0, 'Amphi Michelin':0, 'RU Bréguet':0},
    'prix_achat':{'Cafet Bréguet': 200, 'Interlocal': 250, 'RU Eiffel': 300, 'Local ViaRézo': 350, 'Musée': 400, 'Amphi Michelin': 450, 'RU Bréguet': 500},
    'loyer':{'Cafet Bréguet': 5, 'Interlocal': 10, 'RU Eiffel': 15, 'Local ViaRézo': 20, 'Musée': 25, 'Amphi Michelin': 30, 'RU Bréguet': 35}}

    joueurs_1={'nom':{}, 'argent':{'1': 1000, '2': 1000}, 'position':{'1':2, '2':0}, 'prison':{'1': False, '2':False}}    


    monkeypatch.setattr('builtins.input',mock_return_1)
    placement=joueurs_1['position']['1']
    nom_prop=monopoly_1['nom'][placement]
    assert joueurs_1['argent']['1']>monopoly_1['prix_achat'][nom_prop]
    achat(1, monopoly_1, joueurs_1)
    assert monopoly_1['possédé'][nom_prop] == 1
    assert joueurs_1['argent']['1']==750

    ## Le joueur a assez d'argent mais il n'achète pas

    monopoly_2={'nom':{0:'APL',1:'Cafet Bréguet', 2: 'Interlocal', 3:'RU Eiffel', 4:'Local ViaRézo', 5:'Musée',6:'Amphi Michelin',7:'RU Bréguet'},
    'possédé':{'Cafet Bréguet':0, 'Interlocal':0, 'RU Eiffel':0, 'Local ViaRézo':0, 'Musée':0, 'Amphi Michelin':0, 'RU Bréguet':0},
    'prix_achat':{'Cafet Bréguet': 200, 'Interlocal': 250, 'RU Eiffel': 300, 'Local ViaRézo': 350, 'Musée': 400, 'Amphi Michelin': 450, 'RU Bréguet': 500},
    'loyer':{'Cafet Bréguet': 5, 'Interlocal': 10, 'RU Eiffel': 15, 'Local ViaRézo': 20, 'Musée': 25, 'Amphi Michelin': 30, 'RU Bréguet': 35}}

    joueurs_2={'nom':{}, 'argent':{'1': 1000, '2': 1000}, 'position':{'1':2, '2':0}, 'prison':{'1': False, '2':False}}    


    monkeypatch.setattr('builtins.input',mock_return_0)
    placement=joueurs_2['position']['1']
    nom_prop=monopoly_2['nom'][placement]
    assert joueurs_2['argent']['1']>monopoly_2['prix_achat'][nom_prop]
    achat(1, monopoly_2, joueurs_2)
    assert monopoly_2['possédé'][nom_prop] == 0
    assert joueurs_2['argent']['1']== 1000



    ## Le joueur n'a pas assez d'argent
    
    monopoly_3={'nom':{0:'APL',1:'Cafet Bréguet', 2: 'Interlocal', 3:'RU Eiffel', 4:'Local ViaRézo', 5:'Musée',6:'Amphi Michelin',7:'RU Bréguet'},
    'possédé':{'Cafet Bréguet':0, 'Interlocal':0, 'RU Eiffel':0, 'Local ViaRézo':0, 'Musée':0, 'Amphi Michelin':0, 'RU Bréguet':0},
    'prix_achat':{'Cafet Bréguet': 200, 'Interlocal': 250, 'RU Eiffel': 300, 'Local ViaRézo': 350, 'Musée': 400, 'Amphi Michelin': 450, 'RU Bréguet': 500},
    'loyer':{'Cafet Bréguet': 5, 'Interlocal': 10, 'RU Eiffel': 15, 'Local ViaRézo': 20, 'Musée': 25, 'Amphi Michelin': 30, 'RU Bréguet': 35}}

    joueurs_3={'nom':{}, 'argent':{'1': 200, '2': 1000}, 'position':{'1':2, '2':0}, 'prison':{'1': False, '2':False}}   

    monkeypatch.setattr('builtins.input',mock_return_1)
    placement=joueurs_3['position']['1']
    nom_prop=monopoly_3['nom'][placement]
    assert joueurs_3['argent']['1']<monopoly_3['prix_achat'][nom_prop]
    achat(1, monopoly_3, joueurs_3)
    assert monopoly_3['possédé'][nom_prop] == 0
    assert joueurs_3['argent']['1']==200

