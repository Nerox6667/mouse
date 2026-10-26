from turtle import *    # appelle la librairie turtle

setup(width=1920, height=1080)

speed(0)                # permet au stylo d'aller plus vite

hideturtle()            # je fais disparraitre le pointeur du turtle

title("GAME OVER")      # je renomme la fenêtre de dessin "GAME OVER"


def f(f):               # je defini le fonction "f" avec une variable "f"
    forward(f)          # le stylo avance de "f" de long
    # cette fonction me sert à simplifier la commande "forward(...)" par "f(...)" cela me sert a eviter les faute frappe et a gagner du temps



def b(b):                # je defini le fonction "b" avec une variable "b"
    backward(b)          # le stylo recule de "b" dde long
    # cette fonction me sert à simplifier la commande "backward(...)" par "b(...)" cela me sert a eviter les faute frappe et a gagner du temps


def l():                 # je defini le fonction "l"
    left(90)             # tourne le stylo à droite de 90°
    # cette fonction me sert à simplifier la commande "left(90)" par "l()" cela me sert a eviter les faute frappe et a gagner du temps

def r():                 # je defini le fonction "r" 
    right(90)            # tourne le stylo à droite de 90°
    # cette fonction me sert à simplifier la commande "right(90)" par "r()" cela me sert a eviter les faute frappe et a gagner du temps


def fond(fond_c):              # je déffini la fonction "fond" 
    fillcolor(fond_c)    # je choisis comme couleur de remplisage le gris 
    pendown()            # je pose le stylo pour dessiner
    begin_fill()         # je commence le remplissage
    for i in range(4):   # je fais repeter les instruction suivante quatre fois : 
        f(2000)          # avancer de 2000
        r()              # appel la fontion "r"
    end_fill()           # j'arréte le remplissage
    penup()              # et je léve le stylo pour ne pas dessiner durant les prochaine manipulation
    # cette fonction me permette donc de dessiner de dessiner un grand carré de 2000 de coté ,je m'en servirais pour créer un fond gris 



def os(os):             # deffini la fonction "os" avec la variable "os"
    f(20*os)            #
    r()                 # appel la fonction "r"
    circle(2*os, 270)   # créer un arc de cercle de 3/4 d'un cercle de rayon deux foix "os"
    right(180)          # le stylo fais un demi tour
    circle(2*os, 270)   # créer un arc de cercle de 3/4 d'un cercle de rayon deux foix "os"
    r()                 # appel la fonction "r"
    f(20*os)            # avance de 20 foix "os"
    # cette fonction dessine un demi os de taille "os"




def croix_os(c_os):     # deffini la fonction "crois_os" avec le variable "c_os"
    fillcolor("white")  # choisis de remplir en blanc cette figure 
    pendown()           # pose le stylo
    begin_fill()        # commence le remplissage
    right(45)           # tourne de 45° vers le droite
    for i in range(4):  # repete 4 foix :
        os(c_os)        # appel la fonction "os" et le dessine de taille "c_os"
        r()             # appel la fonction "r"
    end_fill()          # fin du remplissage
    penup()             # leve le stylo
    # cette fonction sert créer une crois d'os de taille "c_os" grace a la fonction "os" 



def croix(x):        # deffini la fonction "croix" avec la variable "x" 
    pendown()        # pose le stylo
    left(45)         # tourne à gauche de 45°
    b(2.5*x)         # recule
    f(5*x)           # puis avance de deux foix ce qu'il a reculé
    b(2.5*x)         # re recule de la moitié de ce que j'ai avancé pour revenir au milieu
    l()              # appel la fonction "l" pour tourner de 90° vers la gauche
    b(2.5*x)         # recule           
    f(5*x)           # puis avance de deux foix ce qu'il a reculé
    b(2.5*x)         # re recule de la moitié de ce que j'ai avancé pour revenir au milieu
    penup()          # leve le stylo
    left(45)         # tourne à gauche de 45° pour remettre le stylo dans le bon axe
    # cette fonction sert à dessiné une croix de taille "x"


