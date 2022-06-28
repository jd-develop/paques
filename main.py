#!/usr/bin/env python3
# PâquesCalculator : a program who calculates easter date.
# Copyright (C) 2020-2022  Jean Dubois
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

# Importation de Tkinter pour faire des fenêtres, de datetime pour calculer les dates, et de webbrowser pour ouvrir des
# pages dans le navigateur.
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from datetime import *
import webbrowser
import sys

BACKGROUND = '#87CEEB'

__version__ = "22w26a (2022-06-28)"
__author__ = "Jean Dubois <jd-dev@laposte.net>"

# création de la variable year (année)
tabsList = []


def int_month_to_str_month(month_int: int):
    calendar_ = {
        "1": "janvier",
        "2": "février",
        "3": "mars",
        "4": "avril",
        "5": "mai",
        "6": "juin",
        "7": "juillet",
        "8": "août",
        "9": "septembre",
        "10": "octobre",
        "11": "novembre",
        "12": "décembre",
    }
    return calendar_[str(month_int)]


def get_year():
    # Vérification de la valeur donnée
    try:
        # Définition de l'année et lancement du calcul
        if 9999 >= int(year_entry.get()) >= 1:
            year = int(year_entry.get())
            calcul(year)
        else:
            # Renvoyer un message d'erreur
            messagebox.showerror("Erreur", "ERREUR : Vous devez entrer un nombre entier compris entre 1 et 9999."
                                           "\n\nPLUS D'INFOS : \n"
                                           "1 est la première année où pâques est célébrée. Il est à noter que ce"
                                           "programme utilise un calcul différent entre 1 et 1582 (calendrier julien)"
                                           "et entre 1583 et 9999 (calendrier grégorien jusqu'alors)\n"
                                           "9999 est la dernière année que prends en charge l'outil Timedelta, "
                                           "nécessaire au calcul de la pentecôte et de l'ascension.")
    except ValueError:
        if str(year_entry.get()) == "easter":
            messagebox.showinfo("Easter egg", "EASTER EGG (c'est le cas de le dire :P)")
        elif str(year_entry.get()) == "":
            # Renvoyer un message d'erreur
            error_1()
        else:
            # Renvoyer un message d'erreur
            messagebox.showerror("Erreur", "ERREUR : Vous devez entrer un nombre entier compris entre 1 et 9999."
                                           "\n\nPLUS D'INFOS : \n"
                                           "1 est la première année où pâques est célébrée. Il est à noter que ce"
                                           "programme utilise un calcul différent entre 1 et 1582 (calendrier julien)"
                                           "et entre 1583 et 9999 (calendrier grégorien jusqu'alors)\n"
                                           "9999 est la dernière année que prends en charge l'outil Timedelta, "
                                           "nécessaire au calcul de la pentecôte et de l'ascension.")


