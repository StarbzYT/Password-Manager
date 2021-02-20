from tkinter import *
from db import Database

database = Database("passwords")


class Application:
    window = Tk()  # mainframe/root (class attribute)

    def __init__(self):
        Application.window.title("Password Manager")
        Application.window.geometry("700x550")
        icon = PhotoImage(file='lock-icon.png')
        # Setting icon png type file
        Application.window.iconphoto(False, icon)
        # run to get all widgets i.e buttons, labels, etc
        self.labels()
        self.buttons()
        self.list_box()

    # create labels and input boxes
    def labels(self):
        website_label = Label(Application.window,
                              text="Website", font=("calibre", 12, "bold"))
        website_label.grid(column=0, row=0, pady=20)
        # input box for website
        website = Entry(Application.window, font=("calibre", 12, "normal"))
        website.grid(column=1, row=0, pady=20)
        password_label = Label(
            Application.window, text="Password", font=("calibre", 12, "bold"))
        password_label.grid(column=2, row=0, pady=20)
        # input box for password
        password = Entry(Application.window, font=("calibre", 12, "normal"))
        password.grid(column=3, row=0, pady=20)

    # create buttons
    def buttons(self):
        # buttons
        add_password = Button(Application.window,
                              text="Add Password", bg="green", bd="3", width=14)
        add_password.grid(column=0, row=1, pady=20, padx=15)
        delete_password = Button(Application.window,
                                 text="Delete Password", bg="red", bd="3", width=14)
        delete_password.grid(column=1, row=1, pady=20, padx=15)
        update_password = Button(
            Application.window, text="Update Password", bd="3", width=14)
        update_password.grid(column=2, row=1, pady=20, padx=15)
        clear_input = Button(
            Application.window, text="Clear Input", bd="3", width=14)
        clear_input.grid(column=3, row=1, pady=20, padx=15)

    # list box to store website and passwords
    def list_box(self):
        data = Listbox(Application.window, height=20, width=80, border=0)
        data.grid(column=0, row=3, columnspan=4,
                  rowspan=3, pady=20, padx=15)
        # scrollbar/slider
        # Create scrollbar
        scrollbar = Scrollbar(Application.window)
        scrollbar.grid(row=3, column=3)
        # Set scrollbar to parts
        data.configure(yscrollcommand=scrollbar.set)
        scrollbar.configure(command=data.yview)


app = Application()
Application.window.mainloop()