def coeur(coeur_):     # deffini la fonction "coeur" avec la variable "coeur_"
    r()                # appel la fonction "r"
    f(1.5*coeur_)     # avance de 1.5*coeur_
    fillcolor("red")  # choisis la couleur de remplissage rouge
    begin_fill()        # commence le remplissage
    pendown()           # pose le stylo pour pouvoir dessiné
    circle(1.5*coeur_, 180) # créer un demi cercle de 3*coeur_ de rayon
    left(30)              # tourne à gauche de 30°
    f(6*coeur_)          # avance de 12*coeur_
    left(120)              # tourne à gauche de 120°
    f(6*coeur_)          # avance de 12*coeur_
    left(30)              # tourne à gauche de 30°
    circle(1.5*coeur_, 180) # créer un demi cercle de 3*coeur_ de rayon
    end_fill()          # fin du remplissage
    penup()             # leve le stylo
    f(1.5*coeur_)     # avance de 1.5*coeur_
    l()                 # j'appell la fonction "l" pour tourner à gauche de 90° 
    # cette fonction me sert a dessiner un coeur rouge de taille "coeur_"

def triangle(t):        # deffini la fonction "triangle" avec la variable "t"
    fillcolor("black")  # choisis la couleur de remplissage noire
    begin_fill()        # commence le remplissage
    pendown()           # pose le stylo pour pouvoir dessiné
    for i in range(3):  # repete les instuction suivante trois fois :
        f(2*t)          # avance de deux fois "t"
        right(120)      # tourne à doite de 120° pour créer un angle de 60° avec le coté tracé précedament
    end_fill()          # fin du remplissage
    penup()             # leve le stylo  
    # cette fonction sert à dessiner un triangle équilateral noire pour former le nez de la souris



def mouse(souris):     # deffini la fonction "mouse" avec la variable "souris"
    b(10*souris)       
    r()
    pendown()          # pose le stylo
    fillcolor("green") # choisis la couleur vert pour le remplissage de ce dessin  
    begin_fill()       # commence le remplissage
    circle(11*souris)  # fais le contour de la tête avec un cercle de 11 foix souris   
    end_fill()         # fin du remplissage
    penup()            # leve le stylo
    l()             # déplace le stylo pour le replacer à l'emplacement des oreilles
    f(3*souris)
    r()
    f(1.5*souris)
    r()
    pendown()            # re pose le stylo
    begin_fill()         # recommence le remplissage  
    circle(5*souris, 300)# dessine les oreilles grace a des arcs de cercle de 5 foix souris
    penup()              # releve le stylo
    right(30)         # créer un ecard et replace le stylo pour la seconde oreille
    f(8*souris)
    right(30)
    pendown()            # re pose le stylo
    circle(5*souris, 300)
    end_fill()           # fin du remplissage
    penup()              # releve le stylo
    f(10*souris)     # replace le stylo pour aller dessiner les yeux 
    l()
    f(3*souris)
    croix(souris)        # appel la fonction croix et la dessine de taille souris pour créer l'oeil 
    f(10*souris)         # ecarte les yeux de 10 foix souris
    croix(souris)        # appel la fonction croix et la dessine de taille souris pour créer l'oeil 
    f(5*souris)     # replace le stylo pour aller dessiné le nez de la souris
    r()
    f(7*souris)
    right(150)
    triangle(souris)     # appel la fonction triangle pour créer le nez et le fait de taille souris
    right(120)      # replace le stylo pour aller dessiner les moustaches
    f(1.5*souris)  
    l()
    f(souris)
    right(130)
    pendown()           # pose le stylo
    for i in range(3):  # repete trois foix :
        f(10*souris)    # avancer de 10 foix souris
        b(10*souris)    # reculer de 10 foix souris 
        left(30)        # tourner à gauche de 30°
    penup()             # lever le stylo        # cela a dessiné les moustaches droite
    left(130)       # replace le stylo pour créer un espace entre les deux moustaches
    f(3*souris)
    left(40)
    pendown()           # pose le stylo
    for i in range(3):  # repete trois foix :
        f(10*souris)    # avancer de 10 foix souris
        b(10*souris)    # reculer de 10 foix souris 
        right(30)       # tourner à droite de 30°
    penup()             # lever le stylo        # cela a dessiné les moustaches gauche
    right(130)      # place le stylo en bas du dessin 
    f(1.5*souris)
    r()
    f(3*souris)
    l()
    # cette fonction sert a dessiné une tête de souris morte de taille "souris"


