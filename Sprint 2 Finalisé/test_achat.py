from fonction_maison import *
from io import StringIO
import sys

def mock_return_function(_):
    return 'oui'

def test_maison(monkeypatch):
    monopoly={'nom':{0:'APL', 1:'Ecsit', 2:'MyWay', 3:'Guilde', 4:'Loyer Césal', 5:'Cafet', 6:'PICS', 7:'MyWay', 8:'Hyris', 9:'ViaRezo', 10:'Visite', 11:'Commus', 12:'Accueil Assistance Réseau ViaRezo', 13:'Musics', 14:'BDA', 15:'RU Eiffel', 16 : 'NCV', 17:'MyWay', 18:'Raid', 19:'BDS', 20:'Clairière', 21:'SBCS', 22:'MyWay', 23:'ADR', 24:'BDE', 25:'RU Bréguet', 26:'Oser', 27:'CheerUp', 28:'Accueil Césal', 29:'Huma', 30:'TrouQuiPue', 31:'PAPS', 32:'FIR', 33:'MyWay', 34:'Impact', 35:'Musée', 36:'MyWay', 37:'JE', 38:'Tour des cotizs', 39:'LeForum'},
    'possédé':{'Ecsit':1, 'Guilde':1, 'Cafet':0, 'PICS':1, 'Hyris':0, 'ViaRezo':0, 'Commus':1, 'Accueil Assistance Réseau ViaRezo':0, 'Musics':0, 'BDA':0, 'RU Eiffel':0, 'NCV':0, 'Raid':0, 'BDS':0, 'SBCS':0, 'ADR':0, 'BDE':0, 'RU Bréguet':0, 'Oser':0, 'CheerUp':0, 'Accueil Césal':0, 'Huma':0, 'PAPS':0, 'FIR':0, 'Impact':0, 'Musée':0, 'JE':0, 'LeForum':0},
    'prix_achat':{'Ecsit':60, 'Guilde':60, 'Cafet':200, 'PICS':100, 'Hyris':100, 'ViaRezo':120, 'Commus':140, 'Accueil Assistance Réseau ViaRezo':150, 'Musics':140, 'BDA':160, 'RU Eiffel':200, 'NCV':180, 'Raid':180, 'BDS':200, 'SBCS':220, 'ADR':220, 'BDE':240, 'RU Bréguet':200, 'Oser':260, 'CheerUp':260, 'Accueil Césal':150, 'Huma':280, 'PAPS':300, 'FIR':300, 'Impact':320, 'Musée':200, 'JE':350, 'LeForum':500},
    'loyer':{'Ecsit':2, 'Guilde':4, 'PICS':6, 'Hyris':6, 'ViaRezo':8, 'Commus':10, 'Musics':10, 'BDA':12, 'NCV':14, 'Raid':14, 'BDS':16, 'SBCS':18, 'ADR':18, 'BDE':20, 'Oser':22, 'CheerUp':22, 'Huma':24, 'PAPS':26, 'FIR':26, 'Impact':28, 'JE':35, 'LeForum':50},
    'maison':{'Ecsit':0, 'Guilde':0, 'PICS':0, 'Hyris':0, 'ViaRezo':0, 'Commus':0, 'Musics':0, 'BDA':0, 'NCV':0, 'Raid':0, 'BDS':0, 'SBCS':0, 'ADR':0, 'BDE':0, 'Oser':0, 'CheerUp':0, 'Huma':0, 'PAPS':0, 'FIR':0, 'Impact':0, 'JE':0, 'LeForum':0},
    'prix maison':{'Ecsit':50, 'Guilde':50, 'PICS':50, 'Hyris':50, 'ViaRezo':50, 'Commus':100, 'Musics':100, 'BDA':100, 'NCV':100, 'Raid':100, 'BDS':100, 'SBCS':150, 'ADR':150, 'BDE':150, 'Oser':150, 'CheerUp':150, 'Huma':150, 'PAPS':200, 'FIR':200, 'Impact':200, 'JE':200, 'LeForum':200}}

    joueurs={'nom':{'Hugo' : 1 , 'Eglantine' : 2}, 'argent':{'1': 1000, '2': 1000}, 'position':{'1':0, '2':0}}
    
    monkeypatch.setattr('builtins.input', mock_return_function)
    achat_maison(1,joueurs,monopoly)

    assert monopoly['maison']['Ecsit'] == 1
    assert monopoly['maison']['Guilde'] == 1
    assert monopoly['maison']['PICS'] == 0
    assert monopoly['maison']['Commus'] == 0
    assert joueurs['argent']['1'] == 900



