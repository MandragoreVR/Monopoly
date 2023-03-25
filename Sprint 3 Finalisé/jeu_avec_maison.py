# coding: utf-8
import random as rd
import tkinter as tk
from PIL import Image, ImageTk
import os
os.chdir("Images")

def joueurs_en_vie(nb_joueurs, joueurs):
    Liste_indice_joueurs_en_vie=[]
    for i in range(int(nb_joueurs)):
        if joueurs['argent'][str(i+1)]>=0:
            Liste_indice_joueurs_en_vie.append(i+1)
    return Liste_indice_joueurs_en_vie


def jouer_monopoly():
    monopoly={'nom':{0:'APL', 1:'Ecsit', 2:'MyWay', 3:'Guilde', 4:'Loyer Césal', 5:'Cafet', 6:'PICS', 7:'MyWay', 8:'Hyris', 9:'ViaRezo', 10:'Visite', 11:'Commus', 12:'Accueil Assistance Réseau ViaRezo', 13:'Musics', 14:'BDA', 15:'RU Eiffel', 16 : 'NCV', 17:'MyWay', 18:'Raid', 19:'BDS', 20:'Clairière', 21:'SBCS', 22:'MyWay', 23:'ADR', 24:'BDE', 25:'RU Bréguet', 26:'Oser', 27:'CheerUp', 28:'Accueil Césal', 29:'Huma', 30:'TrouQuiPue', 31:'PAPS', 32:'FIR', 33:'MyWay', 34:'Impact', 35:'Musée', 36:'MyWay', 37:'JE', 38:'Tour des cotizs', 39:'LeForum'},
    'possédé':{'Ecsit':0, 'Guilde':0, 'Cafet':0, 'PICS':0, 'Hyris':0, 'ViaRezo':0, 'Commus':0, 'Accueil Assistance Réseau ViaRezo':0, 'Musics':0, 'BDA':0, 'RU Eiffel':0, 'NCV':0, 'Raid':0, 'BDS':0, 'SBCS':0, 'ADR':0, 'BDE':0, 'RU Bréguet':0, 'Oser':0, 'CheerUp':0, 'Accueil Césal':0, 'Huma':0, 'PAPS':0, 'FIR':0, 'Impact':0, 'Musée':0, 'JE':0, 'LeForum':0},
    'prix_achat':{'Ecsit':60, 'Guilde':60, 'Cafet':200, 'PICS':100, 'Hyris':100, 'ViaRezo':120, 'Commus':140, 'Accueil Assistance Réseau ViaRezo':150, 'Musics':140, 'BDA':160, 'RU Eiffel':200, 'NCV':180, 'Raid':180, 'BDS':200, 'SBCS':220, 'ADR':220, 'BDE':240, 'RU Bréguet':200, 'Oser':260, 'CheerUp':260, 'Accueil Césal':150, 'Huma':280, 'PAPS':300, 'FIR':300, 'Impact':320, 'Musée':200, 'JE':350, 'LeForum':500},
    'loyer':{'Ecsit':2, 'Guilde':4, 'PICS':6, 'Hyris':6, 'ViaRezo':8, 'Commus':10, 'Musics':10, 'BDA':12, 'NCV':14, 'Raid':14, 'BDS':16, 'SBCS':18, 'ADR':18, 'BDE':20, 'Oser':22, 'CheerUp':22, 'Huma':24, 'PAPS':26, 'FIR':26, 'Impact':28, 'JE':35, 'LeForum':50},
    'maison':{'Ecsit':0, 'Guilde':0, 'PICS':0, 'Hyris':0, 'ViaRezo':0, 'Commus':0, 'Musics':0, 'BDA':0, 'NCV':0, 'Raid':0, 'BDS':0, 'SBCS':0, 'ADR':0, 'BDE':0, 'Oser':0, 'CheerUp':0, 'Huma':0, 'PAPS':0, 'FIR':0, 'Impact':0, 'JE':0, 'LeForum':0},
    'prix maison':{'Ecsit':50, 'Guilde':50, 'PICS':50, 'Hyris':50, 'ViaRezo':50, 'Commus':100, 'Musics':100, 'BDA':100, 'NCV':100, 'Raid':100, 'BDS':100, 'SBCS':150, 'ADR':150, 'BDE':150, 'Oser':150, 'CheerUp':150, 'Huma':150, 'PAPS':200, 'FIR':200, 'Impact':200, 'JE':200, 'LeForum':200}}