def mouse_c(souris_c):     # deffini la fonction "mouse" avec la variable "souris_c"
    b(10*souris_c)       
    r()
    pendown()          # pose le stylo
    fillcolor("white") # choisis la couleur blanc pour le remplissage de ce dessin  
    begin_fill()       # commence le remplissage
    circle(11*souris_c)  # fais le contour de la tête avec un cercle de 11 foix souris_c   
    end_fill()         # fin du remplissage
    penup()            # leve le stylo
    l()             # déplace le stylo pour le replacer à l'emplacement des oreilles
    f(3*souris_c)
    r()
    f(1.5*souris_c)
    r()
    pendown()            # re pose le stylo
    begin_fill()         # recommence le remplissage  
    circle(5*souris_c, 300)# dessine les oreilles grace a des arcs de cercle de 5 foix souris
    penup()              # releve le stylo
    right(30)         # créer un ecard et replace le stylo pour la seconde oreille
    f(8*souris_c)
    right(30)
    pendown()            # re pose le stylo
    circle(5*souris_c, 300)
    end_fill()           # fin du remplissage
    penup()              # releve le stylo
    f(10*souris_c)     # replace le stylo pour aller dessiner les yeux 
    l()
    f(3*souris_c)
    right(180)             # fais faire un demi tour au stylo pour le mettre dans le bon sens
    coeur(souris_c)        # appel la fonction coeur et la dessine de taille souris_c pour créer l'oeil 
    right(180)             # fais faire un demi tour au stylo pour le mettre dans le bon sens
    f(10*souris_c)         # ecarte les yeux de 10 foix souris
    coeur(souris_c)        # appel la fonction coeur et la dessine de taille souris_c pour créer l'oeil 
    f(5*souris_c)     # replace le stylo pour aller dessiné le nez de la souris
    r()
    f(7*souris_c)
    right(150)
    triangle(souris_c)     # appel la fonction triangle pour créer le nez et le fait de taille souris_c
    right(120)      # replace le stylo pour aller dessiner les moustaches
    f(1.5*souris_c)  
    l()
    f(souris_c)
    right(130)
    pendown()           # pose le stylo
    for i in range(3):  # repete trois foix :
        f(10*souris_c)    # avancer de 10 foix souris_c
        b(10*souris_c)    # reculer de 10 foix souris_c 
        left(30)        # tourner à gauche de 30°
    penup()             # lever le stylo        # cela a dessiné les moustaches droite
    left(130)       # replace le stylo pour créer un espace entre les deux moustaches
    f(3*souris_c)
    left(40)
    pendown()           # pose le stylo
    for i in range(3):  # repete trois foix :
        f(10*souris_c)    # avancer de 10 foix souris_c
        b(10*souris_c)    # reculer de 10 foix souris_c 
        right(30)       # tourner à droite de 30°
    penup()             # lever le stylo        # cela a dessiné les moustaches gauche
    right(130)      # place le stylo en bas du dessin 
    f(1.5*souris_c)
    r()
    f(3*souris_c)
    l()
    # cette fonction sert a dessiné une tête de souris contente de taille "souris_c"


def mouse_os(mouse_x):  # deffini la fonction "mouse_os" avec une variable "mouse_x" qui me permet de choisir la taille du dessin 
    croix_os(mouse_x)   # j'appelle la fonction "crois_os" et lui affecte la variable "mouse_x"                
    right(45)           # tourne à droite de 45° pour addapter la croix d'os avec la tête de souris
    mouse(mouse_x)      # j'appelle la fonction "mouse" et lui affecgte la variable "mouse_x"
    # cette fonction sert donc à fusionner la croix d'os et la tête de souris pour former une tête de mort souris


def between(c):      # je defini la fonction "between" avec la variable "c"
    right(180)    # fait faire un demi-tour au stylo
    f(c)    # avance de c
    # cette fonction me sert à créer des ecart entre les lettres




