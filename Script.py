import matplotlib.pyplot as plt #ce module pour afficher les images et les ouvrir sous forme de matrice
import numpy as np #ce module pour manipuler les matrices
import random as rd #ce module pour générer des nombres aléatoires
def AfficherImg(img): 
    plt.axis("off") #les axes du graphe ici désactivés
    #plt.imshow(img, interpolation = 'nearest') # affichage de l'img
    plt.imshow(img, cmap = "gray") # "gray" pour afficher les images en echelle grise
    plt.show() #pour voir l'image dans une fenetre ou à l'interface d'execution

def ouvrirImage(chemin):
    return plt.imread(chemin) #lire où se trouve l'image et retourner une matrice sous forme d'array dans le module numpy

def sauvImage(img):
    chemin = str(input("Entrer le nom de votre nouvelle photo sans oublier son format : ")) #l'utilisateur doit saisir le chemin où il veut enregistrer sa nouvelle image
    plt.imsave(chemin, img, cmap = 'gray' )# enregistrer l'image dans le chemin voulu avec la couleur grise en defaut en format jpg

def image_noire(h, l):
    M = [[0]*l for i in range(h)] #itèrons et créant une matrice à deux dimensions de h lignes et l colonnes juste de 0
    c = np.array(M).astype(np.uint8) # transformant la matrice initialisé en array comme type de 8 bits non int32
    return c

def image_blanche(h, l):
    M = [[1]*l for i in range(h)] #itèrons et créant une matrice à deux dimensions de h lignes et l colonnes juste de 1
    c = np.array(M).astype(np.uint8)
    return c

def creerImgBlancNoir(h, l):
    M = [[0]*l for i in range(h)] #initialisons une matrice de h lignes et l colonnes
    for i in range(h):
        for j in range(l):
            M[i][j] = (i + j + 2)%2 # chaque element reçoit l'indice de colonne et de ligne '+2' car i et j debutent de 0, cette somme modulo 2
    c = np.array(M).astype(np.uint8)
    return c

def negatif(img):
    img = img.tolist() #on transforme en liste car on subit une erreur d'itération avec l'utilisation de type array
    for i in range(len(img)):
        for j in range(len(img[0])):
            if img[i][j] == 0: #verifions si un element egal à 0
                img[i][j] = 1 #pour qu'il reçoit 1
            elif img[i][j] == 1:#ici le contraire si 1 l'element devient 0
                img[i][j] = 0
    c = np.array(img).astype(np.uint8)
    return c

def luminance(img):
    s = 0
    ind = len(img) * len(img[0]) #le nombre d'elements dans la matrice img
    for i in range(len(img)):
        for j in range(len(img[0])):
            s += img[i][j] #sommant toutes les valeurs dans la matrice img
    return s / ind #retournant la moyenne des valeurs de cette matrice

def constrast(img):
    N = len(img) * len(img[0]) #le nombre d'elements dans la matrice img
    moy = luminance(img) #utilisons la fonction luminance() pour retrouver la moyenne de la matrice img
    s = 0
    for i in range(len(img)):
        for j in range(len(img[0])):
            s += (img[i][j] - moy)**2 # chaque pixel ou element de la matrice se reduit par la moyenne le tout à la puissance 2 , on sommme tous les elements par cet algorithme
    return s / N #On divise ensuite cette somme par le nombre d'elements dans la matrice img

def profondeur(img):
    max = img[0][0] #affectons le premier element au maximum
    for i in range(len(img)):
        for j in range(len(img[0])):
            if max < img[i][j]: #verifions si le max est plus petit que le nombre suivant
                max = img[i][j]  # si oui on affecte au max cet element
    return max

def Ouvrir():
    return ouvrirImage("images_o.jpg") #cette fonction retourne la matrice de l'image dans la documentation du projet

def inverser(img):
    return 255 - img #comme img est retournée comme array alors elle peut subir des opérations normal, ici on soustrait 255 de tous les elements de img en retournat une nouvelle matrice

def flipH(img):
    nouv = img.tolist() #.tolist() transforme un array en liste , la fonction list() ne marche pas elle retourne une liste d'arrays car ici on travaille dans les matrice de 2+ dimension
    for i in range(len(img)):
        for j in range(len(img[0])):
            nouv[i][j] = img[-(i+1)][-(j+1)] #renversant la matrice img dans une nouvelle matrice
    c = np.array(nouv).astype(np.uint8)
    return c
    

def poserV(img1, img2):
    M = list(img1) + list(img2) #on ajoute les lignes de la matrice img2 en dessous  de la matrice img1 pour former une matrice M
    c = np.array(M) #ensuite on affecte à c la matrice M en  mode array
    return c
def poserH(img1, img2):
    nouv = [[0]*(2*len(img1[0])) for i in range(len(img1))]#creant une matrice de deux dimensions pour colonne le double de nombre de colonne de la matrice img1
    img1, img2 = img1.tolist(), img2.tolist() #transformons les matrice img1 et img2 en liste
    for i in range(len(img1)):
        nouv[i] = img1[i] + img2[i] # les sous listes ici se concaténe dans une sous liste 
    c = np.array(nouv).astype(np.uint8)
    return c

def AfficherRgb(M):
    plt.imshow((np.array(M)* 255).astype(np.uint8))#ici on affiche tous les elements de la matrice M comme type de 8 bytes
    plt.axis("off")
    plt.show()

def initImageRGB():
    n = rd.randrange(256) #lignes aléatoires
    p = rd.randrange(256) #colonnes aléatoires
    imageRGB = np.zeros((n, p, 3)) #on initialise une matrice de trois dimensions avec n lignes et p colonnes
    for i in range(n):
        for j in range(p):
            for k in range(3):
                imageRGB[i][j][k] = rd.randrange(256) #chaque element prend une valeur aléatoire comprise entre 0 et 255
    return imageRGB

