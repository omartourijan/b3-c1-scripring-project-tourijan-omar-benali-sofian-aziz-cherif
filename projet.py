#overture d'un fichier CSV...
#... creation de la liste de lignes nommée tableau...
#... et affiche des lignes.

import csv
with open('conso-annuelles_v1.csv',newline='')as f:                    #Overture du fichier CSV
    tableau=[]
    lire=csv.reader(f)                                      #chargement des lignes du fichier csv
    print('Affichage des lignes de tableau',end='\n')
    for ligne in lire:                                      #Pour chaque ligne...
        print(ligne, end='\n')                              #...affiche de la ligne dans la console 
        tableau.append(ligne)                               #...on ajoute la ligne dans la liste
                                                            #...de liste nomée tableau
