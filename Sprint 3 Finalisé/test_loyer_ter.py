from loyer_ter import *

def test_loyer_bis():
    monopoly = {
        'nom': {
            0: 'APL',
            1: 'Cafet Bréguet',
            2: 'Interlocal',
            3: 'RU Eiffel',
            4: 'Local ViaRézo',
            5: 'Musée',
            6: 'Amphi Michelin',
            7: 'RU Bréguet'
        },
        'possédé': {
            'Cafet Bréguet': 2,
            'Interlocal': 0,
            'RU Eiffel': 1,
            'Local ViaRézo': 1,
            'Musée': 2,
            'Amphi Michelin': 2,
            'RU Bréguet': 0
        },
        'prix_achat': {
            'Cafet Bréguet': 200,
            'Interlocal': 250,
            'RU Eiffel': 300,
            'Local ViaRézo': 350,
            'Musée': 400,
            'Amphi Michelin': 450,
            'RU Bréguet': 500
        },
        'loyer': {
            'Cafet Bréguet': 5,
            'Interlocal': 10,
            'RU Eiffel': 15,
            'Local ViaRézo': 20,
            'Musée': 25,
            'Amphi Michelin': 30,
            'RU Bréguet': 35
        },
        'maison' : {
            'Cafet Bréguet':0,
            'Interlocal':0,
            'RU Eiffel':0,
            'Local ViaRézo':0,
            'Musée':0,
            'Amphi Michelin':0,
            'RU Bréguet':0
        },
        'prix maison':{
            'Cafet Bréguet': 50,
            'Interlocal': 50,
            'RU Eiffel': 50,
            'Local ViaRézo': 100,
            'Musée': 100,
            'Amphi Michelin': 100,
            'RU Bréguet': 150
        }
    }
    joueurs = {
        'nom': {},
        'argent': {
            '1': 1000,
            '2': 1000
        },
        'position': {
            '1': 4,
            '2': 3
        },
        'prison': {
            '1': 0,
            '2': 0
        },
        'dernier lancer dés': {
            '1': 3,
            '2': 7
        }
    }
    loyer_ter(monopoly, joueurs, 3, 2)
    assert joueurs['argent']['2']==985
    assert joueurs['argent']['1']==1015
    monopoly = {
        'nom': {
            0: 'APL',
            1: 'Cafet Bréguet',
            2: 'Interlocal',
            3: 'RU Eiffel',
            4: 'Local ViaRézo',
            5: 'Musée',
            6: 'Amphi Michelin',
            7: 'RU Bréguet'
        },
        'possédé': {
            'Cafet Bréguet': 0,
            'Interlocal': 0,
            'RU Eiffel': 1,
            'Local ViaRézo': 1,
            'Musée': 0,
            'Amphi Michelin': 1,
            'RU Bréguet': 0
        },
        'prix_achat': {
            'Cafet Bréguet': 200,
            'Interlocal': 250,
            'RU Eiffel': 300,
            'Local ViaRézo': 350,
            'Musée': 400,
            'Amphi Michelin': 450,
            'RU Bréguet': 500
        },
        'loyer': {
            'Cafet Bréguet': 5,
            'Interlocal': 10,
            'RU Eiffel': 15,
            'Local ViaRézo': 20,
            'Musée': 25,
            'Amphi Michelin': 30,
            'RU Bréguet': 35
        },
        'maison' : {
            'Cafet Bréguet':0,
            'Interlocal':0,
            'RU Eiffel':0,
            'Local ViaRézo':0,
            'Musée':0,
            'Amphi Michelin':0,
            'RU Bréguet':0
        },
        'prix maison':{
            'Cafet Bréguet': 50,
            'Interlocal': 50,
            'RU Eiffel': 50,
            'Local ViaRézo': 100,
            'Musée': 100,
            'Amphi Michelin': 100,
            'RU Bréguet': 150
        }
    }
    joueurs = {
        'nom': {},
        'argent': {
            '1': 1000,
            '2': 10
        },
        'position': {
            '1': 4,
            '2': 3
        },
        'prison': {
            '1': 0,
            '2': 0
        },
        'dernier lancer dés': {
            '1': 3,
            '2': 7
        }
    }
    loyer_ter(monopoly, joueurs, 3, 2)
    #2 n'a pas les moyens pour payer le loyer donc 1 ne devrait recevoir que l'argent que possède 2
    assert joueurs['argent']['2']==-5
    assert joueurs['argent']['1']==1010
    monopoly = {
        'nom': {
            0: 'APL',
            1: 'Cafet Bréguet',
            2: 'Interlocal',
            3: 'RU Eiffel',
            4: 'Local ViaRézo',
            5: 'Musée',
            6: 'Amphi Michelin',
            7: 'RU Bréguet'
        },
        'possédé': {
            'Cafet Bréguet': 2,
            'Interlocal': 0,
            'RU Eiffel': 1,
            'Local ViaRézo': 1,
            'Musée': 0,
            'Amphi Michelin': 1,
            'RU Bréguet': 0
        },
        'prix_achat': {
            'Cafet Bréguet': 200,
            'Interlocal': 250,
            'RU Eiffel': 300,
            'Local ViaRézo': 350,
            'Musée': 400,
            'Amphi Michelin': 450,
            'RU Bréguet': 500
        },
        'loyer': {
            'Cafet Bréguet': 5,
            'Interlocal': 10,
            'RU Eiffel': 15,
            'Local ViaRézo': 20,
            'Musée': 25,
            'Amphi Michelin': 30,
            'RU Bréguet': 35
        },
        'maison' : {
            'Cafet Bréguet':0,
            'Interlocal':0,
            'RU Eiffel':0,
            'Local ViaRézo':0,
            'Musée':0,
            'Amphi Michelin':0,
            'RU Bréguet':0
        },
        'prix maison':{
            'Cafet Bréguet': 50,
            'Interlocal': 50,
            'RU Eiffel': 50,
            'Local ViaRézo': 100,
            'Musée': 100,
            'Amphi Michelin': 100,
            'RU Bréguet': 150
        }
    }
    joueurs = {
        'nom': {},
        'argent': {
            '1': 1000,
            '2': 10
        },
        'position': {
            '1': 4,
            '2': 3
        },
        'prison': {
            '1': 0,
            '2': 0
        },
        'dernier lancer dés': {
            '1': 3,
            '2': 7
        }
    }
    loyer_ter(monopoly, joueurs, 3, 2)
    #2 n'a pas les moyens pour payer le loyer donc va devoir vendre sa seule propriété
    assert monopoly['possédé']['Cafet Bréguet']==0
    assert joueurs['argent']['2']==175
    assert joueurs['argent']['1']==1015
    monopoly = {
        'nom': {
            0: 'APL',
            1: 'Cafet Bréguet',
            2: 'Interlocal',
            3: 'RU Eiffel',
            4: 'Local ViaRézo',
            5: 'Musée',
            6: 'Amphi Michelin',
            7: 'RU Bréguet'
        },
        'possédé': {
            'Cafet Bréguet': 2,
            'Interlocal': 0,
            'RU Eiffel': 1,
            'Local ViaRézo': 1,
            'Musée': 0,
            'Amphi Michelin': 1,
            'RU Bréguet': 0
        },
        'prix_achat': {
            'Cafet Bréguet': 200,
            'Interlocal': 250,
            'RU Eiffel': 300,
            'Local ViaRézo': 350,
            'Musée': 400,
            'Amphi Michelin': 450,
            'RU Bréguet': 500
        },
        'loyer': {
            'Cafet Bréguet': 5,
            'Interlocal': 10,
            'RU Eiffel': 15,
            'Local ViaRézo': 20,
            'Musée': 25,
            'Amphi Michelin': 30,
            'RU Bréguet': 35
        },
        'maison' : {
            'Cafet Bréguet':1,
            'Interlocal':0,
            'RU Eiffel':0,
            'Local ViaRézo':0,
            'Musée':0,
            'Amphi Michelin':0,
            'RU Bréguet':0
        },
        'prix maison':{
            'Cafet Bréguet': 50,
            'Interlocal': 50,
            'RU Eiffel': 50,
            'Local ViaRézo': 100,
            'Musée': 100,
            'Amphi Michelin': 100,
            'RU Bréguet': 150
        }
    }
    joueurs = {
        'nom': {},
        'argent': {
            '1': 1000,
            '2': 10
        },
        'position': {
            '1': 4,
            '2': 3
        },
        'prison': {
            '1': 0,
            '2': 0
        },
        'dernier lancer dés': {
            '1': 3,
            '2': 7
        }
    }
    #2 vend sa maison pour pouvoir rembourser sa dette
    loyer_ter(monopoly, joueurs, 3, 2)
    assert monopoly['maison']['Cafet Bréguet']==0
    assert joueurs['argent']['2']==35
    assert joueurs['argent']['1']==1015
    monopoly = {
        'nom': {
            0: 'APL',
            1: 'Cafet Bréguet',
            2: 'Interlocal',
            3: 'RU Eiffel',
            4: 'Local ViaRézo',
            5: 'Musée',
            6: 'Amphi Michelin',
            7: 'RU Bréguet'
        },
        'possédé': {
            'Cafet Bréguet': 2,
            'Interlocal': 2,
            'RU Eiffel': 1,
            'Local ViaRézo': 1,
            'Musée': 0,
            'Amphi Michelin': 1,
            'RU Bréguet': 0
        },
        'prix_achat': {
            'Cafet Bréguet': 200,
            'Interlocal': 250,
            'RU Eiffel': 300,
            'Local ViaRézo': 350,
            'Musée': 400,
            'Amphi Michelin': 450,
            'RU Bréguet': 500
        },
        'loyer': {
            'Cafet Bréguet': 5,
            'Interlocal': 10,
            'RU Eiffel': 15,
            'Local ViaRézo': 20,
            'Musée': 25,
            'Amphi Michelin': 30,
            'RU Bréguet': 35
        },
        'maison' : {
            'Cafet Bréguet':1,
            'Interlocal':0,
            'RU Eiffel':0,
            'Local ViaRézo':0,
            'Musée':0,
            'Amphi Michelin':0,
            'RU Bréguet':0
        },
        'prix maison':{
            'Cafet Bréguet': 50,
            'Interlocal': 50,
            'RU Eiffel': 50,
            'Local ViaRézo': 100,
            'Musée': 100,
            'Amphi Michelin': 100,
            'RU Bréguet': 150
        }
    }
    joueurs = {
        'nom': {},
        'argent': {
            '1': 1000,
            '2': 10
        },
        'position': {
            '1': 4,
            '2': 3
        },
        'prison': {
            '1': 0,
            '2': 0
        },
        'dernier lancer dés': {
            '1': 3,
            '2': 7
        }
    }
    #2 vend Cafet Bréguet pour pouvoir rembourser sa dette
    loyer_ter(monopoly, joueurs, 3, 2)
    assert monopoly['maison']['Cafet Bréguet']==0
    assert monopoly['possédé']['Cafet Bréguet']==0
    assert joueurs['argent']['2']==215
    assert joueurs['argent']['1']==1015


test_loyer_bis()