def G(g):    # je defini la fonction "G" avec la variable "g"
    pendown()    # pose le stylo pour pouvoir dessiner
    l()    # appel la fonction "l" pour tourner à gauche de 90°
    f(20*g)    # avance de 20*g
    r()    # appel la fonction "r" pour tourner à droite de 90°
    f(15*g)    # avance de 15*g
    r()    # appel la fonction "r" pour tourner à droite de 90°
    f(2*g)    # avance de 2*g
    r()    # appel la fonction "r" pour tourner à droite de 90°
    f(13*g)    # avance de 13*g
    l()    # appel la fonction "l" pour tourner à gauche de 90°
    f(16*g)    # avance de 16*g
    l()    # appel la fonction "l" pour tourner à gauche de 90°
    f(11*g)    # avance de 11*g
    l()    # appel la fonction "l" pour tourner à gauche de 90°
    f(6*g)    # avance de 6*g
    l()    # appel la fonction "l" pour tourner à gauche de 90°
    f(4*g)    # avance de 4*g
    r()    # appel la fonction "r" pour tourner à droite de 90°
    f(2*g)    # avance de 2*g
    r()    # appel la fonction "r" pour tourner à droite de 90°
    f(6*g)    # avance de 6*g
    r()    # appel la fonction "r" pour tourner à droite de 90°
    f(10*g)    # avance de 10*g
    r()    # appel la fonction "r" pour tourner à droite de 90°
    f(15*g)    # avance de 15*g
    penup()    # leve le stylo pour se déplacer sans dessiner
    # cette fonction me sert à dessiner un G de taille "g"


def A(a):    # je defini la fonction "A" avec la variable "a"
    pendown()    # pose le stylo pour pouvoir dessiner
    l()    # appel la fonction "l" pour tourner à gauche de 90°
    f(20*a)    # avance de 20*a
    r()    # appel la fonction "r" pour tourner à droite de 90°
    f(15*a)    # avance de 15*a
    r()    # appel la fonction "r" pour tourner à droite de 90°
    f(20*a)    # avance de 20*a
    r()    # appel la fonction "r" pour tourner à droite de 90°
    f(2*a)    # avance de 2*a
    r()    # appel la fonction "r" pour tourner à droite de 90°
    f(8*a)    # avance de 8*a
    penup()    # leve le stylo pour se déplacer sans dessiner
    f(2*a)    # avance de 2*a
    pendown()    # pose le stylo pour pouvoir dessiner
    for i in range(2):    # repete les instructions suivantes deux fois :
        f(8*a)    # avance de 8*a
        l()    # appel la fonction "l" pour tourner à gauche de 90°
        f(11*a)    # avance de 11*a
        l()    # appel la fonction "l" pour tourner à gauche de 90°
    penup()    # leve le stylo pour se déplacer sans dessiner
    b(2*a)    # recule de 2*a
    pendown()    # pose le stylo pour pouvoir dessiner
    l()    # appel la fonction "l" pour tourner à gauche de 90°
    f(11*a)    # avance de 11*a
    l()    # appel la fonction "l" pour tourner à gauche de 90°
    f(8*a)    # avance de 8*a
    r()    # appel la fonction "r" pour tourner à droite de 90°
    f(2*a)    # avance de 2*a
    penup()    # leve le stylo pour se déplacer sans dessiner
    # cette fonction me sert à dessiner un A de taille "a"

