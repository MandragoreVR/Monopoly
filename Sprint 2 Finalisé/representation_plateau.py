import tkinter as tk
from PIL import Image, ImageTk
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
_ = plateau.create_text(longueur_coin/2,largeur_coin/3, text='Clairière\nBouygues')
 
# Case "Allez en prison"
_ = plateau.create_text(taille_plateau - longueur_coin/2, largeur_coin/2, text = "    Allez\n      au\nTroukipu")

# Cases des propriétés
 
_ = plateau.create_text(taille_plateau-longueur_coin-largeur_case_horizontale/2 , taille_plateau-largeur_coin/2,  text = "Ecsit")
_ = plateau.create_text(taille_plateau-longueur_coin-largeur_case_horizontale-largeur_case_horizontale/2, taille_plateau-largeur_coin/2,  text = "MyWay\n     ?")
_ = plateau.create_text(taille_plateau-longueur_coin-largeur_case_horizontale/2-2*largeur_case_horizontale , taille_plateau-largeur_coin/2,  text = "Guilde")
_ = plateau.create_text(taille_plateau-longueur_coin-largeur_case_horizontale/2-3*largeur_case_horizontale , taille_plateau-largeur_coin/2,  text = "Loyer \n Césal")
_ = plateau.create_text(taille_plateau-longueur_coin-largeur_case_horizontale/2-4*largeur_case_horizontale , taille_plateau-largeur_coin/2,  text = "Cafet")
_ = plateau.create_text(taille_plateau-longueur_coin-largeur_case_horizontale/2-5*largeur_case_horizontale , taille_plateau-largeur_coin/2,  text = "PICS")
_ = plateau.create_text(taille_plateau-longueur_coin-largeur_case_horizontale/2-6*largeur_case_horizontale , taille_plateau-largeur_coin/2,  text = "MyWay\n     ?")
_ = plateau.create_text(taille_plateau-longueur_coin-largeur_case_horizontale/2-7*largeur_case_horizontale , taille_plateau-largeur_coin/2,  text = "Hyris")
_ = plateau.create_text(taille_plateau-longueur_coin-largeur_case_horizontale/2-8*largeur_case_horizontale , taille_plateau-largeur_coin/2,  text = "ViaRezo")
 
_ = plateau.create_text(2*longueur_coin/5, taille_plateau-largeur_coin-largeur_case_verticale/2, text = "Commus ")
_ = plateau.create_text(longueur_coin/2,taille_plateau-largeur_coin-largeur_case_verticale-largeur_case_verticale/2, text = " Accueil\n ViaRezo")
_ = plateau.create_text(2*longueur_coin/5,taille_plateau-largeur_coin-2*largeur_case_verticale-largeur_case_verticale/2, text = " Musics")
_ = plateau.create_text(longueur_coin/2,taille_plateau-largeur_coin-3*largeur_case_verticale-largeur_case_verticale/2, text = "BDA")
_ = plateau.create_text(longueur_coin/2,taille_plateau-largeur_coin-4*largeur_case_verticale-largeur_case_verticale/2, text = "RU Eiffel")
_ = plateau.create_text(longueur_coin/2,taille_plateau-largeur_coin-5*largeur_case_verticale-largeur_case_verticale/2, text = "NCV")
_ = plateau.create_text(longueur_coin/2,taille_plateau-largeur_coin-6*largeur_case_verticale-largeur_case_verticale/2, text = "MyWay\n     ?")
_ = plateau.create_text(longueur_coin/2,taille_plateau-largeur_coin-7*largeur_case_verticale-largeur_case_verticale/2, text = "Raid")
_ = plateau.create_text(longueur_coin/2,taille_plateau-largeur_coin-8*largeur_case_verticale-largeur_case_verticale/2, text = "BDS")

_ = plateau.create_text(longueur_coin+ 0* largeur_case_horizontale+largeur_case_horizontale/2,largeur_coin/2, text='SBCS')
_ = plateau.create_text(longueur_coin+ 1* largeur_case_horizontale+largeur_case_horizontale/2,largeur_coin/2, text='MyWay\n     ?')
_ = plateau.create_text(longueur_coin+ 2* largeur_case_horizontale+largeur_case_horizontale/2,largeur_coin/2, text='ADR')
_ = plateau.create_text(longueur_coin+ 3* largeur_case_horizontale+largeur_case_horizontale/2,largeur_coin/2, text='BDE')
_ = plateau.create_text(longueur_coin+ 4* largeur_case_horizontale+largeur_case_horizontale/2,largeur_coin/2, text='RU')
_ = plateau.create_text(longueur_coin+ 4* largeur_case_horizontale+largeur_case_horizontale/2,largeur_coin/2, text='\n \n Bréguet')
_ = plateau.create_text(longueur_coin+ 5* largeur_case_horizontale+largeur_case_horizontale/2,largeur_coin/2, text='Oser')
_ = plateau.create_text(longueur_coin+ 6* largeur_case_horizontale+largeur_case_horizontale/2,largeur_coin/2, text='CheerUp')
_ = plateau.create_text(longueur_coin+ 7* largeur_case_horizontale+largeur_case_horizontale/2,largeur_coin/3, text='Accueil' )
_ = plateau.create_text(longueur_coin+ 8* largeur_case_horizontale+largeur_case_horizontale/2,largeur_coin/2, text='Huma')
 
