from loyer_bis import *

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
    loyer_bis(monopoly, joueurs, 3, 2)
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
    loyer_bis(monopoly, joueurs, 3, 2)
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
    loyer_bis(monopoly, joueurs, 3, 2)
    #2 n'a pas les moyens pour payer le loyer donc va devoir vendre sa seule propriété
    assert monopoly['possédé']['Cafet Bréguet']==0
    assert joueurs['argent']['2']==175
    assert joueurs['argent']['1']==1015

test_loyer_bis()