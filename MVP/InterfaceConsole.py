#Pour tester la fonction, vous pouvez utiliser ces dictionnaires :
# monopoly={'nom':{0:'APL',1:'Cafet Bréguet', 2: 'Interlocal', 3:'RU Eiffel', 4:'Local ViaRézo', 5:'Musée',6:'Amphi Michelin',7:'RU Bréguet'},
#  'possédé':{'Cafet Bréguet':1, 'Interlocal':0, 'RU Eiffel':2, 'Local ViaRézo':2, 'Musée':1, 'Amphi Michelin':0, 'RU Bréguet':0},
#  'prix_achat':{'Cafet Bréguet': 200, 'Interlocal': 250, 'RU Eiffel': 300, 'Local ViaRézo': 350, 'Musée': 400, 'Amphi Michelin': 450, 'RU Bréguet': 500},
#  'loyer':{'Cafet Bréguet': 5, 'Interlocal': 10, 'RU Eiffel': 15, 'Local ViaRézo': 20, 'Musée': 25, 'Amphi Michelin': 30, 'RU Bréguet': 35}}

# joueurs={'nom':{}, 'argent':{'1': 1000, '2': 1000}, 'position':{'1':6, '2':3}}

#Cette fonction affiche la grille lorsque l'on lui donne un dictionnaire Monopoly. La grille est une grille 3*3 se décomposant en des cases de 4 lignes.
#La première ligne est le nom de la propriété, la deuxième est le prix de vente / le propriétaire si la propriété est déjà vendue
#Les troisième et quatrième lignes servent à placer les pions des joueurs s'ils sont sur la case.
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

def ajout_ligne_proprietaire(monopoly, indiceprop): #Fonction permettant d'afficher la deuxième ligne de chaque case.
    if monopoly['possédé'][monopoly['nom'][indiceprop]]==0:
        return(('A vendre : '+ str(monopoly['prix_achat'][monopoly['nom'][indiceprop]])).center(15))
    if monopoly['possédé'][monopoly['nom'][indiceprop]]==1:
        return('Propriété de *'.center(15))
    if monopoly['possédé'][monopoly['nom'][indiceprop]]==2:
        return('Propriété de §'.center(15))

def ajout_ligne_presence_1(joueurs, indiceprop): #Fonction permettant d'afficher la troisième ligne de chaque case. * est le pion du joueur 1.
    if joueurs['position']['1']==indiceprop:
        return('*'.center(15))
    else:
        return(' '.center(15))


def ajout_ligne_presence_2(joueurs, indiceprop): #Fonction permettant d'afficher la quatrième ligne de chaque case. § est le pion du joueur 2.
    if joueurs['position']['2']==indiceprop:
        return('§'.center(15))
    else:
        return(' '.center(15))