_ = plateau.create_text(taille_plateau - longueur_coin/2, largeur_coin+ largeur_case_verticale/2, text = "PAPS")
_ = plateau.create_text(taille_plateau - longueur_coin/2, largeur_coin+ largeur_case_verticale/2+largeur_case_verticale, text = "FIR")
_ = plateau.create_text(taille_plateau - longueur_coin/2, largeur_coin+ largeur_case_verticale/2+2*largeur_case_verticale, text = "MyWay\n     ?")
_ = plateau.create_text(taille_plateau - longueur_coin/2, largeur_coin+ largeur_case_verticale/2+3*largeur_case_verticale, text = "  Impact")
_ = plateau.create_text(taille_plateau - longueur_coin/2, largeur_coin+ largeur_case_verticale/2+4*largeur_case_verticale, text = "Musée")
_ = plateau.create_text(taille_plateau - longueur_coin/2, largeur_coin+ largeur_case_verticale/2+5*largeur_case_verticale, text = "MyWay\n     ?")
_ = plateau.create_text(taille_plateau - longueur_coin/2, largeur_coin+ largeur_case_verticale/2+6*largeur_case_verticale, text = "JE")
_ = plateau.create_text(taille_plateau - longueur_coin/2, largeur_coin+ largeur_case_verticale/2+7*largeur_case_verticale, text = "   Tour\ndes cotizs")
_ = plateau.create_text(taille_plateau - longueur_coin/2, largeur_coin+ largeur_case_verticale/2+8*largeur_case_verticale, text = " Forum")

# insertion des points d'interrogation sur les cases chance (MyWay)
image= Image.open("ptinterrogation.png")
 
image = image.resize((int(taille_plateau*1/30), int(taille_plateau*1/30)), Image.ANTIALIAS)
 
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
 
_ = plateau.create_image(longueur_coin+ 7* largeur_case_horizontale+largeur_case_horizontale/2,largeur_coin/2+largeur_case_verticale/4, image=pointss)

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

def mise_a_jour(joueurs, pions, coordonnees, argent): #fonction pour mettre à jouer la grille 
    for i in range(len(pions)):
        if i == 10:
            x, y = coordonnees[40]
        else:
            x, y = coordonnees[joueurs['position'][str(i+1)]]
        placer_pion(x, y, i+1, pions) #et on le replace au nouvel endroit
        ### Lignes à rajouter dans la fonction principale pour l'argent en direct 
        plateau.delete(argent[i])
        text = plateau.create_text(taille_plateau/2, largeur_coin * 3/2 + (i+1)*taille_plateau/30, text = "Joueur n°" + str(i+1) + ": " + str(joueurs['argent'][str(i+1)]) + '€')
        argent[i] = text
        ###

joueurs={'nom':{}, 'argent':{'1': 1000, '2': 1000, '3': 1000, '4': 1000}, 'position':{'1':0, '2':0, '3':0, '4':0}, 'prison':{'1': 0, '2':0, '3':0, '4':0},'libere de prison':{'1':1,'2':0},
 'nombre de double':{'1':0,'2':0}}


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


# Test pour que 4 joueurs aillent sur la case 9, puis 10, puis 20, puis 40 (prison) consécutivement
if __name__ == "__main__":
    plusieurs_pions_sur_meme_case(0, joueurs, pions)
    _ = input(",")
    for i in range(nb_joueurs):
        joueurs['position'][str(i+1)] = 10
        mise_a_jour(joueurs, pions, coordonnees, argent)
        plusieurs_pions_sur_meme_case(10, joueurs, pions)
        plusieurs_pions_sur_meme_case(0, joueurs, pions)
        _ = input(",")
    for i in range(nb_joueurs):
        joueurs['prison'][str(i+1)] = 1
        mise_a_jour(joueurs, pions, coordonnees, argent)
        plusieurs_pions_sur_meme_case(10, joueurs, pions)
        _ = input(",")


root.mainloop()