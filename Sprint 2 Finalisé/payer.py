monopoly={'nom':{0:'APL', 1:'Ecsit', 2:'mail BDE', 3:'Guilde', 4:'Loyer Césal', 5:'Cafet', 6:'PICS', 7:'MyWay', 8:'Hyris', 9:'ViaRezo', 10:'Visite', 11:'Commus', 12:'Accueil Assistance Réseau ViaRezo', 13:'Musics', 14:'BDA', 15:'RU Eiffel', 16 : 'NCV', 17:'mail BDE', 18:'Raid', 19:'BDS', 20:'Clairière', 21:'SBCS', 22:'MyWay', 23:'ADR', 24:'BDE', 25:'RU Bréguet', 26:'Oser', 27:'CheerUp', 28:'Accueil Césal', 29:'Huma', 30:'TrouQuiPue', 31:'PAPS', 32:'FIR', 33:'mail BDE', 34:'Impact', 35:'Musée', 36:'MyWay', 37:'JE', 38:'Tour des cotizs', 39:'LeForum'},
'possédé':{'Ecsit':0, 'Guilde':0, 'Cafet':0, 'PICS':0, 'Hyris':0, 'ViaRezo':0, 'Commus':2, 'Accueil Assistance Réseau ViaRezo':0, 'Musics':0, 'BDA':0, 'RU Eiffel':0, 'NCV':0, 'Raid':0, 'BDS':0, 'SBCS':0, 'ADR':0, 'BDE':0, 'RU Bréguet':0, 'Oser':0, 'CheerUp':0, 'Accueil Césal':0, 'Huma':0, 'PAPS':0, 'FIR':0, 'Impact':0, 'Musée':0, 'JE':0, 'LeForum':0},
'prix_achat':{'Ecsit':60, 'Guilde':60, 'Cafet':200, 'PICS':100, 'Hyris':100, 'ViaRezo':120, 'Commus':140, 'Accueil Assistance Réseau ViaRezo':150, 'Musics':140, 'BDA':160, 'RU Eiffel':200, 'NCV':180, 'Raid':180, 'BDS':200, 'SBCS':220, 'ADR':220, 'BDE':240, 'RU Bréguet':200, 'Oser':260, 'CheerUp':260, 'Accueil Césal':150, 'Huma':280, 'PAPS':300, 'FIR':300, 'Impact':320, 'Musée':200, 'JE':350, 'LeForum':400},
'loyer':{'Ecsit':2, 'Guilde':4, 'PICS':6, 'Hyris':6, 'ViaRezo':8, 'Commus':10, 'Musics':10, 'BDA':12, 'NCV':14, 'Raid':14, 'BDS':16, 'SBCS':18, 'ADR':18, 'BDE':20, 'Oser':22, 'CheerUp':22, 'Huma':24, 'PAPS':26, 'FIR':26, 'Impact':28, 'JE':35, 'LeForum':50}}


def listes_proprietes(numero_joueur, monopoly, joueurs):
    L=[]
    for l in monopoly['possédé']:
        if monopoly['possédé'][l]==numero_joueur :
            L.append(l)
    return (L)

def payer(montant, numero_joueur, monopoly, joueurs):
    if joueurs['argent'][str(numero_joueur)]>= montant:
        joueurs['argent'][str(numero_joueur)]-=montant
    else :
        dette=montant-joueurs['argent'][str(numero_joueur)]
        joueurs['argent'][str(numero_joueur)]=0
        print("Vous devez vendre des propriétés pour régler votre dette.")
        somme=0
        print("Voici les propriété que vous possédez et leurs prix :")
        L=listes_proprietes(numero_joueur, monopoly, joueurs)
        for l in L: #On informe le joueurs de ce qu'il peut vendre.
            print(l + " peut se vendre à " + str(int(monopoly['prix_achat'][l]*0.9)) + ".")
            somme+=monopoly['prix_achat'][l]
        if somme >= dette : #La somme des valeurs de toutes ses propriétés est supérieur à ça dette, il peut donc la rembourser.
            print("Vous pouvez rembourser votre dette.")
            restant=dette
            while restant > 0 : # Il faut vendre jusqu'à ce qu'on puisse rembourser.
                print("Il reste " + str(restant) + " à rembourser.")
                choix = input("Entrez le nom du bien que vous souhaitez vendre.")
                if choix in L :
                    restant-=int(monopoly['prix_achat'][choix]*0.9)
                    monopoly['possédé'][choix]=0
                    L.remove(choix)
            joueurs['argent'][str(numero_joueur)]+=(-1)*restant
            print("Votre dette est remboursée, l'argent restant de la vente est ajouté à votre compte.")
        else :
            print("Il vous est impossible de rembourser votre dette.")
            for l in L :
                monopoly['possédé'][l]=0
            joueurs['argent'][str(numero_joueur)]=somme-dette # une valeur négative d'argent implique une défaite

