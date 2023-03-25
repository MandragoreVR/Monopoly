import tkinter as tk
from PIL import Image, ImageTk
from dictionnaire_ter import monopoly

import os
os.chdir("Images")


taille_plateau = 600
nb_joueurs = 4
# Quelques valeurs du vrai plateau de Monopoly (afin d'avoir un coefficient de proportionnalité)
longueur = 22.6
coef = taille_plateau/longueur  #coef de proportionnalité (permet aussi de zoomer plus ou moins sur le plateau)
longueur_coin = 2.9 * coef
largeur_coin = 2.4 * coef
largeur_case_horizontale = 1.866666666666 * coef
largeur_case_verticale = 1.97777777777777 * coef
zone_coloree_horizontale = 0.65 * coef
zone_coloree_verticale = 0.8 * coef

 #coef de proportionnalité (permet aussi de zoomer plus ou moins sur le plateau)

root = tk.Tk()
root.title('Monopoly')
f1 = tk.Frame(root, bd=1, relief='solid')
plateau = tk.Canvas(f1, bg = '#ECFCCC', height = taille_plateau, width = taille_plateau)

# Contour du plateau
_ = plateau.create_line(0, 0, 0, taille_plateau)
_ = plateau.create_line(0, 0, taille_plateau, 0)
_ = plateau.create_line(taille_plateau, 0, taille_plateau, taille_plateau)
_ = plateau.create_line(0, taille_plateau, taille_plateau, taille_plateau)

##  Dessin des cases

# Les grandes lignes
_ = plateau.create_line(longueur_coin, 0, longueur_coin, taille_plateau) # grande ligne verticale gauche
_ = plateau.create_line(0, largeur_coin, taille_plateau, largeur_coin) # grande ligne horizontale haute
_ = plateau.create_line(taille_plateau - longueur_coin, 0, taille_plateau - longueur_coin, taille_plateau) # grande ligne verticale droite
_ = plateau.create_line(0, taille_plateau - largeur_coin, taille_plateau, taille_plateau - largeur_coin) # grande ligne horizontale basse

# Les cases
for i in range(1, 9):
    # Cases du haut 
    _ = plateau.create_line(longueur_coin + i*largeur_case_horizontale, 0, longueur_coin + i*largeur_case_horizontale, largeur_coin)
    # Cases de gauche
    _ = plateau.create_line(0, largeur_coin + i*largeur_case_verticale, longueur_coin, largeur_coin + i*largeur_case_verticale)
    # Cases du bas
    _ = plateau.create_line(longueur_coin + i*largeur_case_horizontale, taille_plateau - largeur_coin, longueur_coin + i*largeur_case_horizontale, taille_plateau)
    # Cases de droite
    _ = plateau.create_line(taille_plateau - longueur_coin, largeur_coin + i*largeur_case_verticale, taille_plateau, largeur_coin + i*largeur_case_verticale)


# Les couleurs des cases
# Colonne de gauche
for i in range(9):
    if i not in [2, 4, 7]: # la liste contient les cases qui ne sont pas coloriées dans cette colonne
        if i < 5: # on sépare suivant les deux couleurs de la colonne
            fill = "#FF6600"
        else:
            fill = "#F044DC"
        _ = plateau.create_rectangle(longueur_coin - zone_coloree_verticale, largeur_coin + i*largeur_case_verticale, longueur_coin, largeur_coin + (i+1)*largeur_case_verticale, fill = fill)

# Ligne du haut
for i in range(9):
    if i not in [1, 4, 7]: #idem
        if i < 5:
            fill = "#FF0000"
        else:
            fill = "#FFFF00"
        _ = plateau.create_rectangle(longueur_coin + i*largeur_case_horizontale, largeur_coin - zone_coloree_horizontale, longueur_coin + (i+1)*largeur_case_horizontale, largeur_coin, fill = fill)

# Colonne de droite
for i in range(9):
    if i not in [2, 4, 5, 7]:
        if i < 5:
            fill = "#008000"
        else:
            fill = "#3333FF"
        _ = plateau.create_rectangle(taille_plateau - longueur_coin, largeur_coin + i*largeur_case_verticale, taille_plateau - longueur_coin + zone_coloree_verticale, largeur_coin + (i+1)*largeur_case_verticale, fill = fill)

# Ligne du bas   
for i in range(9):
    if i not in [2, 4, 5, 7]:
        if i < 5:
            fill = "#ACCCFC"
        else:
            fill = "#9C349C"
        _ = plateau.create_rectangle(longueur_coin + i*largeur_case_horizontale, taille_plateau - largeur_coin, longueur_coin + (i+1)*largeur_case_horizontale, taille_plateau - largeur_coin + zone_coloree_horizontale, fill = fill)


# Case départ : 
_ = plateau.create_text(taille_plateau - longueur_coin/2, taille_plateau - largeur_coin/2, text = " Case \n  APL \n+200€")
 
