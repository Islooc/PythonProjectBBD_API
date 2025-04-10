from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import requests
# Config FastAPI
app = FastAPI()

# Connexion à MySQL (ajuste si tu as un mot de passe)
DATABASE_URL = "mysql+pymysql://root:@localhost/fastapi_test"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

# Modèle SQLAlchemy
class Utilisateur(Base):
    __tablename__ = "utilisateurs"
    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String(50))
    email = Column(String(100))

# Création des tables (optionnel ici car elles existent déjà)
Base.metadata.create_all(bind=engine)

# Schéma Pydantic pour requêtes
class UtilisateurSchema(BaseModel):
    nom: str
    email: str

@app.post("/utilisateurs/")
def creer_utilisateur(utilisateur: UtilisateurSchema):
    db = SessionLocal()
    db_utilisateur = Utilisateur(**utilisateur.dict())
    db.add(db_utilisateur)
    db.commit()
    db.refresh(db_utilisateur)
    db.close()
    return db_utilisateur

@app.get("/utilisateurs/")
def lire_utilisateurs():
    db = SessionLocal()
    utilisateurs = db.query(Utilisateur).all()
    db.close()
    return utilisateurs

@app.delete("/utilisateurs/{id}")
def supprimer_utilisateur(id: int):
    db = SessionLocal()
    utilisateur = db.query(Utilisateur).filter(Utilisateur.id == id).first()
    if utilisateur:
        db.delete(utilisateur)
        db.commit()
        db.close()
        return {"message": "Utilisateur supprimé"}
    db.close()
    raise HTTPException(status_code=404, detail="Utilisateur non trouvé")

def afficher_utilisateurs():
    res = requests.get(DATABASE_URL)
    print("Utilisateurs :", res.json())

def ajouter_utilisateur(nom, email):
    data = {"nom": nom, "email": email}
    res = requests.post(DATABASE_URL, json=data)
    print("Ajouté :", res.json())

def supprimer_utilisateur(id):
    res = requests.delete(DATABASE_URL + str(id))
    print(res.json())

# TESTS
afficher_utilisateurs()
ajouter_utilisateur("Jean", "jean@example.com")
supprimer_utilisateur(1)  # supprime l’utilisateur avec ID 1
