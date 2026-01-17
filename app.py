from flask import Flask, render_template, request, jsonify
import requests
from dotenv import load_dotenv
import os

load_dotenv(".env")

app = Flask(__name__)

# Ta clé API Météo (ex: OpenWeatherMap)
API_KEY = os.getenv("API_KEY")


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recevoir-coordonnees', methods=['POST'])
def recevoir_coordonnees():
    # 1. On récupère les données envoyées par le JS
    data = request.get_json()
    
    # 2. On extrait les valeurs
    latitude = data.get('lat')
    longitude = data.get('lon')
    
    print(f"✅ Python a bien reçu : Lat {latitude}, Lon {longitude}")
    
    # --- ICI TU FERAIS TON APPEL API MÉTÉO ---
    # Pour l'exemple, on renvoie juste un message de succès
    resultat = {
        "status": "success", 
        "message": f"Localisation reçue pour {latitude}, {longitude}",
        "temperature_fictive": 22  # Exemple
    }
    
    # 3. On répond au JavaScript (très important !)
    return jsonify(resultat)

if __name__ == '__main__':
    app.run(debug=True)
    recevoir_coordonnees()