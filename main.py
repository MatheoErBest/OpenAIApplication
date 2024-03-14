import tkinter as tk
from tkinter import messagebox
import pymysql
import openai

# Opprett forbindelse til MySQL-databasen
def connect_to_database():
    return pymysql.connect(host='172.20.128.80', user='admin', password='123Akademiet', database='user')

# Opprett en bruker i databasen
def add_user_to_db(username, password):
    connection = connect_to_database()
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO users (username, password) VALUES (%s, %s)"
            cursor.execute(sql, (username, password))
            connection.commit()
    finally:
        connection.close()

# Sjekk om brukeren er i databasen
def user_exists(username):
    connection = connect_to_database()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM users WHERE username = %s"
            cursor.execute(sql, (username,))
            result = cursor.fetchone()
            return result is not None
    finally:
        connection.close()

# Logg inn brukeren
def login_user(username):
    # implementer logikk for å åpne hovedvinduet etter innlogging
    print("Logged in as:", username)

# Registrer en ny bruker
def register_user(username, password):
    if not user_exists(username):
        add_user_to_db(username, password)
        messagebox.showinfo("Success", "User registered successfully!")
    else:
        messagebox.showerror("Error", "Username already exists")

# Still spørsmål til OpenAI API og vis svaret
def ask_openai(question):
    openai.api_key = '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'
    response = openai.Completion.create(
        engine="davinci",
        prompt=question,
        max_tokens=100
    )
    answer = response.choices[0].text.strip()
    return answer

# GUI for innloggingsside
class LoginApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Login")
        
        self.label_username = tk.Label(master, text="Username:")
        self.label_username.pack()
        self.entry_username = tk.Entry(master)
        self.entry_username.pack()
        
        self.label_password = tk.Label(master, text="Password:")
        self.label_password.pack()
        self.entry_password = tk.Entry(master, show="*")
        self.entry_password.pack()
        
        self.btn_login = tk.Button(master, text="Login", command=self.login)
        self.btn_login.pack()

        self.btn_register = tk.Button(master, text="Register", command=self.register)
        self.btn_register.pack()

    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        if user_exists(username):
            login_user(username)
            self.master.destroy()  # Lukk innloggingsvinduet
            MainApp(username)  # Åpne hovedvinduet
        else:
            messagebox.showerror("Error", "Invalid username or password")

    def register(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        register_user(username, password)

# GUI for hovedvinduet
class MainApp:
    def __init__(self, username):
        self.root = tk.Tk()
        self.root.title("Main Window")

        self.label_username = tk.Label(self.root, text="Logged in as: " + username)
        self.label_username.pack()

        self.label_question = tk.Label(self.root, text="Ask a question:")
        self.label_question.pack()
        self.entry_question = tk.Entry(self.root)
        self.entry_question.pack()

        self.btn_ask = tk.Button(self.root, text="Ask", command=self.ask)
        self.btn_ask.pack()

        self.btn_fullscreen = tk.Button(self.root, text="Toggle Fullscreen", command=self.toggle_fullscreen)
        self.btn_fullscreen.pack()

        self.root.mainloop()

    def ask(self):
        question = self.entry_question.get()
        answer = ask_openai(question)
        messagebox.showinfo("Answer", answer)

    def toggle_fullscreen(self):
        self.root.attributes("-fullscreen", not self.root.attributes("-fullscreen"))

# Opprett hovedvinduet
def main():
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