#Les cases ayant des loyers spéciaux (c'est à dire les gares et les compagnies) ne sont pas dans loyer car une fonction s'occupera de les calculer.

    cartes_chance = {
    1 : "Allez à la case APL.",
    2 : "Allez au local PICS.",
    3 : "Payez 200€ ou piochez une autre carte chance.",
    4 : "Reculez de trois cases.",
    5 : "Allez en prison, sans passer par la case APL.",
    6 : "Césal a prélevé trop d'argent sur votre dernier loyer, vous touchez 200€.",
    7 : "Vous êtes libérés de prison ! Cette carte peut être conservée.",
    8 : "Vous avez mis le feu à votre appartement, payez 200€ de réparations."
    }
    liste_cartes_chance=melanger_cartes_chance(cartes_chance)
    nb_joueurs=0
    while nb_joueurs !='2' and nb_joueurs != '3' and nb_joueurs != '4':
        nb_joueurs = input('Entrez le nombre de joueurs (entre 2 et 4 joueurs) : ')
    nb_joueurs=int(nb_joueurs)
    joueurs = {'nom':{},'argent':{},'position':{},'prison':{},'libere de prison':{},'nombre de double':{},'dernier lancer dés':{}}
    for i in range(nb_joueurs):             #On initialise le dictionnaire joueur pour tout les joueurs
        joueurs['nom'][str(i+1)]=input('Entrez le nom du joueur '+str(i+1)+' : ')
        joueurs['argent'][str(i+1)] = 1500
        joueurs['position'][str(i+1)] = 0
        joueurs['prison'][str(i+1)] = 0
        joueurs['libere de prison'][str(i+1)] = 0
        joueurs['nombre de double'][str(i+1)] = 0
        joueurs['dernier lancer dés'][str(i+1)] = 0
    input('Le joueur qui commence sera... (appuyez sur une touche pour lancer le choix) ')
    premier_joueur=rd.randint(1,nb_joueurs)
    print(joueurs['nom'][str(premier_joueur)] + ' ! \n')
    nb_tours=1
    ordre_joueurs=[] #Liste contenant l'ordre des joueurs, commence par le premier joueur
    for i in range(nb_joueurs):
        if premier_joueur+i>nb_joueurs:
            ordre_joueurs.append(premier_joueur+i-nb_joueurs)
        else:
            ordre_joueurs.append(premier_joueur+i)



    ######Insérer ici l'initialisation de l'interface graphique
    taille_plateau = 600
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
    f1 = tk.Frame(root, bd=1)
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

    _ = plateau.create_text(taille_plateau/2, largeur_coin *3/2, text = 'Argent restant par joueur :')
    argent = []
    for i in range(1, nb_joueurs + 1):
        text = plateau.create_text(taille_plateau/2, largeur_coin * 3/2 + i*taille_plateau/30, text = "Joueur n°" + str(i) + ": 1000€")
        argent.append(text)
    # Dictionnaire des maisons (chaque clé est l'indice de la case, la liste correspondante est la liste des images)
    maisons = {}
    for i in range(1, 40):
        if i not in [0, 2, 4, 5, 7, 10, 12, 15, 17, 20, 22, 25, 28, 30, 33, 35, 36, 38]:
            maisons[i] = []


    # Import de l'image 
    rayon_maison = int(taille_plateau * 17/600)
    maison = Image.open("maison.png")
    maison = maison.resize((rayon_maison, rayon_maison), Image.ANTIALIAS)
    photo_maison = ImageTk.PhotoImage(maison)

    hotel = Image.open("hotel.png")
    hotel = hotel.resize((rayon_maison, rayon_maison), Image.ANTIALIAS)
    photo_hotel = ImageTk.PhotoImage(hotel)


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


    def mise_a_jour(joueurs, monopoly, pions, coordonnees, argent, maisons, photo_maison, photo_hotel, liste_tableaux_bord): # fonction pour mettre à jour la grille 
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
        # Mise à jour des tableaux de bord
        clear_toplevels(liste_tableaux_bord)
        update_tableaux_bord(liste_tableaux_bord, nb_joueurs, joueurs, monopoly)

    def plusieurs_pions_sur_meme_case(id_case, joueurs, pions, coordonnees):
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

    # Implémentation des tableaux de bord
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

    liste_tableaux_bord = init_tableaux_bord(nb_joueurs, joueurs, monopoly)
    update_tableaux_bord(liste_tableaux_bord, nb_joueurs, joueurs, monopoly)







    f1.pack()
    plateau.pack()
    plusieurs_pions_sur_meme_case(0, joueurs, pions, coordonnees)
    





