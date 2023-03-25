from joueurs_en_vie import *



def test_joueurs_en_vie():
    
    joueurs={'nom':{}, 'argent':{'1': 1000, '2': -10,'3': 200,'4': 0}, 'position':{'1':0, '2':0,'3':0,'4':0}, 'prison':{'1': False, '2':False,'3': False, '4':False}}

    res=joueurs_en_vie(4, joueurs)
    assert res==[1,3,4]
