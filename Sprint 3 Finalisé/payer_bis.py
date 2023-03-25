monopoly={'nom':{0:'APL', 1:'Ecsit', 2:'MyWay', 3:'Guilde', 4:'Loyer Césal', 5:'Cafet', 6:'PICS', 7:'MyWay', 8:'Hyris', 9:'ViaRezo', 10:'Visite', 11:'Commus', 12:'Accueil Assistance Réseau ViaRezo', 13:'Musics', 14:'BDA', 15:'RU Eiffel', 16 : 'NCV', 17:'MyWay', 18:'Raid', 19:'BDS', 20:'Clairière', 21:'SBCS', 22:'MyWay', 23:'ADR', 24:'BDE', 25:'RU Bréguet', 26:'Oser', 27:'CheerUp', 28:'Accueil Césal', 29:'Huma', 30:'TrouQuiPue', 31:'PAPS', 32:'FIR', 33:'MyWay', 34:'Impact', 35:'Musée', 36:'MyWay', 37:'JE', 38:'Tour des cotizs', 39:'LeForum'},
'possédé':{'Ecsit':0, 'Guilde':0, 'Cafet':0, 'PICS':0, 'Hyris':0, 'ViaRezo':0, 'Commus':0, 'Accueil Assistance Réseau ViaRezo':0, 'Musics':0, 'BDA':0, 'RU Eiffel':0, 'NCV':0, 'Raid':0, 'BDS':0, 'SBCS':0, 'ADR':0, 'BDE':0, 'RU Bréguet':0, 'Oser':0, 'CheerUp':0, 'Accueil Césal':0, 'Huma':0, 'PAPS':0, 'FIR':0, 'Impact':0, 'Musée':0, 'JE':0, 'LeForum':0},
'prix_achat':{'Ecsit':60, 'Guilde':60, 'Cafet':200, 'PICS':100, 'Hyris':100, 'ViaRezo':120, 'Commus':140, 'Accueil Assistance Réseau ViaRezo':150, 'Musics':140, 'BDA':160, 'RU Eiffel':200, 'NCV':180, 'Raid':180, 'BDS':200, 'SBCS':220, 'ADR':220, 'BDE':240, 'RU Bréguet':200, 'Oser':260, 'CheerUp':260, 'Accueil Césal':150, 'Huma':280, 'PAPS':300, 'FIR':300, 'Impact':320, 'Musée':200, 'JE':350, 'LeForum':500},
'loyer':{'Ecsit':2, 'Guilde':4, 'PICS':6, 'Hyris':6, 'ViaRezo':8, 'Commus':10, 'Musics':10, 'BDA':12, 'NCV':14, 'Raid':14, 'BDS':16, 'SBCS':18, 'ADR':18, 'BDE':20, 'Oser':22, 'CheerUp':22, 'Huma':24, 'PAPS':26, 'FIR':26, 'Impact':28, 'JE':35, 'LeForum':50},
'maison':{'Ecsit':0, 'Guilde':0, 'PICS':0, 'Hyris':0, 'ViaRezo':0, 'Commus':0, 'Musics':0, 'BDA':0, 'NCV':0, 'Raid':0, 'BDS':0, 'SBCS':0, 'ADR':0, 'BDE':0, 'Oser':0, 'CheerUp':0, 'Huma':0, 'PAPS':0, 'FIR':0, 'Impact':0, 'JE':0, 'LeForum':0},
'prix maison':{'Ecsit':50, 'Guilde':50, 'PICS':50, 'Hyris':50, 'ViaRezo':50, 'Commus':100, 'Musics':100, 'BDA':100, 'NCV':100, 'Raid':100, 'BDS':100, 'SBCS':150, 'ADR':150, 'BDE':150, 'Oser':150, 'CheerUp':150, 'Huma':150, 'PAPS':200, 'FIR':200, 'Impact':200, 'JE':200, 'LeForum':200}}