########################################################################### Partie clé du code de la fonction jouer_monopoly() (Boucle du jeu)


    while nb_tours<=40 and len(joueurs_en_vie(nb_joueurs,joueurs))>1:
        print('\nNous sommes au tour '+str(nb_tours) +'.')
        if nb_tours == 39:
            print("Attention, c'est l'avant-dernier tour !")
        if nb_tours == 40:
            print("Attention, c'est le dernier tour !")

        for numero_joueur in ordre_joueurs:
            rejouer=1
            while rejouer==1:
                print("\n C'est au tour de "+str(joueurs['nom'][str(numero_joueur)]))
                plusieurs_pions_sur_meme_case(joueurs['position'][str(numero_joueur)], joueurs, pions, coordonnees)
                if joueurs['prison'][str(numero_joueur)]==0:
                    print(joueurs['nom'][str(numero_joueur)] + ' lance le dé : (Appuie sur une touche pour lancer)')
                    input('')
                    position_avant_lancer=joueurs['position'][str(numero_joueur)]
                    [joueurs['dernier lancer dés'][str(numero_joueur)], rejouer] = lancer_de(numero_joueur, monopoly, joueurs, cartes_chance, liste_cartes_chance)
                    

                    mise_a_jour(joueurs, monopoly, pions, coordonnees, argent, maisons, photo_maison, photo_hotel, liste_tableaux_bord)
                    plusieurs_pions_sur_meme_case(position_avant_lancer, joueurs, pions, coordonnees)
                    plusieurs_pions_sur_meme_case(joueurs['position'][str(numero_joueur)], joueurs, pions, coordonnees)
                    position_apres_lancer=joueurs['position'][str(numero_joueur)]
                    arrivee(numero_joueur, joueurs, monopoly, cartes_chance, liste_cartes_chance)
                    plusieurs_pions_sur_meme_case(position_apres_lancer, joueurs, pions, coordonnees)
                    plusieurs_pions_sur_meme_case(joueurs['position'][str(numero_joueur)], joueurs, pions, coordonnees)
                    achat_maison(numero_joueur,joueurs,monopoly)
                    mise_a_jour(joueurs, monopoly, pions, coordonnees, argent, maisons, photo_maison, photo_hotel, liste_tableaux_bord)
                    plusieurs_pions_sur_meme_case(joueurs['position'][str(numero_joueur)], joueurs, pions, coordonnees)
                else :
                    mise_a_jour(joueurs, monopoly, pions, coordonnees, argent, maisons, photo_maison, photo_hotel, liste_tableaux_bord)
                    plusieurs_pions_sur_meme_case(position_avant_lancer, joueurs, pions, coordonnees)
                    plusieurs_pions_sur_meme_case(joueurs['position'][str(numero_joueur)], joueurs, pions, coordonnees)
                    rejouer=prison(numero_joueur, monopoly, joueurs, cartes_chance, liste_cartes_chance)
                    arrivee(numero_joueur, joueurs, monopoly, cartes_chance, liste_cartes_chance)
                    mise_a_jour(joueurs, monopoly, pions, coordonnees, argent, maisons, photo_maison, photo_hotel, liste_tableaux_bord)
                    plusieurs_pions_sur_meme_case(joueurs['position'][str(numero_joueur)], joueurs, pions, coordonnees)
            
        #Faire un appel pour vérifier les joueurs en vie ici
        nb_tours+=1

    root.mainloop()



########################################################################################################################################## Fin de la partie clé du code


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
            input("Appuyez sur la touche entrée pour continuer")


def melanger_cartes_chance(cartes_chance):
    # Renvoie une liste mélangée des cartes chance
    n = len(cartes_chance)
    L = [i for i in range(1, n+1)]
    cartes = []
    while len(L) >= 1:
        i = rd.randint(0, len(L) - 1)
        cartes.append(L.pop(i))
    return cartes



