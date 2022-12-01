
#Importation de modules
import csv

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

        liste2=[]


        # Supresion de lignes sans type
        for ligne in liste:
            if ligne[3] == '\n' :
                test=0
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
                    val2 = float(ligne[2].replace("-","0"))
                else : 
                    val2 = float(ligne[2].replace(",","."))
                    val1 = float(ligne[1].replace(",","."))
                    val3 = val1 + val2
                    ligne.insert(3, str(val3))
            count1 += 1
  
        #Suppression des collonee an1 e an2
        for ligne in liste2:
            ligne.pop(1)
            ligne.pop(1)
            print(ligne)
            
        return liste2

def sort_csv(liste1):
    print()


def write_csv(liste1):
    
    with open('conso-clean.csv', 'w') as f:
        write = csv.writer(f)
        write.writerows(liste1)


#Program pprincipal

#Appel de la fonction 
list1 = clean_csv()

#Affichage ligne par ligne
# for ligne in list1:
#     print(ligne)

#Ecrire  dans un fichier csv
write = write_csv(list1)



  





