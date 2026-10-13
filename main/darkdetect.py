# Fichier darkdetect.py de secours pour la NSI
import tkinter as tk

def theme():
    # Par défaut, on retourne 'Light' pour éviter tout plantage sur les PC du lycée
    return "Light"

def isDark():
    return False

def isLight():
    return True

def listener(callback):
    # Fonction vide obligatoire requise par CustomTkinter
    pass