def M(m):    # je defini la fonction "M" avec la variable "m"
    pendown()    # pose le stylo pour pouvoir dessiner
    l()    # appel la fonction "l" pour tourner à gauche de 90°
    f(20*m)    # avance de 20*m
    r()    # appel la fonction "r" pour tourner à droite de 90°
    f(2*m)    # avance de 2*m
    right(60)    # tourne le stylo de 60° vers la droite
    f(11*m)    # avance de 11*m
    left(120)    # tourne le stylo de 120° vers la gauche
    f(11*m)    # avance de 11*m
    right(60)    # tourne le stylo de 60° vers la droite
    f(2*m)    # avance de 2*m
    r()    # appel la fonction "r" pour tourner à droite de 90°
    f(20*m)    # avance de 20*m
    r()    # appel la fonction "r" pour tourner à droite de 90°
    f(2*m)    # avance de 2*m
    r()    # appel la fonction "r" pour tourner à droite de 90°
    f(17*m)    # avance de 17*m
    left(150)    # tourne le stylo de 150° vers la gauche
    f(11*m)    # avance de 11*m
    right(120)    # tourne le stylo de 120° vers la droite
    f(11*m)    # avance de 11*m
    left(150)    # tourne le stylo de 150° vers la gauche
    f(17*m)    # avance de 17*m
    r()    # appel la fonction "r" pour tourner à droite de 90°
    f(2*m)    # avance de 2*m
    penup()    # leve le stylo pour se déplacer sans dessiner
    # cette fonction me sert à dessiné un M de taille "m"

def E(e):    # je defini la fonction "E" avec la variable "e"
    pendown()    # pose le stylo pour pouvoir dessiner
    l()    # appel la fonction "l" pour tourner à gauche de 90°
    f(20*e)    # avance de 20*e
    r()    # appel la fonction "r" pour tourner à droite de 90°
    f(15*e)    # avance de 15*e
    for i in range(2):    # repete les instructions suivantes deux fois :
        r()    # appel la fonction "r" pour tourner à droite de 90°
        f(2*e)    # avance de 2*e
        r()    # appel la fonction "r" pour tourner à droite de 90°
        f(13*e)    # avance de 13*e
        l()    # appel la fonction "l" pour tourner à gauche de 90°
        f(7*e)    # avance de 7*e
        l()    # appel la fonction "l" pour tourner à gauche de 90°
        f(13*e)    # avance de 13*e
    r()    # appel la fonction "r" pour tourner à droite de 90°
    f(2*e)    # avance de 2*e
    r()    # appel la fonction "r" pour tourner à droite de 90°
    f(15*e)    # avance de 15*e
    penup()    # leve le stylo pour se déplacer sans dessiner
    # cette fonction sert à desssiner un E de taille "e"


def O(o):    # je defini la fonction "O" avec la variable "o"
    l()    # appel la fonction "l" pour tourner à gauche de 90°
    pendown()    # pose le stylo pour pouvoir dessiner
    for i in range(2):    # repete les instructions suivantes deux fois :
        f(20*o)    # avance de 20*o
        r()    # appel la fonction "r" pour tourner à droite de 90°
        f(15*o)    # avance de 15*o
        r()    # appel la fonction "r" pour tourner à droite de 90°
    penup()    # leve le stylo pour se déplacer sans dessiner
    l()    # appel la fonction "l" pour tourner à gauche de 90°
    b(2*o)    # recule de 2*o
    l()    # appel la fonction "l" pour tourner à gauche de 90°
    b(2*o)    # recule de 2*o
    l()    # appel la fonction "l" pour tourner à gauche de 90°
    l()    # appel la fonction "l" pour tourner à gauche de 90°
    pendown()    # pose le stylo pour pouvoir dessiner
    for i in range(2):    # repete les instructions suivantes deux fois :
        f(16*o)    # avance de 16*o
        r()    # appel la fonction "r" pour tourner à droite de 90°
        f(11*o)    # avance de 11*o
        r()    # appel la fonction "r" pour tourner à droite de 90°
    penup()    # leve le stylo pour se déplacer sans dessiner
    b(2*o)    # recule de 2*o
    l()    # appel la fonction "l" pour tourner à gauche de 90°
    f(2*o)    # avance de 2*o
    #cette fonction sert à dessiner un O de taille "o"




