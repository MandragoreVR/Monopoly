## Renvoie les joueurs en vie, c'est-à-dire ceux qui ne sont pas en négatif

def joueurs_en_vie(nb_joueurs, joueurs):
    Liste_indice_joueurs_en_vie=[]
    for i in range(int(nb_joueurs)):
        if joueurs['argent'][str(i+1)]>=0:
            Liste_indice_joueurs_en_vie.append(i+1)
    return Liste_indice_joueurs_en_vie