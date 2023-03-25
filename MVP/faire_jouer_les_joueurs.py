def joueurs_en_vie(nb_joueurs, joueurs):
    Liste_indice_joueurs_en_vie=[]
    for i in range(int(nb_joueurs)):
        if joueurs['argent'][str(i+1)]>=0:
            Liste_indice_joueurs_en_vie.append(i+1)
    return Liste_indice_joueurs_en_vie

def play_monopoly():
    monopoly={'nom':{0:'APL',1:'Cafet Bréguet', 2: 'Interlocal', 3:'RU Eiffel', 4:'Local ViaRézo', 5:'Musée',6:'Amphi Michelin',7:'RU Bréguet'},
 'possédé':{'Cafet Bréguet':0, 'Interlocal':0, 'RU Eiffel':0, 'Local ViaRézo':0, 'Musée':0, 'Amphi Michelin':0, 'RU Bréguet':0},
 'prix_achat':{'Cafet Bréguet': 200, 'Interlocal': 250, 'RU Eiffel': 300, 'Local ViaRézo': 350, 'Musée': 400, 'Amphi Michelin': 450, 'RU Bréguet': 500},
 'loyer':{'Cafet Bréguet': 5, 'Interlocal': 10, 'RU Eiffel': 15, 'Local ViaRézo': 20, 'Musée': 25, 'Amphi Michelin': 30, 'RU Bréguet': 35}}
    input ('Bienvenue sur le Monopoly ! Appuyez sur entrée pour lancer la partie !')
    nb_joueurs = 2
    joueurs = {'nom':{},'argent':{},'position':{}}
    for i in range(int(nb_joueurs)):
        joueurs['nom'][str(i+1)]=input('Entrez le nom du joueur ' + str(i+1) +' : ')
        joueurs['argent'][str(i+1)] = 1000
        joueurs['position'][str(i+1)] = 0
    print(monopoly)
    print(joueurs)
    affichage(monopoly,joueurs)
    nb_tours = 0 
    L=joueurs_en_vie(nb_joueurs, joueurs)
    while nb_tours <30 and len(L)>=2 :
        for i in L:
            print(joueurs['nom'][str(i)] + ' lance le dé')
            lancer_de(i, monopoly, joueurs )
            affichage(monopoly,joueurs)
            arrivee(i,joueurs, monopoly)
            affichage(monopoly,joueurs)
            
        L=joueurs_en_vie(nb_joueurs, joueurs)
        nb_tours+=1
    
    if len(L)==1:
        print (joueurs['nom'][str(L[0])] +' a gagné')
    else :
        M=0
        for jr in L :
            if joueurs['argent'][str(jr)]>M:
                M=joueurs['argent'][str(jr)]
        indice_gagnants=[]
        for jr in L :
            if joueurs['argent'][str(jr)]==M:
                indice_gagnants.append(jr)
        
        for i in indice_gagnants:
            print("Bravo "+joueurs['nom'][str(i)]+', tu as gagné !\n')




def achat(numero_joueur, monopoly, joueurs) :
    position_joueur=joueurs['position'][str(numero_joueur)]
    if monopoly['nom'][position_joueur] in monopoly['possédé'] and monopoly['possédé'][monopoly['nom'][position_joueur]] ==0:
        print('La propriété est vacante, son nom est ' + monopoly['nom'][position_joueur] + ",son prix d'achat est " + str(monopoly['prix_achat'][monopoly['nom'][position_joueur]]) + ' et son loyer est de ' + str(monopoly['loyer'][monopoly['nom'][position_joueur]]) + " .")
        if monopoly['prix_achat'][monopoly['nom'][position_joueur]] <= joueurs['argent'][str(numero_joueur)] :
            print('Vous avez les fonds nécéssaires pour acheter cette propriété.')
            print("Souhaitez-vous l'acquérir?")
            choix = -1
            while choix!='0' and choix!='1' :
                choix = input("Entrez 0 pour non et 1 pour oui : ")
            choix=int(choix)
            if choix == 1 :
                monopoly['possédé'][monopoly['nom'][position_joueur]] = numero_joueur
                joueurs['argent'][str(numero_joueur)]-=monopoly['prix_achat'][monopoly['nom'][position_joueur]]
                print ("Vous avez acquéri " + monopoly['nom'][position_joueur] + '.')
            elif choix == 0 :
                print("Vous n'avez pas acquéri la propriété.")
        else :
            print ("Vous n'avez pas les fonds pour l'acquérir.")
            a=input("Appuyez sur la touche entrée pour continuer")

