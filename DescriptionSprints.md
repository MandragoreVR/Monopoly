# Monopoly – Equipe 9

Ce fichier contient le détail de l'ensemble des sprints, en explicitant les tâches effectuées. Pour chaque tâche, un Référent s'est porté volontaire pour mener la tâche à bien (il est bien entendu aidé par les autres si nécessaires et n'a pas à faire la tâche tout seul s'il a besoin de plus de personnes).

## Sprint 1 

**Sprint 1** : Objectif : Construction d’un MVP : jeu de monopoly sur un carré 3 par 3 (8 cases), à 2 joueurs, chacun a son stock d’argent, et peut acheter des propriétés. Une fois qu’une propriété est achetée, elle est achetée et ne peut être revendue. Si un joueur tombe sur une case qui lui appartient, rien ne se passe, sinon il doit payer au propriétaire le loyer si la case a un propriétaire ou il peut l’acheter si la case n’a pas de propriétaire. Les joueurs lancent un dé 3 pour jouer. Les joueurs gagnent de l’argent à chaque fois qu’ils passent par la case APL. Si un joueur a un compte négatif il est éliminé, sinon, si au bout de 30 tours la partie n’est pas finie, le jeu se termine et le joueur avec le plus de sous gagne. Les joueurs commencent avec 1000€, et passer par la case APL rapporte 200€.


*Comment le construit-on concrètement ?*
-Liste des propriétés gérée par un dictionnaire qui contient un dictionnaire pour le nom, le propriétaire (0 : signifie que la propriété n’est pas acheté, sinon c’est l’indice du joueur qui la possède (joueur 1, joueur 2…)), le prix d’achat et le loyer.
-Pour les joueurs, on les gère aussi avec un dictionnaire contenant le nom du joueur, sa somme d’argent, sa position sur le plateau.



Tâches : 

-**Interface graphique** (version console). Doit afficher les dictionnaires en temps réels sous forme d’interface graphique.

*Référent* : Cyprien

*Etat* : Fini

*Résultat* : Après avoir compilé le code contenu dans InterfaceConsole.py, entrer affichage(monopoly, joueurs) pour obtenir l'affichage.


-**Achat de propriété** : lorsqu’un joueur tombe sur une propriété, la commande achat(indice de la propriété, indice du joueur) affiche le nom, le prix de la propriété, et lui propose de l’acheter, auquel cas le joueur est débité et la propriété lui appartient.

*Référent* : Eglantine

*Etat* : Fini

*Résultat* : Après avoir compilé le code contenu dans achat.py, entrer achat(indice_joueur, monopoly, joueurs) pour que le joueur indice_joueur achète la propriété sur laquelle il se trouve et soit débité du montant équivalent.


-**Paiement de loyer** : si un joueur tombe sur une propriété possédée par un autre joueur, la commande loyer(indice de la propriété, indice du joueur) doit débiter le joueur qui tombe dessus et créditer celui qui la possède.

*Référent* : Téo

*Etat* : Fini

*Résultat* : Après avoir compilé le code contenu dans loyer.py, l'appel loyer(monopoly, joueur, indice_prop, indice_joueur) débite le joueur indice_joueur et créditer le propriétaire du terrain sur lequel il se trouve.


-**Déplacement sur le plateau**: une fonction prenant en paramètre indice_joueur doit lui faire lancer le dé, le déplacer d’autant de cases, lui ajouter de l’argent s’il est passé par la case APL au cours de son déplacement et lui dire sur quelle case il se trouve.

*Référent* : Thomas

*Etat* : Fini

*Résultat* : Après avoir compilé le code contenu dans deplacements.py, l'appel lancer_de(indice_joueur, monopoly, joueur) fait lancer le dé au joueur, modifie sa position et lui affiche ce qu'il s'est passé au cours du lancer.


-**Gestion des arrivées du joueur sur une case** : la fonction arrivee(indice joueur, indice case) doit le renvoyer vers la fonction nécessaire (soit achat, soit loyer).

*Référent* : Louis

*Etat* : Fini

*Résultat* : Après avoir compilé le code contenu dans gestion_arrivee.py, l'appel arrivee(indice_joueur, joueurs, monopoly) déclenche les effets de la case surlequel le joueur est tombé.


-**Faire jouer le joueur** : le programme play_monopoly() fait tourner le jeu en réunissant tous les programmes précédents.

*Référent* : Hugo

