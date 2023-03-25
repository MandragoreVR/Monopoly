def listes_proprietes(numero_joueur, monopoly, joueurs):
    L=[]
    for l in monopoly['possédé']:
        if monopoly['possédé'][l]==numero_joueur :
            L.append(l)
    return (L)

def revendre(dette, numero_joueur, indice_proprietaire, monopoly, joueurs): #La dette est égale à la somme que le joueur doit payer moins l'argent qu'il possédait.
    print("Vous devez vendre des propriétés pour régler votre dette.")
    somme=0
    print("Voici les propriété que vous possédez et leurs prix :")
    L=listes_proprietes(numero_joueur, monopoly, joueurs)
    for l in L:
        print(l + " peut se vendre à " + str(int(monopoly['prix_achat'][l]*0.9)) + ".")
        somme+=monopoly['prix_achat'][l]
    if somme >= dette : #La somme des valeurs de toutes ses propriétés est supérieur à ça dette, il peut donc la rembourser 
        print("Vous pouvez rembourser votre dette.")
        restant=dette
        while restant > 0 : # Il faut vendre jusqu'à ce qu'on puisse rembourser.
            print("Il reste " + str(restant) + " à rembourser.")
            choix = input("Entrez le nom du bien que vous souhaitez vendre. ")
            if choix in L :
                restant-=int(monopoly['prix_achat'][choix]*0.9)
                monopoly['possédé'][choix]=0
                L.remove(choix)
        joueurs['argent'][str(numero_joueur)]+=(-1)*restant
        joueurs['argent'][str(indice_proprietaire)]+=dette
        print("Votre dette est remboursée, l'argent restant de la vente est ajouté à votre compte.")
    else :
        print("Il vous est impossible de rembourser votre dette.")
        for l in L :
            monopoly['possédé'][l]=0
        joueurs['argent'][str(indice_proprietaire)]+=somme
        joueurs['argent'][str(numero_joueur)]=somme-dette # une valeur négative d'argent implique une défaite