def grayscale(imageRGB):
    M = np.zeros((len(imageRGB), len(imageRGB[0]))) #initialisons une matrice de meme dimension que imageRGB
    for i in range(len(imageRGB)):
        for j in range(len(imageRGB[0])):
            M[i][j] = (max(imageRGB[i][j]) + min(imageRGB[i][j])) // 2 #chaque element on le remplace par le max et le min valeur entière des deux par 2
    return M

def symetrieV(img):
    nouv = np.full(img.shape, 0)# on initialise une matrice de meme dimension que img, on peut meme utiliser np.zeros(img.shape)
    for i in range(len(img)):
        nouv[i] = img[-i-1]# on inverse les lignes pour que la première ligne sois la dernière
    c = np.array(nouv).astype(np.uint8)
    return c

    


def main(): #on declare une fonction main qui contient les traitements possibles
    print("Outils:")
    print("1- Afficher l'image")
    print("2- Sauvegarder l'image")
    print("3- Creer une image noir")
    print("4- Creer une image blanche")
    print("5- Creer une image blanc et noir")
    print("6- Retrouver le negatif d'une image blanc et noir")
    print("7- Avoir la luminance de l'image ")
    print("8- Avoir le constrast de l'image")
    print("9- Avoir la profondeur de l'image")
    print("10- Retrouver l'inverse de l'image")
    print("11- Renverser l'image")
    print("12- Poser deux image l'une en dessus de l'autre")
    print("13- Poser deux images l'une à coté de l'autre")
    print("14- Initialiser une image en couleur aléatoiremet")
    print("15- Avoir la symétrie vertical de l'image ")
    print("16- Transformer l'image en couleur à echelle grise")
    print("17- Pour Afficher une image en couleur RGB")
    print("18- Pour quitter")
    choix = int(input("Entrez votre choix: ")) #l'utilisateur entre son choix
    if choix == 18 :
        exit(0) # pour sortir du programme
    elif choix == 1:
        AfficherImg(img)
        
    elif choix == 2:
        sauvImage(img)#pour sauvegarder l'image
        main() # pour retourner au liste des choix
    elif choix == 3:
        h = int(input("Entrer le nombre de lignes de la matrice: "))
        l = int(input("Entrer le nombre de colonnes de la matrice: "))
        img1 = image_noire(h, l)
        sauvImage(img1) #pour sauvegarder l'image
        main()
    elif choix == 4:
        k = int(input("Entrer le nombre de lignes de la matrice: "))
        j = int(input("Entrer le nombre de colonnes de la matrice: "))
        img2 = image_blanche(k, j)
        chemin = str(input("Entrer le nom de votre nouvelle photo sans oubliant son format : ")) #l'utilisateur doit saisir le chemin où il veut enregistrer sa nouvelle image
        plt.imsave(chemin, img2, cmap = 'binary' )# on choisit colormap comme binary qui peut avoir juste 0 et 1 ici 1 alors tout blanc
        main()
    elif choix == 5:
        m = int(input("Entrer le nombre de lignes de la matrice: "))
        n = int(input("Entrer le nombre de colonnes de la matrice: "))
        img3 = creerImgBlancNoir(m, n)
        sauvImage(img3)
        main()
    elif choix == 6:
        img4 = negatif(img)
        sauvImage(img4)
        main()
    elif choix == 7:
        print(luminance(img))
        main()
    elif choix == 8:
        print(constrast(img))
        main()
    elif choix == 9:
        print(profondeur(img))
        main()
    elif choix == 10:
        img5 = inverser(img)
        sauvImage(img5)
        main()
    elif choix == 11:
        img6 = flipH(img)
        sauvImage(img6)
        main()
    elif choix == 12:
        ch1 = str(input("Veuillez saisir le nom  de la première image  que vous voulez à la base sans oubliant son format à la fin :"))
        ch2 = str(input("Veuillez saisir le nom  de l'image  que vous voulez en dessus sans oubliant son format à la fin :"))
        img7 , img8 = ouvrirImage(ch1) , ouvrirImage(ch2)
        img9 = poserV(img7, img8)
        sauvImage(img9)
        main()
    elif choix == 13:
        ch3 = str(input("Veuillez saisir le nom  de la première image  que vous voulez à droite sans oubliant son format à la fin :"))
        ch4 = str(input("Veuillez saisir le nom  de l'image  que vous voulez à gauche sans oublier son format à la fin :"))
        img10 , img11 = ouvrirImage(ch3) , ouvrirImage(ch4)
        img12 = poserH(img10, img11)
        sauvImage(img12)
        main()

    elif choix == 14:
        img13 = initImageRGB()
        img13 =  img13.astype('uint8') #comme type de 8 bits pour cette matrice peut avoir 255 valeurs comme valeur d'interval des RGB 
        sauvImage(img13)
        main()
    elif choix == 15:
        img14 = symetrieV(img)
        sauvImage(img14)
        main()
        
    elif choix == 16:
        img15 = grayscale(img)
        sauvImage(img15)
        main()
    
    elif choix == 17:
        AfficherRgb(img)

if __name__ == '__main__':
    chemin = str(input("Veuillez saisir le nom  de l'image  que vous voulez traiter sans oubliant le format à la fin :"))
    while not "." in chemin: # si l'utilisateur n'entre pas le format 
        chemin = str(input("Vous avez oublier le format d'image veuillez resaisir :"))# il doit resaisir le chemin
    img = ouvrirImage(chemin)
    main()
    
    