*Etat* : Fini

*Résultat* : Après avoir compilé le code contenu dans faire_jouer_les_joueurs.py, l'appel play_monopoly() lance une partie. Un screenshot du résultat est visible sur le README.



**Etat du Sprint 1** : Fini.

*Quelles sont les priorités pour le sprint 2 ?* Après quelques parties faites avec le MVP, le manque d'interface graphique plus travaillé se fait ressentir. En outre, la grille est vraiment petite et sa taille limite assez vite l'intêret des parties.

## Sprint 2


**Sprint 2** : Objectif : Monopoly plus proche du jeu réel avec interface graphique, le plateau 11*11, la vente de propriétés, les cartes chances et caisse de communauté qui seront pour l'instant regroupées uniquement en cartes chance (5 cartes différentes)


Tâches:

-**Obtenir une interface graphique faite à l'aide de tkinter d'un plateau 11*11** : Pouvoir afficher la grille à l'aide de tkinter et gérer le déplacement des pions sur le plateau.

*Référent* : Téo

*Etat* : Fini

*Résultat* : Initialisation et affichage de la grille disponible dans le programme representation_plateau.py et dans le programme final JeuAvecGraphismes.py. Création des fonctions placer_pion pour placer un pion, mise_a_jour pour mettre à jour l'affichage graphique au vu de l'avancement du jeu après une action d'un joueur (par exemple, son déplacement) et plusieurs_pions_sur_meme_case permettant d'obtenir un affichage propre de plusieurs pions se trouvant sur une seule case. Ces fonctions sont visibles dans representation_plateau.py.


-**Remplir l'interface graphique** : Après avoir construit le squelette de l'interface, il s'agit de la remplir les noms des propriétés, des images...

*Référent* : Louis

*Etat* : Fini

*Résultat* : Ajout de texte sur toutes les cases du plateau, ainsi que d'images sur le plateau pour le rendre plus joli, visible dans le programme representation_plateau.py et JeuAvecGraphismes.py.


-**Définir les dictionnaires sur le même modèle que ce que l'on utilise jusqu'ici** : sachant que le nombre de joueurs peut désormais aller de 2 à 4 joueurs et qu'il faut ajouter beaucoup de nouvelles propriétés, il va falloir renouveler le dictionnaire.

*Référent* : Hugo

*Etat* : Fini

*Résultat* : Création d'un nouveau dictionnaire appelé monopoly présent dans le fichier dictionnaire_11_cases.py.


-**Implémentation des cartes chances** : Certaines des cases du Monopoly sont des cases "chance", ayant des effets pouvant être positifs ou négatifs pour le jouer. Il s'agit de coder ces cartes.

*Référent* : Téo

*Etat* : Fini

*Résultat* : Création du fichier cartes_chance.py permettant de gérer ces cartes chances, contenant un dictionnaire cartes_chances stockant l'ensemble des cartes chance, une fonction melanger_cartes_chance pour mélanger ce paquet, et une fonction piocher_carte_chance afin de piocher et déclencher l'effet écrit sur une carte chance.


-**Vente de propriétés** : Si un joueur est en faillite (i.e il possède une somme d'argent négatif), il doit pouvoir vendre ses propriétés (pour un prix fixé inférieur au prix d'achat initial) afin de retourner s'il le peut à un montant d'argent positif.

*Référent* : Eglantine

*Etat* : Fini

*Résultat* : Le fichier revente.py gère la revente des propriétés contre de l'argent en montrant au joueur la liste de ces propriétés avec la fonction listes_proprietes et en lui permettant de revendre une/des propriétés choisies avec la fonction revendre. Le fichier payer.py permet à un joueur de payer un montant en appelant la fonction revente pour gérer le cas où son total d'argent devient négatif.


-**Adaptation de la fonction deplacement.py au plateau 11*11** : Le programme utilisé précedemment pour gérer les déplacements sur le plateau 3 par 3 ne convient plus, la fonction doit être modifiée pour s'adapter au nouveau plateau et au lancer de deux dés 6. Le lancer de 3 doubles de suite doit aussi conduire le joueur en prison.

*Référent* : Thomas

*Etat* : Fini

*Résultat* : Le fichier deplacement_plateau_11.py contient une fonction lancer_de mise à jour afin de se déplacer sur la nouveau plateau, de faire rejouer un joueur en cas de double, et envoyant en prison un joueur qui fait de 3 doubles à la suite.


