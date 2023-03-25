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
            joueurs['argent'][str(indice_joueur)] = joueurs['argent'][str(indice_joueur)] - loyer # Une somme d'argent négative implique une défaite.


