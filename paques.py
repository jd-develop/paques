#!/usr/bin/env python3
# dev by Jean Dubois
# This program is in the public domain, open source.
# Ce programme est dans le domaine public, en "open source"
# dev from 02-19-2020 to 05-25-2020
# developpé du 19/02/2020 au 25/05/2020
# version 2.0.2 (release)

# Importation de Tkinter pour faire des fenêtres.
from tkinter import *

# créaion de la variable year
year = 0


# definition de la commande qui récupère l'année
def get_year():
    # récupération de l'année
    global year
    # Vérification de la valeur donnée
    try:
        # Définition de l'année et lancement du calcul
        year = int(year_entry.get())
        calcul()
    except ValueError:
        # Renvoyer un message d'érreur
        result_window = Tk()
        result_window.title("Erreur")
        result_window.geometry("300x50")
        result_window.minsize(300, 50)
        result_window.maxsize(500, 100)
        result_window.iconbitmap('icon.ico')
        result_window.config(background='#87CEEB')
        error_label = Label(result_window, text="ERREUR : Vous devez entrer un nombre entier.", font=('Tahoma', 10),
                            bg='#87CEEB')
        error_label.pack()
        result_window.mainloop()


# definition de la commande qui calcule
def calcul():
    # récupération de l'année et de la fenêtre
    global year
    global main_window
    # Vérification de l'année
    # 'if' veut dire 'si' en anglais. 'else', c'est 'sinon', 'elif', c'est 'sinon, si'.
    if int(year) < 1583:
        # Message d'érreur
        result_window = Tk()
        result_window.title("Erreur")
        result_window.geometry("800x100")
        result_window.minsize(800, 100)
        result_window.maxsize(800, 100)
        result_window.iconbitmap('icon.ico')
        result_window.config(background='#87CEEB')
        error_label = Label(result_window, text=("ERREUR : L'année doit être supérieure ou égale à 1583."
                                                 " Merci de spécifier une autre année que " + str(year) + "."),
                            font=('Tahoma', 10), bg='#87CEEB')
        error_label.pack()
        result_window.mainloop()
    else:
        # CALCUL
        # Ici, le % permet de faire le modulo (le reste d'une division Euclidienne). +, *, - et / sont les opérations
        # mathématiques de base, à savoir respectivement addition, multiplication, soustraction et division.
        # 'int()' permet d'avoir la partie entière (le quotient) d'une division Euclidienne.
        n = year % 19
        c = int(year / 100)
        u = year % 100
        s = int(c / 4)
        t = c & 4
        p = int((c + 8) / 25)
        q = int((c - p + 1) / 3)
        e = (19 * n + c - s - q + 15) % 30
        b = int(u / 4)
        d = u % 4
        lvariable = (2 * t + 2 * b - e - d + 32) % 7
        h = int((n + 11 * e + 22 * lvariable) / 451)
        m = int((e + lvariable - 7 * h + 114) / 31)
        j = (e + lvariable - 7 * h + 114) % 31
        lundi = j + 1
        mlundi = m

        # correction pour lundi = 32

        if lundi == 32:
            lundi = "premier"
            mlundi = m + 1

        # correction si le dimanche tombe le 1er avril

        if j == 0 and m == 4:
            j = "premier"
            lundi = "2"

        # NOTE : pour le dimanche de pâques, pas besoin de faire la même correction que le lundi, car
        # si le dimanche est le 1er avril, comme en 2018, alors j = 0

        # améliorations de la leture

        if m == 3:
            mstring = "mars"
        else:
            mstring = "avril"

        if mlundi == 3:
            mlstring = "mars"
        else:
            mlstring = "avril"

        if j == 1:
            j = "premier"

        if lundi == 1:
            lundi = "premier"

        # résultat
        result_window = Tk()
        result_window.title("Résultat")
        result_window.geometry("500x100")
        result_window.minsize(500, 100)
        result_window.maxsize(500, 100)
        result_window.iconbitmap('icon.ico')
        result_window.config(background='#87CEEB')
        result_label_sunday = Label(result_window, text=("Pour l'année " + str(year) + ", le dimanche de pâques tombe"
                                                                                       " le "
                                    + str(j) + " " + mstring + "."), font=('Tahoma', 10), bg='#87CEEB')
        result_label_monday = Label(result_window, text=("Le lundi de pâques tombe donc le " + str(lundi) + " "
                                                         + mlstring + "."),
                                    font=('Tahoma', 10), bg='#87CEEB')
        result_label_sunday.pack()
        result_label_monday.pack()
        result_window.mainloop()
        return [result_label_monday, result_label_sunday]


__version__ = "2.0.1"
__author__ = "Jean Dubois <jd-dev@laposte.net>"

# Fabrication de la fenêtre
main_window = Tk()
main_window.title("PâquesCalculator by Jean Dubois")
main_window.geometry("900x500")
main_window.minsize(900, 500)
main_window.iconbitmap('icon.ico')
main_window.config(background='#87CEEB')

# Fabrication d'une "boîte"
frame1 = Frame(main_window, bg='#87CEEB')

# Fabrication de texte à l'interieur de la boîte
label_title = Label(frame1, text='PâquesCalculator', font=('Tahoma', 40), bg='#87CEEB')
label_title.pack()

label_subtitle = Label(frame1, text='Créé par {}'.format(__author__), font=('Tahoma', 10), bg='#87CEEB')
label_subtitle.pack()

label_subtitle1 = Label(frame1, text='version {}'.format(__version__), font=('Tahoma', 10), bg='#87CEEB')
label_subtitle1.pack()

label_subtitle2 = Label(frame1, text="Veuillez entrer l'année pour laquelle vous souhaitez connaître la date de pâques"
                                     " :", font=('Tahoma', 10), bg='#87CEEB')
label_subtitle2.pack()

# Création d'une entrée input
year_entry = Entry(frame1, font=('Tahoma', 10), bg='#87CEEB')
year_entry.pack()

# Création d'un bouton dans la boîte
get_year_button = Button(frame1, text='OK', font=('Tahoma', 15), bg='#87CEEB',
                         command=lambda: get_year())
get_year_button.pack()

# "Empaquetage" de la boîte et de la fenêtre
frame1.pack(expand=YES)
main_window.mainloop()

# Le calcul a été trouvé sur : "https://fr.wikipedia.org/wiki/Calcul_de_la_date_de_P%C3%A2ques"

print("À bientôt ;)")
# Merci d'avoir utilisé mon programme :) !
