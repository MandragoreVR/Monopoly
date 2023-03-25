## Fichier de test pour le script plateau_gestion_arrivee.py

from plateau_gestion_arrivee import *


def test_arrivee():
    joueurs = {
        'nom': {},
        'argent': {
            '1': 1000,
            '2': 1000
        },
        'position': {
            '1': 0,
            '2': 0
        },
        'prison': {
            '1': 0,
            '2': 0
        },
        'libere de prison':{
            '1': 0,
            '2': 0
        }
    }
    monopoly = {
        'nom': {
            0: 'APL',
            1: 'Ecsit',
            2: 'MyWay',
            3: 'Guilde',
            4: 'Loyer Césal',
            5: 'Cafet',
            6: 'PICS',
            7: 'MyWay',
            8: 'Hyris',
            9: 'ViaRezo',
            10: 'Visite',
            11: 'Commus',
            12: 'Accueil Assistance Réseau ViaRezo',
            13: 'Musics',
            14: 'BDA',
            15: 'RU Eiffel',
            16: 'NCV',
            17: 'MyWay',
            18: 'Raid',
            19: 'BDS',
            20: 'Clairière',
            21: 'SBCS',
            22: 'MyWay',
            23: 'ADR',
            24: 'BDE',
            25: 'RU Bréguet',
            26: 'Oser',
            27: 'CheerUp',
            28: 'Accueil Césal',
            29: 'Huma',
            30: 'TrouQuiPue',
            31: 'PAPS',
            32: 'FIR',
            33: 'MyWay',
            34: 'Impact',
            35: 'Musée',
            36: 'MyWay',
            37: 'JE',
            38: 'Tour des cotizs',
            39: 'LeForum'
        },
        'possédé': {
            'Ecsit': 0,
            'Guilde': 0,
            'Cafet': 0,
            'PICS': 0,
            'Hyris': 0,
            'ViaRezo': 0,
            'Commus': 0,
            'Accueil Assistance Réseau ViaRezo': 0,
            'Musics': 0,
            'BDA': 0,
            'RU Eiffel': 0,
            'NCV': 0,
            'Raid': 0,
            'BDS': 0,
            'SBCS': 0,
            'ADR': 0,
            'BDE': 0,
            'RU Bréguet': 0,
            'Oser': 0,
            'CheerUp': 0,
            'Accueil Césal': 0,
            'Huma': 0,
            'PAPS': 0,
            'FIR': 0,
            'Impact': 0,
            'Musée': 0,
            'JE': 0,
            'LeForum': 0
        },
        'prix_achat': {
            'Ecsit': 60,
            'Guilde': 60,
            'Cafet': 200,
            'PICS': 100,
            'Hyris': 100,
            'ViaRezo': 120,
            'Commus': 140,
            'Accueil Assistance Réseau ViaRezo': 150,
            'Musics': 140,
            'BDA': 160,
            'RU Eiffel': 200,
            'NCV': 180,
            'Raid': 180,
            'BDS': 200,
            'SBCS': 220,
            'ADR': 220,
            'BDE': 240,
            'RU Bréguet': 200,
            'Oser': 260,
            'CheerUp': 260,
            'Accueil Césal': 150,
            'Huma': 280,
            'PAPS': 300,
            'FIR': 300,
            'Impact': 320,
            'Musée': 200,
            'JE': 350,
            'LeForum': 500
        },
        'loyer': {
            'Ecsit': 2,
            'Guilde': 4,
            'PICS': 6,
            'Hyris': 6,
            'ViaRezo': 8,
            'Commus': 10,
            'Musics': 10,
            'BDA': 12,
            'NCV': 14,
            'Raid': 14,
            'BDS': 16,
            'SBCS': 18,
            'ADR': 18,
            'BDE': 20,
            'Oser': 22,
            'CheerUp': 22,
            'Huma': 24,
            'PAPS': 26,
            'FIR': 26,
            'Impact': 28,
            'JE': 35,
            'LeForum': 50
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
    liste_des_cartes_chance = [i for i in range(9)]
    joueurs['position']['1'] = 4  # Case Loyer Césal
    arrivee(1, joueurs, monopoly, cartes_chance, liste_des_cartes_chance)
    assert joueurs['argent']['1'] == 800
    joueurs['position']['2'] = 38  # Case Tour des cotizs'
    arrivee(2, joueurs, monopoly, cartes_chance, liste_des_cartes_chance)
    assert joueurs['argent']['2'] == 900
    joueurs['position']['1'] = 30  # Case Troukipu (allez en prison)
    arrivee(1, joueurs, monopoly, cartes_chance, liste_des_cartes_chance)
    # Premier aller en prison où l'on accepte de payer les 50€ directement
    assert joueurs['prison']['1'] == 0
    print(joueurs['argent']['1'])
    assert joueurs['argent']['1'] == 750
    assert joueurs['position']['1'] == 10
    joueurs['prison']['1'] = 0
    joueurs['position']['2'] = 30
    arrivee(2, joueurs, monopoly, cartes_chance, liste_des_cartes_chance)
    # Ensuite on refuse l'amende
    assert joueurs['prison']['2'] == 1
    assert joueurs['position']['2'] == 10
    joueurs['prison']['2'] = 0

    monopoly['possédé']['Guilde'] = 2
    joueurs['position']['1'] = 3
    arrivee(1, joueurs, monopoly, cartes_chance, liste_des_cartes_chance)
    assert joueurs['argent']['1'] == 750 - monopoly['loyer']['Guilde']
    monopoly['possédé']['Guilde'] = 0
    joueurs['position']['1'] = 3
    arrivee(1, joueurs, monopoly, cartes_chance, liste_des_cartes_chance)
    assert joueurs['argent']['1'] == 750 - monopoly['prix_achat']['Guilde']


test_arrivee()
