from tkinter import *
from tkinter.messagebox import showerror
from tkinter.messagebox import askquestion
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
        # initial selected item
        self.selected_item = 0  # nothing initially selectedS
        # run to get all widgets i.e buttons, labels, etc
        self.labels()
        self.buttons()
        self.list_box()
        self.populate_list()  # will immediately show data when run

    # create labels and input boxes
    def labels(self):
        self.website_label = Label(Application.window,
                                   text="Website", font=("calibre", 12, "bold"))
        self.website_label.grid(column=0, row=0, pady=20)
        # input box for website
        self.website = Entry(Application.window, font=(
            "calibre", 12, "normal"), borderwidth=2)
        self.website.grid(column=1, row=0, pady=20)
        self.password_label = Label(
            Application.window, text="Password", font=("calibre", 12, "bold"))
        self.password_label.grid(column=2, row=0, pady=28)
        # input box for password
        self.password = Entry(Application.window, font=(
            "calibre", 12, "normal"), borderwidth=2)
        self.password.grid(column=3, row=0)

    # create buttons

    def buttons(self):
        # buttons
        self.add_password = Button(Application.window,
                                   text="Add Password", bg="green", bd="3", width=14, command=self.add)
        self.add_password.grid(column=0, row=1, pady=20, padx=22)
        self.delete_password = Button(Application.window,
                                      text="Delete Password", bg="red", bd="3", width=14, command=self.delete)
        self.delete_password.grid(column=1, row=1, pady=20, padx=12)
        self.update_password = Button(
            Application.window, text="Update", bd="3", width=14, command=self.update)
        self.update_password.grid(column=2, row=1, pady=20, padx=12)
        self.clear_input = Button(
            Application.window, text="Clear Input", bd="3", width=14, command=self.clear)
        self.clear_input.grid(column=3, row=1, pady=20, padx=15)

    # list box to store website and passwords
    def list_box(self):
        self.data = Listbox(Application.window, height=20,
                            width=69, border=2, font=("calibre", 10))
        self.data.grid(column=0, row=3, columnspan=4,
                       rowspan=3, pady=25, padx=20)
        # Create a scrollbar
        self.scrollbar = Scrollbar(Application.window,)
        self.scrollbar.grid(row=3, column=3)
        # Set scrollbar to our data
        # set to scrollbar instead of mouse
        self.data.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.configure(command=self.data.yview)
        # Bind select
        self.data.bind("<<ListboxSelect>>", self.select_item)

    # button commands
    # add website and password to database
    def add(self):
        # check if both inputs are filled
        if self.website.get() == "" or self.password.get() == "":
            showerror(title="Error",
                      message="Please fill in all the information")
            return
        # otherwise insert into database
        database.insert_data(self.website.get(), self.password.get())
        # insert then clear input boxes
        self.clear()
        self.populate_list()

    def populate_list(self):
        # first delete to prevent same data showing in listbox
        self.data.delete(0, END)
        for data in database.get_data():  # loop through ALL websites and passwords
            # show_this = f"Website: {data[1]}, Password: {data[2]}"
            self.data.insert(END, data)  # insert into listbox

        # Runs when item is selected
    def select_item(self, event):
        # # Create global selected item to use in other functions
        try:
            # Get index
            # only one item in tuple so get it out
            index = self.data.curselection()[0]
            # Get selected item
            self.selected_item = self.data.get(index)
            self.entries = self.selected_item
            # Add text to entries when selected then delete when another item is selected
            self.website.delete(0, END)
            # slice to take out comma
            self.website.insert(END, self.entries[1])
            self.password.delete(0, END)
            self.password.insert(END, self.entries[2])

        except IndexError:  # if user clicks unreachable index (not item)
            pass

    # update selected passwords
    def update(self):
        database.update_data(self.selected_item[0],
                             self.website.get(), self.password.get())
        self.clear()
        self.populate_list()  # show new data

    # delete data
    def delete(self):
        response = askquestion(title="Warning",
                               message="Are you sure you want to delete this?")
        if response == "yes":  # if they click yes, delete selected item
            database.delete_data(self.selected_item[0])
            self.clear()
            self.populate_list()  # show new data
        else:  # if no, pass
            pass

        # clear input button functionality

    def clear(self):
        self.website.delete(0, END)
        self.password.delete(0, END)


app = Application()
Application.window.mainloop()
