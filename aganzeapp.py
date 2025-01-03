import streamlit as st
from PIL import Image

# Titre de l'application
st.title("Application génératrice de la Carte d'étudiant")

# Téléchargeur de fichiers pour la photo de passeport
uploaded_file = st.file_uploader("Téléchargez votre photo de passeport", type=["jpg", "jpeg", "png"])

# Informations pour la carte d'étudiant
nom = st.text_input("Nom:")
prenom = st.text_input("Prénom:")
date_naissance = st.date_input("Date de Naissance:")
numero_etudiant = st.text_input("Numéro d'Étudiant:")
filiere = st.text_input("Filière:")

if uploaded_file is not None and nom and prenom and date_naissance and numero_etudiant and filiere:
    # Ouvrir et afficher l'image
    image = Image.open(uploaded_file) 
    # Afficher la carte d'étudiant
    st.subheader("Carte d'Étudiant")
    st.image(image, caption='Photo de Passeport', use_column_width=True)
    st.write(f"**Nom :** {nom}")
    st.write(f"**Prénom :** {prenom}")
    st.write(f"**Date de Naissance :** {date_naissance}")
    st.write(f"**Numéro d'Étudiant :** {numero_etudiant}")
    st.write(f"**Filière :** {filiere}")

    # Option pour télécharger la carte d'étudiant
    st.download_button("Télécharger la carte", "Voici votre carte d'étudiant.")
else:
    st.warning("Veuillez remplir tous les champs et télécharger votre photo.")

