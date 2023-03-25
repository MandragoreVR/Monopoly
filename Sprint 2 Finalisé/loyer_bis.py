from revente import listes_proprietes, revendre

monopoly={'nom':{0:'APL', 1:'Ecsit', 2:'MyWay', 3:'Guilde', 4:'Loyer Césal', 5:'Cafet', 6:'PICS', 7:'MyWay', 8:'Hyris', 9:'ViaRezo', 10:'Visite', 11:'Commus', 12:'Accueil Assistance Réseau ViaRezo', 13:'Musics', 14:'BDA', 15:'RU Eiffel', 16 : 'NCV', 17:'MyWay', 18:'Raid', 19:'BDS', 20:'Clairière', 21:'SBCS', 22:'MyWay', 23:'ADR', 24:'BDE', 25:'RU Bréguet', 26:'Oser', 27:'CheerUp', 28:'Accueil Césal', 29:'Huma', 30:'TrouQuiPue', 31:'PAPS', 32:'FIR', 33:'MyWay', 34:'Impact', 35:'Musée', 36:'MyWay', 37:'JE', 38:'Tour des cotizs', 39:'LeForum'},
'possédé':{'Ecsit':0, 'Guilde':0, 'Cafet':0, 'PICS':0, 'Hyris':0, 'ViaRezo':0, 'Commus':0, 'Accueil Assistance Réseau ViaRezo':0, 'Musics':0, 'BDA':0, 'RU Eiffel':0, 'NCV':0, 'Raid':0, 'BDS':0, 'SBCS':0, 'ADR':0, 'BDE':0, 'RU Bréguet':0, 'Oser':0, 'CheerUp':0, 'Accueil Césal':0, 'Huma':0, 'PAPS':0, 'FIR':0, 'Impact':0, 'Musée':0, 'JE':0, 'LeForum':0},
'prix_achat':{'Ecsit':60, 'Guilde':60, 'Cafet':200, 'PICS':100, 'Hyris':100, 'ViaRezo':120, 'Commus':140, 'Accueil Assistance Réseau ViaRezo':150, 'Musics':140, 'BDA':160, 'RU Eiffel':200, 'NCV':180, 'Raid':180, 'BDS':200, 'SBCS':220, 'ADR':220, 'BDE':240, 'RU Bréguet':200, 'Oser':260, 'CheerUp':260, 'Accueil Césal':150, 'Huma':280, 'PAPS':300, 'FIR':300, 'Impact':320, 'Musée':200, 'JE':350, 'LeForum':500},
'loyer':{'Ecsit':2, 'Guilde':4, 'PICS':6, 'Hyris':6, 'ViaRezo':8, 'Commus':10, 'Musics':10, 'BDA':12, 'NCV':14, 'Raid':14, 'BDS':16, 'SBCS':18, 'ADR':18, 'BDE':20, 'Oser':22, 'CheerUp':22, 'Huma':24, 'PAPS':26, 'FIR':26, 'Impact':28, 'JE':35, 'LeForum':50}
}
#Les cases ayant des loyers spéciaux (c'est à dire les gares et les compagnies) ne sont pas dans loyer car une fonction s'occupera de les calculer.


def loyer_bis(monopoly, joueurs, indice_prop, indice_joueur):
    # La fonction débite le joueur indice_joueur du loyer de la propriété indice_prop, et crédite 
    # le propriétaire de cette propriété (si la propriété est possédée par quelqu'un d'autre que le joueur indice_joueur)
    nom_de_la_propriete = monopoly['nom'][indice_prop]
    indice_proprietaire = str(monopoly['possédé'][nom_de_la_propriete])
    if int(indice_proprietaire) not in [0, indice_joueur]: # C'est la condition entre parenthèses 
        if nom_de_la_propriete in monopoly['loyer']: #On modifie le prix du loyer en fonction du nombre de maison sur le local.
            loyer=monopoly['loyer'][nom_de_la_propriete]
        elif indice_prop in [5,15,25,35]: # On calcule le loyer pour le restaurant.
            loyer=loyer_RU(monopoly, int(indice_proprietaire))
        else : #On calcule le loyer pour les accueils.
            loyer=loyer_accueil(monopoly, joueurs, int(indice_proprietaire), indice_joueur)
        if joueurs['argent'][str(indice_joueur)] >= loyer:
            # On débite celui qui paye le loyer
            joueurs['argent'][str(indice_joueur)] -= loyer
            # Et on crédite le propriétaire
            joueurs['argent'][indice_proprietaire] += loyer
        else:
        # Si le joueur ne peut pas payer
            # Le propriétaire récupère tout l'argent que le joueur possède et l'argent issu de la vente de ses propriétés
            dette=loyer - joueurs['argent'][str(indice_joueur)]
            joueurs['argent'][str(indice_joueur)], joueurs['argent'][indice_proprietaire]=0, joueurs['argent'][indice_proprietaire]+joueurs['argent'][str(indice_joueur)]
            revendre(dette, indice_joueur, monopoly['possédé'][nom_de_la_propriete], monopoly, joueurs)

def loyer_RU(monopoly, indice_proprietaire):
    count=0
    for i in range (5, 36, 10): #Les numéros des restaurants(gares)
        N=monopoly['nom'][i] #le nom de la propriété
        if monopoly['possédé'][N]==indice_proprietaire:
            count+=1
    if count ==1:  #Le loyer des restaurants dépend du nombre de restaurant que le joueur possède.
        return(25)
    if count ==2:
        return(50)
    if count ==3:
        return(100)
    if count ==4:
        return(200)

def loyer_accueil(monopoly, joueurs, indice_proprietaire, indice_joueur):
    count=0
    if monopoly['possédé'][monopoly['nom'][12]]==indice_proprietaire : #12 et 28 sont les numéros des accueils (compagnies).
        count+=1
    if monopoly['possédé'][monopoly['nom'][28]]==indice_proprietaire :
        count+=1 
    if count==1:
        return (int(4*joueurs['dernier lancer dés'][str(indice_joueur)])) #Pour une carte accueil, le loyer est de 4 fois le résultat des dés.
    if count==2:
        return (int(10*joueurs['dernier lancer dés'][str(indice_joueur)])) #Pour 2 accueils, c'est fois 10.


