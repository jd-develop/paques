#!/usr/bin/env python3
# dev by Jean Dubois
# This program is in the public domain, open source.
# Ce programme est dans le domaine public, en "open source"
# dev from 02-19-2020 to 05-25-2020
# developpé du 19/02/2020 au 25/05/2020
# version 3.0 (release)

# Importation de Tkinter pour faire des fenêtres.
from tkinter import *
from datetime import *
import webbrowser

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
        if str(year_entry.get()) == "easter":
            result_window = Tk()
            result_window.title("Erreur")
            result_window.geometry("300x50")
            result_window.minsize(300, 50)
            result_window.maxsize(500, 100)
            result_window.iconbitmap('icon.ico')
            result_window.config(background='#87CEEB')
            easter_label = Label(result_window, text="EASTER EGG !", font=('Tahoma', 10), bg='#87CEEB')
            easter_label.pack()
            result_window.mainloop()
        elif str(year_entry.get()) == "":
            # Renvoyer un message d'érreur
            result_window = Tk()
            result_window.title("Erreur")
            result_window.geometry("300x50")
            result_window.minsize(300, 50)
            result_window.maxsize(500, 100)
            result_window.iconbitmap('icon.ico')
            result_window.config(background='#87CEEB')
            error_label = Label(result_window, text="ERREUR : Le champ d'entrée est vide.", font=('Tahoma', 10),
                                bg='#87CEEB')
            error_label.pack()
            result_window.mainloop()
        else:
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

        paquestimedelta = datetime(year, m, j)
        ascensiontimedelta = paquestimedelta + timedelta(39)
        ascension = str(ascensiontimedelta)
        ascension = ascension[:10]
        ascension = ascension.split("-")
        mascension = ascension[1]
        jascension = ascension[2]

        pentecotetimedelta = ascensiontimedelta + timedelta(10)
        pentecote = str(pentecotetimedelta)
        pentecote = pentecote[:10]
        pentecote = pentecote.split("-")
        mpentecote = pentecote[1]
        jpentecote = pentecote[2]

        # améliorations de la leture
        if m == 3:
            mstring = "mars"
        else:
            mstring = "avril"

        if int(mascension) == 3:
            mascensionstring = "mars"
        elif int(mascension) == 4:
            mascensionstring = "avril"
        elif int(mascension) == 5:
            mascensionstring = "mai"
        else:
            mascensionstring = "juin"

        if int(mpentecote) == 3:
            mpentecotestr = "mars"
        elif int(mpentecote) == 4:
            mpentecotestr = "avril"
        elif int(mpentecote) == 5:
            mpentecotestr = "mai"
        elif int(mpentecote) == 6:
            mpentecotestr = "juin"
        else:
            mpentecotestr = "juillet"

        if mlundi == 3:
            mlstring = "mars"
        else:
            mlstring = "avril"

        if j == 1:
            j = "premier"

        if lundi == 1:
            lundi = "premier"

        if str(jascension) == "01":
            jascension = "premier"

        # tombe ou tombera ?
        currentyear = datetime.today().strftime("%Y")
        currentmonth = datetime.today().strftime("%m")
        currentday = datetime.today().strftime("%d")
        if year == int(currentyear):
            if m == int(currentmonth):
                if j > int(currentday):
                    tot = 'tombera'
                elif j == int(currentday):
                    tot = 'tombe'
                else:
                    tot = 'tombait'
            elif m > int(currentmonth):
                tot = 'tombera'
            else:
                tot = 'tombait'
        elif year > int(currentyear):
            tot = 'tombera'
        else:
            tot = 'tombait'

        # résultat
        result_window = Tk()
        result_window.title("Résultat")
        result_window.geometry("500x100")
        result_window.minsize(500, 100)
        result_window.maxsize(500, 100)
        result_window.iconbitmap('icon.ico')
        result_window.config(background='#87CEEB')
        result_label_sunday = Label(result_window, text=("Pour l'année " + str(year) + ", le dimanche de pâques " + tot
                                                         + " le " + str(j) + " " + mstring + ","), font=('Tahoma', 10),
                                    bg='#87CEEB')
        result_label_monday = Label(result_window, text=("le lundi de pâques le " + str(lundi) + " " + mlstring + ", "),
                                    font=('Tahoma', 10), bg='#87CEEB')
        result_label_ascension = Label(result_window, text=("le jeudi de l'ascension le " + str(jascension) + " "
                                                            + str(mascensionstring) + ","),
                                       font=('Tahoma', 10), bg='#87CEEB')
        result_label_pentecote = Label(result_window, text=("et le dimanche de la pentecôte le " + str(jpentecote) + " "
                                                            + str(mpentecotestr) + "."),
                                       font=('Tahoma', 10), bg='#87CEEB')
        result_label_sunday.pack()
        result_label_monday.pack()
        result_label_ascension.pack()
        result_label_pentecote.pack()
        result_window.mainloop()


