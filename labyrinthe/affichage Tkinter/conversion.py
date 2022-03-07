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


