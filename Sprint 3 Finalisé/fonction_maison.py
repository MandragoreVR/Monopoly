# le nouveau dictionnaire monopoly doit contenir le nombre de 'maisons' associé à chaque propriété


def achat_maison(ind_joueur , joueurs , monopoly):
    nb_propriétés_jr = 0
    liste_propriétés = []
    for i in monopoly['possédé']:
        if monopoly['possédé'][i]==ind_joueur:
                nb_propriétés_jr += 1
                liste_propriétés.append(i)                  #on renvoie la liste des propriétés possédés par le joueur et leur nombre
    
    prop_améliorables=[]                                    #on crée la liste des propriétés améliorables, i.e. celles où on a toutes les cases d'une même couleur
    if nb_propriétés_jr > 0 :
        for prop in liste_propriétés :                      #pour chaque propriété, on vérifie si le joueur a toutes les cases d'une même couleur
            if prop == 'Ecsit' :
                if monopoly['possédé']['Guilde'] == ind_joueur :                                    #pour chaque couleur, si le joueur n'a pas au minimum la première propriété de cette couleur, il ne pourra pas acheter de maison dessus. on vérifie cela pour toutes les couleurs
                    print('Vous avez bien toutes les cases de même couleur que la Guilde')
                    prop_améliorables.append('Ecsit')
                    prop_améliorables.append('Guilde')

            elif prop == 'PICS' :
                if monopoly['possédé']['Hyris'] == ind_joueur  and monopoly['possédé']['ViaRezo'] == ind_joueur:
                    print('Vous avez bien toutes les cases de même couleur que Pics')
                    prop_améliorables.append('PICS')
                    prop_améliorables.append('Hyris')
                    prop_améliorables.append('ViaRezo')

            elif prop == 'Commus' :
                if monopoly['possédé']['Musics'] == ind_joueur  and monopoly['possédé']['BDA'] == ind_joueur:
                    print('Vous avez bien toutes les cases de même couleur que la Commus')
                    prop_améliorables.append('Commus')
                    prop_améliorables.append('Musics')
                    prop_améliorables.append('BDA')

            elif prop == 'NCV' :
                if monopoly['possédé']['Raid'] == ind_joueur  and monopoly['possédé']['BDS'] == ind_joueur:
                    print('Vous avez bien toutes les cases de même couleur que la NCV')
                    prop_améliorables.append('NCV')
                    prop_améliorables.append('Raid')
                    prop_améliorables.append('BDS')

            elif prop == 'SBCS' :
                if monopoly['possédé']['ADR'] == ind_joueur  and monopoly['possédé']['BDE'] == ind_joueur:
                    print('Vous avez bien toutes les cases de même couleur que SBCS')
                    prop_améliorables.append('SBCS')
                    prop_améliorables.append('ADR')
                    prop_améliorables.append('BDE')

            elif prop == 'Oser' :
                if monopoly['possédé']['CheerUp'] == ind_joueur  and monopoly['possédé']['Huma'] == ind_joueur:
                    print('Vous avez bien toutes les cases de même couleur que Oser')
                    prop_améliorables.append('Oser')
                    prop_améliorables.append('CheerUp')
                    prop_améliorables.append('Huma')

            elif prop == 'PAPS' :
                if monopoly['possédé']['FIR'] == ind_joueur  and monopoly['possédé']['Impact'] == ind_joueur:
                    print('Vous avez bien toutes les cases de même couleur que PAPS')
                    prop_améliorables.append('PAPS')
                    prop_améliorables.append('FIR')
                    prop_améliorables.append('Impact')

            elif prop == 'JE' :
                if monopoly['possédé']['LeForum'] == ind_joueur :
                    print('Vous avez bien toutes les cases de même couleur que la JE')
                    prop_améliorables.append('JE')
                    prop_améliorables.append('LeForum')

    if len(prop_améliorables) > 0 :                                                             #si on a au moins une couleur, d'où au moins quelques propriétés qu'on peut améliorer        
    if monopoly['nom'][joueurs['position'][str(ind_joueur)]] in prop_améliorables :
        prop=monopoly['nom'][joueurs['position'][str(ind_joueur)]]
        maison=monopoly['maison'][prop]       
        print("Vous pouvez acheter "+str(int(5-maison))+ " maison(s) sur " + prop + " pour " + str(monopoly['prix maison'][prop]) + " chacune.")
        txt=0
        while txt!='oui' and txt!='non':
            txt = input('Voulez vous acheter une amélioration pour' + prop + '? dites oui ou non : ')
        
        if txt == 'oui':
            nombre = -1
            test=True
            while test :
                while nombre !='0' and nombre!='1' and nombre!='2' and nombre!='3' and nombre !='4' and nombre !='5':
                    nombre = input('Combien voulez vous en acheter (pas plus que vos fonds vous le permettent) ? ')
                nombre=int(nombre)  
                if joueurs['argent'][str(ind_joueur)]>=(nombre*monopoly['prix maison'][prop]) and nombre <= 5-monopoly['maison'][prop] :
                    test=False                                                                                  
            joueurs['argent'][str(ind_joueur)] -= monopoly['prix maison'][prop]*nombre #s'il n'a pas les fonds suffisants ou s'il n'en achète pas, on ne le débite pas.
            monopoly['maison'][prop] += nombre
            print('Vous avez acheté ' + str(nombre)+ ' amélioration(s) de ' + prop)
            print('Il vous reste '+ str(joueurs['argent'][str(ind_joueur)]))
            if monopoly['maison'][prop]==0 : 
                print('Le loyer passe à '+ str(monopoly['loyer'][prop]) + '.')
            if monopoly['maison'][prop]==1 :
                print('Le loyer passe à '+ str(monopoly['loyer'][prop]*5) + '.')
            if monopoly['maison'][prop]==2 :
                print('Le loyer passe à '+ str(monopoly['loyer'][prop]*15) + '.')
            if monopoly['maison'][prop]==3 :
                print('Le loyer passe à '+ str(monopoly['loyer'][prop]*40) + '.')
            if monopoly['maison'][prop]==4 :
                print('Le loyer passe à '+ str(monopoly['loyer'][prop]*60) + '.')
            if monopoly['maison'][prop]==5 :
                print('Le loyer passe à '+ str(monopoly['loyer'][prop]*80) + '.')                                              
        else : 
            print("Vous n'avez rien acheté.")
