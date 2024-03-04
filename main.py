import tkinter as tk
import mysql

def addUserDB(brukernavn, passord):
    try:
         # Koble til MySQL-databasen
        connection = pymysql.connect(
            host='your_host',
            user='your_username',
            password='your_password',
            database='your_database'
        )

        # Opprett en databasekursor
        cursor = connection.cursor()

        # SQL-spørring for å legge til bruker
        query = "INSERT INTO users (username, password) VALUES (%s, %s)"
        cursor.execute(query, (username, password))

        # Bekreft endringene
        connection.commit()

        # Lukk kursor og tilkobling
        cursor.close()
        connection.close()

        print("Bruker lagt til i databasen!")

    except Exception as e:
        print("Feil ved tilkobling til databasen:", e)


def login():
    # Opprett et nytt vindu for innlogging
    login_window = tk.Toplevel(root)
    login_window.title("Logg inn")
    login_window.geometry("300x200")
    login_window.configure(bg="white")

    # Tekstbokser for brukernavn og passord
    username_label = tk.Label(login_window, text="Brukernavn:")
    username_label.pack()
    username_entry = tk.Entry(login_window)
    username_entry.pack()

    password_label = tk.Label(login_window, text="Passord:")
    password_label.pack()
    password_entry = tk.Entry(login_window, show="*")  # Viser * i stedet for passordet
    password_entry.pack()

    # Opprett en tilbakeknapp
    back_button = tk.Button(login_window, text="Tilbake", command=login_window.destroy)
    back_button.pack()

def regIDB():
    pass

def register():
    # Opprett et nytt vindu for registrering
    register_window = tk.Toplevel(root)
    register_window.title("Registrer")
    register_window.geometry("300x200")
    register_window.configure(bg="white")

    # Tekstbokser for brukernavn og passord
    username_label = tk.Label(register_window, text="Brukernavn:")
    username_label.pack()
    username_entry = tk.Entry(register_window)
    username_entry.pack()

    password_label = tk.Label(register_window, text="Passord:")
    password_label.pack()
    password_entry = tk.Entry(register_window, show="*")  # Viser * i stedet for passordet
    password_entry.pack()

    password_label = tk.Label(register_window, text="Bekreft Passord:")
    password_label.pack()
    password_entry = tk.Entry(register_window, show="*")  # Viser * i stedet for passordet
    password_entry.pack()

    reg_button = tk.Button(register_window, text="Registrer", command=regIDB)
    reg_button.pack()

    # Opprett en tilbakeknapp
    back_button = tk.Button(register_window, text="Tilbake", command=register_window.destroy)
    back_button.pack()

# Opprett et tkinter-vindu
root = tk.Tk()
root.title("Open AI")
root.geometry("400x300")

root.configure(bg="white")

# Opprett en knapp for innlogging
login_button = tk.Button(root, text="Logg inn!", command=login)
login_button.pack()

# Opprett en knapp for registrering
register_button = tk.Button(root, text="Registrer!", command=register)
register_button.pack()

# Start Tkinter-løkken
root.mainloop()
