
#Importation de modules
import csv
import operator

#Definition de fonctions 

#Fonction qui nettoie le fichier csv
def clean_csv():

    #Overture du fichier csv
    with open('conso-annuelles_v1.csv', 'r') as csvfile :

        count = 0
        liste=[]
        # Suppresion de toutes les lignes avec au moins une cellule vide
        for ligne in csvfile:
            x = ligne.split(";")
            #Si la ligne ne contien pas de celule vide on la garde dans la liste
            if not '' in x :
                liste.append(x)
                count += 1
            #Dans le cas contraire on les suprime
            else :
                count += 1
                x.clear()

        # Supression de la colonne ID logement
        num = 0
        for ligne in liste:
            num += 1
            ligne.pop(1)

        #Supresion de lignes sans type
        liste2=[]
        count2 = 0
        for ligne in liste:
            if ligne[3] == '\n' :
                count2 += 1
            else :
                liste2.append(ligne)
                  
        # Addition des consommation sur les deux années 
        count1 = 0
        count3 = 0

        for ligne in liste2 :

            #Insertion de la colonne dans le tableau
            if count3 == 0 :
                ligne.insert(3,  'consommation sur les deux années' )
                count3 += 1
            
            #insertion et adittion de la consommation des 2 annes 
            if count1 > 0 :
                
                if ligne[2] == '-':
                    ligne.insert(3, float(5033.1))
               
                elif count > 0 : 
                    val1 = float(ligne[1].replace(",","."))
                    val2 = float(ligne[2].replace(",","."))
                    val3 = val1 + val2
                    ligne.insert(3, float(val3))
            count1 += 1
  
        #Suppression des collonee an1 e an2
        for ligne in liste2:
            ligne.pop(1)
            ligne.pop(1)
            
        return liste2

# Fonction qui Regroupe par type et par consomation par ordre decroissant

def sort_csv(liste1):

# Rangemrnt des valeurs 
    liste2 = sorted(liste1, key=operator.itemgetter(0))

    #Declaration des liste
    liste3 = []

    #insertion du titre
    liste3.append(liste2[0])

    #Declaration des compteurs
    count = 0
    k=2
    g = 1
    
    # Regroupement par type et par consomation par ordre decroissant

    while count < 556 :
        if count > 0 and k < 556 :
            
            if liste2[g][0] == liste2[k][0] and liste2[g][2] == liste2[k][2]:
                temp = liste2[g]
                liste3.append(temp)

            else :

                temp = liste2[g]
                liste3.append(temp)

            k += 1
            g += 1

        count += 1

    liste3.append(liste2[555])

    return liste3
   
# Function qui ecrit dans un fichier csv

def write_csv(liste1):

    with open('conso-clean.csv', 'w') as f:
         write = csv.writer(f)
         write.writerows(liste1)

#Program pprincipal

#Appel de la fonction qui nettoie le fichier csv
clean = clean_csv()

# Appel de la onction qui Regroupe par type et par consomation par ordre decroissant
organize = sort_csv(clean)

#Ecrire  dans un fichier csv
write = write_csv(organize)



  





