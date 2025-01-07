import openai
import streamlit as st

# Configurez votre clé API OpenAI
openai.api_key = "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"  # Remplacez par votre clé API réelle

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
