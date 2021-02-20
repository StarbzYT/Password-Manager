from tkinter import *
from tkinter.ttk import *
from db import Database

database = Database("passwords.db")


class Application:
    def __init__(self):
        window = Tk()  # mainframe/root
        window.title("Password Manager")
        window.geometry("750x600")
        icon = PhotoImage(file='lock-icon.png')
        # Setting icon png type file
        window.iconphoto(False, icon)


app = Application()
