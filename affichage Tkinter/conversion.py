def convertisseur(nombreAconvertir):
    
    """
    Cette fonction permet de convertir de base 10 en n'importe qu'elle base.
    Si le nombre de base n'est pas en base 10, alors une autre fonction se charge de le transformer.
    -----------------
    paramètre : 
        nombreAconvertir : un int 
        baseDuNombre : un int 
        baseVoulu : un int
    -----------------
    renvoie le nombre initial, puis ce qu'il donne dans une autre base
    """
    
    resultat=[]
    nombre=nombreAconvertir
    
    while nombre!=0:
        if nombre%16>=10:
            if nombre%16==10:
                resultat.append("a")
            elif nombre%16==11:
                resultat.append("b")
            elif nombre%16==12:
                resultat.append("c")
            elif nombre%16==13:
                resultat.append("d")
            elif nombre%16==14:
                resultat.append("e")
            elif nombre%16==15:
                resultat.append("f")
        else:
            resultat.append(nombre%16)
        nombre=nombre//16
    
    resultat.reverse()
    reponse = ''.join(str(elem)for elem in resultat)#permet de transformer la liste en texte compact
    
    return reponse


def decimal (nombreAconvertir,baseDuNombre):
    
    """
    ce programme permet de convertir un nombre de n'importe qu'elle base en base 10. 
    Si vous utilisez une base supérieur à  la base 10,
    mettez des "" lorsque vous écrivez le nombre à convertir.
    -----------------
    paramètre : 
        nombreAconvertir : un int 
        baseDuNombre : un int 
    -----------------
    renvoie le nombre initial et sa base, et sa valeur en base 10
    """
    
    compteur=x=puissance=résultat=0
    nombreCaractère=len(str(nombreAconvertir))#compte le nombre de caractère du nombre
    liste=list(str(nombreAconvertir))#transforme un nombre compact en liste
    liste.reverse()#inverse les valeurs de la liste
    
    if baseDuNombre>10:
        while compteur!=nombreCaractère:
            if liste[x].lower()=="a":
                liste[x]=10
            elif liste[x].lower()=="b":
                liste[x]=11
            elif liste[x].lower()=="c":
                liste[x]=12
            elif liste[x].lower()=="d":
                liste[x]=13
            elif liste[x].lower()=="e":
                liste[x]=14
            elif str(liste[x]).lower()=="f":
                liste[x]=15
            compteur=compteur+1
            x=x+1

    compteur=x=0
    
    while compteur!=nombreCaractère:
        résultat=résultat+int(liste[x])*baseDuNombre**puissance
        compteur=compteur+1
        x=x+1
        puissance=puissance+1
    return résultat