import tkinter as tk
from tkinter import messagebox
import pymysql

# Connexion à MySQL (XAMPP)
def connect_db():
    try:
        conn = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            db='fastapi_test'
        )
        return conn
    except Exception as e:
        messagebox.showerror("Erreur DB", f"Connexion échouée : {e}")
        return None

# Ajouter un utilisateur
def ajouter_utilisateur():
    nom = entry_nom.get()
    email = entry_email.get()

    if not nom or not email:
        messagebox.showwarning("Champs manquants", "Merci de remplir tous les champs.")
        return

    conn = connect_db()
    if conn:
        try:
            with conn.cursor() as cursor:
                cursor.execute("INSERT INTO utilisateurs (nom, email) VALUES (%s, %s)", (nom, email))
                conn.commit()
                messagebox.showinfo("Succès", "Utilisateur ajouté avec succès.")
                afficher_utilisateurs()
        finally:
            conn.close()

# Afficher les utilisateurs
def afficher_utilisateurs():
    conn = connect_db()
    if conn:
        try:
            with conn.cursor() as cursor:
                cursor.execute("SELECT * FROM utilisateurs")
                rows = cursor.fetchall()
                text_affichage.delete("1.0", tk.END)
                for row in rows:
                    text_affichage.insert(tk.END, f"ID: {row[0]}, Nom: {row[1]}, Email: {row[2]}\n")
        finally:
            conn.close()

# Interface Tkinter
root = tk.Tk()
root.title("📋 Interface MySQL - XAMPP (utilisateurs)")
root.geometry("500x400")

frame = tk.Frame(root, padx=10, pady=10)
frame.pack()

tk.Label(frame, text="Nom:").grid(row=0, column=0, sticky="e")
entry_nom = tk.Entry(frame, width=30)
entry_nom.grid(row=0, column=1)

tk.Label(frame, text="Email:").grid(row=1, column=0, sticky="e")
entry_email = tk.Entry(frame, width=30)
entry_email.grid(row=1, column=1)

tk.Button(frame, text="Ajouter utilisateur", command=ajouter_utilisateur, bg="green", fg="white").grid(row=2, column=0, columnspan=2, pady=10)

tk.Button(frame, text="Afficher utilisateurs", command=afficher_utilisateurs, bg="blue", fg="white").grid(row=3, column=0, columnspan=2, pady=5)

text_affichage = tk.Text(root, height=10, width=60)
text_affichage.pack(pady=10)

root.mainloop()
