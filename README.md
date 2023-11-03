# Introduction 
![Preview](https://raw.githubusercontent.com/phil1057/nhl_simulator/main/img/main_menu/icon-nhl-logo.png?token=GHSAT0AAAAAACJ2KYZBV4LR77DY2JZ6IFGEZKFAXXQ)

## Vision du projet

Le projet va simuler en temps accéléré des matchs entre deux équipes de la Ligue nationale de hockey. Il y aura possibilité de contrôler une équipe, les deux équipes ou simplement regarder le match. Possiblement, il y aura un mode directeur général, qui simulera la saison au complet et gardera les statistiques des joueurs et des équipes. Les équipes qui seront intégrées dans le jeu seront les équipes qui font partie de la division Atlantique de la Ligue nationale de hockey, les équipes seront listées :

* Boston Bruins
* Buffalo Sabres
* Detroit Red Wings
* Florida Panthers
* Montreal Canadiens
* Ottawa Senators
* Tampa Bay Lightning
* Toronto Maple Leafs

## Comment le jeu va fonctionner

Le projet de jeu de simulation de match de hockey va se baser sur les évaluations des joueurs du jeu EA SPORTS NHL23 pour simuler les matches. Plus l’évaluation d’un joueur sur la glace est haute, plus de chances l’équipe à d’être plus efficace. 

### Système d'évaluation

Les évaluations vont se baser sur l’attaque et la défense, l’attaque va augmenter les probabilités d’une équipe à marquer et la défense va réduire les probabilités de l’autre équipe à marquer un but. La cote sera un nombre qui détermine le talent d’un joueur de 0 à 100, cent était le joueur le plus talentueux.

## Développement

Le projet sera développé avec le langage de programmation Python et une interface graphique avec Tkinter et les extensions de Pygubu en XML. Les variables et les classes utiliseront la nomenclature camel case et les fichiers auront la nomenclature snake case.

## Cas principal

Le strict minimum pour ce projet est de faire un programme qui simule un match entre deux équipes de la division Atlantique de la Ligue Nationale de Hockey. Avoir une base de données avec les joueurs des équipes et leur cote de joueur.

### Diagramme de séquences

![Diagramme Sequences](https://raw.githubusercontent.com/phil1057/nhl_simulator/main/img/seqdiagram.png?token=GHSAT0AAAAAACJ2KYZABG4BZ3CJLPNARKZ4ZKFA2GQ)

### Glossaire

Le glossaire est disponible en PDF [ici](https://github.com/phil1057/nhl_simulator/blob/main/Glossaire.pdf).

# Maquettes

## Simulation de matchs

![sim](https://raw.githubusercontent.com/phil1057/nhl_simulator/main/img/game.png?token=GHSAT0AAAAAACJ2KYZB7W3DBMXREPHV4WRSZKFA2TQ)

La maquette représente une maquette de la simulation d’un match. Le gardien de but sur la glace, les joueurs sur la glace et les joueurs sur le banc sont représentés avec des statistiques sur le match en cours. Si un but est marqué, une alerte apparait avec le marqueur du but et les assistances s’ils ont lieu sur la patinoire ou les actions fictives ont lieu. La partie évènements est un résumé des actions récentes. Si une pénalité a lieu, elle sera affichée du côté de l’équipe qui est en avantage numérique. Le contrôle d’une équipe se fait à partir des flèches de tempo de l’équipe. Il sera possible de contrôler une équipe, les deux ou aucune des deux. 

![Strats](https://raw.githubusercontent.com/phil1057/nhl_simulator/main/img/strats.png?token=GHSAT0AAAAAACJ2KYZBAE45NVOTSHEM5SW2ZKFA3DA)

Le tempo très défensif va augmenter de +2 la cote défensive de tous les joueurs et baisser la cote offensive de -2, le tempo défensif va augmenter de +1 la cote défensive des joueurs et modifier de -1 la cote offensive. Le tempo neutre ne modifiera pas la cote. Le même principe s’applique pour les tempos offensifs qui boosteront la cote offensive de +1 et baissera la cote défensive de -1 et le tempo très offensif va modifier la cote offensive de +1 et la cote défensive de -1.

## Menu principal
![MainMenu](https://raw.githubusercontent.com/phil1057/nhl_simulator/main/img/mainmenu.png?token=GHSAT0AAAAAACJ2KYZAVGZMR5D26QZXFN7UZKFAOMA)

Lors de l’ouverture du jeu, le menu principal sera la première page présentée. Elle dirigera l’utilisateur ou il souhaite aller, soit dans un match immédiat, fonctionnalité qui permet de simuler un match avec les équipes que l’utilisateur choisira. Ou le mode Directeur général ou l’utilisateur pourra joueur une saison avec une équipe de son choix.

## Match immédiat

![QuickGame](https://raw.githubusercontent.com/phil1057/nhl_simulator/main/img/quickgame.png?token=GHSAT0AAAAAACJ2KYZBPOGNWMW4N2GZO6TGZKFASEA)

La carte du match immédiat permet de sélectionner dans les équipes sélectionnées deux équipes qui vont s’affronter pour seulement une partie sans garder les statistiques qui sont utiles pour la saison régulière.

## Diagramme de classes
![ClassDiagram](https://raw.githubusercontent.com/phil1057/nhl_simulator/main/img/classdiagram.png?token=GHSAT0AAAAAACJ2KYZBVLS7DOYUNTFWDP2EZKFATAQ)

# User Stories

## Faire un match immédiat

L’objectif du match immédiat est de simuler un match avec les équipes sélectionnées sans passer par la création d’une saison pour simuler un match entre deux équipes sélectionnées.

Précondition : L’utilisateur est dans le mode de jeu « Match immédiat » et dans l’onglet

1.	L’utilisateur sélectionne l’équipe qui va jouer à l’étranger.
2.	L’utilisateur sélectionne l’équipe qui va jouer à domicile.
3.	L’utilisateur sélectionne quelle équipe il veut contrôler.
4.	L’utilisateur clique le bouton Confirmer et le match entre les deux équipes démarre.

## Match (Gameplay)

Précondition : Un match est débuté dans le mode « Match immédiat » et une équipe peux être contrôlée. 

1.	Un joueur peut contrôler la stratégie de l’équipe ou des équipes sélectionnées.
2.	Il peut choisir entre les stratégies « Très défensif », « Défensif », « Neutre », « Offensif » et « Très offensif ».