# Case prison :
hauteur_prison = 1.8 *coef
largeur_prison = 2.2*coef
_ = plateau.create_rectangle(longueur_coin - largeur_prison, taille_plateau - largeur_coin, longueur_coin, taille_plateau - largeur_coin + hauteur_prison, fill = "#FF0000")
_ = plateau.create_text(longueur_coin - largeur_prison/2, taille_plateau - largeur_coin + hauteur_prison/2, text = "Troukipu")
_ = plateau.create_text(longueur_coin - largeur_prison/2, taille_plateau-(largeur_coin/2-hauteur_prison/2),text= "Visite")
 
# Case parc gratuit : 
_ = plateau.create_text(longueur_coin/2,largeur_coin/3-largeur_coin/9, text='Clairière\nBouygues')
 
# Case "Allez en prison"
_ = plateau.create_text(taille_plateau - longueur_coin/2, largeur_coin/2, text = "    Allez\n      au\nTroukipu")

# Cases des propriétés
 
_ = plateau.create_text(taille_plateau-longueur_coin-largeur_case_horizontale/2 , taille_plateau-largeur_coin/2,  text = "Ecsit")
_ = plateau.create_text(taille_plateau-longueur_coin-largeur_case_horizontale-largeur_case_horizontale/2, taille_plateau-largeur_coin/2,  text = "MyWay\n     ")
_ = plateau.create_text(taille_plateau-longueur_coin-largeur_case_horizontale/2-2*largeur_case_horizontale , taille_plateau-largeur_coin/2,  text = "Guilde")
_ = plateau.create_text(taille_plateau-longueur_coin-largeur_case_horizontale/2-3*largeur_case_horizontale , taille_plateau-largeur_coin/2-largeur_case_horizontale/3,  text = "Loyer \n Césal")
_ = plateau.create_text(taille_plateau-longueur_coin-largeur_case_horizontale/2-4*largeur_case_horizontale , taille_plateau-largeur_coin/2-largeur_case_horizontale/3,  text = "Cafet")
_ = plateau.create_text(taille_plateau-longueur_coin-largeur_case_horizontale/2-5*largeur_case_horizontale , taille_plateau-largeur_coin/2,  text = "PICS")
_ = plateau.create_text(taille_plateau-longueur_coin-largeur_case_horizontale/2-6*largeur_case_horizontale , taille_plateau-largeur_coin/2,  text = "MyWay\n     ")
_ = plateau.create_text(taille_plateau-longueur_coin-largeur_case_horizontale/2-7*largeur_case_horizontale , taille_plateau-largeur_coin/2,  text = "Hyris")
_ = plateau.create_text(taille_plateau-longueur_coin-largeur_case_horizontale/2-8*largeur_case_horizontale , taille_plateau-largeur_coin/2,  text = "ViaRezo")
 
_ = plateau.create_text(2*longueur_coin/5, taille_plateau-largeur_coin-largeur_case_verticale/2, text = "Commus ")
_ = plateau.create_text(longueur_coin/2,taille_plateau-largeur_coin-largeur_case_verticale-largeur_case_verticale/2-largeur_case_horizontale/5, text = " Accueil\n ")
_ = plateau.create_text(2*longueur_coin/5,taille_plateau-largeur_coin-2*largeur_case_verticale-largeur_case_verticale/2, text = " Musics")
_ = plateau.create_text(longueur_coin/2,taille_plateau-largeur_coin-3*largeur_case_verticale-largeur_case_verticale/2, text = "BDA")
_ = plateau.create_text(longueur_coin/2,taille_plateau-largeur_coin-4*largeur_case_verticale-largeur_case_verticale/2-largeur_case_verticale/3, text = "RU Eiffel")
_ = plateau.create_text(longueur_coin/2,taille_plateau-largeur_coin-5*largeur_case_verticale-largeur_case_verticale/2, text = "NCV")
_ = plateau.create_text(longueur_coin/2,taille_plateau-largeur_coin-6*largeur_case_verticale-largeur_case_verticale/2-largeur_case_verticale/9, text = "MyWay\n     ")
_ = plateau.create_text(longueur_coin/2,taille_plateau-largeur_coin-7*largeur_case_verticale-largeur_case_verticale/2, text = "Raid")
_ = plateau.create_text(longueur_coin/2,taille_plateau-largeur_coin-8*largeur_case_verticale-largeur_case_verticale/2, text = "BDS")

