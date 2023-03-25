from loyer import *

def test_loyer():

    ## Test 1 : Le joueur peut payer

    monopoly_1={'nom':{0:'APL',1:'Cafet Bréguet', 2: 'Interlocal', 3:'RU Eiffel', 4:'Local ViaRézo', 5:'Musée',6:'Amphi Michelin',7:'RU Bréguet'},
    'possédé':{'Cafet Bréguet':0, 'Interlocal':0, 'RU Eiffel':2, 'Local ViaRézo':0, 'Musée':0, 'Amphi Michelin':0, 'RU Bréguet':0},
    'prix_achat':{'Cafet Bréguet': 200, 'Interlocal': 250, 'RU Eiffel': 300, 'Local ViaRézo': 350, 'Musée': 400, 'Amphi Michelin': 450, 'RU Bréguet': 500},
    'loyer':{'Cafet Bréguet': 5, 'Interlocal': 10, 'RU Eiffel': 15, 'Local ViaRézo': 20, 'Musée': 25, 'Amphi Michelin': 30, 'RU Bréguet': 35}}
    
    joueurs_1={'nom':{}, 'argent':{'1': 1000, '2': 1000}, 'position':{'1':0, '2':0}, 'prison':{'1': False, '2':False}}

    assert joueurs_1['argent']['1']>monopoly_1['loyer']['RU Eiffel']
    loyer(monopoly_1, joueurs_1, 3, 1)
    assert joueurs_1['argent']['1']==985
    assert joueurs_1['argent']['2']==1015


    ## Test 2 : le joueur ne peut pas payer

    monopoly_2={'nom':{0:'APL',1:'Cafet Bréguet', 2: 'Interlocal', 3:'RU Eiffel', 4:'Local ViaRézo', 5:'Musée',6:'Amphi Michelin',7:'RU Bréguet'},
    'possédé':{'Cafet Bréguet':0, 'Interlocal':0, 'RU Eiffel':2, 'Local ViaRézo':0, 'Musée':0, 'Amphi Michelin':0, 'RU Bréguet':0},
    'prix_achat':{'Cafet Bréguet': 200, 'Interlocal': 250, 'RU Eiffel': 300, 'Local ViaRézo': 350, 'Musée': 400, 'Amphi Michelin': 450, 'RU Bréguet': 500},
    'loyer':{'Cafet Bréguet': 5, 'Interlocal': 10, 'RU Eiffel': 15, 'Local ViaRézo': 20, 'Musée': 25, 'Amphi Michelin': 30, 'RU Bréguet': 35}}
    
    joueurs_2={'nom':{}, 'argent':{'1': 10, '2': 1000}, 'position':{'1':0, '2':0}, 'prison':{'1': False, '2':False}}



    assert joueurs_2['argent']['1']<monopoly_2['loyer']['RU Eiffel']
    loyer(monopoly_2, joueurs_2, 3, 1)
    assert joueurs_2['argent']['1']==0
    assert joueurs_2['argent']['2']==1010
