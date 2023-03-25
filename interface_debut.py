## Codage de l'interface de début du Monopoly 
from PIL import Image, ImageTk
import tkinter as tk
import tkinter.font as tkfont
from functools import partial

debut = tk.Tk()
debut.title("Ecran d'accueil")
debut.geometry("400x300")
f1 = tk.Frame(debut, bd = 0, bg = 'white', highlightthickness = 0)
debut.configure(bg = 'white')

conteneur_logo = tk.Canvas(f1, bd = 0, height = 120, width = 450, bg = 'white', highlightthickness = 0)

# Texte de bienveune
helvetica = tkfont.Font(family = 'Helvetica', size = 15, weight = 'bold')
conteneur_logo.create_text(200, 20, text = 'BIENVENUE AU JEU DU', font = helvetica)

# Logo du Monopoly
logo = Image.open("logo_monopoly_debut.jpg")
logo = logo.resize((300, 80), Image.ANTIALIAS)
image = ImageTk.PhotoImage(logo)
conteneur_logo.create_image(200, 70, image = image)

# Nombre de joueurs : 
texte = tk.Label(debut, text = "Nombre de joueurs", bg = 'white', bd = 0)
nbr_players = tk.StringVar()
echelle = tk.Scale(debut, orient='horizontal', from_ = 2, to = 4, resolution = 1, length = 100, variable = nbr_players, bg = 'white', highlightthickness = 0)
echelle.set(3)
nb_joueurs = int(nbr_players.get())

L = [] #contient les labels d'affichage des noms des joueurs 
i = 1

def valider(nbr_players, L, i):
    n = int(nbr_players.get())
    if n < len(L):
        for i in range(len(L) - 1, n - 1, -1):
            L[i].pack_forget()
            L.pop(-1)
        i = 1
    else:
        if len(L) < n:
            for i in range(len(L) + 1, n+1):
                label = tk.Label(debut, text = "Joueur n°" + str(i) + " : ", bg = 'white', highlightthickness = 0)
                label.pack()
                L.append(label)
            i = 1

# Bouton valider
Valider = tk.Button(debut, text = 'Valider', command = partial(valider, nbr_players, L, i))


# Nom des joueurs :
liste_des_noms = []
def enter_username(name, liste_des_noms):
    nom = name.get()
    if nom != '':
        echelle.configure(state = ['disabled'])




texte2 = tk.Label(debut, bd = 0, highlightthickness = 0)
name = tk.StringVar()
entree = tk.Entry(debut, textvariable = name, length = 100, command = partial(enter_username, liste_des_noms, i)
while i <= int(nbr_players.get()):
    texte2.configure(text = "Entrer le nom du joueur " + str(i))




# Affichage des noms des joueurs 


quitter = tk.Button(debut, text = "Quitter", command = debut.destroy)


f1.pack()
conteneur_logo.pack()
texte.pack()
echelle.pack()
Valider.pack()
debut.mainloop()