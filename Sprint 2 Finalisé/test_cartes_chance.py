## Fichier de tests du script cartes_chance.py

from cartes_chance import melanger_cartes_chance, piocher_carte_chance


def test_melanger_cartes_chance():
    cartes_chance = {
        1: "Allez à la case APL.",
        2: "Allez au local ViaRézo.",
        3: "Payez 200€ ou piochez une autre carte chance.",
        4: "Reculez de trois cases.",
        5: "Allez en prison, sans passer par la case APL.",
        6:
        "Césal a prélevé trop d'argent sur votre dernier loyer, vous touchez 200€.",
        7: "Vous êtes libérés de prison ! Cette carte peut être conservée.",
        8:
        "Vous avez mis le feu à votre appartement, payez 200€ de réparations."
    }
    L = melanger_cartes_chance(cartes_chance)
    L.sort()
    assert L == [i for i in range(1, 9)]


def test_piocher_carte_chance():
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
            'RU Eiffel': 0,
            'Local ViaRézo': 0,
            'Musée': 0,
            'Amphi Michelin': 0,
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
        'libere de prison': {
            '1': 0,
            '2': 0
        }
    }
    cartes_chance = {
        1: "Allez à la case APL.",
        2: "Allez au local ViaRézo.",
        3: "Payez 200€ ou piochez une autre carte chance.",
        4: "Reculez de trois cases.",
        5: "Allez en prison, sans passer par la case APL.",
        6:
        "Césal a prélevé trop d'argent sur votre dernier loyer, vous touchez 200€.",
        7: "Vous êtes libérés de prison ! Cette carte peut être conservée.",
        8:
        "Vous avez mis le feu à votre appartement, payez 200€ de réparations."
    }
    L = [i for i in range(1, 9)]
    piocher_carte_chance(monopoly, joueurs, 1, L, cartes_chance)
    assert joueurs['position']['1'] == 0
    assert joueurs['argent']['1'] == 1400
    assert L == [i for i in range(2, 9)] + [1]
    piocher_carte_chance(monopoly, joueurs, 2, L, cartes_chance)
    assert L == [i for i in range(3, 9)] + [1, 2]
    assert joueurs['position']['2'] == 6
    piocher_carte_chance(monopoly, joueurs, 1, L, cartes_chance)
    # L'utilisateur rentre 0 au premier input et 1 au second
    assert L == [i for i in range(4, 9)] + [1, 2, 3]
    assert joueurs['argent']['1'] == 1200
    L = [i for i in range(3, 9)] + [1, 2]
    piocher_carte_chance(monopoly, joueurs, 2, L, cartes_chance)
    # On répond 1 à l'input, ça va lancer la pioche de la prochaine carte pour le joueur 2
    assert L == [5, 6, 7, 8, 1, 2, 3, 4]
    assert joueurs['position']['2'] == 3
    piocher_carte_chance(monopoly, joueurs, 1, L, cartes_chance)
    assert L == [6, 7, 8, 1, 2, 3, 4, 5]
    piocher_carte_chance(monopoly, joueurs, 2, L, cartes_chance)
    assert L == [7, 8] + [i for i in range(1, 7)]
    assert joueurs['argent']['2'] == 1200
    piocher_carte_chance(monopoly, joueurs, 1, L, cartes_chance)
    assert L == [8] + [i for i in range(1, 8)]
    piocher_carte_chance(monopoly, joueurs, 2, L, cartes_chance)
    assert L == [i for i in range(1, 9)]
    assert joueurs['argent']['2'] == 1000


test_melanger_cartes_chance()
test_piocher_carte_chance()
