import tkinter as tk

def login():
    # Opprett et nytt vindu for innlogging
    login_window = tk.Toplevel(root)
    login_window.title("Logg inn")
    login_window.geometry("300x200")
    login_window.configure(bg="white")

    # Opprett en tilbakeknapp
    back_button = tk.Button(login_window, text="Tilbake", command=login_window.destroy)
    back_button.pack()

def register():
    # Opprett et nytt vindu for registrering
    register_window = tk.Toplevel(root)
    register_window.title("Registrer")
    register_window.geometry("300x200")
    register_window.configure(bg="white")

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
