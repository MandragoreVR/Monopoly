monopoly={'nom':{0:'APL', 1:'Ecsit', 2:'MyWay', 3:'Guilde', 4:'Loyer Césal', 5:'Cafet', 6:'PICS', 7:'MyWay', 8:'Hyris', 9:'ViaRezo', 10:'Visite', 11:'Commus', 12:'Accueil Assistance Réseau ViaRezo', 13:'Musics', 14:'BDA', 15:'RU Eiffel', 16 : 'NCV', 17:'MyWay', 18:'Raid', 19:'BDS', 20:'Clairière', 21:'SBCS', 22:'MyWay', 23:'ADR', 24:'BDE', 25:'RU Bréguet', 26:'Oser', 27:'CheerUp', 28:'Accueil Césal', 29:'Huma', 30:'TrouQuiPue', 31:'PAPS', 32:'FIR', 33:'MyWay', 34:'Impact', 35:'Musée', 36:'MyWay', 37:'JE', 38:'Tour des cotizs', 39:'LeForum'},
'possédé':{'Ecsit':0, 'Guilde':0, 'Cafet':0, 'PICS':0, 'Hyris':0, 'ViaRezo':0, 'Commus':0, 'Accueil Assistance Réseau ViaRezo':0, 'Musics':0, 'BDA':0, 'RU Eiffel':0, 'NCV':0, 'Raid':0, 'BDS':0, 'SBCS':0, 'ADR':0, 'BDE':0, 'RU Bréguet':0, 'Oser':0, 'CheerUp':0, 'Accueil Césal':0, 'Huma':0, 'PAPS':0, 'FIR':0, 'Impact':0, 'Musée':0, 'JE':0, 'LeForum':0},
'prix_achat':{'Ecsit':60, 'Guilde':60, 'Cafet':200, 'PICS':100, 'Hyris':100, 'ViaRezo':120, 'Commus':140, 'Accueil Assistance Réseau ViaRezo':150, 'Musics':140, 'BDA':160, 'RU Eiffel':200, 'NCV':180, 'Raid':180, 'BDS':200, 'SBCS':220, 'ADR':220, 'BDE':240, 'RU Bréguet':200, 'Oser':260, 'CheerUp':260, 'Accueil Césal':150, 'Huma':280, 'PAPS':300, 'FIR':300, 'Impact':320, 'Musée':200, 'JE':350, 'LeForum':500},
'loyer':{'Ecsit':2, 'Guilde':4, 'PICS':6, 'Hyris':6, 'ViaRezo':8, 'Commus':10, 'Musics':10, 'BDA':12, 'NCV':14, 'Raid':14, 'BDS':16, 'SBCS':18, 'ADR':18, 'BDE':20, 'Oser':22, 'CheerUp':22, 'Huma':24, 'PAPS':26, 'FIR':26, 'Impact':28, 'JE':35, 'LeForum':50},
'maison':{'Ecsit':0, 'Guilde':0, 'PICS':0, 'Hyris':0, 'ViaRezo':0, 'Commus':0, 'Musics':0, 'BDA':0, 'NCV':0, 'Raid':0, 'BDS':0, 'SBCS':0, 'ADR':0, 'BDE':0, 'Oser':0, 'CheerUp':0, 'Huma':0, 'PAPS':0, 'FIR':0, 'Impact':0, 'JE':0, 'LeForum':0}}
#Les cases ayant des loyers spéciaux (c'est à dire les gares et les compagnies) ne sont pas dans loyer car une fonction s'occupera de les calculer.


joueurs={'nom':{}, 'argent':{'1': 1000, '2': 1000}, 'position':{'1':0, '2':0}, 'prison':{'1': 0, '2':0},'libere de prison':{'1':1,'2':0},
 'nombre de double':{'1':0,'2':0}}

# pour la valeur de prison : 0 :pas en prison
#                              1 premier tour en prison
#                              2 deuxieme tour en prison
#                              3 troisième tour en prison


# libere de prison : nombre de carte 'vous etes libéré de prison' du joueur


cartes_chance = {
    1 : "Allez à la case APL.",
    2 : "Allez au local ViaRézo.",
    3 : "Payez 200€ ou piochez une autre carte chance.",
    4 : "Reculez de trois cases.",
    5 : "Allez en prison, sans passer par la case APL.",
    6 : "Césal a prélevé trop d'argent sur votre dernier loyer, vous touchez 200€.",
    7 : "Vous êtes libérés de prison ! Cette carte peut être conservée.",
    8 : "Vous avez mis le feu à votre appartement, payez 200€ de réparations."
}

liste_des_cartes_chance = [i for i in range(1,9)]


import plateau_gestion_arrivee as cga       
import random as rd                         # Pour faire les lancers de dés