def V(v):    # je defini la fonction "V" avec la variable "v"
    l()    # appel la fonction "l" pour tourner à gauche de 90°
    f(20*v)    # avance de 20*v
    r()    # appel la fonction "r" pour tourner à droite de 90°
    pendown()    # pose le stylo pour pouvoir dessiner
    f(2*v)    # avance de 2*v
    right(73)    # tourne le stylo de 73° vers la droite
    f(18.8*v)    # avance de 18.8*v
    left(146)    # tourne le stylo vers la gauche de l'angle indiqué
    f(18.8*v)    # avance de 18.8*v
    right(73)    # tourne le stylo de 73° vers la droite
    f(2*v)    # avance de 2*v
    right(107)    # tourne le stylo de 107° vers la droite
    f(21.2*v)    # avance de 21.2*v
    right(73)    # tourne le stylo de 73° vers la droite
    f(2.6*v)    # avance de 2.6*v
    right(73)    # tourne le stylo de 73° vers la droite
    f(21.2*v)    # avance de 21.2*v
    penup()    # leve le stylo pour se déplacer sans dessiner
    right(17)    # ajuste l'orientation du stylo de 17°
    b(20*v)    # recule de 20*v
    l()    # appel la fonction "l" pour tourner à gauche de 90°
    # cette fonction sert à dessiner un V de taille "v"

def R(r1):    # je defini la fonction "R" avec la variable "r1"
    pendown()    # pose le stylo pour pouvoir dessiner
    begin_fill()    # commence le remplissage de la figure
    l()    # appel la fonction "l" pour tourner à gauche de 90°
    f(20*r1)    # avance de 20*r1
    r()    # appel la fonction "r" pour tourner à droite de 90°
    f(15*r1)    # avance de 15*r1
    r()    # appel la fonction "r" pour tourner à droite de 90°
    f(12*r1)    # avance de 12*r1
    r()    # appel la fonction "r" pour tourner à droite de 90°
    f(2*r1)    # avance de 2*r1
    r()    # appel la fonction "r" pour tourner à droite de 90°
    penup()    # leve le stylo pour se déplacer sans dessiner
    f(2*r1)    # avance de 2*r1
    pendown()    # pose le stylo pour pouvoir dessiner
    for i in range(2):    # repete les instructions suivantes deux fois :
        f(8*r1)    # avance de 8*r1
        l()    # appel la fonction "l" pour tourner à gauche de 90°
        f(11*r1)    # avance de 11*r1
        l()    # appel la fonction "l" pour tourner à gauche de 90°
    penup()    # leve le stylo pour se déplacer sans dessiner
    b(2*r1)    # recule de 2*r1
    pendown()    # pose le stylo pour pouvoir dessiner
    l()    # appel la fonction "l" pour tourner à gauche de 90°
    f(11*r1)    # avance de 11*r1
    l()    # appel la fonction "l" pour tourner à gauche de 90°
    f(8*r1)    # avance de 8*r1
    r()    # appel la fonction "r" pour tourner à droite de 90°
    f(2*r1)    # avance de 2*r1
    end_fill()    # termine le remplissage de la figure
    penup()    # leve le stylo pour se déplacer sans dessiner
    r()    # appel la fonction "r" pour tourner à droite de 90°
    f(8*r1)    # avance de 8*r1
    r()    # appel la fonction "r" pour tourner à droite de 90°
    f(10*r1)    # avance de 10*r1
    pendown()    # pose le stylo pour pouvoir dessiner
    begin_fill()    # commence le remplissage de la figure
    right(60)    # tourne le stylo de 60° vers la droite
    f(9.2*r1)    # avance de 9.2*r1
    right(300)    # tourne le stylo de 300° vers la droite
    f(2*r1)    # avance de 2*r1
    left(120)    # tourne le stylo de 120° vers la gauche
    f(9.2*r1)    # avance de 9.2*r1
    end_fill()    # termine le remplissage de la figure
    penup()    # leve le stylo pour se déplacer sans dessiner
    right(30)    # tourne le stylo de 30° vers la droite
    b(8*r1)    # recule de 8*r1
    l()    # appel la fonction "l" pour tourner à gauche de 90°
    f(12*r1)    # avance de 12*r1
    # cette fonction me sert à dessiner un R de taille "r"



def game_over(game):    # je defini la fonction "game_over" avec la variable "game"
    fillcolor("red")    # choisit le rouge comme couleur de remplissage
#lettre G
    begin_fill()    # commence le remplissage de la figure
    G(game)    # appelle la fonction pour dessiner la lettre correspondante
    end_fill()    # termine le remplissage de la figure

    between(17*game)    # espace les lettres pour ne pas qu'elles se touchent