-**Ajout de la prison** : la case "Prison" située en bas à gauche du plateau de Monopoly nécessite une fonction afin de gérer l'emprisonnement des joueurs, et leur libération vers la case simple visite (qui peut se faire soit à l'aide d'une carte "Vous êtes libéré de prison", soit en payant la caution, soit en tirant un double pour essayer d'en sortir).

*Référent* : Thomas

*Etat* : Fini

*Résultat* : le fichier deplacements_plateau_11.py contient une fonction prison gérant s'occupant de l'emprisonnement d'un joueur et sa libération. Ajout dans le dictionnaire joueurs de deux clés 'prison' (valant 0 si le joueur n'est pas en prison, 1 si c'est son premier tour en prison, 2 pour le deuxième, 3 pour le troisième) et 'libere de prison' (stockant le nombre de cartes chance libéré de prison que chaque joueur possède).


-**Mise à jour de la fonction loyer pour gérer les gares et les compagnies** : Dans le jeu Monopoly, le loyer des gares et des compagnies varie selon le nombre de propriétés de ce genre que le joueur possède, et, dans le cas des compagnies, de son dernier résultat au dé. Il est donc impossible de stocker un loyer fixe dans le dictionnaire monopoly pour ces cases. Il s'agit donc de mettre à jour la fonction loyer pour prendre en compte le loyer variable de ces cases.

*Référent* : Eglantine

*Etat* : Fini

*Résultat* : Le fichier loyer_bis.py reprend la fonction loyer, mais dispose désormais aussi des fonctions loyer_RU afin de calculer le loyer des gares (symbolisées sur le plateau par des restaurants universitaires), et loyer_accueil afin de calculer le loyer des compagnies (symbolisées sur le plateau par des accueils). Le dictionnaire joueur s'est vu ajouté une clé 'dernier lancer dés' permettant de stocker la valeur du dernier lancer de dés d'un joueur.


-**Obtention d'une version fonctionnelle du jeu à l'aide de tout les programmes précedents** : Les divers programmes codés nous ont pour but d'améliorer le jeu par rapport au sprint 1, mais il faut les assembler en un seul fichier et les rendre compatibles les uns les autres.

*Référent* : Cyprien

*Etat* : Fini

*Résultat* : Le fichier JeuAvecGraphismes.py contient une fonction jouer_monopoly permettant au joueur de jouer au jeu avec toutes les améliorations qui y ont été faites au cours du sprint. Un screenshot du résultat est visible sur le README.



**Etat du Sprint 2** : Fini.

*Quelles sont les priorités pour le sprint 2 ?* L'interface graphique est beaucoup plus confortable qu'à la fin du sprint 1, mais il reste encore du travail pour que les joueurs puissent facilement voir les informations qui les concernent : quels propriétés leur appartiennent ? quel est leur pion sur le plateau ? En outre, les maisons sont un composant caractéristique du Monopoly, il semble donc pertinent de les ajouter dans une optique de se rapprocher d'un jeu plus en phase avec le vrai Monopoly, et plus intéressant.


## Sprint 3 

**Sprint 3** : Objectif : Ajout de maisons et d'hôtels sur le jeu, ajout de tableaux de bord pour chaque joueur. Commenter et tester les programmes du MVP. Améliorer le README.

Tâches : 

-**Obtenir un programme gérant l'achat et la revente de maisons et d'hôtels** : lorsqu'un joueur possède toutes les propriétés d'une même couleur, il peut alors acheter des maisons ou hôtels sur ces propriétés quand il se trouve sur l'une d'entre elles.

*Référent* : Hugo

*Etat* : Fini

*Résultat* : Le fichier fonction_maison.py contient une fonction achat_maison.py indiquant au joueur sur quelles propriétés il peut acheter des maisons lorsque c'est son tour. Si le joueur tombe sur l'une de ces propriétés, le jeu lui propose d'acheter des maisons, avec un maximum de 5 maisons sur une case simultanément (5 maisons correspondent à un hôtel). Si le joueur en achète, le programme lui indique alors le nouveau loyer de la propriété.


-**Décorer le plateau avec quelques images** : Afin d'habiller le plateau, nous souhaiterions rajouter quelques images sur le plateau.

*Référent* : Louis

*Etat* : Fini

*Résultat* : Ajout d'un logo ViaRézo sur l'accueil ViaRézo, d'un symbole euro sur les cases de taxe, et d'un symbole de fourchette et couteau sur les RU.


