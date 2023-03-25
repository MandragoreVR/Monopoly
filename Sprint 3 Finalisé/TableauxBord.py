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

#Afin d'implémenter les tableaux de bord dans le programme "Mise à jour" de l'interface graphique, il faut :
#Ajouter le programme listes_proprietes quelque part dans le programme représentation_plateau
#Ajouter les programmes init_tableaux_bord, clear_toplevels, update_tableaux_bord à représentation plateau.
#Créer une liste liste_tableaux_bord=init_tableaux_bord(nb_joueurs, joueurs, monopoly)
#Lui appliquer update_tableaux_bord (commande : update_tableaux_bord(liste_tableaux_bord, nb_joueurs, joueurs, monopoly)
#Dans le programme mise à jour, ajouter les deux lignes : clear_toplevels(liste_tableaux_bord) suivi de update_tableaux_bord(liste_tableaux_bord,nb_joueurs,joueurs, monopoly)
nb_joueurs = 4
taille_plateau = 600

import tkinter as tk
root = tk.Tk()
root.title('Monopoly')
f1 = tk.Frame(root, bd=1, relief='solid')
plateau = tk.Canvas(f1, bg = '#ECFCCC', height = taille_plateau, width = taille_plateau)

def listes_proprietes(numero_joueur, monopoly, joueurs):
    L=[]
    for l in monopoly['possédé']:
        if monopoly['possédé'][l]==numero_joueur :
            L.append(l)
    return (L)




def init_tableaux_bord(nb_joueurs, joueurs, monopoly): #Ce programme crée les tableaux de bord (sous forme de Toplevel)
    liste_tableaux_bord=[0 for t in range(nb_joueurs)]
    for i in range(nb_joueurs):
        liste_tableaux_bord[i] = tk.Toplevel(root, height=200, width=200, bg='#F0F0F0')
        liste_tableaux_bord[i].title(joueurs['nom'][str(i+1)])
    return liste_tableaux_bord



liste_tableaux_bord=init_tableaux_bord(nb_joueurs, joueurs, monopoly)



def clear_toplevels(liste_tableaux_bord): #Ce programme vide tout les tableaux de bord afin de les re-remplir ensuite
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

            





update_tableaux_bord(liste_tableaux_bord, nb_joueurs, joueurs, monopoly)
clear_toplevels(liste_tableaux_bord)
joueurs['nom']['1']='Je suis le joueur 1'
update_tableaux_bord(liste_tableaux_bord,nb_joueurs,joueurs, monopoly)



root.mainloop()