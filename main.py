import tkinter as tk

# Opprett et tkinter-vindu
root = tk.Tk()
root.title("Open AI")

# Sett størrelsen på vinduet
root.geometry("400x300")

# Endre bakgrunnsfargen til svart
root.configure(bg="black")

def login():
    print('du er logget inn')

def registrer():
    print('registrerer')

# Opprett en knapp
logInKnapp = tk.Button(root, text="Log in!", command=login)
logInKnapp.pack()

registrerKnapp = tk.Button(root, text="Registrer!", command=registrer)
registrerKnapp.pack()



# Start Tkinter-løkken
root.mainloop()
