from revente_avec_maison import listes_proprietes, revendre_bis

def loyer_ter(monopoly, joueurs, indice_prop, indice_joueur):
    # La fonction débite le joueur indice_joueur du loyer de la propriété indice_prop, et crédite 
    # le propriétaire de cette propriété (si la propriété est possédée par quelqu'un d'autre que le joueur indice_joueur)
    nom_de_la_propriete = monopoly['nom'][indice_prop]
    indice_proprietaire = str(monopoly['possédé'][nom_de_la_propriete])
    if int(indice_proprietaire) not in [0, indice_joueur]: # C'est la condition entre parenthèses 
        if nom_de_la_propriete in monopoly['loyer']: #On modifie le prix du loyer en fonction du nombre de maison sur le local.
            if monopoly['maison'][nom_de_la_propriete]==0 :
                loyer=monopoly['loyer'][nom_de_la_propriete]
            if monopoly['maison'][nom_de_la_propriete]==1 :
                loyer=monopoly['loyer'][nom_de_la_propriete]*5
            if monopoly['maison'][nom_de_la_propriete]==2 :
                loyer=monopoly['loyer'][nom_de_la_propriete]*15
            if monopoly['maison'][nom_de_la_propriete]==3 :
                loyer=monopoly['loyer'][nom_de_la_propriete]*40
            if monopoly['maison'][nom_de_la_propriete]==4 :
                loyer=monopoly['loyer'][nom_de_la_propriete]*60
            if monopoly['maison'][nom_de_la_propriete]==5 :
                loyer=monopoly['loyer'][nom_de_la_propriete]*80
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
            revendre_bis(dette, indice_joueur, monopoly['possédé'][nom_de_la_propriete], monopoly, joueurs)

def loyer_RU(monopoly, indice_proprietaire):
    count=0
    for i in range (5, 36, 10): #Les numéros des restaurants(gares)
        N=monopoly['nom'][i] #le nom de la propriété
        if monopoly['possédé'][N]==indice_proprietaire:
            count+=1
    if count ==1:
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
        return (int(4*joueurs['dernier lancer dés'][str(indice_joueur)]))  
    if count==2:
        return (int(10*joueurs['dernier lancer dés'][str(indice_joueur)])) 