def piocher_carte_chance(monopoly, joueurs, id_joueur, liste_cartes_chance, cartes_chance):
    
    # La liste liste_ces_cartes_chance permet de représenter les cartes comme un paquet. Quand une carte est piochée,
    # retourne en bas du paquet
    position_actuelle = joueurs['position'][str(id_joueur)]
    id_carte =  liste_cartes_chance.pop(0)
    liste_cartes_chance.append(id_carte)
    print(cartes_chance[id_carte])
    if id_carte == 1:
        joueurs['position'][str(id_joueur)] = 0
        print("Vous touchez 400€ d'APL !")
        joueurs['argent'][str(id_joueur)] += 400
    elif id_carte == 2:
        joueurs['position'][str(id_joueur)] = 6 # En supposant que le Local ViaRézo soit la première des propriétés bleu clair
    elif id_carte == 3:
        choix=-1
        while choix!='0' and choix!='1':
            choix = input("Que choisissez-vous ? (0 = Payer 200€, 1 = Piocher une autre carte chance)")
        if int(choix) == 0:
            payer(200, id_joueur, monopoly, joueurs)
            print("Vous avez été débité de 200€")
        else:
            piocher_carte_chance(monopoly, joueurs, id_joueur, liste_cartes_chance, cartes_chance)
    elif id_carte == 4:
        joueurs['position'][str(id_joueur)] = (position_actuelle - 3) % 42
    elif id_carte == 5:
        print("Vous devez aller en prison")
        prison(id_joueur, monopoly, joueurs, cartes_chance, liste_cartes_chance)
    elif id_carte == 6:
        joueurs['argent'][str(id_joueur)] += 200
    elif id_carte == 7:
        joueurs['libere de prison'][str(id_joueur)] += 1
    else:
        payer(200, id_joueur, monopoly, joueurs)
    if joueurs['position'][str(id_joueur)] != position_actuelle: # si le joueur a changé de position
        arrivee(id_joueur, joueurs, monopoly, cartes_chance, liste_cartes_chance)



def lancer_de(ind_joueur,monopoly,joueurs, cartes_chance, liste_cartes_chance):                       #joueur est l'entier correspondant au numéro du joueur
    de_1=rd.randint(1,6)              # on lance le premier dé de 6
    de_2=rd.randint(1,6)            # on lance le deuxième dé de 6  
    print("Vous avez lancé", de_1,"et",de_2) 
    rejouer=0
    if de_1==de_2:
        joueurs['nombre de double'][str(ind_joueur)]+=1
        if joueurs['nombre de double'][str(ind_joueur)]==3:
            print("Vous avez fait 3 doubles consécutifs. Vous allez en prison :( !")
            joueurs['nombre de double'][str(ind_joueur)]=0
            prison(ind_joueur, monopoly, joueurs, cartes_chance, liste_cartes_chance)
               #pas de déplacement dû au troisième lancer
        else :   
            print("Vous avez fait un double. Vous pourrez rejouer.")
            rejouer=1

    nb_de_cases=de_1+de_2
    print('Le joueur ',ind_joueur,'avance de ', nb_de_cases,'cases.')
    placement=joueurs['position'][str(ind_joueur)]
    placement+=nb_de_cases

    if placement>39:             
        placement=placement-40                #pour repartir sur le bon numéro de case si c'est supérieur à 7
        print("Vous touchez 200 euros d'APL :) ")
        joueurs['argent'][str(ind_joueur)]+=200
        print ("Vous avez actuellement",joueurs['argent'][str(ind_joueur)],"euros.")


    joueurs['position'][str(ind_joueur)]=placement
    print('Le joueur ',ind_joueur,'est sur la case',placement,'.' )              #monopoly['nom'][placement]
    
    return [de_1+de_2, rejouer]





