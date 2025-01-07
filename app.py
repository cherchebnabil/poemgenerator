import openai
import streamlit as st
import os

# Récupérer la clé API à partir de la variable d'environnement
openai.api_key = os.getenv("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")  # Utiliser la clé API stockée dans les variables d'environnement

# Vérifier si la clé API est définie
if openai.api_key is None:
    st.error("Clé API OpenAI manquante. Veuillez définir la variable d'environnement OPENAI_API_KEY.")
else:
    # Interface Streamlit
    st.title("Générateur de poèmes")
    prompt = st.text_area("Saisissez un thème pour votre poème :")

    if st.button("Générer un poème"):
        if prompt:
            # Utilisez la méthode `openai.ChatCompletion.create` pour interagir avec le modèle GPT
            response = openai.ChatCompletion.create(  # Méthode correcte dans la version actuelle
                model="gpt-3.5-turbo",  # Choisissez un modèle adapté
                messages=[
                    {"role": "system", "content": "Vous êtes un poète."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=150,
                temperature=0.7,
            )
            
            st.text_area("Voici votre poème :", response['choices'][0]['message']['content'].strip(), height=200)
        else:
            st.warning("Veuillez saisir un thème avant de générer un poème.")
