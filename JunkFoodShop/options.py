import json
import tkinter as tk
from tkinter import*

import login
import register
import menu


def welcome(selection):

    print("\nWelcome to the JunkFood Delivery!\n1. Login\n2. Register\n3. Menu\n0. Exit")
    selection = 0
    try:
        selection = input()
        selection = int(selection)
    except ValueError:
        print("Please enter the number in the list")

    if selection == 1:
        login.login_page(username="", password="")
    if selection == 2:
        register.register_user(user="",password="")
    if selection == 3:
        menu.Menu()
    if selection == 0:
        print("ByeBye!")
        quit()
    return selection

def login_options():
    pass