def lancer_de(ind_joueur,monopoly,joueurs, cartes_chance, liste_cartes_chance):                       #joueur est l'entier correspondant au numéro du joueur
    de_1=rd.randint(1,6)                                                               # on lance le premier dé de 6
    de_2=rd.randint(1,6)                                                               # on lance le deuxième dé de 6  
    print("Vous avez lancé", de_1,"et",de_2) 
    rejouer=0                                                                          # compteur pour savoir si le joueur doit rejouer
    if de_1==de_2:                                                      # Cas où on a un double
        joueurs['nombre de double'][str(ind_joueur)]+=1                 # Compteur du nombre de double 
        if joueurs['nombre de double'][str(ind_joueur)]==3:             # Pour gérer le cas où 3 doubles d'affilé
            print("Vous avez fait 3 doubles consécutifs. Vous allez en prison :( !")
            joueurs['nombre de double'][str(ind_joueur)]=0
            prison(ind_joueur, monopoly, joueurs, cartes_chance, liste_cartes_chance)           #Envoie en prison
               #pas de déplacement dû au troisième lancer
        else :   
            print("Vous avez fait un double. Vous pourrez rejouer.")
            rejouer=1

    nb_de_cases=de_1+de_2                                               # Fait avancer le joueur
    print('Le joueur ',ind_joueur,'avance de ', nb_de_cases,'cases.')
    placement=joueurs['position'][str(ind_joueur)]
    placement+=nb_de_cases

    if placement>39:             
        placement=placement-40                # Pour repartir sur le bon numéro de case si le joueur a terminé un tour
        print("Vous touchez 200 euros d'APL :) ")           # Passage par la case départ
        joueurs['argent'][str(ind_joueur)]+=200
        print ("Vous avez actuellement",joueurs['argent'][str(ind_joueur)],"euros.")


    joueurs['position'][str(ind_joueur)]=placement
    print('Le joueur ',ind_joueur,'est sur la case',monopoly['nom'][placement],'.' )            # Affiche le placement du joueur 
    
    return [de_1+de_2, rejouer]





def prison(ind_joueur,monopoly,joueurs, cartes_chance, liste_des_cartes_chance):

    joueurs['prison'][str(ind_joueur)]+=1                               # Indicateur qui compte le nombre de tours en prison
    if joueurs['prison'][str(ind_joueur)] == 3:                         # Trop de tours en prison
        print("Cela fait 3 tours que vous êtes en prison, vous êtes libéré après avoir payé votre caution.")
        joueurs['argent'][str(ind_joueur)]=-50                          # On peut utiliser payer dans le programme final de fonctionnement
        joueurs['prison'][str(ind_joueur)] = 0
        return 1                                                        # 1 signifie qu'il a le droit de jouer, 0 signifie qu'il n'a pas la droit de jouer
    if joueurs['prison'][str(ind_joueur)] == 1:
        joueurs['position'][str(ind_joueur)]=10 
        print("Vous êtes arrivés en prison !")    
    nbr_carte_libere = joueurs['libere de prison'][str(ind_joueur)]

    ##carte sortir de prison
    if nbr_carte_libere == 0:
        print("Vous n'avez pas de cartes pour vous libérer de prison.")
    else:
        print("Vous avez",nbr_carte_libere,"carte(s) 'Vous êtes libéré de prison'")
        utilise = input("Voulez-vous utiliser une carte ? (1 si oui, 2 si non) ")           # Demande s'il veut utilisé une carte chance
        if utilise == '1':
            print("Vous avez utilisé une carte.")
            print("Vous êtes libéré de prison !")
            joueurs['prison'][str(ind_joueur)] = 0            # libéré : joue normalement   
            joueurs['libere de prison'][str(ind_joueur)] -= 1
            return 1
        else :
            print("Vous n'avez pas utilisé de carte.")


    ## payer pour sortir
    res=input("Voulez-vous payez 50 euros pour sortir de prison ? 1 si oui, 2 si non \n")
    if res=='1':
        joueurs['argent'][str(ind_joueur)]=-50              # On peut utiliser payer dans le programme final de fonctionnement
        print("Vous avez payé 50 euros pour sortir.")
        print("Vous êtes libéré de prison !")
        joueurs['prison'][str(ind_joueur)]=0                # libéré : joue normalement
        return 1


    ## lancer les dés pour essayer de faire un double    
    else :
        print("Vous n'avez pas payé.")
        _ = input("Vous allez lancer deux dés pour tenter de faire un double (appuyez sur entrée pour continuer)")
        de_1=rd.randint(1,6)              # on lance le premier dé de 6
        de_2=rd.randint(1,6)              # on lance le deucième dé de 6
        if de_1==de_2:              ## double effectué
            print("Vous avez fait ", de_1, " et ", de_2)
            print("Vous avez fait un double, vous pouvez sortir de prison.")
            joueurs['prison'][str(ind_joueur)]=0            # libéré de prison

            nb_de_cases=de_1+de_2                                   #Faire avancer le joueur car double effectué
            joueurs['nombre de double'][str(ind_joueur)]+=1
            joueurs['dernier lancer dés']=nb_de_cases
            print('Le joueur ',ind_joueur,'avance de ', nb_de_cases,'cases.')
            joueurs['position'][str(ind_joueur)] += nb_de_cases
            placement=joueurs['position'][str(ind_joueur)]
            print('Le joueur ',ind_joueur,'est sur la case',monopoly['nom'][placement],'.' )      
            cga.arrivee(ind_joueur, joueurs, monopoly, cartes_chance, liste_des_cartes_chance)              #gère l'arrivée sur la case
        else:                                ## Pas de double : reste en prison        
            print("Vous avez fait",de_1, "et", de_2,". Vous n'avez pas fait de double. Vous restez en prison.")
            print("Cela fait",joueurs['prison'][str(ind_joueur)],"tour(s) que vous êtes en prison.")            
            return 0                        # 1 signifie qu'il a le droit de jouer, 0 signifie qu'il n'a pas la droit de jouer




if __name__ == "__main__":                                  # Exécute la fonction quand on run le fichier
    prison(2, monopoly, joueurs, cartes_chance, liste_des_cartes_chance)