#lettre A
    begin_fill()    # commence le remplissage de la figure
    A(game)    # appelle la fonction pour dessiner la lettre correspondante
    end_fill()    # termine le remplissage de la figure

    between(17*game)    # espace les lettres pour ne pas qu'elles se touchent

#lettre M
    begin_fill()    # commence le remplissage de la figure
    M(game)    # appelle la fonction pour dessiner la lettre correspondante
    end_fill()    # termine le remplissage de la figure

    between(17*game)    # espace les lettres pour ne pas qu'elles se touchent

#lettre E
    begin_fill()    # commence le remplissage de la figure
    E(game)    # appelle la fonction pour dessiner la lettre correspondante
    end_fill()    # termine le remplissage de la figure


    between(25*game)    # espace les lettres pour ne pas qu'elles se touchent


#lettre O
    begin_fill()    # commence le remplissage de la figure
    O(game)    # appelle la fonction pour dessiner la lettre correspondante
    end_fill()    # termine le remplissage de la figure

    between(17*game)    # espace les lettres pour ne pas qu'elles se touchent

#lettre V
    begin_fill()    # commence le remplissage de la figure
    V(game)    # appelle la fonction pour dessiner la lettre correspondante
    end_fill()    # termine le remplissage de la figure

    between(17*game)    # espace les lettres pour ne pas qu'elles se touchent

#lettre E
    begin_fill()    # commence le remplissage de la figure
    E(game)    # appelle la fonction pour dessiner la lettre correspondante
    end_fill()    # termine le remplissage de la figure

    between(17*game)    # espace les lettres pour ne pas qu'elles se touchent

#lettre R
    begin_fill()    # commence le remplissage de la figure
    R(game)    # appelle la fonction pour dessiner la lettre correspondante
    end_fill()    # termine le remplissage de la figure

    # cette fonction sert à dessiner GAME OVER en rouge de taille "game" en appelant les fonctions G; A; M; E; O; V; R; between



def cheese(fromage):      # je deffini la fonction "cheese" avec une variable "fromage"
    pendown()              # pose le stylo pour pouvoir dessiner
    width(2)               # je rend le trait du stylo un peu moins gros
    fillcolor("yellow")    # choisis de remplir en jaune cette figure 
    begin_fill()           # je commence le remplissage
    for i in range(2):     # repete les instructions suivantes deux fois :
        f(5*fromage)       # avance de 5*fromage
        r()                # appel la fonction "r" pour tourner à droite de 90°
        f(3*fromage)       # avance de 3*fromage
        r()                # appel la fonction "r" pour tourner à droite de 90°
    f(5*fromage)           # avance de 5*fromage 
    l()                    # appel la fonction "l" pour tourner à gauche de 90°
    circle(3*fromage, 50)  # créer un arc de cercle
    left(70)               # tourne à gauche de 70°
    f(4.5*fromage)           # avance de 5*fromage
    left(150)              # tourne à gauche de 150°
    end_fill()             # fin du remplissage
    penup()                # leve le stylo pour se déplacer sans dessiner
    #cette fonction me sert à dessiner un fromage de taille "fromage"




## appel des fonctions pour créer le dessin final



penup()                     # je commence par levé le stylo pour ne pas que ça dessine un trait quand le stylo va ce placer


goto(1000, -500)            # je place le stylo tout en bas en droite carrement hors de l'écran 
right(180)                  # je fais faire un demi tour au le stylo pour qu'il soit dans le bon sens pour dessiné la fonction qui arrive


fond("grey")                      # j'appelle la fonction "fond" et la dessine en gris
 

goto(0, -40)                # je place le stylo un peu vers le bas et au milieu
right(180)                  # je fais faire un demi tour au le stylo pour qu'il soit dans le bon sens pour dessiné la fonction qui arrive


width(10)                   # je fais grossir le trait du stylo pour tout les dessins qui suivent


mouse_os(20)               # appel la fonction "mouse_os" avec la taille 20