# definition de la commande qui calcule
def calcul(year_):
    # récupération de l'année et de la fenêtre
    global main_window, tabs
    # CALCUL
    if year_ >= 1583:
        n = year_ % 19
        c = int(year_ / 100)
        u = year_ % 100
        s = int(c / 4)
        t = c % 4
        p = int((c + 8) / 25)
        q = int((c - p + 1) / 3)
        e = (19 * n + c - s - q + 15) % 30
        b = int(u / 4)
        d = u % 4
        ld = (2 * t + 2 * b - e - d + 32) % 7  # dans le calcul sur Wiki, c'est L
        h = int((n + 11 * e + 22 * ld) / 451)
        m = int((e + ld - 7 * h + 114) / 31)
        j = (e + ld - 7 * h + 114) % 31
    else:
        # calcul trouvé sur :
        # https://codes-sources.commentcamarche.net/source/21243-calcul-de-la-date-de-paques-ascension-et-pentecote
        # ça reprend le calcul de S Butcher : https://play.google.com/books/reader?id=qbA-rzFsIoMC&pg=GBS.PR12&hl=fr
        # je ne l'ai pas trouvé dans le livre par contre.... je serai intéressé de connaître la page :)
        a = year_ % 19
        e = year_ % 4
        i = year_ % 7
        h = (19*a + 15) % 30
        r = (34 + 2*e + 4*i - h) % 7
        m = int((h + r + 114) / 31)
        j = ((h + r + 114) % 31) + 1

    if m == 3 or m == 4:
        j += 1
    
    lundi = j + 1
    mois_lundi = m
    # correction pour lundi = 32
    if lundi == 32:
        lundi = "premier"
        mois_lundi = m + 1
    # correction si le dimanche tombe le 1er avril
    if j == 0 and m == 4:
        j = "premier"
        lundi = "2"

    # NOTE : pour le dimanche de pâques, pas besoin de faire la même correction que le lundi, car
    # si le dimanche est le 1er avril, comme en 2018, alors j = 0

    paques_timedelta = datetime(year_, m, j)
    
    ascension_timedelta = paques_timedelta + timedelta(39)
    mois_ascension = ascension_timedelta.month
    jour_ascension = ascension_timedelta.day

    pentecote_timedelta = ascension_timedelta + timedelta(10)
    mois_pentecote = pentecote_timedelta.month
    jour_pentecote = pentecote_timedelta.day

    # améliorations de la lecture
    str_month = int_month_to_str_month(m)

    mois_ascension_str = int_month_to_str_month(mois_ascension)

    mois_pentecote_str = int_month_to_str_month(mois_pentecote)

    mois_lundi_str = int_month_to_str_month(mois_lundi)

    if j == 1:
        j = "premier"

    if lundi == 1:
        lundi = "premier"

    if jour_ascension == 1:
        jour_ascension = "premier"

    if jour_pentecote == 1:
        jour_pentecote = "premier"

    # tombe ou tombera ?
    current_year = datetime.today().strftime("%Y")
    current_month = datetime.today().strftime("%m")
    current_day = datetime.today().strftime("%d")
    if year_ == int(current_year):
        if m == int(current_month):
            if j > int(current_day):
                tot = 'tombera'
            elif j == int(current_day):
                tot = 'tombe'
            else:
                tot = 'tombait'
        elif m > int(current_month):
            tot = 'tombera'
        else:
            tot = 'tombait'
    elif year_ > int(current_year):
        tot = 'tombera'
    else:
        tot = 'tombait'

    # résultat
    for tab in tabsList:
        if str(tab[0]) == str(year_):
            tabs.select(tab[1])
            return "TabSelected"

    new_frame = Frame(tabs, bg=BACKGROUND)
    result_label_sunday = Label(
        new_frame,
        text=f"Pour l'année {year_}, le dimanche de pâques {tot} le {j} {str_month},",
        font=('Tahoma', 10),
        bg=BACKGROUND
    )
    result_label_monday = Label(
        new_frame,
        text=f"le lundi de pâques le {lundi} {mois_lundi_str},",
        font=('Tahoma', 10),
        bg=BACKGROUND
    )
    result_label_ascension = Label(
        new_frame,
        text=f"le jeudi de l'ascension le {jour_ascension} {mois_ascension_str},",
        font=('Tahoma', 10),
        bg=BACKGROUND
    )
    result_label_pentecote = Label(
        new_frame,
        text=f"et le dimanche de la pentecôte le {jour_pentecote} {mois_pentecote_str}.",
        font=('Tahoma', 10),
        bg=BACKGROUND
    )

    result_label_sunday.pack()
    result_label_monday.pack()
    result_label_ascension.pack()
    result_label_pentecote.pack()

    tabs.add(new_frame, text=str(year_))
    tabs.select(new_frame)
    tab_selected = [tabs.tab(tabs.select(), "text"), tabs.select()]
    tabsList.append(tab_selected)
    close_tab_button = Button(new_frame, text="Fermer", font=('Tahoma', 10), bg=BACKGROUND,
                              command=lambda: close_tab(new_frame, tab_selected))
    close_tab_button.pack()


def close_tab(tab_frame, tab_name_in_list):
    global tabs, tabsList, frame1
    tabs.forget(tab_frame)
    tabsList.remove(tab_name_in_list)
    tabs.select(frame1)