def prison(ind_joueur,monopoly,joueurs, cartes_chance, liste_cartes_chance):

    joueurs['prison'][str(ind_joueur)]+=1
    if joueurs['prison'][str(ind_joueur)] == 3:
        print("Cela fait 3 tours que vous êtes en prison, vous êtes libéré après avoir payé votre caution")
        joueurs['argent'][str(ind_joueur)]-=50
        joueurs['prison'][str(ind_joueur)] = 0
        return 1 #1 signifie qu'il a le droit de jouer, 0 signifie qu'il n'a pas la droit de jouer
    if joueurs['prison'][str(ind_joueur)] == 1:
        joueurs['position'][str(ind_joueur)]=10 
        print("Vous êtes arrivés en prison !")    
    nbr_carte_libere = joueurs['libere de prison'][str(ind_joueur)]
    ##carte sortir de prison
    if nbr_carte_libere == 0:
        print("Vous n'avez pas de cartes pour vous libérer de prison.")
    else:
        print("Vous avez",nbr_carte_libere,"carte(s) 'Vous êtes libéré de prison'")
        utilise = input("Voulez-vous utiliser une carte ? (1 si oui, 2 si non) ")
        if utilise == '1':
            print("Vous avez utilisé une carte.")
            print("Vous êtes libéré de prison !")
            joueurs['prison'][str(ind_joueur)] = 0            ## libéré : joue normalement   
            joueurs['libere de prison'][str(ind_joueur)] -= 1
            return 1
        else :
            print("Vous n'avez pas utilisé de carte.")


    ## payer pour sortir
    res=input("Voulez-vous payez 50 euros pour sortir de prison ? 1 si oui, 2 si non \n")
    if res=='1':
        joueurs['argent'][str(ind_joueur)]-=50
        #argent_centre_du jeu+=50                           ## coder l'argent au milieu du jeu
        print("Vous avez payé 50 euros pour sortir.")
        print("Vous êtes libéré de prison !")
        joueurs['prison'][str(ind_joueur)]=0                ## libéré joue normalement
        return 1
    ## lancer les dés pour essayer de faire un double    
    else :
        print("Vous n'avez pas payé.")
        _ = input("Vous allez lancer deux dés pour tenter de faire un double (appuyez sur entrée pour continuer)")
        de_1=rd.randint(1,6)              # on lance le premier dé de 6
        de_2=rd.randint(1,6)
        if de_1==de_2:              ## double effectué
            print("Vous avez fait ", de_1, " et ", de_2)
            print("Vous avez fait un double, vous pouvez sortir de prison.")
            joueurs['prison'][str(ind_joueur)]=0

            nb_de_cases=de_1+de_2
            joueurs['nombre de double'][str(ind_joueur)]+=1
            joueurs['dernier lancer dés']=nb_de_cases
            print('Le joueur ',ind_joueur,'avance de ', nb_de_cases,'cases.')
            joueurs['position'][str(ind_joueur)] += nb_de_cases
            print('Le joueur ',ind_joueur,'est sur la case',joueurs['position'][str(ind_joueur)],'.' )      #monopoly['nom'][placement]
            arrivee(ind_joueur, joueurs, monopoly, cartes_chance, liste_cartes_chance)
        else:                                        
            print("Vous avez fait",de_1, "et", de_2,". Vous n'avez pas fait de double. Vous restez en prison.")
            print("Cela fait",joueurs['prison'][str(ind_joueur)],"tour(s) que vous êtes en prison.")
            return 0




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



def payer(montant, numero_joueur, monopoly, joueurs):
    if joueurs['argent'][str(numero_joueur)]>= montant:
        joueurs['argent'][str(numero_joueur)]-=montant
    else :
        dette=montant-joueurs['argent'][str(numero_joueur)]
        joueurs['argent'][str(numero_joueur)]=0
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
                    if monopoly['maison'][l]!=0 :
                        print(l + " posséde " + str(monopoly['maison'][l]) + " maisons qui peuvent se vendre chacune à " + str(int(monopoly['prix maison'][l]*0.8)) + ".")
                txt  = input("Voulez vous revendre des améliorations ou vos propriétés ? dites améliorations ou propriétés : ")
                if txt == 'améliorations':
                    choix = input("Entrez le nom du bien où vous souhaitez revendre les améliorations.")
                    nombre= input("Entrez le nombre d'améliorations que vous souhaitez vendre.")
                    nombre=int(nombre)      
                    if choix in L and monopoly['maison'][choix] != 0 and nombre in range(0, monopoly['maison'][choix]+1):
                        restant-=int(monopoly['prix maison'][choix]*0.8*nombre)
                        monopoly['maison'][choix]-=nombre                                                                        #les améliorations que le joueur revend, disparaissent et l'argent réduit la dette
                
                elif txt == 'propriétés' :
                    choix = input("Entrez le nom du bien que vous souhaitez vendre.")      
                    if choix in L :
                        if monopoly['maison'][choix]!=0:
                            print("Vous vendez également les maisons qui lui sont associées.")
                            restant-=int(monopoly['maison'][choix]*monopoly['prix maison'][choix]*0.8)
                            monopoly['maison'][choix]=0
                        restant-=int(monopoly['prix_achat'][choix]*0.9)
                        monopoly['possédé'][choix]=0
                        L.remove(choix)                                                                                    #les propriétés que le joueur revend, retournent à la banque et peuvent être rachetées et les maisons dessus sont vendues. l'argent réduit la dette
            joueurs['argent'][str(numero_joueur)]+=(-1)*restant
            print("Votre dette est remboursée, l'argent restant de la vente est ajouté à votre compte.")
        else :
            print("Il vous est impossible de rembourser votre dette.")                                               #si le joueur n'avait pas un capital suffisant, toutes ses possessions sont revendues et il finit dans le négatif
            for l in L :
                monopoly['possédé'][l]=0
                monopoly['maison'][l]=0
            joueurs['argent'][str(numero_joueur)]=somme-dette # une valeur négative d'argent implique une défaite




