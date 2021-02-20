from tkinter import *
from tkinter.ttk import *
from db import Database

database = Database("passwords.db")


class Application:
    window = Tk()  # mainframe/root

    def __init__(self):
        Application.window.title("Password Manager")
        Application.window.geometry("650x500")
        icon = PhotoImage(file='lock-icon.png')
        # Setting icon png type file
        Application.window.iconphoto(False, icon)
        self.widgets()  # run widgets method to get all widgets

    # create widgets
    def widgets(self):
        website_label = Label(Application.window,
                              text="Website", font=("calibre", 12, "bold"))
        website_label.grid(column=0, row=0)
        # input box for website
        website = Entry(Application.window, font=("calibre", 12, "normal"))
        website.grid(column=1, row=0)
        password_label = Label(
            Application.window, text="Password", font=("calibre", 12, "bold"))
        password_label.grid(column=2, row=0)
        # input box for password
        password = Entry(Application.window, font=("calibre", 12, "normal"))
        password.grid(column=3, row=0)
        # buttons


app = Application()
Application.window.mainloop()