def listes_proprietes(numero_joueur, monopoly, joueurs):
    L=[]
    for l in monopoly['possédé']:
        if monopoly['possédé'][l]==numero_joueur :
            L.append(l)
    return (L) # renvoie la liste des propriétés du joueur 

def payer(montant, numero_joueur, monopoly, joueurs):
    if joueurs['argent'][str(numero_joueur)]>= montant:
        joueurs['argent'][str(numero_joueur)]-=montant
    else :
        dette=montant-joueurs['argent'][str(numero_joueur)]
        joueurs['argent'][str(numero_joueur)]=0
        print("Vous devez vendre des propriétés pour régler votre dette.")
        somme_pro=0
        somme_amé=0
        print("Voici les propriété que vous possédez et leurs prix :")
        L=listes_proprietes(numero_joueur, monopoly, joueurs)
        for l in L:
            somme_pro+=monopoly['prix_achat'][l]*0.9 #Les propriétés peuvent se vendre pour 90% de leur valeur d'achat.
            somme_amé += monopoly['maison'][l]*(monopoly['prix maison'][l]*0.8) #Les améliorations peuvent se vendre pour 80 % de leur valeur d'achat.
        somme=int(somme_amé+somme_pro) #Cela représente tout le capital du joueur.
        if somme >= dette :                                                     
            print("Vous pouvez rembourser votre dette.")                                                             #si le joueur a un capital supérieur à sa dette, il peut revendre ses améliorations et/ou propriétés jusqu'à ce qu'il n'ait plus de dette
            restant=dette
            while restant > 0:
                print("Il reste " + str(restant) + " à rembourser.")
                for l in L:
                    print(l + " peut se vendre à " + str(int(monopoly['prix_achat'][l]*0.9)) + ".")
                    if monopoly['maison'][l]!=0 :
                        print(l + " posséde " + str(monopoly['maison'][l]) + " maisons qui peuvent se vendre chacune à " + str(int(monopoly['prix maison'][l]*0.8)) + ".")
                txt  = input("Voulez vous revendre des améliorations ou vos propriétés ? dites améliorations ou propriétés : ")
                if txt == 'améliorations':
                    choix = input("Entrez le nom du bien où vous souhaitez revendre les améliorations.")
                    nombre= input("Entrez le nombre d'améliorations que vous souhaitez vendre.")
                    nombre=int(nombre)      
                    if choix in L and monopoly['maison'][choix] != 0 and nombre in range(0, monopoly['maison'][choix]+1):
                        restant-=int(monopoly['prix maison'][choix]*0.8*nombre)
                        monopoly['maison'][choix]-=nombre                                                                        #les améliorations que le joueur revend, disparaissent et l'argent réduit la dette
                
                elif txt == 'propriétés' :
                    choix = input("Entrez le nom du bien que vous souhaitez vendre.")      
                    if choix in L :
                        if monopoly['maison'][choix]!=0:
                            print("Vous vendez également les maisons qui lui sont associées.")
                            restant-=int(monopoly['maison'][choix]*monopoly['prix maison'][choix]*0.8)
                            monopoly['maison'][choix]=0
                        restant-=int(monopoly['prix_achat'][choix]*0.9)
                        monopoly['possédé'][choix]=0
                        L.remove(choix)                                                                                    #les propriétés que le joueur revend, retournent à la banque et peuvent être rachetées et les maisons dessus sont vendues. l'argent réduit la dette
            joueurs['argent'][str(numero_joueur)]+=(-1)*restant
            print("Votre dette est remboursée, l'argent restant de la vente est ajouté à votre compte.")
        else :
            print("Il vous est impossible de rembourser votre dette.")                                               #si le joueur n'avait pas un capital suffisant, toutes ses possessions sont revendues et il finit dans le négatif
            for l in L :
                monopoly['possédé'][l]=0
                monopoly['maison'][l]=0
            joueurs['argent'][str(numero_joueur)]=somme-dette # une valeur négative d'argent implique une défaite


