import time
import tkinter
from PIL import ImageTk, Image
from labyrintheCreation import Labyrinthe
from couleur import couleur
import random

#classe menu, se charge de la page menu
class Menu:
    
    #créer nos différents objets ( boutons ou frame contenant d'autres objets )
    def __init__(self):
        
        self.menu=tkinter.Tk()#créer la fenêtre
        self.frameBouton=tkinter.Frame(bg="#EB9F1B")#créer la frame bouton
        self.frameImage=tkinter.Frame(bg="#EB9F1B")#créer la frame image
        self.frameInput=tkinter.Frame(bg="#EB9F1B")#créer la frame Input
        
        self.boutonTab1=tkinter.Button(self.frameBouton,text="lancer U",font=("Kokonor",20),bg="#EB9F1B",command=self.Commande1)#créer le 1er bouton " lancer U "
        self.boutonQuitter=tkinter.Button(self.menu,text="quitter",font=("Kokonor",20),bg="#EB9F1B",command=self.quitter)#créer le 4ème bouton " Quitter "
        self.boutonInput=tkinter.Button(self.frameInput,text="envoyer les informations",font=("Kokonor",20),bg="#EB9F1B",command=self.InputUtilisateur)#créer le 5ème bouton " envoyer les informations
        
    #se charge de faire apparaître et de placer les images, boutons  et entrées de texte
    def lancerMenu(self):
        self.menu.title("Jeu de la Vie")#ajoute un titre à la fenêtre
        self.menu.geometry("1920x1080")#donne les dimensions de la fenêtre
        self.menu.iconbitmap("logo.ico")#ajoute une icône à la fenêtre
        self.menu.minsize(1920,1080)#donne une taille minimale à la fenêtre
        self.menu.config(background="#EB9F1B")#change la couleur de fond de la fenêtre
        
        img1 = ImageTk.PhotoImage(Image.open("Uresized.jpg"))#importe l'image 
        panel1 = tkinter.Label(self.frameImage, image = img1)#créer un label à partir de l'image et la place dans la frame image
        panel1.pack(side="left",padx=10)#affiche le label en la collant à gauche de la frame et en lui ajoutant une marge externe à droite et à gauche
        
        img4 = ImageTk.PhotoImage(Image.open("PointInterrogation.png"))
        panel4 = tkinter.Button(self.menu, image = img4,bg="#EB9F1B",command=self.PointInterrogation)#créer un bouton à partir de l'image 
        panel4.place(x=1325,y=25)#place le bouton à des coordonnées précises
        
        self.frameImage.pack(expand="yes")#affiche et centre la frame image
        
        self.InputLongueur=tkinter.Entry(self.frameInput,font=("Kokonor",20))#créer un input 
        self.InputLongueur.insert(0,"écrire le nombre de tour")#le placeholder de l'input
        self.InputLongueur.bind('<FocusIn>', self.removeTour)#si on clique dessus, lance la fonction removeTour
        self.InputLongueur.pack(pady=10)#affiche l'input avec une marge externe en haut et en bas
        
        self.InputDelai=tkinter.Entry(self.frameInput,font=("Kokonor",20))
        self.InputDelai.insert(0,"écrire le temps de delai")
        self.InputDelai.bind('<FocusIn>', self.removeDelai)
        self.InputDelai.pack(pady=10)
        
        self.boutonInput.pack(pady=10)
        self.frameInput.place(x=1200,y=540)
        
        self.boutonTab1.pack(side="left",padx=10)
        
        self.frameBouton.pack(expand="yes")
        
        self.boutonQuitter.place(x=1400,y=25)
        
        self.menu.mainloop()#permet de voir si il y a des interactions avec la fenêtre 
    
    #commande du bouton " Envoyer les informations ",récupère les informations envoyé par l'utilisateur
    def InputUtilisateur(self):
        self.NbLongueur=self.InputLongueur.get()#reçoit les informations données par l'utilisateur pour pouvoir les utiliser afin de lancer le jeu
        self.DelaiSec=self.InputDelai.get()
        return self.NbLongueur,self.DelaiSec
       
    #commande qui supprime le placeholder dans l'entree tour
    def removeTour(self,event):
        self.InputLongueur.delete(0, tkinter.END)#supprime le texte, appelez placeholder, qui est afficher dans l'input quand on clique dessus
        
    #commande qui supprime le placeholder dans l'entree delai
    def removeDelai(self,event):
        self.InputDelai.delete(0, tkinter.END)
        
    #message d'information
    def PointInterrogation(self):
        popUp=tkinter.Tk()
        popUp.title("Informations supplémentaires")
        popUp.geometry("1080x360+200+200")
        popUp.iconbitmap("logo.ico")
        popUp.minsize(1080,360)
        popUp.config(background="#EB9F1B")
        labelPopUp=tkinter.Label(popUp, text="Bonjour et merci d'utiliser notre application !\n Pour jouer, vous devez d'abord envoyer les informations demandées en bas à droite,\n puis choisir un tableau.\n A chaque utilisation, vous devrez renoter les informations. ",justify="center",font=("Kokonor",20),bg="#EB9F1B")
        labelPopUp.pack(expand="yes")
        
    #commande du bouton " quitter ",ferme la fenêtre menu
    def quitter(self):
        self.menu.destroy()
        
    #commande du bouton " lancer U ", lance la fenêtre jeu et ferme la fenêtre menu
    def Commande1(self):
        
        try:
            if int(self.NbLongueur)<0:
                self.Erreur()
            elif float(self.DelaiSec)<0:
                self.Erreur()
            else:
                tableau=Labyrinthe(int(self.NbLongueur))
                self.menu.destroy()#ferme la fenêtre menu
                JeuVie=Jeu(tableau)#créer un objet de la classe jeu
                JeuVie.lancerJeu(int(self.NbLongueur),float(self.DelaiSec))#lance le jeu avec les informations de l'utilisateur
         
        except AttributeError:#si attribut non conforme, on envoie une erreur
            print("problème d'attribut")
            self.Erreur()   
            
        except ValueError:#si valeur non conforme, on envoie une erreur
            print("problème de valeur")
            self.Erreur() 
        
    
        