def about():
    about_window = Tk()
    about_window.title("À propos de PâquesCalculator")
    about_window.geometry("800x200")
    about_window.minsize(800, 200)
    about_window.maxsize(800, 200)
    about_window.iconbitmap('icon.ico')
    about_window.config(background='#87CEEB')
    about_title = Label(about_window, text='PâquesCalculator', font=('Tahoma', 40), bg='#87CEEB')
    author_subtitle = Label(about_window, text='Créé par {}'.format(__author__), font=('Tahoma', 10), bg='#87CEEB')
    version_subtitle = Label(about_window, text='version {}'.format(__version__), font=('Tahoma', 10), bg='#87CEEB')
    subtitle = Label(about_window, text='', bg='#87CEEB')
    wiki_label = Label(about_window, text='Calcul trouvé sur Wikipédia', font="Tahoma 10 underline", bg='#87CEEB',
                       foreground='#FF4500', cursor='hand2')
    about_title.pack()
    author_subtitle.pack()
    version_subtitle.pack()
    subtitle.pack()
    wiki_label.pack()
    wiki_label.bind("<Button-1>",
                    lambda e: webbrowser.open_new(r"https://fr.wikipedia.org/wiki/Calcul_de_la_date_de_P%C3%A2ques"))
    about_window.mainloop()


__version__ = "3.0"
__author__ = "Jean Dubois <jd-dev@laposte.net>"

# Fabrication de la fenêtre
main_window = Tk()
main_window.title("PâquesCalculator")
main_window.geometry("900x500")
main_window.minsize(900, 500)
main_window.iconbitmap('icon.ico')
main_window.config(background='#87CEEB')

# Fabrication d'une "boîte"
frame1 = Frame(main_window, bg='#87CEEB')

# Fabrication de texte à l'interieur de la boîte
label_title = Label(frame1, text='PâquesCalculator', font=('Tahoma', 40), bg='#87CEEB')
label_title.pack()

label_subtitle = Label(frame1, text='', font=('Tahoma', 10), bg='#87CEEB')
label_subtitle.pack()

label_subtitle1 = Label(frame1, text='', font=('Tahoma', 10), bg='#87CEEB')
label_subtitle1.pack()

label_subtitle2 = Label(frame1, text="Veuillez entrer l'année pour laquelle vous souhaitez connaître la date de pâques"
                                     ", celle de l'ascencion et celle de la pentecôte :", font=('Tahoma', 10),
                        bg='#87CEEB')
label_subtitle2.pack()

# Création d'une entrée input
year_entry = Entry(frame1, font=('Tahoma', 10), bg='#87CEEB')
year_entry.pack()

# Création d'un bouton dans la boîte
get_year_button = Button(frame1, text='OK', font=('Tahoma', 15), bg='#87CEEB',
                         command=lambda: get_year())
get_year_button.pack()

# Barre de menus
menu_bar = Menu(main_window)
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label='Soumettre cette année', command=lambda: get_year())
file_menu.add_command(label='À propos de PâquesCalculator', command=lambda: about())
file_menu.add_command(label='Quitter', command=lambda: quit(0))
menu_bar.add_cascade(label='Options', menu=file_menu)
main_window.config(menu=menu_bar)

# "Empaquetage" de la boîte et de la fenêtre
frame1.pack(expand=YES)
main_window.mainloop()

# Merci d'avoir utilisé mon programme :) !