def arrivee(indice_joueur,joueurs,monopoly):
    indice_case=joueurs['position'][str(indice_joueur)]
    N=monopoly['nom'][indice_case] #on appelle N le nom du lieu sur lequel arrive le joueur
    print('Vous êtes sur la case ' + N)
    if N == 'APL':
        print('Rien à faire, profitez :)')
        a=input('Appuyez sur entrée pour continuer')
    elif monopoly['possédé'][N] != indice_joueur:        #si le joueur ne possède pas le lieu soit il l'achète soit il paie un loyer
        print('Cette propriété ne vous appartient pas')
        if monopoly['possédé'][N]== 0:
            achat(indice_joueur, monopoly, joueurs)

        elif monopoly['possédé'][N] != 0:
            print('Vous devez payer un loyer')
            loyer(monopoly, joueurs, joueurs['position'][str(indice_joueur)], indice_joueur)
            a=input('Vous avez été débité. Appuyez sur la touche entrée pour continuer')
    else:
        print('Vous êtes chez vous !')
        a=input("Appuyez sur entrée pour continuer")



def affichage(monopoly, joueurs):
    visuel_plateau=""
    visuel_plateau+=" _______________ _______________ _______________ \n"
    visuel_plateau+="|"+'Local ViaRézo'.center(15)+'|'+'Musée'.center(15)+'|'+'Amphi Michelin'.center(15)+'|\n'
    visuel_plateau+="|"+ ajout_ligne_proprietaire(monopoly, 4)+"|"+ ajout_ligne_proprietaire(monopoly, 5)+"|"+ ajout_ligne_proprietaire(monopoly, 6)+"|\n"
    visuel_plateau+="|"+ ajout_ligne_presence_1(joueurs, 4)+"|"+ ajout_ligne_presence_1(joueurs, 5)+"|"+ ajout_ligne_presence_1(joueurs, 6)+"|\n"
    visuel_plateau+="|"+ ajout_ligne_presence_2(joueurs, 4)+"|"+ ajout_ligne_presence_2(joueurs, 5)+"|"+ ajout_ligne_presence_2(joueurs, 6)+"|\n"
    visuel_plateau+=" _______________ _______________ _______________ \n"
    visuel_plateau+="|"+'RU Eiffel'.center(15)+'|'+'Pion de 1 : *'.center(15)+'|'+'RU Bréguet'.center(15)+'|\n'
    visuel_plateau+="|"+ ajout_ligne_proprietaire(monopoly, 3)+"|"+ ('1 : '+ str(joueurs['argent']['1'])+'€').center(15) +"|"+ ajout_ligne_proprietaire(monopoly, 7)+"|\n"
    visuel_plateau+="|"+ ajout_ligne_presence_1(joueurs, 3)+"|"+ 'Pion de 2 : §'.center(15) +"|"+ ajout_ligne_presence_1(joueurs, 7)+"|\n"
    visuel_plateau+="|"+ ajout_ligne_presence_2(joueurs, 3)+"|"+ ('2 : '+ str(joueurs['argent']['2'])+'€').center(15) +"|"+ ajout_ligne_presence_2(joueurs, 7)+"|\n"
    visuel_plateau+=" _______________ _______________ _______________ \n"
    visuel_plateau+="|"+'Interlocal'.center(15)+'|'+'Cafet Bréguet'.center(15)+'|'+'APL'.center(15)+'|\n'
    visuel_plateau+="|"+ ajout_ligne_proprietaire(monopoly, 2)+"|"+ ajout_ligne_proprietaire(monopoly, 1)+"|"+ '200€/passage'.center(15)+"|\n"
    visuel_plateau+="|"+ ajout_ligne_presence_1(joueurs, 2)+"|"+ ajout_ligne_presence_1(joueurs, 1)+"|"+ ajout_ligne_presence_1(joueurs, 0)+"|\n"
    visuel_plateau+="|"+ ajout_ligne_presence_2(joueurs, 2)+"|"+ ajout_ligne_presence_2(joueurs, 1)+"|"+ ajout_ligne_presence_2(joueurs, 0)+"|\n"
    visuel_plateau+=" _______________ _______________ _______________ \n"

    print(visuel_plateau)

