import openai
import streamlit as st

# Configurez votre clé API OpenAI
openai.api_key = "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"

# Interface Streamlit
st.title("Générateur de poèmes")
prompt = st.text_area("Saisissez un thème pour votre poème :")

if st.button("Générer un poème"):
    if prompt:
        response = openai.completions.create(
            model="gpt-3.5-turbo",  # Choisissez un modèle adapté
            prompt=prompt,  # Utilisation du prompt saisi par l'utilisateur
            max_tokens=150,
            temperature=0.7,
        )
        
        st.text_area("Voici votre poème :", response['choices'][0]['text'].strip(), height=200)
    else:
        st.warning("Veuillez saisir un thème avant de générer un poème.")
