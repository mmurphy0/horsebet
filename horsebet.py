import random
import time
import tkinter as tk
from tkinter import Toplevel
from tkinter import messagebox
from tkinter import Label

#verifies age is 18 or over for access
#asks for login details
#shows homepage with horses and odds
#no functionality to place bets yet - coming soon
#users deposit money for each round
#forced to withdraw after each round

balance = float(0.0)

logins = {
    'admin' : 'admin',
    'user1' : 'password1',
}

def checkusr():
    usr = l3.get()
    pwd = l5.get()

    if usr in logins and logins[usr] == pwd:
        homepage()
    
    else:
        messagebox.showinfo('Error','Incorrect login details')
        login()

def checkage():
    age = int(age_entry.get())

    if age >= 18:
        login()
    
    else:
        messagebox.showinfo('Error','You must be 18 or older to play')
        root.destroy()

def logout():
    messagebox.showinfo('Confirmation','Successfully logged out')
    login()


def login():
    loginpage = Toplevel()
    loginpage.title('Login')
    loginpage.geometry('280x130')
    loginpage.minsize(280,145)

    global l3
    global l5

    l1 = tk.Label(
        loginpage,
        text='Login:',
        width=20,
        font=('Arial',20,'bold')
    )
    l1.grid(
        row=1,
        column=1,
        columnspan=2
    )

    l2 = tk.Label(
        loginpage,
        text='Username',
        font=('Arial',15)
    )
    l2.grid(
        row=2,
        column=1
    )

    l3 = tk.Entry(loginpage)
    l3.grid(
        row=2,
        column=2
    )

    l4 = tk.Label(
        loginpage,
        text='Password',
        font=('Arial',15)
    )
    l4.grid(
        row=3,
        column=1
    )

    l5 = tk.Entry(loginpage)
    l5.grid(
        row=3,
        column=2
    )

    l6 = tk.Button(
        loginpage,
        text='Login',
        width=20,
        command=checkusr
    )
    l6.grid(
        row=4,
        column=1,
        columnspan=2,
        pady=0
    )

    l7 = tk.Button(
        loginpage,
        text='Exit',
        width=20,
        command=loginpage.destroy
    )
    l7.grid(
        row=5,
        column=1,
        columnspan=2,
        pady=0
    )

def homepage():
    messagebox.showinfo('Error','Your balance will be reset to £10 each round')    
    
    home = Toplevel()
    home.update_idletasks()
    home.geometry('335x200')
    home.title('Home')
    home.minsize(340, 200)
    
    home_title = tk.Label(
        home,
        text='horsebet.com',
        font=('Arial',20, 'bold'),
        width=20,
        height=2,
        anchor='center'
    )
    home_title.grid(
        row=1,
        column=1,
        columnspan=4
    )

    horse_title = tk.Label(
        home,
        text='Todays Horses:',
        font=('Arial',15,'bold')
    )
    horse_title.grid(
        row=3,
        column=1
    )

    horse_1 = tk.Label(
        home,
        text='Thunder | 2/10',
        font=('Arial',15)
    )
    horse_1.grid(
        row=4,
        column=1
    )

    horse_2 = tk.Label(
        home,
        text='Storm | 5/10',
        font=('Arial',15)
    )
    horse_2.grid(
        row=5,
        column=1
    )

    horse_3 = tk.Label(
        home,
        text='Shadow | 3/10',
        font=('Arial',15)
    )
    horse_3.grid(
        row=6,
        column=1
    )

    horse_4 = tk.Label(
        home,
        text='Ghost | 4/10',
        font=('Arial',15)
    )
    horse_4.grid(
        row=7,
        column=1
    )

    bet_button = tk.Button(
        home,
        text='Place Bet',
        width=20
    )
    bet_button.grid(
        row=4,
        column=3,
        columnspan=2,
        pady=0
    )
    
    deposit_button = tk.Button(
        home,
        text='Deposit to balance',
        width=20,
        command=deposit
    )
    deposit_button.grid(
        row=5,
        column=3,
        columnspan=2,
        pady=0
    )

    logout_button = tk.Button(
        home,
        text='Logout',
        width=20,
        command=logout
    )
    logout_button.grid(
        row=6,
        column=3,
        columnspan=2,
        pady=0
    )


root = tk.Tk()
root.title('Verify Age')
root.geometry('230x100')

age_title = tk.Label(
    root,
    text='Please verify your age',
    font=('Arial',20)
)
age_title.grid(
    row=1,
    column=1,
    columnspan=2
)

age_label = tk.Label(
    root,
    text='Age:',
    font=('Arial',15)
)
age_label.grid(
    row=2,
    column=1
)

age_entry = tk.Entry(root)
age_entry.grid(
    row=2,
    column=2
)

submit_button = tk.Button(
    root,
    text='Submit',
    command=checkage
)
submit_button.grid(
    row=3,
    column=1,
    columnspan=2
)

root.mainloop()