-**Ajouter sur l'interface graphique les maisons en les hôtels** : L'ajout de maisons et d'hôtels doit aller de pair avec leur affichage sur le plateau.

*Référent* : Téo

*Etat* : Fini

*Résultat* : Le fichier representation_plateau_v3.py contient désormais les fonctions ajouter_maison (place une maison sur le plateau) et collision_maison (s'occupe de placer plusieurs maisons sur une même case, ou de les remplacer par un hôtel s'il y en a 5) afin de gérer l'affichage des maisons sur le plateau.


-**Ajout de tableaux de bord graphiques contenant les informations de chaque joueur en temps réel** : Afin de pouvoir donner au joueurs ses informations à tout moment, il semble pertinent d'ajouter pour chacun d'entre eux des tableaux de bord réunissant les informations qui le concernent.

*Référent* : Cyprien

*Etat* : Fini

*Résultat* : Le fichier representation_plateau_v3.py contient désormais les fonctions init_tableaux_bord (créant une liste de Toplevel permettant d'afficher les tableaux de bord), update_tableaux_bord (remplissant les tableaux de bord avec toutes les informations du joueur) et clear_toplevels (afin d'effacer le contenu des tableaux de bord pour les remplir ensuite avec les informations plus récentes). Ajout dans le programme mise_a_jour de lignes pour effacer le contenu puis le remplir à nouveau afin de le mettre à jour.


-**Obtenir un programme qui réunit tout les sous-programmes et permet de jouer avec toutes ces nouveautés** : Il s'agit de réunir tout les programmes effectués en un seul programme fonctionnel.

*Référent* : Eglantine

*Etat* : Fini

*Résultat* : Le fichier jeu_avec_maison.py nous permet de jouer à l'aide de la fonction jouer_monopoly() en l'éxecutant (en entrant par exemple dans le terminal bash : `python jeu_avec_maison.py`) ou en compilant le fichier. 


-**Amélioration du README.md pour le rendre clair autant que possible, expliquer le fonctionnement du MVP et du programme avec interface graphique à l'issue des sprints, préciser les requirements** : Le README a besoin d'être mis à jour au vu du travail effectué au cours des derniers sprints. Il s'agit donc d'ajouter tout ce qui lui manque.

*Référent* : Cyprien

*Etat* : Fini

*Résultat* : Le README a été mis à jour. Une vidéo de démonstration a été tournée et montée, et son lien est disponible sur le README.

-**Commenter et tester ses programmes** : Certains programmes manquent un peu de clarté, et il faudrait ajouter des fonctions de test à chacun de ces programmes.

*Référent* : Thomas

*Etat* : Fini (MVP)

*Résultat* : Couverture de test complète pour le MVP. Quelques programmes de test sont disponibles pour la version du Sprint 2.



**Etat du Sprint 3** : Fini

*Remarques à l'issue du Sprint 3* : A l'issue de ce sprint, il nous reste assez peu de temps pour coder de nouvelles fonctionnalités. Nous avons donc décidé de nous focaliser sur la clarté de nos codes existants, les programmes de test, la propreté du repo Gitlab, du README et de DescriptionSprints.


-**Préparer un Powerpoint de présentation du projet** : Afin de préparer notre soutenance, il est nécessaire de faire des slides Powerpoint pour notre présentation. Cette tâche ne nécessite pas de référent, étant donné que tout les membres du groupe y participent à peu près autant les uns les autres.

## Sprint 4

**Sprint 4** : Objectif : Jouer au jeu entièrement depuis l'interface graphique et plus du tout depuis la console


-**Créer une interface intéractive sur tkinter pour choisir le nombre de joueurs**, et faire tout les choix du jeu / afficher toutes les informations depuis une interface graphique et non la console.

*Référent* : Téo

*Etat* : Non commencé (NB : Comme l'indique la remarque du Sprint 3, nous n'avons pas souhaité concrétiser ce sprint par manque de temps)



-**Obtenir un programme qui incorpore cette interface intéractive au jeu final** : Le jeu se joue actuellement sur la console, il faut donc modifier le programme principal pour pouvoir jeu purement depuis l'interface graphique.

*Référent* : Cyprien

*Etat* : Non commencé (NB : Comme l'indique la remarque du Sprint 3, nous n'avons pas souhaité concrétiser ce sprint par manque de temps)


