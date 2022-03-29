import random          
     
def calcul(a):#calcul le nombre de 0 en fonction de la longueur du labyrinthe
    return a**2-(a**2-2*(a//2+1)*a+((a//2+1)**2)+2)

def Labyrinthe(longueurLabyrinthe):
    
    
    labyrinthe=[]
    #longueur donne par l'utilisateur
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
    
    return labyrinthe