_ = plateau.create_text(longueur_coin+ 0* largeur_case_horizontale+largeur_case_horizontale/2,largeur_coin/2, text='SBCS')
_ = plateau.create_text(longueur_coin+ 1* largeur_case_horizontale+largeur_case_horizontale/2,largeur_coin/2, text='MyWay\n     ')
_ = plateau.create_text(longueur_coin+ 2* largeur_case_horizontale+largeur_case_horizontale/2,largeur_coin/2, text='ADR')
_ = plateau.create_text(longueur_coin+ 3* largeur_case_horizontale+largeur_case_horizontale/2,largeur_coin/2, text='BDE')
_ = plateau.create_text(longueur_coin+ 4* largeur_case_horizontale+largeur_case_horizontale/2,largeur_coin/2-largeur_case_horizontale/2, text='RU')
_ = plateau.create_text(longueur_coin+ 4* largeur_case_horizontale+largeur_case_horizontale/2,largeur_coin/2-largeur_case_horizontale/2, text='\n \n Bréguet')
_ = plateau.create_text(longueur_coin+ 5* largeur_case_horizontale+largeur_case_horizontale/2,largeur_coin/2, text='Oser')
_ = plateau.create_text(longueur_coin+ 6* largeur_case_horizontale+largeur_case_horizontale/2,largeur_coin/2, text='CheerUp')
_ = plateau.create_text(longueur_coin+ 7* largeur_case_horizontale+largeur_case_horizontale/2,largeur_coin/3-largeur_coin/6, text='Accueil' )
_ = plateau.create_text(longueur_coin+ 8* largeur_case_horizontale+largeur_case_horizontale/2,largeur_coin/2, text='Huma')
 
_ = plateau.create_text(taille_plateau - longueur_coin/2, largeur_coin+ largeur_case_verticale/2, text = "PAPS")
_ = plateau.create_text(taille_plateau - longueur_coin/2, largeur_coin+ largeur_case_verticale/2+largeur_case_verticale, text = "FIR")
_ = plateau.create_text(taille_plateau - longueur_coin/2, largeur_coin+ largeur_case_verticale/2+2*largeur_case_verticale-largeur_case_verticale/9 , text = "MyWay\n     ")
_ = plateau.create_text(taille_plateau - longueur_coin/2, largeur_coin+ largeur_case_verticale/2+3*largeur_case_verticale, text = "  Impact")
_ = plateau.create_text(taille_plateau - longueur_coin/2, largeur_coin+ largeur_case_verticale/2+4*largeur_case_verticale-largeur_case_verticale/3, text = "Musée")
_ = plateau.create_text(taille_plateau - longueur_coin/2, largeur_coin+ largeur_case_verticale/2+5*largeur_case_verticale-largeur_case_verticale/9, text = "MyWay\n     ")
_ = plateau.create_text(taille_plateau - longueur_coin/2, largeur_coin+ largeur_case_verticale/2+6*largeur_case_verticale, text = "JE")
_ = plateau.create_text(taille_plateau - longueur_coin/2, largeur_coin+ largeur_case_verticale/2+7*largeur_case_verticale-largeur_case_verticale/4.5, text = "   Tour\ndes cotizs")
_ = plateau.create_text(taille_plateau - longueur_coin/2, largeur_coin+ largeur_case_verticale/2+8*largeur_case_verticale, text = " Forum")

# insertion des points d'interrogation sur les cases chance (MyWay)
image= Image.open("ptinterrogationV2.png")
 
image = image.resize((int(taille_plateau*1/26), int(taille_plateau*1/24)), Image.ANTIALIAS)
 
point = ImageTk.PhotoImage(image)
 
_ = plateau.create_image(taille_plateau - longueur_coin/2, largeur_coin+ largeur_case_verticale/2+5*largeur_case_verticale+largeur_case_verticale/5 , image=point)
 
_ = plateau.create_image( taille_plateau - longueur_coin/2, largeur_coin+ largeur_case_verticale/2+2*largeur_case_verticale+largeur_case_verticale/5 , image=point)
 
_ = plateau.create_image(longueur_coin+ 1* largeur_case_horizontale+largeur_case_horizontale/2,largeur_coin/2+largeur_case_verticale/4 , image=point)
 
_ = plateau.create_image(longueur_coin/2,taille_plateau-largeur_coin-6*largeur_case_verticale-largeur_case_verticale/2+largeur_case_verticale/5 , image=point)
 
_ = plateau.create_image(taille_plateau-longueur_coin-largeur_case_horizontale/2-6*largeur_case_horizontale , taille_plateau-largeur_coin/2+largeur_case_verticale/4 , image=point)
 
_ = plateau.create_image(taille_plateau-longueur_coin-largeur_case_horizontale-largeur_case_horizontale/2, taille_plateau-largeur_coin/2+largeur_case_verticale/4 , image=point)
 
#insertion d'une illustration pour la clairière
 
imagess= Image.open("bouyguesV2.png")
 
imagess = imagess.resize((int(taille_plateau*1/20), int(taille_plateau*1/20)), Image.ANTIALIAS)
 
points = ImageTk.PhotoImage(imagess)
 
_ = plateau.create_image(longueur_coin/2,largeur_coin/3+largeur_case_verticale/2, image=points)
 
#insertion d'une illustration pour l'accueil césal
 
imagesss= Image.open("césal.png")
 
imagesss= imagesss.resize((int(taille_plateau*1/17), int(taille_plateau*1/17)), Image.ANTIALIAS)
 
