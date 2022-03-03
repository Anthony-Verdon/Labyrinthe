import random          
     
def calcul(a):#calcul le nombre de 0 en fonction de la longueur du labyrinthe
    return a**2-(a**2-2*(a//2+1)*a+((a//2+1)**2)+2)

def Labyrinthe():

    labyrinthe=[]

    longueurLabyrinthe=25#longueur donne par l'utilisateur
    longueurLabyrinthe=longueurLabyrinthe//2*2+1#on passe la longueur sur un chiffre impair pour pas de murs avec 2 epaisseurs en bas et à droite
    nombre=[x for x in range(2,calcul(longueurLabyrinthe)+2)]
    random.shuffle(nombre)
    z=0
    
    assert longueurLabyrinthe>=2,"veuillez saisir une valeur plus grande"#sinon c'est juste un carré de 2x2 donc sans entree ni sortie
    for x in range(0,longueurLabyrinthe):#on remplit le tableau de tableaux
        labyrinthe.append([])
        for y in range(0,longueurLabyrinthe):
            if x%2==0 or x==longueurLabyrinthe-1 or y%2==0 or y==longueurLabyrinthe-1:#pour les murs, pour faire un grillage
                labyrinthe[x].append(1)
            else:
                labyrinthe[x].append(nombre[z])#longueurLabyrinthe**2//2 #pour le reste on remplit avec des nombres au pif
                z+=1
     
    labyrinthe[1][0]=labyrinthe[1][1]#entree
    labyrinthe[longueurLabyrinthe-2][longueurLabyrinthe-1]=labyrinthe[longueurLabyrinthe-2][longueurLabyrinthe-2]#sortie
    
    z=0
    while z!=2*calcul(longueurLabyrinthe):
        z+=1
        ouvertureMur(labyrinthe,longueurLabyrinthe)
        
    z=0
    while z<2/100*calcul(longueurLabyrinthe):
        z+=1
        cassageMur(labyrinthe,longueurLabyrinthe)
        
    return labyrinthe

def ouvertureMur(labyrinthe,longueurLabyrinthe):
        x=random.randint(1,longueurLabyrinthe-2)#on prend un mur au pif
        
        if x%2==0:
            y=random.randint(1,longueurLabyrinthe-2)//2*2+1
        else:
            y=random.randint(2,longueurLabyrinthe-3)//2*2
        
        if labyrinthe[x][y]==1:
            if x%2==0:
                if labyrinthe[x-1][y]!=labyrinthe[x+1][y]:
                    if labyrinthe[x-1][y]<labyrinthe[x+1][y]:
                        
                        labyrinthe[x][y]=labyrinthe[x+1][y]
                        variableTemporaire=labyrinthe[x-1][y]
                        for i in range(0,longueurLabyrinthe):
                            for j in range (0,longueurLabyrinthe):
                                if labyrinthe[i][j]==variableTemporaire:
                                    labyrinthe[i][j]=labyrinthe[x+1][y]
                    else:
                        labyrinthe[x][y]=labyrinthe[x-1][y]
                        variableTemporaire=labyrinthe[x+1][y]
                        for i in range(0,longueurLabyrinthe):
                            for j in range (0,longueurLabyrinthe):
                                if labyrinthe[i][j]==variableTemporaire:
                                    labyrinthe[i][j]=labyrinthe[x-1][y]
    
            else:
                if labyrinthe[x][y-1]!=labyrinthe[x][y+1]:
                    if labyrinthe[x][y-1]<labyrinthe[x][y+1]:
                        
                        labyrinthe[x][y]=labyrinthe[x][y+1]
                        variableTemporaire=labyrinthe[x][y-1]
                        for i in range(0,longueurLabyrinthe):
                            for j in range (0,longueurLabyrinthe):
                                if labyrinthe[i][j]==variableTemporaire:
                                    labyrinthe[i][j]=labyrinthe[x][y+1]
                    else:
                        labyrinthe[x][y]=labyrinthe[x][y-1]
                        variableTemporaire=labyrinthe[x][y+1]
                        for i in range(0,longueurLabyrinthe):
                            for j in range (0,longueurLabyrinthe):
                                if labyrinthe[i][j]==variableTemporaire:
                                    labyrinthe[i][j]=labyrinthe[x][y-1]
        return labyrinthe
    
def cassageMur(labyrinthe,longueurLabyrinthe):
        x=random.randint(1,longueurLabyrinthe-2)#on prend un mur au pif
        
        if x%2==0:
            y=random.randint(1,longueurLabyrinthe-2)//2*2+1
        else:
            y=random.randint(2,longueurLabyrinthe-3)//2*2
        
        if labyrinthe[x][y]==1:
            
            if x%2==0:
                labyrinthe[x][y]=labyrinthe[x+1][y]
    
            else:
                labyrinthe[x][y]=labyrinthe[x][y+1]
    
        return labyrinthe#pour l'affichage dans tkinter

