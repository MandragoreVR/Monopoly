# monopoly={'nom':{0:'APL',1:'Cafet Bréguet', 2: 'Interlocal', 3:'RU Eiffel', 4:'Local ViaRézo', 5:'Musée',6:'Amphi Michelin',7:'RU Bréguet'},
#  'possédé':{'Cafet Bréguet':0, 'Interlocal':0, 'RU Eiffel':0, 'Local ViaRézo':0, 'Musée':0, 'Amphi Michelin':0, 'RU Bréguet':0},
#  'prix_achat':{'Cafet Bréguet': 200, 'Interlocal': 250, 'RU Eiffel': 300, 'Local ViaRézo': 350, 'Musée': 400, 'Amphi Michelin': 450, 'RU Bréguet': 500},
#  'loyer':{'Cafet Bréguet': 5, 'Interlocal': 10, 'RU Eiffel': 15, 'Local ViaRézo': 20, 'Musée': 25, 'Amphi Michelin': 30, 'RU Bréguet': 35}}

# joueurs={'nom':{}, 'argent':{'1': 1000, '2': 1000}, 'position':{'1':0, '2':0}} # 1 et 2 sont des entiers et non des strings

def achat(numero_joueur, monopoly, joueurs) :
    position_joueur=joueurs['position'][str(numero_joueur)]
    if monopoly['nom'][position_joueur] in monopoly['possédé'] and monopoly['possédé'][monopoly['nom'][position_joueur]] == 0:
        if monopoly['nom'][position_joueur] in monopoly['loyer'] :        #On prend ceux qui n'ont pas de loyer spécial.
            print('La propriété est vacante, son nom est ' + monopoly['nom'][position_joueur] + ", son prix d'achat est " + str(monopoly['prix_achat'][monopoly['nom'][position_joueur]]) + ' et son loyer est de ' + str(monopoly['loyer'][monopoly['nom'][position_joueur]]) + ".")
        if position_joueur in [5,15,25,35] :        #On prend ceux qui sont des restaurants.
            print('La propriété est vacante, son nom est ' + monopoly['nom'][position_joueur] + ", son prix d'achat est " + str(monopoly['prix_achat'][monopoly['nom'][position_joueur]]) + " et son loyer est variable en fonction du nombre de restaurants que vous possédez : 25 pour 1, 50 pour 2, 100 pour 3 et 200 pour les 4.")
        if position_joueur in [12,28] :        #On prend ceux qui sont des accueils
            print('La propriété est vacante, son nom est ' + monopoly['nom'][position_joueur] + ", son prix d'achat est " + str(monopoly['prix_achat'][monopoly['nom'][position_joueur]]) + " et son loyer est variable en fonction du nombre d'accueils que vous possédez et de la somme des dés du joueur tombant dessus : 4 fois la somme des dés pour 1 et 10 fois pour les 2.")
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
