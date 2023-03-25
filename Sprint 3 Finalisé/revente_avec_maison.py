def listes_proprietes(numero_joueur, monopoly, joueurs):
    L=[]
    for l in monopoly['possédé']:
        if monopoly['possédé'][l]==numero_joueur :
            L.append(l)
    return (L)

def revendre_bis(dette, numero_joueur, indice_proprietaire, monopoly, joueurs):
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
                if monopoly['maison'][l]==1 :
                    print(l + " posséde " + str(monopoly['maison'][l]) + " maison qui peut se vendre à " + str(int(monopoly['prix maison'][l]*0.8)) + ".")
                if monopoly['maison'][l] in [2,3,4] :
                    print(l + " posséde " + str(monopoly['maison'][l]) + " maisons qui peuvent se vendre chacune à " + str(int(monopoly['prix maison'][l]*0.8)) + ".")
                if monopoly['maison'][l]==5 :
                    print(l + " posséde un hotel qui peut se vendre à " + str(int(monopoly['prix maison'][l]*0.8*5)) + "et peut être considéré comme 5 maisons valant chacune" + str(int(monopoly['prix maison'][l]*0.8))+ ".")
            txt  = input("Voulez vous revendre des améliorations ou vos propriétés ? dites améliorations ou propriétés : ")
            if txt == 'améliorations':
                choix = input("Entrez le nom du bien où vous souhaitez revendre les améliorations. ")
                nombre= input("Entrez le nombre d'améliorations que vous souhaitez vendre. ")
                nombre=int(nombre)      
                if choix in L and monopoly['maison'][choix] != 0 and nombre in range(0, monopoly['maison'][choix]+1):
                    restant-=int(monopoly['prix maison'][choix]*0.8*nombre)
                    monopoly['maison'][choix]-=nombre                                                                        #les améliorations que le joueur revend, disparaissent et l'argent réduit la dette
            
            elif txt == 'propriétés' :
                choix = input("Entrez le nom du bien que vous souhaitez vendre. ")      
                if choix in L :
                    if monopoly['maison'][choix]!=0:
                        print("Vous vendez également les maisons qui lui sont associées.")
                        restant-=int(monopoly['maison'][choix]*monopoly['prix maison'][choix]*0.8)
                        monopoly['maison'][choix]=0
                    restant-=int(monopoly['prix_achat'][choix]*0.9)
                    monopoly['possédé'][choix]=0
                    L.remove(choix)                                                                                    #les propriétés que le joueur revend, retournent à la banque et peuvent être rachetées et les maisons dessus sont vendues. l'argent réduit la dette
        joueurs['argent'][str(numero_joueur)]+=(-1)*restant
        joueurs['argent'][str(indice_proprietaire)]+=dette
        print("Votre dette est remboursée, l'argent restant de la vente est ajouté à votre compte.")
    else :
        print("Il vous est impossible de rembourser votre dette.")                                               #si le joueur n'avait pas un capital suffisant, toutes ses possessions sont revendues et il finit dans le négatif
        for l in L :
            monopoly['possédé'][l]=0
            monopoly['maison'][l]=0
        joueurs['argent'][str(indice_proprietaire)]+=somme
        joueurs['argent'][str(numero_joueur)]=somme-dette # une valeur négative d'argent implique une défaite


