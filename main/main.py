#main

import customtkinter
import random
import subprocess # bibliothèque qui permet d'exécuter des fichiers

customtkinter.set_appearance_mode("dark") # applique le mode sombre à la fenêtre

# Création d'une classe --> permet l'utilisation de "self" (toutes les méthodes peuvent accéder aux mêmes données) + meilleure organisation de tous les objets
class Game(customtkinter.CTk):
    def __init__(self): # initialisation de la fenêtre avec "__init__" qui permet d'exécuter directement la fonction dès l'appel d'un objet
        super().__init__() # appelle la classe parente
        self.geometry("900x800+600+200") # taille de la fenêtre (900px par 800px) + position sur l'écran (600px en x et 200px en y)
        self.title("Mouse Game") # titre de la fenêtre : "Mouse Game"
        self.resizable(False, False) # la taille de la fenêtre ne peut pas être modifiée

        self.create_menu() # lance l'affichage du menu principal au démarrage

    def create_menu(self): # Crée l'écran d'accueil avec les boutons Play et Exit
        self.menu_frame = customtkinter.CTkFrame(self, fg_color="transparent")
        self.menu_frame.pack(expand=True)

        self.title_label = customtkinter.CTkLabel( # création d'un label qui permet d'afficher le titre de la fenetre avec la bibliothèque customtkinter et la méthode CTkLabel()
            self.menu_frame, # le label est un enfant de menu_frame
            text="MOUSE GAME", # le label affiche "Mouse Game"
            font=("Arial", 40, "bold") # utilisation d'une police Arial de 40px en gras
        )
        self.title_label.pack(pady=30) # on affiche le label avec .pack (affiche l'objet à l'écran), et une marge verticale de 30px avec pady=30

        self.btn_play = customtkinter.CTkButton( # création d'un bouton "play" avec la bibliothèque customtkinter et la méthode CTkButton()
            self.menu_frame, # le bouton est un enfant de menu_frame
            text="Play", # le bouton affiche "Play"
            width=220, # le bouton a une largeur de 220px
            height=60, # le bouton a une hauteur de 60px
            font=("Arial", 22), # utilisation d'une police Arial de 22px
            command=self.start_game # lorsque ce bouton est cliqué, lance la partie en exécutant la méthode "start_game"
        )
        self.btn_play.pack(pady=15) # on affiche le bouton avec .pack et une marge verticale de 15px avec pady=15

        self.btn_exit = customtkinter.CTkButton( # création d'un bouton "exit" avec la bibliothèque customtkinter et la méthode CTkButton()
            self.menu_frame, # le bouton est un enfant de menu_frame
            text="Exit", # le bouton affiche "Exit"
            width=220, # le bouton a une largeur de 220px
            height=60, # le bouton a une hauteur de 60px
            font=("Arial", 22), # utilisation d'une police Arial de 22px
            fg_color="red", # couleur du bouton
            hover_color="darkred", # couleur lorsque l'on passe la souris sur le bouton
            command=self.destroy # ferme la fenetre avec .destroy si le joueur clique sur le bouton
        )
        self.btn_exit.pack(pady=15)

    def start_game(self): # Efface le menu et initialise le jeu
        self.menu_frame.destroy() # on ferme la fenetre du menu d'accueil avec .destroy
        
        # Création de la zone de jeu à l'aide d'un canva
        self.canva_width = 500 # largeur de la fenêtre de 500px
        self.canva_height = 500 # hauteur de la fenêtre de 500px
        self.canva = customtkinter.CTkCanvas(  # création du canva
            self, # le canva est un enfant de la classe "Game"
            width=self.canva_width, # largeur de la fenêtre
            height=self.canva_height, # hauteur de la fenêtre
            bg ="#DEB887" # couleur de l'arrière plan
        )
        self.canva.pack(pady=20) # "pack()" insère le widget dans la fenêtre parent et "pady=20" crée une marge de 20px en haut + en bas

        # =================================================================================ANTOINE Début==========================================================================
        # Création du quadrillage
        # 1. Création des lignes du quadrillage
        ligne1 = self.canva.create_line(0, 50, 500, 50, fill="black") # création d'une ligne horizontale à 50px du haut de la fenêtre cela correspond à (X_début, Y_début, X_fin, Y_fin)
        ligne2 = self.canva.create_line(0, 100, 500, 100, fill="black") # création d'une ligne horizontale à 100px du haut de la fenêtre
        ligne3 = self.canva.create_line(0, 150, 500, 150, fill="black") # création d'une ligne horizontale à 150px du haut de la fenêtre
        ligne4 = self.canva.create_line(0, 200, 500, 200, fill="black") # création d'une ligne horizontale à 200px du haut de la fenêtre
        ligne5 = self.canva.create_line(0, 250, 500, 250, fill="black") # création d'une ligne horizontale à 250px du haut de la fenêtre
        ligne6 = self.canva.create_line(0, 300, 500, 300, fill="black") # création d'une ligne horizontale à 300px du haut de la fenêtre
        ligne7 = self.canva.create_line(0, 350, 500, 350, fill="black") # création d'une ligne horizontale à 350px du haut de la fenêtre
        ligne8 = self.canva.create_line(0, 400, 500, 400, fill="black") # création d'une ligne horizontale à 400px du haut de la fenêtre
        ligne9 = self.canva.create_line(0, 450, 500, 450, fill="black") # création d'une ligne horizontale à 450px du haut de la fenêtre

        # 2. Création des colonnes du quadrillage 
        colonne1 = self.canva.create_line(50, 0, 50, 500, fill="black") # création d'une ligne verticale à 50px du haut de la fenêtre cela correspond à (X_début, Y_début, X_fin, Y_fin)
        colonne2 = self.canva.create_line(100, 0, 100, 500, fill="black") # création d'une ligne verticale à 100px du haut de la fenêtre
        colonne3 = self.canva.create_line(150, 0, 150, 500, fill="black") # création d'une ligne verticale à 150px du haut de la fenêtre
        colonne4 = self.canva.create_line(200, 0, 200, 500, fill="black") # création d'une ligne verticale à 200px du haut de la fenêtre
        colonne5 = self.canva.create_line(250, 0, 250, 500, fill="black") # création d'une ligne verticale à 250px du haut de la fenêtre
        colonne6 = self.canva.create_line(300, 0, 300, 500, fill="black") # création d'une ligne verticale à 300px du haut de la fenêtre
        colonne7 = self.canva.create_line(350, 0, 350, 500, fill="black") # création d'une ligne verticale à 350px du haut de la fenêtre
        colonne8 = self.canva.create_line(400, 0, 400, 500, fill="black") # création d'une ligne verticale à 400px du haut de la fenêtre
        colonne9 = self.canva.create_line(450, 0, 450, 500, fill="black") # création d'une ligne verticale à 450px du haut de la fenêtre

        # Début Léo 
        # Création de l'apparition de la souris sur le canva (Gestion multi-segments type Snake)
        self.direction = "DROITE" # Définition de la direction initiale de la souris
        self.souris_coords = [
            [250, 250],
            [200, 250],
            [150, 250]  
        ] # Utilisation d'une liste de listes pour stocker les coordonnées [x, y] de chaque morceau du corps de la souris

        # Création de la position du fromage (on s'assure qu'il n'apparaît pas sur le corps de la souris)
        self.frommage_position_x = random.randrange(0, 450, 50)
        self.frommage_position_y = random.randrange(0, 450, 50)
        while [self.frommage_position_x, self.frommage_position_y] in self.souris_coords:
            self.frommage_position_x = random.randrange(0, 450, 50)
            self.frommage_position_y = random.randrange(0, 450, 50)
            
        self.frommage_taille = 50 # taille du fromage de 50px
        # Création de l'apparition du fromage sur le canva
        self.frommage = self.canva.create_rectangle( # création du fromage
            self.frommage_position_x, # position du fromage sur l'axe des x
            self.frommage_position_y, # position du fromage sur l'axe des y
            self.frommage_position_x + self.frommage_taille, # position du fromage sur l'axe des x + taille du fromage
            self.frommage_position_y + self.frommage_taille, # position du fromage sur l'axe des y + taille du fromage
            fill="#FFD700", # couleur du fromage
        )

        # Création de la position du chat
        self.chat_position_x = random.randrange(0, 450, 50) # position aléatoire du chat sur l'axe des x (de 0 à 450px avec un pas de 50px)
        self.chat_position_y = random.randrange(0, 450, 50) # position aléatoire du chat sur l'axe des y (de 0 à 450px avec un pas de 50px)
        self.chat_taille = 50 # taille du chat de 50px
        # Création de l'apparition du chat sur le canva
        self.chat = self.canva.create_rectangle( # création du chat
            self.chat_position_x, # position du chat sur l'axe x
            self.chat_position_y, # position du chat sur l'axe y
            self.chat_position_x + self.chat_taille, # position du chat sur l'axe x + taille du chat
            self.chat_position_y + self.chat_taille, # position du chat sur l'axe y + taille du chat
            fill="red", # couleur du chat
        )

        self.souris_rects = [] # Liste qui contiendra les identifiants graphiques (ID) des rectangles et yeux dessinés sur le canvas
        for index, coords in enumerate(self.souris_coords):
            rect = self.canva.create_rectangle(
                coords[0], coords[1],
                coords[0] + 50, coords[1] + 50,
                fill="green",
                outline="white",
                width=3         
            )
            self.souris_rects.append(rect)

            # Si c'est la tête de la souris (index 0), on ajoute des yeux pour voir où elle regarde !
            if index == 0:
                x, y = coords[0], coords[1]
                if self.direction == "DROITE":
                    e1 = self.canva.create_oval(x + 35, y + 10, x + 45, y + 20, fill="black")
                    e2 = self.canva.create_oval(x + 35, y + 30, x + 45, y + 40, fill="black")
                elif self.direction == "GAUCHE":
                    e1 = self.canva.create_oval(x + 5, y + 10, x + 15, y + 20, fill="black")
                    e2 = self.canva.create_oval(x + 5, y + 30, x + 15, y + 40, fill="black")
                elif self.direction == "HAUT":
                    e1 = self.canva.create_oval(x + 10, y + 5, x + 20, y + 15, fill="black")
                    e2 = self.canva.create_oval(x + 30, y + 5, x + 40, y + 15, fill="black")
                elif self.direction == "BAS":
                    e1 = self.canva.create_oval(x + 10, y + 35, x + 20, y + 45, fill="black")
                    e2 = self.canva.create_oval(x + 30, y + 35, x + 40, y + 45, fill="black")
                self.souris_rects.append(e1)
                self.souris_rects.append(e2)

        

        # On veut s'assurer que le chat et le fromage n'apparaissent pas au même endroit
        while self.chat_position_x == self.frommage_position_x and self.chat_position_y == self.frommage_position_y: # tant que le chat et le fromage sont au même endroit
            self.chat_position_x = random.randrange(0, 450, 50) # on change la position du chat sur l'axe des x
            self.chat_position_y = random.randrange(0, 450, 50) # on change la position du chat sur l'axe des y
            self.canva.coords(self.chat, self.chat_position_x, self.chat_position_y, self.chat_position_x + self.chat_taille, self.chat_position_y + self.chat_taille) # on met à jour la position du chat sur le canva

        # Fin Léo

        # Création du score
        self.score = 0 # initialisation du score à 0
        self.score_label = customtkinter.CTkLabel( # création du label pour afficher le score
            self, # le label est un enfant de la classe "Game"
            text=f"Score : {self.score}", # texte du label
            font=("Arial", 20) # police et taille du texte
        )
        # =================================================================================ANTOINE Fin==========================================================================
        
        self.score_label.pack(pady=10) # "pack()" insère le widget dans la fenêtre parent et "pady=10" crée une marge de 10px en haut + en bas

        # Création d'un frame pour regrouper les boutons de direction
        self.controls_frame = customtkinter.CTkFrame( # création du cadre
            self, # le frame est un enfant de "Game"
            fg_color="transparent" # le frame est transparent
        )
        self.controls_frame.pack(pady=10) # "pack()" insère le widget dans la fenêtre parent et "pady=10" crée une marge de 10px en haut + en bas
        
        # Création des boutons de directions
        self.btn_up = customtkinter.CTkButton( # création du bouton pour aller vers le haut
            self.controls_frame, # le bouton sera rangé dans le frame créé plus tôt ("controls_frame")
            text="up", # le bouton affiche "up"
            width=60, # largeur du bouton de 60px
            height=50, # hauteur du bouton de 50px
            command=lambda: self.change_direction("HAUT") # le lambda passe "HAUT" en argument de change_direction() lorsque l'on clique sur le bouton
        )
        self.btn_up.grid(row=0, column=1, padx=5, pady=5) # position du bouton dans la fenêtre

        self.btn_down = customtkinter.CTkButton( # création du bouton pour aller vers le bas
            self.controls_frame, # le bouton sera rangé dans le frame créé plus tôt ("controls_frame")
            text="down", # le bouton affiche "down"
            width=60, # largeur du bouton de 60px
            height=50, # hauteur du bouton de 50px 
            command=lambda: self.change_direction("BAS") # le lambda passe "BAS" en argument de change_direction() lorsque l'on clique sur le bouton
        )
        self.btn_down.grid(row=2, column=1, padx=5, pady=5) # position du bouton dans la fenêtre

        self.btn_left = customtkinter.CTkButton( # création du bouton pour aller vers la gauche
            self.controls_frame, # le bouton sera rangé dans le frame créé plus tôt ("controls_frame")
            text="left", # le bouton affiche "left"
            width=60, # largeur du bouton de 60px
            height=50, # hauteur du bouton de 50px
            command=lambda: self.change_direction("GAUCHE") # le lambda passe "GAUCHE" en argument de change_direction() lorsque l'on clique sur le bouton
        )
        self.btn_left.grid(row=1, column=0, padx=5, pady=5) # position du bouton dans la fenêtre

        self.btn_right = customtkinter.CTkButton( # création du bouton pour aller vers la droite
            self.controls_frame, # le bouton sera rangé dans le frame créé plus tôt ("controls_frame")
            text="right", # le bouton affiche "right"
            width=60, # largeur du bouton de 60px
            height=50, # hauteur du bouton de 50px
            command=lambda: self.change_direction("DROITE") # le lambda passe "DROITE" en argument de change_direction() lorsque l'on clique sur le bouton
        )
        self.btn_right.grid(row=1, column=2, padx=5, pady=5) # position du bouton dans la fenêtre

        # Mise en place des touches sur le clavier pour modifier le comportement de la souris
        # Association des flèches directionnelles
        self.bind("<Up>", lambda event: self.change_direction("HAUT")) # flèche du haut
        self.bind("<Down>", lambda event: self.change_direction("BAS")) # flèche du bas
        self.bind("<Left>", lambda event: self.change_direction("GAUCHE")) # flèche de gauche
        self.bind("<Right>", lambda event: self.change_direction("DROITE")) # flèche de droite

        # Association des touches ZQSD (minuscules et majuscules pour le verrouillage des majuscules)
        self.bind("z", lambda event: self.change_direction("HAUT"))
        self.bind("Z", lambda event: self.change_direction("HAUT"))
        self.bind("s", lambda event: self.change_direction("BAS"))
        self.bind("S", lambda event: self.change_direction("BAS"))
        self.bind("q", lambda event: self.change_direction("GAUCHE"))
        self.bind("Q", lambda event: self.change_direction("GAUCHE"))
        self.bind("d", lambda event: self.change_direction("DROITE"))
        self.bind("D", lambda event: self.change_direction("DROITE"))

        self.focus_set() # "focus_set" s'assure que la fenêtre capture bien le focus du clavier dès son lancement

        # Lancement initial de la boucle de déplacement automatique du serpent toutes les 300 millisecondes
        self.after(300, self.deplacer)
        
    def change_direction(self, nouvelle_direction): # méthode que l'on utilise pour changer la direction de la souris avec les boutons ou le clavier
        if nouvelle_direction == "HAUT" and self.direction != "BAS": # empêche d'aller en haut si on va déjà vers le bas
            self.direction = nouvelle_direction # actualisation de la position
        elif nouvelle_direction == "BAS" and self.direction != "HAUT": # empêche d'aller en bas si on va déjà vers le haut
            self.direction = nouvelle_direction # actualisation de la position
        elif nouvelle_direction == "GAUCHE" and self.direction != "DROITE": # empêche d'aller à gauche si on va déjà vers la droite
            self.direction = nouvelle_direction # actualisation de la position
        elif nouvelle_direction == "DROITE" and self.direction != "GAUCHE": # empêche d'aller à droite si on va déjà vers la gauche
            self.direction = nouvelle_direction # actualisation de la position

    def deplacer(self): # méthode qui gère le mouvement automatique, les collisions, la croissance et le rafraîchissement graphique
        tete_x, tete_y = self.souris_coords[0] # récupère les coordonnées actuelles de la tête de la souris

        # Calcule la nouvelle position de la tête selon la direction active (1 pas = 50px)
        if self.direction == "HAUT":
            tete_y -= 50 # monter = soustraction
        elif self.direction == "BAS":
            tete_y += 50 # descendre = addition
        elif self.direction == "GAUCHE":
            tete_x -= 50 # gauche = soustraction
        elif self.direction == "DROITE":
            tete_x += 50 # droite = addition

        # 1. Vérification des collisions avec les murs de la fenêtre (Fin de partie)
        if tete_x < 0 or tete_x >= 500 or tete_y < 0 or tete_y >= 500: # si la position de la tête de la souris dépasse le quadrillage
            subprocess.Popen(["python", "disign.py"]) # Lance l'écran de Game Over de Stanislas
            self.canva.destroy()
            self.score_label.destroy()
            self.controls_frame.destroy()
            self.create_menu()
            return  # Arrête l'exécution de la fonction

        # 2. Vérification de la collision avec le chat (Fin de partie)
        if tete_x == self.chat_position_x and tete_y == self.chat_position_y: # si la position de la tête de la souris = position du chat
            subprocess.Popen(["python", "disign.py"]) # Lance l'écran de Game Over de Stanislas
            self.canva.destroy()
            self.score_label.destroy()
            self.controls_frame.destroy()
            self.create_menu()
            return  # Arrête l'exécution de la fonction

        # 3. Vérification de l'auto-collision (si la tête touche son propre corps)
        if [tete_x, tete_y] in self.souris_coords:
            subprocess.Popen(["python", "disign.py"]) # Lance l'écran de Game Over de Stanislas
            self.canva.destroy()
            self.score_label.destroy()
            self.controls_frame.destroy()
            self.create_menu()
            return  # Arrête l'exécution de la fonction

        # Insère la nouvelle tête calculée au tout début de la liste des coordonnées
        self.souris_coords.insert(0, [tete_x, tete_y]) # le premier élément de la liste souris_coords devient la position de la tête calculée

        # Vérifier si la tête de la souris est sur le fromage
        fromage_coords = self.canva.coords(self.frommage) # Récupère [x1, y1, x2, y2] du fromage
        if fromage_coords and tete_x == fromage_coords[0] and tete_y == fromage_coords[1]: # si la tête est sur le fromage
            self.score += 1 # incrémentation du score par 1
            self.score_label.configure(text=f"Score : {self.score}") # configure permet de modifier le label score

            # Déplacer le fromage de manière aléatoire sur une nouvelle case (hors du corps de la souris)
            self.frommage_position_x = random.randrange(0, 450, 50)
            self.frommage_position_y = random.randrange(0, 450, 50)
            while [self.frommage_position_x, self.frommage_position_y] in self.souris_coords:
                self.frommage_position_x = random.randrange(0, 450, 50)
                self.frommage_position_y = random.randrange(0, 450, 50)

            self.canva.coords(
                self.frommage,
                self.frommage_position_x, self.frommage_position_y,
                self.frommage_position_x + 50, self.frommage_position_y + 50
            )

            # Déplacer également le chat à un nouvel endroit aléatoire à chaque fromage mangé
            self.chat_position_x = random.randrange(0, 450, 50)
            self.chat_position_y = random.randrange(0, 450, 50)
            self.canva.coords(
                self.chat,
                self.chat_position_x, self.chat_position_y,
                self.chat_position_x + self.chat_taille, self.chat_position_y + self.chat_taille
            )
        else:
            # Si on ne mange pas de fromage, on retire le dernier morceau de la queue (mouvement normal sans grandir)
            self.souris_coords.pop() # la méthode pop retire le dernier élément de la liste self.souris_coords

        # Redessiner tous les rectangles de la souris (et ses yeux) sur le canvas pour refléter le mouvement
        for rect in self.souris_rects: # pour tous les rectangles/yeux stockés
            self.canva.delete(rect) # on supprime visuellement
        self.souris_rects.clear() # on vide la liste

        # On recrée tous les segments de la souris et les yeux sur la tête selon la direction
        for index, coords in enumerate(self.souris_coords):
            rect = self.canva.create_rectangle(
                coords[0], coords[1],
                coords[0] + 50, coords[1] + 50,
                fill="green",
                outline="white",
                width=3         
            )
            self.souris_rects.append(rect)

            # Redessiner les yeux sur la tête à chaque mouvement
            if index == 0:
                x, y = coords[0], coords[1]
                if self.direction == "DROITE":
                    e1 = self.canva.create_oval(x + 35, y + 10, x + 45, y + 20, fill="black")
                    e2 = self.canva.create_oval(x + 35, y + 30, x + 45, y + 40, fill="black")
                elif self.direction == "GAUCHE":
                    e1 = self.canva.create_oval(x + 5, y + 10, x + 15, y + 20, fill="black")
                    e2 = self.canva.create_oval(x + 5, y + 30, x + 15, y + 40, fill="black")
                elif self.direction == "HAUT":
                    e1 = self.canva.create_oval(x + 10, y + 5, x + 20, y + 15, fill="black")
                    e2 = self.canva.create_oval(x + 30, y + 5, x + 40, y + 15, fill="black")
                elif self.direction == "BAS":
                    e1 = self.canva.create_oval(x + 10, y + 35, x + 20, y + 45, fill="black")
                    e2 = self.canva.create_oval(x + 30, y + 35, x + 40, y + 45, fill="black")
                self.souris_rects.append(e1)
                self.souris_rects.append(e2)

        # Relancer automatiquement cette fonction après 300 millisecondes pour maintenir l'animation (vitesse du jeu)
        self.after(250, self.deplacer)

if __name__ == "__main__": # vérification que le fichier exécuté est bien le fichier "main.py"
    game = Game() # création d'un objet, stocké dans "game" + exécution de __init__
    game.mainloop() # lancement de l'interface graphique