import os
from dotenv import load_dotenv
import requests
import sqlite3

def sauvegarder_mes_donnees(self):

        # 2. Connexion à la base (crée le fichier 'mes_donnees.db' sur Linux)
        conn = sqlite3.connect('mes_donnees.db')
        cursor = conn.cursor()

        # 3. Création de la table (si elle n'existe pas encore)
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS resultats_api (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titre TEXT,
            valeur TEXT
        )
    ''')