def ajout_ligne_proprietaire(monopoly, indiceprop): #Fonction permettant d'afficher la deuxième ligne de chaque case
    if monopoly['possédé'][monopoly['nom'][indiceprop]]==0:
        return(('A vendre : '+ str(monopoly['prix_achat'][monopoly['nom'][indiceprop]])).center(15))
    if monopoly['possédé'][monopoly['nom'][indiceprop]]==1:
        return('Propriété de *'.center(15))
    if monopoly['possédé'][monopoly['nom'][indiceprop]]==2:
        return('Propriété de §'.center(15))

def ajout_ligne_presence_1(joueurs, indiceprop): #Fonction permettant d'afficher la troisième ligne de chaque case
    if joueurs['position']['1']==indiceprop:
        return('*'.center(15))
    else:
        return(' '.center(15))

def ajout_ligne_presence_2(joueurs, indiceprop): #Fonction permettant d'afficher la quatrième ligne de chaque case
    if joueurs['position']['2']==indiceprop:
        return('§'.center(15))
    else:
        return(' '.center(15))

def loyer(monopoly, joueurs, indice_prop, indice_joueur):
    # La fonction débite le joueur indice_joueur du loyer de la propriété indice_prop, et crédite 
    # le propriétaire de cette propriété (si la propriété est possédée par quelqu'un d'autre que le joueur indice_joueur)
    nom_de_la_propriete = monopoly['nom'][indice_prop]
    indice_proprietaire = str(monopoly['possédé'][nom_de_la_propriete])
    loyer = monopoly['loyer'][nom_de_la_propriete]
    if int(indice_proprietaire) not in [0, indice_joueur]: # C'est la condition entre parenthèses 
        if joueurs['argent'][str(indice_joueur)] >= loyer:
            # On débite celui qui paye le loyer
            joueurs['argent'][str(indice_joueur)] -= loyer
            # Et on crédite le propriétaire
            joueurs['argent'][indice_proprietaire] += loyer
            print("Vous avez payé " + str(loyer) + " au joueur " + str(indice_proprietaire))
        else:
        # Si le joueur ne peut pas payer
            # Le propriétaire récupère tout l'argent que le joueur possède
            print("Vous ne pouvez pas payer le loyer")
            joueurs['argent'][indice_proprietaire] += joueurs['argent'][str(indice_joueur)]    
            joueurs['argent'][str(indice_joueur)] = 0

import random as rd

def lancer_de(ind_joueur, monopoly, joueurs):    #joueur est l'entier correspondant au numéro du joueur
    nb_de_cases=rd.randint(1,3)   # on lance un dé de 3 pour déterminer le nombre de cases dont le joueur va avancer
    print('Le joueur ' + str(ind_joueur) + ' avance de ' + str(nb_de_cases) +' cases.')
    placement=joueurs['position'][str(ind_joueur)]
    placement+=nb_de_cases

    if placement>8:             
        placement=placement-8                # pour repartir sur le bon numéro de case si c'est supérieur à 7
        print("Vous touchez 200€ d'APL :) ")
        joueurs['argent'][str(ind_joueur)]+=200
        print ("Vous avez actuellement " + str(joueurs['argent'][str(ind_joueur)]) + " euros.")
    elif placement == 8:
        placement = 0
        print("Vous touchez 400€d'APL :) ")
        joueurs['argent'][str(ind_joueur)] += 400
        print ("Vous avez actuellement " + str(joueurs['argent'][str(ind_joueur)]) + " euros.")

    joueurs['position'][str(ind_joueur)]=placement