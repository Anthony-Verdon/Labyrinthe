import random
import conversion

def couleur(a):#on prend notre nombre
    
    a=list(str(a))#on le met en str puis en list
    if len(a)<9:
        while len(a)<9:#on rajoute des 0 avant le nombre pour qu'il soit sur 9 chiffres
            a.insert(0,"0")
    
    random.shuffle(a)#on mélange et on associe 3  chiffres aux 3 variables RGB
    R=int(a[0]+a[1]+a[2])
    G=int(a[3]+a[4]+a[5])
    B=int(a[6]+a[7]+a[8])
    
    
    if R>255:#si il est supérieur à 255(valeur max), on additionne les 2 premiers nombres et ça donne les 2 nouveaux chiffres du début du nombre
        R=list(str(R))
        VarTemporaire=int(R[0])+int(R[1])
        if VarTemporaire<10:
            VarTemporaire=list(str(VarTemporaire))
            VarTemporaire.insert(0,'0')
            VarTemporaire = ''.join(str(elem)for elem in VarTemporaire)
        VarTemporaire=list(str(VarTemporaire))
        R[0]=str(VarTemporaire[0])
        R[1]=str(VarTemporaire[1])
        R[2]=str(R[2])
        R=int(R[0]+R[1]+R[2])

    if G>255:
        G=list(str(G))
        VarTemporaire=int(G[0])+int(G[1])
        if VarTemporaire<10:
            VarTemporaire=list(str(VarTemporaire))
            VarTemporaire.insert(0,'0')
            VarTemporaire = ''.join(str(elem)for elem in VarTemporaire)
        VarTemporaire=list(str(VarTemporaire))
        G[0]=str(VarTemporaire[0])
        G[1]=str(VarTemporaire[1])
        G[2]=str(G[2])
        G=int(G[0]+G[1]+G[2])
        
    if B>255:
        B=list(str(B))
        VarTemporaire=int(B[0])+int(B[1])
        if VarTemporaire<10:
            VarTemporaire=list(str(VarTemporaire))
            VarTemporaire.insert(0,'0')
            VarTemporaire = ''.join(str(elem)for elem in VarTemporaire)
        VarTemporaire=list(str(VarTemporaire))
        B[0]=str(VarTemporaire[0])
        B[1]=str(VarTemporaire[1])
        B[2]=str(B[2])
        B=int(B[0]+B[1]+B[2])
    
    
    R=list(conversion.convertisseur(R))
    G=list(conversion.convertisseur(G))
    B=list(conversion.convertisseur(B))
    
    while len(R)!=2:
        R.insert(0,'0')  
    R = ''.join(str(elem)for elem in R)
    
    while len(G)!=2:
        G.insert(0,'0')
    G = ''.join(str(elem)for elem in G)
    
    while len(B)!=2:
        B.insert(0,'0')
    B = ''.join(str(elem)for elem in B)
    
    codeHexa=R+G+B
    return "#"+codeHexa.upper()