def about():
    about_window = Tk()
    about_window.title("À propos de PâquesCalculator")
    about_window.geometry("800x200")
    about_window.minsize(800, 200)
    about_window.resizable(False, False)
    about_window.iconbitmap('icon.ico')
    about_window.config(background=BACKGROUND)
    about_title = Label(about_window, text='PâquesCalculator', font=('Tahoma', 40), bg=BACKGROUND)
    author_subtitle = Label(about_window, text=f'Copyright (C) {__author__}', font=('Tahoma', 10), bg=BACKGROUND)
    version_subtitle = Label(about_window, text=f'Version {__version__}', font=('Tahoma', 10), bg=BACKGROUND)
    open_source_mention = Label(about_window, text="Sous licence GPL3", font=('Tahoma', 10), bg=BACKGROUND)
    subtitle = Label(about_window, text='', bg=BACKGROUND)
    wiki_label = Label(about_window, text='Calcul trouvé sur Wikipédia', font="Tahoma 10 underline", bg=BACKGROUND,
                       foreground='#FF4500', cursor='hand2')
    about_title.pack()
    author_subtitle.pack()
    version_subtitle.pack()
    open_source_mention.pack()
    subtitle.pack()
    wiki_label.pack()
    wiki_label.bind("<Button-1>",
                    lambda: webbrowser.open_new(r"https://fr.wikipedia.org/wiki/Calcul_de_la_date_de_P%C3%A2ques"))
    about_window.mainloop()
    

def error_1():
    messagebox.showerror("Erreur", "ERREUR : Le champ d'entrée est vide.\n"
                                   "Vous devez entrer une année dans le champ d'entrée")


def pressed_enter(event):
    get_year()


def go_to_home_tab(event):
    global tabs, frame1
    tabs.select(frame1)


# Fabrication de la fenêtre
main_window = Tk()
main_window.title("PâquesCalculator")
main_window.geometry("900x500")
main_window.minsize(900, 500)
try:
    main_window.iconbitmap('icon.ico')
except TclError:
    pass
main_window.config(background=BACKGROUND)

tabs = ttk.Notebook(main_window)

# Fabrication d'une "boîte"
frame1 = Frame(tabs, bg=BACKGROUND)
# resultFrame = Frame(tabs, bg=BACKGROUND)
tabs.add(frame1, text="Onglet principal")
tabs.pack(expand=1, fill="both")

# Fabrication de texte à l'intérieur de la boîte
label_title = Label(frame1, text='PâquesCalculator', font=('Tahoma', 40), bg=BACKGROUND)
label_title.pack()

label_subtitle = Label(frame1, text='', font=('Tahoma', 10), bg=BACKGROUND)
label_subtitle.pack()

label_subtitle1 = Label(frame1, text='', font=('Tahoma', 10), bg=BACKGROUND)
label_subtitle1.pack()

label_subtitle2 = Label(frame1, text="Veuillez entrer l'année pour laquelle vous souhaitez connaître la date de pâques"
                                     ", celle de l'ascension et celle de la pentecôte :", font=('Tahoma', 10),
                        bg=BACKGROUND)
label_subtitle2.pack()

# Création d'une entrée input
year_entry = Entry(frame1, font=('Tahoma', 10), bg=BACKGROUND)
year_entry.pack()

# Création d'un bouton dans la boîte
get_year_button = Button(frame1, text='OK', font=('Tahoma', 15), bg=BACKGROUND,
                         command=lambda: get_year())
get_year_button.pack()

# Barre de menus
menu_bar = Menu(main_window)
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label='Soumettre cette année', command=lambda: get_year(), accelerator="Entrée")
file_menu.add_command(label='À propos de PâquesCalculator', command=lambda: about())
file_menu.add_separator()
file_menu.add_command(label="Retour à l'onglet principal", command=lambda: tabs.select(frame1), accelerator="F1")
file_menu.add_command(label='Quitter', command=lambda: quit(0), accelerator="Ctrl+q")
menu_bar.add_cascade(label='Options', menu=file_menu)
main_window.config(menu=menu_bar)

# "Empaquetage" de la boîte et de la fenêtre
# frame1.pack(expand=YES)
year_entry.focus()
main_window.bind('<Return>', pressed_enter)
main_window.bind('<F1>', go_to_home_tab)
main_window.bind('<Control-q>', sys.exit)
main_window.mainloop()

# Merci d'avoir utilisé mon programme :) !