pointss = ImageTk.PhotoImage(imagesss)
 
_ = plateau.create_image(longueur_coin+ 7* largeur_case_horizontale+largeur_case_horizontale/2,largeur_coin/2+largeur_case_verticale/4-largeur_case_verticale/7, image=pointss)

#insertion d'une illustration pour l'accueil viarezo
imagevia= Image.open("logoviarezo.png")
 
imagevia= imagevia.resize((int(taille_plateau*1/11), int(taille_plateau*1/18)), Image.ANTIALIAS)
 
pointvia = ImageTk.PhotoImage(imagevia)

_ = plateau.create_image(longueur_coin/2,taille_plateau-largeur_coin-largeur_case_verticale-largeur_case_verticale/2+largeur_case_verticale/7, image=pointvia)

#insertion d'une illustration pour les RU/cafet

imageRU= Image.open("symboleRU.png")
 
imageRU= imageRU.resize((int(taille_plateau*1/20), int(taille_plateau*1/20)), Image.ANTIALIAS)
 
pointRU= ImageTk.PhotoImage(imageRU)

_ = plateau.create_image(longueur_coin+ 4* largeur_case_horizontale+largeur_case_horizontale/2,largeur_coin/2+largeur_case_verticale/3.5, image=pointRU)
_ = plateau.create_image(longueur_coin/2,taille_plateau-largeur_coin-4*largeur_case_verticale-largeur_case_verticale/2-largeur_case_verticale/3+largeur_case_verticale/2.3, image=pointRU)
_ = plateau.create_image(taille_plateau - longueur_coin/2, largeur_coin+ largeur_case_verticale/2+4*largeur_case_verticale+largeur_case_verticale/6, image=pointRU)
_ = plateau.create_image(taille_plateau-longueur_coin-largeur_case_horizontale/2-4*largeur_case_horizontale , taille_plateau-largeur_coin/2+largeur_case_horizontale/4, image=pointRU)

#ajout d'une illustration pour les cases de type 'taxe de luxe'
imagear= Image.open("symboleeuro.png")
 
imagear= imagear.resize((int(taille_plateau*1/20), int(taille_plateau*1/20)), Image.ANTIALIAS)
 
pointar= ImageTk.PhotoImage(imagear)

_ = plateau.create_image(taille_plateau - longueur_coin/2, largeur_coin+ largeur_case_verticale/2+7*largeur_case_verticale+largeur_case_verticale/4, image=pointar)
_ = plateau.create_image(taille_plateau-longueur_coin-largeur_case_horizontale/2-3*largeur_case_horizontale , taille_plateau-largeur_coin/2+largeur_case_horizontale/3.5, image=pointar)


 

# Logo de CS au milieu du plateau
image = Image.open("monopoly.png")
image = image.resize((int(taille_plateau * 340/600), int(taille_plateau * 85/600)), Image.ANTIALIAS)
logo = ImageTk.PhotoImage(image)
_ = plateau.create_image(taille_plateau/2 + taille_plateau/120, taille_plateau/2 - taille_plateau/12, image = logo)

images = Image.open("LogoCS1.png")
images = images.resize((int(130 * taille_plateau/600), int(100 * taille_plateau/600)), Image.ANTIALIAS)
logos = ImageTk.PhotoImage(images)
_ = plateau.create_image(taille_plateau/2 + taille_plateau/120, taille_plateau/2 + taille_plateau/12, image = logos)

## Codage des pions 
rayon = taille_plateau / 60
couleurs_pions = ["#FF0000", "#3333FF", "#008000", "#FFFF00"] # rouge, bleu, vert, jaune
pions = []
for i in range(nb_joueurs):
    pion = plateau.create_oval(taille_plateau - longueur_coin/2 - rayon, taille_plateau - largeur_coin/2 - rayon, taille_plateau - longueur_coin/2 + rayon, taille_plateau - largeur_coin/2 + rayon, fill = couleurs_pions[i])
    if i == 3:
        fill = 'black'
    else:
        fill = 'white'
    texte = plateau.create_text(taille_plateau - longueur_coin/2, taille_plateau - largeur_coin/2, text = str(i+1), fill = fill)
    pions.append((pion, texte))

# Pour placer un pion sur la case i, on a besoin des coordonnées du milieu de la case i. Ces coordonnées seront contenues dans la liste coordonnees
coordonnees = [(taille_plateau - longueur_coin/2, taille_plateau - largeur_coin /2)]
for i in range(8, -1, -1): # coordonnees de la ligne du bas
    coordonnees.append((longueur_coin + (2*i+1)*largeur_case_horizontale/2, taille_plateau - (largeur_coin - zone_coloree_horizontale)/2))
coordonnees.append((taille_plateau / 40, taille_plateau *39/40)) # Case prison (visite seule)

for i in range(8, -1, -1): # colonne de gauche
    coordonnees.append(((longueur_coin - zone_coloree_verticale)/2, largeur_coin + (2*i+1)*largeur_case_verticale/2))
