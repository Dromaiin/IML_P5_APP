import streamlit as st
import requests

# Fonction pour envoyer les données à l'API Flask
def envoyer_a_api(titre, body):
    url_api = "http://127.0.0.1:8080/"
    data = {"titre_test": titre, "body_test": body}

    # Envoi de la requête à l'API Flask
    response = requests.post(url_api, json=data)

    # Affichage de la réponse de l'API
    if response.status_code == 200:
        st.success("Données envoyées avec succès à l'API!")
        result = response.json()
        rec = result.get("message")
        st.write(rec)  # Ajout de l'affichage des résultats de l'API
    else:
        st.error(f"Erreur lors de l'envoi des données à l'API. Code d'erreur : {response.status_code}")

# Interface utilisateur Streamlit
st.title("Application Streamlit avec API Flask")

# Entrées utilisateur pour le titre et le body
titre = st.text_input("Entrez le titre:")
body = st.text_area("Entrez le corps du texte:")

# Bouton pour envoyer les données à l'API lorsqu'il est cliqué
if st.button("Envoyer à l'API"):
    if titre and body:  # Vérifie que le titre et le body ne sont pas vides
        envoyer_a_api(titre, body)
    else:
        st.warning("Veuillez remplir le titre et le corps du texte avant d'envoyer à l'API.")

