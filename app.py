import openai
import streamlit as st

# Configurez votre clé API OpenAI
openai.api_key = "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"

# Interface Streamlit
st.title("Générateur de poèmes")
prompt = st.text_area("Saisissez un thème pour votre poème :")

if st.button("Générer un poème"):
    if prompt:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"Écris un poème sur : {prompt}",
            max_tokens=100,
            temperature=0.7,
        )
        st.text_area("Voici votre poème :", response.choices[0].text.strip(), height=200)
    else:
        st.warning("Veuillez saisir un thème avant de générer un poème.")