coordonnees.append((longueur_coin/2, largeur_coin/2)) #case parc gratuit

for i in range(9): # ligne du haut
    coordonnees.append((longueur_coin + (2*i+1)*largeur_case_horizontale/2, (largeur_coin - zone_coloree_horizontale)/2))
coordonnees.append((taille_plateau - longueur_coin/2, largeur_coin/2)) # Case "allez en prison" 

for i in range(9): # Colonne de droite
    coordonnees.append((taille_plateau - (longueur_coin - zone_coloree_verticale)/2, largeur_coin + (2*i+1)*largeur_case_verticale/2))
coordonnees.append((longueur_coin - largeur_prison/2, taille_plateau - largeur_coin + hauteur_prison/2)) # Case ^prison (réel emprisonnement)


def placer_pion(x, y, id_joueur, pions):
    plateau.delete(pions[id_joueur - 1][0]) #on retire le pion précédent
    plateau.delete(pions[id_joueur - 1][1])
    pion = plateau.create_oval(x - rayon, y - rayon, x + rayon, y + rayon, fill = couleurs_pions[id_joueur - 1])
    if id_joueur == 4:
        fill = 'black'
    else:
        fill = 'white'
    texte = plateau.create_text(x, y, text = str(id_joueur), fill = fill)
    pions[id_joueur - 1] = (pion, texte)

### Ajout de l'affichage de l'argent en direct
_ = plateau.create_text(taille_plateau/2, largeur_coin *3/2, text = 'Argent restant par joueur :')
argent = []
for i in range(1, nb_joueurs + 1):
    text = plateau.create_text(taille_plateau/2, largeur_coin * 3/2 + i*taille_plateau/30, text = "Joueur n°" + str(i) + ": 1000€")
    argent.append(text)
###

def mise_a_jour(joueurs, monopoly, pions, coordonnees, argent, maisons, photo_maison, photo_hotel): # fonction pour mettre à jour la grille 
    # Mise à jour des pions
    for i in range(len(pions)):
        if i == 10:
            x, y = coordonnees[40]
        else:
            x, y = coordonnees[joueurs['position'][str(i+1)]]
        placer_pion(x, y, i+1, pions) #et on le replace au nouvel endroit
        # Mise à jour de l'affichage de l'argent
        plateau.delete(argent[i])
        text = plateau.create_text(taille_plateau/2, largeur_coin * 3/2 + (i+1)*taille_plateau/30, text = "Joueur n°" + str(i+1) + ": " + str(joueurs['argent'][str(i+1)]) + '€')
        argent[i] = text
    for i in range(1, 40):
        if i not in [2, 4, 5, 7, 10, 12, 15, 17, 20, 22, 25, 28, 30, 33, 35, 36, 38]: # les cases qui ne contiennent pas de maison
        # On efface les maisons précédentes 
            for k in range(len(maisons[i])):
                plateau.delete(maisons[i][k])
            maisons[i] = []
            nbr_maison = monopoly['maison'][monopoly['nom'][i]]
            if nbr_maison > 0:
                for _ in range(nbr_maison):
                    ajouter_maison(i, maisons, photo_maison, coordonnees)
                collisions_maisons(i, maisons, photo_maison, coordonnees, photo_hotel)
    ## Mise à jour des tableaux de bord
    clear_toplevels(liste_tableaux_bord)
    update_tableaux_bord(liste_tableaux_bord, nb_joueurs, joueurs, monopoly)



