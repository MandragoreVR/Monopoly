# monopoly={'nom':{0:'APL',1:'Cafet Bréguet', 2: 'Interlocal', 3:'RU Eiffel', 4:'Local ViaRézo', 5:'Musée',6:'Amphi Michelin',7:'RU Bréguet'},
#  'possédé':{'Cafet Bréguet':0, 'Interlocal':0, 'RU Eiffel':0, 'Local ViaRézo':0, 'Musée':0, 'Amphi Michelin':0, 'RU Bréguet':0},
#  'prix_achat':{'Cafet Bréguet': 200, 'Interlocal': 250, 'RU Eiffel': 300, 'Local ViaRézo': 350, 'Musée': 400, 'Amphi Michelin': 450, 'RU Bréguet': 500},
#  'loyer':{'Cafet Bréguet': 5, 'Interlocal': 10, 'RU Eiffel': 15, 'Local ViaRézo': 20, 'Musée': 25, 'Amphi Michelin': 30, 'RU Bréguet': 35}}

# joueurs={'nom':{}, 'argent':{'1': 1000, '2': 1000}, 'position':{'1':0, '2':0}} # 1 et 2 sont des entiers et non des strings

def achat(numero_joueur, monopoly, joueurs) :
    position_joueur=joueurs['position'][str(numero_joueur)]
    if monopoly['nom'][position_joueur] in monopoly['possédé'] and monopoly['possédé'][monopoly['nom'][position_joueur]] == 0: #Si monopoly['possédé'][nom_de_la_propriété]=0 cela signifie que cette propriété n'appartient à personne et donc elle peut être achetée.
        print('La propriété est vacante, son nom est ' + monopoly['nom'][position_joueur] + ", son prix d'achat est " + str(monopoly['prix_achat'][monopoly['nom'][position_joueur]]) + ' et son loyer est de ' + str(monopoly['loyer'][monopoly['nom'][position_joueur]]) + ".")
        if monopoly['prix_achat'][monopoly['nom'][position_joueur]] <= joueurs['argent'][str(numero_joueur)] : #Le joueur peut acheter si et seulement si il a les fonds pour, il ne peut pas s'endetter.
            print('Vous avez les fonds nécéssaires pour acheter cette propriété.')
            print("Souhaitez-vous l'acquérir?")
            choix = -1
            while choix!='0' and choix!='1' : #permet de vérifier que choix est forcément égal à '0 ou '1'.
                choix = input("Entrez 0 pour non et 1 pour oui : ")
            choix=int(choix)
            if choix == 1 :
                monopoly['possédé'][monopoly['nom'][position_joueur]] = numero_joueur #On remplace dans monopoly['possédé'][nom_de_la_propriete] 0 par le numéro du joueur pour indiquer que la propriété lui appartient.
                joueurs['argent'][str(numero_joueur)]-=monopoly['prix_achat'][monopoly['nom'][position_joueur]] #On débite le joueur du prix d'achat de la propriété.
                print ("Vous avez acquéri " + monopoly['nom'][position_joueur] + '.')
            elif choix == 0 :
                print("Vous n'avez pas acquéri la propriété.")
        else :
            print ("Vous n'avez pas les fonds pour l'acquérir.")
            a=input("Appuyez sur la touche entrée pour continuer")
