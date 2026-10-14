#main

import customtkinter

customtkinter.set_appearance_mode("dark") #applique le mode sombre à la fenètre

#Création d'une classe --> permet l'utilisation de "self" (toutes les méthodes peuvent accéder aux mêmes données) + meilleur organisation de tous les objets
class Game(customtkinter.CTk):
    def __init__(self): #initialisation de la fenètre avec "__init__" qui permet d'éxécuter directement la fonction dès l'appel d'un objet
        super().__init__() #appel la classe parente
        self.geometry("900x800+600+200") #taille de la fenêtre (900px par 800px) + position sur l'écran (600px en x et 200px en y)
        self.title("Snake Game") #titre de la fenètre
        self.resizable(False, False) #la taille de la fenêtre ne peut pas être modifier

        #Création de la zone de jeu à l'aide d'un canva
        self.canva_width = 600 #largeur de la fenètre de 600px
        self.canva_height = 500 #hauteur de la fenètre de 500px
        self.canva = customtkinter.CTkCanvas(  #création du canva
            self, #le canva est un enfant de la classe "Game"
            width=self.canva_width, #largeur de la fenètre
            height=self.canva_height, #hauteur de la fenètre
            bg ="#2b2b2b" #couleur de l'arrère plan
        )
        self.canva.pack(pady=20) #"pack()" insère le widget (l'objet) dans la fenètre parent et "pady=20" créer une marge de 20px en haut + en bas

        #Création d'un frame pour regrouper les boutons de direction
        self.controls_frame = customtkinter.CTkFrame( #création du conteneur=cadre=frame
            self, #le frame est un enfant de "Game"
            fg_color="transparent" #le frame est invisible
        )
        self.controls_frame.pack(pady=10) #"pack()" insère le widget (l'objet) dans la fenètre parent et "pady=10" créer une marge de 10px en haut + en bas

        #Création des boutons de directions
        self.btn_up = customtkinter.CTkButton( #création du bouton pour aller vers le haut
            self.controls_frame, #le bouton sera rangé dans le frame crée plus tôt ("control_frame")
            text="up", #le bouton affiche "up"
            width=60, #largeur du bouton de 60px
            height=50, #hauteur du bouton de 50px
            command=lambda: self.change_direction("HAUT") #le lambda passe "HAUT" en argument de change_direction() lorsque l'on clique sur le bouton
        )
        self.btn_up.grid(row=0, column=1, padx=5, pady=5) #position du bouton dans la fenètre

        self.btn_down = customtkinter.CTkButton( #création du bouton pour aller vers le bas
            self.controls_frame, #le bouton sera rangé dans le frame crée plus tôt ("control_frame")
            text="down", #le bouton affiche "down"
            width=60, #largeur du bouton de 60px
            height=50, #hauteur du bouton de 50px 
            command=lambda: self.change_direction("BAS") #le lambda passe "BAS" en argument de change_direction() lorsque l'on clique sur le bouton
        )
        self.btn_down.grid(row=2, column=1, padx=5, pady=5) #position du bouton dans la fenètre

        self.btn_left = customtkinter.CTkButton( #création du bouton pour aller vers la gauche
            self.controls_frame, #le bouton sera rangé dans le frame crée plus tôt ("control_frame")
            text="left", #le bouton affiche "left"
            width=60, #largeur du bouton de 60px
            height=50, #hauteur du bouton de 50px
            command=lambda: self.change_direction("GAUCHE") #le lambda passe "GAUCHE" en argument de change_direction() lorsque l'on clique sur le bouton
        )
        self.btn_left.grid(row=1, column=0, padx=5, pady=5) #position du bouton dans la fenètre

        self.btn_right = customtkinter.CTkButton( #création du bouton pour aller vers la droite
            self.controls_frame, #le bouton sera rangé dans le frame crée plus tôt ("control_frame")
            text="right", #le bouton affiche "right"
            width=60, #largeur du bouton de 60px
            height=50, #hauteur du bouton de 50px
            command=lambda: self.change_direction("DROITE") #le lambda passe "DROITE" en argument de  change_direction() lorsque l'on clique sur le bouton
        )
        self.btn_right.grid(row=1, column=2, padx=5, pady=5) #position du bouton dans la fenètre
        
    def change_direction(self, direction): #méthode que l'on utilise pour l'instant dans le but de tester nos boutons directionnelles
        print(f"Direction demandée : {direction}") #afficher dans la console la direction souhaitée par l'utilisateur 

if __name__ == "__main__": #vérification que le fichier exécuté est bien le fichier "main.py"
    game = Game() #création d'un objet, stocké dans "game" + exécution de __init__
    game.mainloop() #lancement de l'interface graphique