def plusieurs_pions_sur_meme_case(id_case, joueurs, pions):
    # On cherche les joueurs qui sont sur la même case
    ecart = taille_plateau / 60
    if id_case != 10:
        players_on_same_case = []
        for i in range(len(pions)):
            if joueurs['position'][str(i+1)] == id_case:
                players_on_same_case.append(i+1)
        nombre_joueurs = len(players_on_same_case)
        x, y = coordonnees[id_case]
        if nombre_joueurs == 1:
            return ()
        elif nombre_joueurs == 2:
            nouvelles_coordonnees = []
            nouvelles_coordonnees.append((x-ecart, y))
            nouvelles_coordonnees.append((x+ecart, y))
        elif nombre_joueurs == 3:
            nouvelles_coordonnees = []
            nouvelles_coordonnees.append((x-ecart, y-ecart))
            nouvelles_coordonnees.append((x+ecart, y-ecart))
            nouvelles_coordonnees.append((x, y+ecart))
        else:
            nouvelles_coordonnees = []
            nouvelles_coordonnees.append((x-ecart, y-ecart))
            nouvelles_coordonnees.append((x+ecart, y-ecart))
            nouvelles_coordonnees.append((x-ecart, y+ecart))
            nouvelles_coordonnees.append((x+ecart, y+ecart))
        for i in range(nombre_joueurs):
            a, b = nouvelles_coordonnees[i]
            placer_pion(a, b, players_on_same_case[i], pions)
    else:
        players_in_prison = []
        players_in_visit = []
        for i in range(len(pions)):
            if joueurs['position'][str(i+1)] == id_case:
                if joueurs['prison'][str(i+1)] > 0:
                    players_in_prison.append(i+1)
                else:
                    players_in_visit.append(i+1)
        nombre_prison = len(players_in_prison)
        nombre_visite = len(players_in_visit)
        nouvelles_coordonnees_prison = []
        nouvelles_coordonnees_visite = []
        # On implémente les coordonnées des 4 pions, même s'il y en a moins
        nouvelles_coordonnees_visite.append((ecart, taille_plateau - largeur_coin + ecart))
        nouvelles_coordonnees_visite.append((ecart, taille_plateau - largeur_coin + 3*ecart))
        nouvelles_coordonnees_visite.append((longueur_coin - largeur_prison + ecart, taille_plateau - ecart))
        nouvelles_coordonnees_visite.append((longueur_coin - largeur_prison + 3*ecart, taille_plateau - ecart))
        nouvelles_coordonnees_prison.append((longueur_coin - ecart, taille_plateau - largeur_coin + ecart))
        nouvelles_coordonnees_prison.append((longueur_coin - ecart, taille_plateau - largeur_coin + 3*ecart))
        nouvelles_coordonnees_prison.append((longueur_coin - 3*ecart, taille_plateau - largeur_coin + ecart))
        nouvelles_coordonnees_prison.append((longueur_coin - 3*ecart, taille_plateau - largeur_coin + 3*ecart))
        for i in range(nombre_visite):
            a, b = nouvelles_coordonnees_visite[i]
            placer_pion(a, b, players_in_visit[i], pions)
        for i in range(nombre_prison):
            a, b = nouvelles_coordonnees_prison[i]
            placer_pion(a, b, players_in_prison[i], pions)

f1.pack()
plateau.pack()

## Codage des maisons 

# Dictionnaire des maisons (chaque clé est l'indice de la case, la liste correspondante est la liste des images)
maisons = {}
for i in range(1, 40):
    if i not in [2, 4, 5, 7, 10, 12, 15, 17, 20, 22, 25, 28, 30, 33, 35, 36, 38]:
        maisons[i] = []

