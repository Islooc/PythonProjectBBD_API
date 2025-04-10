📋 Interface Utilisateurs + API FastAPI avec MySQL (XAMPP)
Ce projet regroupe :

Une interface graphique Tkinter en Python pour interagir avec une base de données MySQL locale

Une API REST avec FastAPI pour gérer les utilisateurs (CRUD)

Le tout relié à une base de données MySQL locale via XAMPP

📌 Endpoints de l’API
Méthode	Endpoint	Description
GET	/utilisateurs/	Liste tous les utilisateurs
POST	/utilisateurs/	Crée un utilisateur
DELETE	/utilisateurs/{id}	Supprime un utilisateur par ID
🛠️ Fonctions disponibles dans les scripts
interface_tkinter.py
ajouter_utilisateur() : ajoute un utilisateur dans la BDD

afficher_utilisateurs() : affiche tous les utilisateurs dans la fenêtre

api_fastapi.py
creer_utilisateur() : crée un utilisateur via l'API

lire_utilisateurs() : liste tous les utilisateurs via l'API

supprimer_utilisateur() : supprime un utilisateur par ID via l'API

🧪 Exemple d'utilisation API
python
Copier
Modifier
ajouter_utilisateur("Alice", "alice@example.com")
afficher_utilisateurs()
supprimer_utilisateur(2)