#############################################################################################################





def arrivee(indice_joueur, joueurs, monopoly, cartes_chance, liste_cartes_chance):
    indice_case=joueurs['position'][str(indice_joueur)]
    N=monopoly['nom'][indice_case] #on appelle N le nom du lieu sur lequel arrive le joueur
    if N == 'APL':
        print('Vous êtes sur la case APL')
        _ = input('Appuyez sur entrée pour continuer')
    elif N == 'MyWay':
        print('Vous tirez une carte chance')
        piocher_carte_chance(monopoly, joueurs, indice_joueur, liste_cartes_chance, cartes_chance)
    elif N== 'Loyer Césal':
        print("Césal est venu réclamer votre loyer, payez 200.")
        payer(200, indice_joueur, monopoly, joueurs)
    elif N== 'Tour des cotizs':
        print("Le tour des cotizs vous a ruiné ! Payez 100.")
        payer(100, indice_joueur, monopoly, joueurs)
    elif N=='Clairière':
        print("Vous êtes à la clairière.")
    elif N=='Visite':
        print('Vous visitez ceux qui ont eu le malheur de tomber dans le trou.')
    elif N=='TrouQuiPue':
        prison(indice_joueur,monopoly,joueurs, cartes_chance, liste_cartes_chance)
    else :
        if monopoly['possédé'][N] != indice_joueur:        #si le joueur ne possède pas le lieu soit il l'achète soit il paie un loyer
            print('Cette propriété ne vous appartient pas')
            if monopoly['possédé'][N] == 0:
                achat(indice_joueur, monopoly, joueurs)
            else:
                print('Vous devez payer un loyer')
                loyer_ter(monopoly, joueurs, joueurs['position'][str(indice_joueur)], indice_joueur)
                _ = input('Vous avez été débité. Appuyez sur la touche entrée pour continuer')
        else:
            print('Vous êtes chez vous !')
            _ = input("Appuyez sur entrée pour continuer")







#################################################################################################################



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
                if monopoly['maison'][l]!=0 :
                    print(l + " posséde " + str(monopoly['maison'][l]) + " maisons qui peuvent se vendre chacune à " + str(int(monopoly['prix maison'][l]*0.8)) + ".")
            txt  = input("Voulez vous revendre des améliorations ou vos propriétés ? dites améliorations ou propriétés : ")
            if txt == 'améliorations':
                choix = input("Entrez le nom du bien où vous souhaitez revendre les améliorations.")
                nombre= input("Entrez le nombre d'améliorations que vous souhaitez vendre.")
                nombre=int(nombre)      
                if choix in L and monopoly['maison'][choix] != 0 and nombre in range(0, monopoly['maison'][choix]+1):
                    restant-=int(monopoly['prix maison'][choix]*0.8*nombre)
                    monopoly['maison'][choix]-=nombre                                                                        #les améliorations que le joueur revend, disparaissent et l'argent réduit la dette
            
            elif txt == 'propriétés' :
                choix = input("Entrez le nom du bien que vous souhaitez vendre.")      
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






###########################################################################################################""






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
 





################################################################################################################


if __name__ == "__main__":
    jouer_monopoly()