# Import de l'image 
rayon_maison = int(taille_plateau * 17/600)
maison = Image.open("maison.png")
maison = maison.resize((rayon_maison, rayon_maison), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(maison)

hotel = Image.open("hotel.png")
hotel = hotel.resize((rayon_maison, rayon_maison), Image.ANTIALIAS)
picture = ImageTk.PhotoImage(hotel)

def ajouter_maison(indice_case, maisons, photo_maison, coordonnees):
    if indice_case in maisons:
        x, y = coordonnees[indice_case]
        if 0 < indice_case < 10:
            maison = plateau.create_image(x, y - largeur_coin/2, image = photo_maison)
        elif 10 < indice_case < 20:
            maison = plateau.create_image(x + longueur_coin/2, y, image = photo_maison)
        elif 20 < indice_case < 30:
            maison = plateau.create_image(x, y + largeur_coin/2, image = photo_maison)
        else:
            maison = plateau.create_image(x - longueur_coin/2, y, image = photo_maison)
        maisons[indice_case].append(maison)

def collisions_maisons(indice_case, maisons, photo_maison, coordonnees, photo_hotel):
    n = len(maisons[indice_case]) # nombre de maisons sur la case
    if n > 1 and indice_case in maisons:
        for image in maisons[indice_case]:
            plateau.delete(image)
        x, y = coordonnees[indice_case]
        nouvelles_maisons = []
        if n <= 3: #on peut afficher les maisons côte à côte s'il n'y en pas trop
            if 0 < indice_case < 10:
                for i in range(1, n+1):
                    print("here !")
                    house = plateau.create_image(x - largeur_case_horizontale/2 + largeur_case_horizontale * i/(n+1), y - largeur_coin/2, image = photo_maison)
                    nouvelles_maisons.append(house)
            elif 10 < indice_case < 20:
                for i in range(1, n+1):
                    house = plateau.create_image(x + longueur_coin/2, y - largeur_case_verticale/2 + largeur_case_verticale * i/(n+1), image = photo_maison)
                    nouvelles_maisons.append(house)
            elif 20 < indice_case < 30:
                for i in range(1, n+1):
                    house = plateau.create_image(x - largeur_case_horizontale/2 + largeur_case_horizontale * i/(n+1), y + largeur_coin/2, image = photo_maison)
                    nouvelles_maisons.append(house)
            else:
                for i in range(1, n+1):
                    house = plateau.create_image(x - longueur_coin/2, y - largeur_case_verticale/2 + largeur_case_verticale * i/(n+1), image = photo_maison)
                    nouvelles_maisons.append(house)
            maisons[indice_case] = nouvelles_maisons
        elif n == 4: #s'il y en a 4 ou plus, on affiche le nombre
            if 0 < indice_case < 10:
                if indice_case < 5:
                    couleur = 'white'
                else:
                    couleur = 'black'
                house = plateau.create_image(x + taille_plateau* 7/600, y - largeur_coin/2, image = photo_maison)
                texte = plateau.create_text(x - taille_plateau* 7/600, y - largeur_coin/2, text = str(n), fill = couleur)
            elif 10 < indice_case < 20:
                house = plateau.create_image(x + longueur_coin/2, y + taille_plateau* 7/600, image = photo_maison)
                texte = plateau.create_text(x + longueur_coin/2, y - taille_plateau* 7/600, text = str(n), fill = 'white')
            elif 20 < indice_case < 30:
                if indice_case < 25:
                    couleur = 'white'
                else:
                    couleur = 'black'
                house = plateau.create_image(x + taille_plateau * 7/600, y + largeur_coin/2, image = photo_maison)
                texte = plateau.create_text(x - taille_plateau*7/600, y + largeur_coin/2, text = str(n), fill = couleur)
            else: 
                house = plateau.create_image(x -longueur_coin/2, y + taille_plateau*7/600, image = photo_maison)
                texte = plateau.create_text(x - longueur_coin/2, y - taille_plateau*7/600, text = str(n), fill = 'white')
            maisons[indice_case] = [house]*(n-1) + [texte] # pour que la longueur de la liste corresponde au nombre de maisons
        else:
            if 0 < indice_case < 10:
                hotel = plateau.create_image(x, y - largeur_coin/2, image = photo_hotel)
            elif 10 < indice_case < 20:
                hotel = plateau.create_image(x + longueur_coin/2, y, image = photo_hotel)
            elif 20 < indice_case < 30:
                hotel = plateau.create_image(x, y + largeur_coin/2, image = photo_hotel)
            else:
                hotel = plateau.create_image(x - longueur_coin/2, y, image = photo_hotel)
            maisons[indice_case] = [hotel]*n # pour que la longueur de la liste corresponde au nombre de maisons


### Implémentation des tableaux de bord 

def listes_proprietes(numero_joueur, monopoly, joueurs):
    # Retourne la liste des propriétés du joueur numero_joueur
    L=[]
    for l in monopoly['possédé']:
        if monopoly['possédé'][l] == numero_joueur :
            L.append(l)
    return L

def init_tableaux_bord(nb_joueurs, joueurs, monopoly): 
    # Ce programme crée les tableaux de bord (sous forme de Toplevel)
    liste_tableaux_bord=[0 for _ in range(nb_joueurs)]
    for i in range(nb_joueurs):
        liste_tableaux_bord[i] = tk.Toplevel(root, height=200, width=200, bg='#F0F0F0')
        liste_tableaux_bord[i].title(joueurs['nom'][str(i+1)])
    return liste_tableaux_bord


def clear_toplevels(liste_tableaux_bord): 
    # Ce programme vide tout les tableaux de bord afin de les re-remplir ensuite
    for i in range(len(liste_tableaux_bord)):
        list = liste_tableaux_bord[i].grid_slaves()
        for l in list:
            l.destroy()


def update_tableaux_bord(liste_tableaux_bord, nb_joueurs, joueurs, monopoly): 
    # Ce programme ajoute les informations du joueur à son tableau de bord
    label_nom = [0 for t in range(nb_joueurs)]
    label_argent = [0 for t in range(nb_joueurs)]
    label_libere_prison= [0 for t in range(nb_joueurs)]
    label_vouspossedez = [0 for t in range(nb_joueurs+1)]
    label_proprietes = [0 for t in range(nb_joueurs+1)]
    for i in range(nb_joueurs):
        label_nom[i]=tk.Label(liste_tableaux_bord[i], text=('Nom du joueur : '+joueurs['nom'][str(i+1)]))
        label_nom[i].grid(row=0)
        label_argent[i]=tk.Label(liste_tableaux_bord[i], text=('Argent du joueur : '+str(joueurs['argent'][str(i+1)])+' €'))
        label_argent[i].grid(row=1)
        label_libere_prison[i]=tk.Label(liste_tableaux_bord[i], text=('Vous avez '+str(joueurs['libere de prison'][str(i+1)])+' carte(s) "Libéré de prison".'))
        label_libere_prison[i].grid(row=2)
        proprietes=listes_proprietes(i+1, monopoly, joueurs)    #On stocke temporairement les propriétés du joueur ici, cette liste changera à la prochaine étape de la boucle for
        label_vouspossedez[i]=tk.Label(liste_tableaux_bord[i], text='Vous possédez les propriétés suivantes : ')
        label_vouspossedez[i].grid(row=3)
        label_proprietes[i]=[0 for t in range(len(proprietes))]
        for j in range(len(proprietes)):
            label_proprietes[i][j]=tk.Label(liste_tableaux_bord[i], text=proprietes[j])
            label_proprietes[i][j].grid(row=4+j)

            

if __name__ == "__main__":
    monopoly={'nom':{0:'APL', 1:'Ecsit', 2:'MyWay', 3:'Guilde', 4:'Loyer Césal', 5:'Cafet', 6:'PICS', 7:'MyWay', 8:'Hyris', 9:'ViaRezo', 10:'Visite', 11:'Commus', 12:'Accueil Assistance Réseau ViaRezo', 13:'Musics', 14:'BDA', 15:'RU Eiffel', 16 : 'NCV', 17:'MyWay', 18:'Raid', 19:'BDS', 20:'Clairière', 21:'SBCS', 22:'MyWay', 23:'ADR', 24:'BDE', 25:'RU Bréguet', 26:'Oser', 27:'CheerUp', 28:'Accueil Césal', 29:'Huma', 30:'TrouQuiPue', 31:'PAPS', 32:'FIR', 33:'MyWay', 34:'Impact', 35:'Musée', 36:'MyWay', 37:'JE', 38:'Tour des cotizs', 39:'LeForum'},
    'possédé':{'Ecsit':3, 'Guilde':1, 'Cafet':0, 'PICS':0, 'Hyris':4, 'ViaRezo':4, 'Commus':4, 'Accueil Assistance Réseau ViaRezo':2, 'Musics':0, 'BDA':0, 'RU Eiffel':0, 'NCV':0, 'Raid':0, 'BDS':0, 'SBCS':0, 'ADR':0, 'BDE':0, 'RU Bréguet':0, 'Oser':0, 'CheerUp':0, 'Accueil Césal':0, 'Huma':0, 'PAPS':0, 'FIR':0, 'Impact':0, 'Musée':0, 'JE':0, 'LeForum':0},
    'prix_achat':{'Ecsit':60, 'Guilde':60, 'Cafet':200, 'PICS':100, 'Hyris':100, 'ViaRezo':120, 'Commus':140, 'Accueil Assistance Réseau ViaRezo':150, 'Musics':140, 'BDA':160, 'RU Eiffel':200, 'NCV':180, 'Raid':180, 'BDS':200, 'SBCS':220, 'ADR':220, 'BDE':240, 'RU Bréguet':200, 'Oser':260, 'CheerUp':260, 'Accueil Césal':150, 'Huma':280, 'PAPS':300, 'FIR':300, 'Impact':320, 'Musée':200, 'JE':350, 'LeForum':500},
    'loyer':{'Ecsit':2, 'Guilde':4, 'PICS':6, 'Hyris':6, 'ViaRezo':8, 'Commus':10, 'Musics':10, 'BDA':12, 'NCV':14, 'Raid':14, 'BDS':16, 'SBCS':18, 'ADR':18, 'BDE':20, 'Oser':22, 'CheerUp':22, 'Huma':24, 'PAPS':26, 'FIR':26, 'Impact':28, 'JE':35, 'LeForum':50},
    'maison':{'Ecsit':0, 'Guilde':0, 'PICS':0, 'Hyris':0, 'ViaRezo':0, 'Commus':0, 'Musics':0, 'BDA':0, 'NCV':0, 'Raid':0, 'BDS':0, 'SBCS':0, 'ADR':0, 'BDE':0, 'Oser':0, 'CheerUp':0, 'Huma':0, 'PAPS':0, 'FIR':0, 'Impact':0, 'JE':0, 'LeForum':0}}
   
    joueurs = {'nom': {}, 'argent': {}, 'position': {}, 'prison': {}, 'libere de prison': {}, 'nombre de double': {}, 'dernier lancer dés': {}}
    joueurs['nom']['1']='J1'
    joueurs['nom']['2']='J2'
    joueurs['nom']['3']='J3'
    joueurs['nom']['4']='J4'
    joueurs['libere de prison']['3']=2
    joueurs['libere de prison']['4']=0
    for i in range(4):
        joueurs['nom'][str(i+1)]=input('Entrez le nom du joueur '+str(i+1)+' : ')
        joueurs['argent'][str(i+1)] = 1500
        joueurs['position'][str(i+1)] = 0
        joueurs['prison'][str(i+1)] = 0
        joueurs['libere de prison'][str(i+1)] = 0
        joueurs['nombre de double'][str(i+1)] = 0
        joueurs['dernier lancer dés'][str(i+1)] = 0
        

    liste_tableaux_bord = init_tableaux_bord(nb_joueurs, joueurs, monopoly)



    update_tableaux_bord(liste_tableaux_bord, nb_joueurs, joueurs, monopoly)
    clear_toplevels(liste_tableaux_bord)
    joueurs['nom']['1']='Je suis le joueur 1'
    update_tableaux_bord(liste_tableaux_bord,nb_joueurs,joueurs, monopoly)







# Test pour que 4 joueurs aillent sur la case 9, puis 10, puis 20, puis 40 (prison) consécutivement
    None
        


root.mainloop()