#message d'erreur
    def Erreur(self):
        MessageErreur=tkinter.Tk()
        MessageErreur.title("Erreur : informations manquantes")
        MessageErreur.geometry("1080x360+200+200")
        MessageErreur.iconbitmap("logo.ico")
        MessageErreur.minsize(1080,360)#donne une taille minimale à la fenêtre
        MessageErreur.config(background="#EB9F1B")
        labelErreur=tkinter.Label(MessageErreur, text="Informations manquantes,\n merci de spécifier les valeurs nécessaires\n en chiffres ( supérieurs ou égaux à 0 ) en bas à droite.\n Pour plus d'informations cliquez sur le bouton  ? en haut à droite  ",justify="center",font=("Kokonor",20),bg="#EB9F1B")
        labelErreur.pack(expand="yes")

#classe jeu, se charge de la page jeu
class Jeu:
    
    #créer nos différents objets ( boutons ou frame contenant d'autres objets )
    def __init__(self,tableau):
        self.jeu=tkinter.Tk()
        self._tableau=tableau
        self.bigframe=tkinter.Frame(self.jeu,bd=10,relief=tkinter.SUNKEN)
        self.frameCompteur=tkinter.Frame(self.jeu)
        self.bouton=tkinter.Button(self.jeu,text="revenir au menu",font=("Kokonor",20),bg="#EB9F1B",command=self.quitter) 
        
    #gère l'affichage de la page jeu
    def lancerJeu(self,longueurLabyrinthe,delai):
        
        self.jeu.title("Jeu de la Vie")
        self.jeu.geometry("1920x1080")
        self.jeu.iconbitmap("logo.ico")
        self.jeu.minsize(1920,1080)
        self.jeu.config(background="#EB9F1B")
        self.bouton.place(x=1300,y=25)
        
        #bouton Pause
        self.nbPause=1#créer une variable égal à 1 de base pour que le jeu soit en pause quand on lance le jeu
        self.img5 = ImageTk.PhotoImage(Image.open("PauseImageResize.png"))
        self.img6 = ImageTk.PhotoImage(Image.open("PlayImageResize.png"))
        self.Pause = tkinter.Button(self.jeu,image = self.img6,bg="#EB9F1B",command=self.etatBouton) 
        self.Pause.place(x=200,y=390)
        
        
        #bouton Finir
        self.finir = tkinter.Button(self.jeu,text="finir",font=("Kokonor",20),bg="#EB9F1B",command=self.Finir) 
        self.fini=False
        self.finir.place(x=200,y=700)
        
        
        self.dico={}
        
        for x in range(len(self._tableau)):
            for y in range(len(self._tableau[x])):
                self.dico[self._tableau[x][y]]=couleur(self._tableau[x][y])
        
        self.dico[self._tableau[1][0]]=self.dico[self._tableau[1][0]]
        self.dico[self._tableau[len(self._tableau[x])-2][len(self._tableau[x])-1]]=self.dico[self._tableau[len(self._tableau[x])-2][len(self._tableau[x])-2]]
        self.dico[1]="silver"
        
        self.liste=[]
        x=0
        self.AffichageTableau()
        
        while len(self.liste)!=2:
            if self.fini==True:
                self.tour(longueurLabyrinthe)
                x+=1
            else:
                if self.nbPause%2==1:#si la variable%2 == 1, on met en pause tant que c'est égal à 1
                    while self.nbPause%2==1:
                        self.jeu.update()
                else:
                    time.sleep(delai)
                    self.compteur(x)
                    x+=1
                    self.tour(longueurLabyrinthe)
                    self.AffichageTableau()
             
        self.compteurCassageMur=1#round(longueurLabyrinthe/5)          
        for y in range(self.compteurCassageMur):
            if self.fini==True:
                self.cassageMur(longueurLabyrinthe)
                x+=1
            else:
                if self.nbPause%2==1:#si la variable%2 == 1, on met en pause tant que c'est égal à 1
                    while self.nbPause%2==1:
                        self.jeu.update()
                else:
                    time.sleep(delai)
                    self.compteur(x)
                    x+=1
                    self.cassageMur(longueurLabyrinthe)
                    self.AffichageTableau()
        
        self.AffichageTableau()
        self.EtatStable(x)
        
    
        self.jeu.mainloop()
    
    #affiche le tableau 
    def AffichageTableau(self):
        self.clear_frame()#lance la méthode clear_frame pour vider le tableau
        tabFrame=[]#créer un 2nd tableau
        self.bigframe=tkinter.Frame(self.jeu,bd=10,relief=tkinter.SUNKEN)
        self.bigframe.pack(expand="yes")
        
        for x in range(len(self._tableau)):
            #creation et affichage de la nouvelle frame ( 1 par ligne du tableau )
            tabFrame.append(tkinter.Frame(self.bigframe))
            tabFrame[x].pack()
            for y in range(len(self._tableau[x])):
                Couleur=self.dico[self._tableau[x][y]]
                label_title=tkinter.Label(tabFrame[x],text="11",font=("Courrier",5),bg=Couleur,fg=Couleur)
                label_title.pack(side="left")#pour que cela s'affiche en ligne
                  
        self.jeu.update()#permet de mettre à jour le tableau
    
    #supprime le tableau
    def clear_frame(self):
        self.bigframe.destroy()
        
    #met à jour le tableau
    def tour(self,longueurLabyrinthe):
        labyrinthe=self._tableau
        x=random.randint(1,len(self._tableau)-2)#on prend un mur au pif
        if x%2==0:
            y=random.randint(1,len(self._tableau)-2)//2*2+1
        else:
            y=random.randint(2,len(self._tableau) -3)//2*2
        
        if labyrinthe[x][y]==1:
            if x%2==0:
                if labyrinthe[x-1][y]!=labyrinthe[x+1][y]:
                    if labyrinthe[x-1][y]<labyrinthe[x+1][y]:
                        labyrinthe[x][y]=labyrinthe[x+1][y]
                        variableTemporaire=labyrinthe[x-1][y]
                        for i in range(0,len(labyrinthe)):
                            for j in range (0,len(labyrinthe[i])):
                                if labyrinthe[i][j]==variableTemporaire:
                                    labyrinthe[i][j]=labyrinthe[x+1][y]
                    else:
                        labyrinthe[x][y]=labyrinthe[x-1][y]
                        variableTemporaire=labyrinthe[x+1][y]
                        for i in range(0,len(labyrinthe)):
                            for j in range (0,len(labyrinthe[i])):
                                if labyrinthe[i][j]==variableTemporaire:
                                    labyrinthe[i][j]=labyrinthe[x-1][y]
                else:
                    self.tour(longueurLabyrinthe)
        
            else:
                if labyrinthe[x][y-1]!=labyrinthe[x][y+1]:
                    if labyrinthe[x][y-1]<labyrinthe[x][y+1]:
                        labyrinthe[x][y]=labyrinthe[x][y+1]
                        variableTemporaire=labyrinthe[x][y-1]
                        for i in range(0,len(labyrinthe)):
                            for j in range (0,len(labyrinthe[i])):
                                if labyrinthe[i][j]==variableTemporaire:
                                    labyrinthe[i][j]=labyrinthe[x][y+1]
                    else:
                        labyrinthe[x][y]=labyrinthe[x][y-1]
                        variableTemporaire=labyrinthe[x][y+1]
                        for i in range(0,len(labyrinthe)):
                            for j in range (0,len(labyrinthe[i])):
                                if labyrinthe[i][j]==variableTemporaire:
                                    labyrinthe[i][j]=labyrinthe[x][y-1]
                else:
                    self.tour(longueurLabyrinthe)
         
        
        self.liste=[]
        for x in range(len(self._tableau)):
            for y in range(len(self._tableau)):
                if self._tableau[x][y] not in self.liste:
                    if len(self.liste)>2:
                        break
                    self.liste.append(self._tableau[x][y])
            if len(self.liste)>2:
                        break
        
        return labyrinthe
    
    def cassageMur(self,longueurLabyrinthe):
        
        labyrinthe=self._tableau
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
                return labyrinthe
        else:
            self.cassageMur(longueurLabyrinthe)
                
            
     
    #compte et affiche le nombre de tours
    def compteur(self,x):
            self.frameCompteur.destroy()
            self.frameCompteur=tkinter.Frame(self.jeu)
            self.frameCompteur.place(x=730,y=150)
            label_title=tkinter.Label(self.frameCompteur,text="tour : "+str(x),font=("Kokonor",20),bg="#EB9F1B",fg="black")
            label_title.pack()
        
    #si le tableau est dans un état stable, alors on change le compteur par cette phrase
    def EtatStable(self,x):
        self.frameCompteur.destroy()
        self.frameCompteur=tkinter.Frame(self.jeu)
        self.frameCompteur.place(x=680,y=150)
        label_title=tkinter.Label(self.frameCompteur,text="tour "+str(x)+" : etat stable",font=("Kokonor",20),bg="#EB9F1B",fg="black")
        label_title.pack()
        
    #modifie l'affichage à côté du bouton Pause
    def etatBouton(self):
        self.nbPause+=1
        if self.nbPause%2==1:
            self.Pause.configure(image=self.img6)#si on est en pause, on affiche le logo play 
        else:
            self.Pause.configure(image=self.img5)#sinon le logo pause
            
    def Finir(self):
        self.fini=True
    
    #quitte la fenêtre jeu et nous renvoie à la fenêtre menu
    def quitter(self):
        self.jeu.destroy()
        MenuVie=Menu()
        MenuVie.lancerMenu()

MenuVie=Menu()
MenuVie.lancerMenu()