goto(-725, -370)           # je place le stylo en bas a gauche pour aller executer la fonction suivante


game_over(10)              # appel la fonction  "game_over" de taille 10


goto(475, -390)            # place le stylo en bas à droite


write("Antoine AMANS, Léo HERNANDEZ, Stanislas CAMELOT")  # écrit "Antoine AMANS, Léo HERNANDEZ, Stanislas CAMELOT"


goto(-150, 300)           # place le stylo en haut et centre le texte suivant au milieu 


write("L'équipe LAS a été meilleure que vous ;)", font=("arial", 12))  # écrit "L'équipe LAS a été meilleure que vous ;)" en arial taille 12


goto(-150, 275)          # place le stylo juste un peu en dessous


write("Montrez nous que vous êtes meilleurs, réessayez !", font=("arial", 12)) # écrit "Prouvez que vous êtes meilleurs, réessayez !" en arial taille 12


goto(-775, 325)   #place ce le stylo en haut à guauche de l'ecran  


write("Votre souris a mangé tout ces fromages :", font=("arial", 13)) # écrit "Nombre de fromage que votre souris a mangé :" en arial taille 13


goto(-750, 275)    # place le stylo un peu en dessous
right(180)          # je fais faire un demi tour au le stylo pour qu'il soit dans le bon sens pour dessiné la fonction qui arrive

###

score = 92

####

i = 0                       # j'assimile la valeur 0 à la variable i

for i in range(score):      # repete "score" foix 
    if score > 60:         # si score est superieur à 60 faire les instrction suivante :
        clear()             # effacer tout les dessin d'avent
        penup()                     # je commence par levé le stylo pour ne pas que ça dessine un trait quand le stylo va ce placer
        goto(1000, -500)            # je place le stylo tout en bas en droite carrement hors de l'écran 
        right(180)                  # je fais faire un demi tour au le stylo pour qu'il soit dans le bon sens pour dessiné la fonction qui arrive
        fond("pink")                      # j'appelle la fonction "fond" et la dessine en rose
        goto(0, 0)                  # depalce le stylo au melieu
        l()                         # appel la fonction "l" pour tourner à gauche de 90°
        width(10)                   # je fais grossir le trait du stylo pour tout les dessins qui suivent
        mouse_c(30)                 # j'appelle la fonctin mouse_c en taille 30 pour dessiner une grosse souris contente 
        goto(-750, 0)               # déplace le stylo tout à auche au milieu
        write("OMG !!! votre souris à mangé plus de 60 fromages avant de mourir!!!", font=("arial", 34))  # écrit "impossible !!! votre souris à mangé plus de 60 fromage avant de mourir!!!" en "arial" taille 34
        break                                                                                    # cette commande me sert a arréter le programme si ça arrive jusqu'ici
        # ce if me permet de si le score est superieur à 160 tout effacer et dessiner tout un nouveau truck
    cheese(14)   # j'appelle la fonction cheese pour dessiner des frmoge de taille 7
    f(90)       # j'avance de 45 pour me decaler et me replacer pour aller dessiner le prochain fromage si besoin
    i += 1      # fais +1 a le variable "i"
    if i % 5 == 0:  # si quand je fais le division entiére de "i" par 5 c'est égal à 0 :
        b(450)       # reculer de 450
        r()          # appel la fonction "r" pour tourner à droite de 90°
        f(80)        # avance de 50
        l()          # appel la fonction "l" pour tourner à gauche de 90°
        # ce if me permet de faire une nouvel ligne de fromage tous les 10 fromage cela et plus facile pour compter vite
    if i == 30:          # si la variable "i" et égal à 30 :
        goto(450, 325)   # le stylo va en haut à droite de l'écran
        write("Vous êtes vraiment fort !", font=("arial", 15)) # écrit "vous êtes vraiment fort !!!!" en "arial" taille 15
        goto(300, 275)   # le stylo se place en dessous pour dessiner d'autre fromage
        # ce if me permet d'aller de l'autre coté de la souris morte pour aller dessiner d'autre fromage si il y a plus de 80 fromage à dessiner


exitonclick()           # permet de sortir du script en cliquant sur la fenêtre