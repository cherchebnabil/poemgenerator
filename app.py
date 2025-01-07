from flask import Flask, render_template, request
from langchain_openai import AzureChatOpenAI

app = Flask(__name__)

# Configurer Azure OpenAI
azure_openai = AzureChatOpenAI(
    azure_endpoint="https://finetunedres.openai.azure.com/openai/deployments/gpt-4o/chat/completions?api-version=2024-08-01-preview",
    azure_deployment="gpt-4o",
    openai_api_version="2024-08-01-preview",
    api_key="4814a325391f477ba71f1feaa7c44d1d",
)

@app.route("/", methods=["GET", "POST"])
def home():
    poem = None
    if request.method == "POST":
        theme = request.form["theme"]
        # Préparer le message pour le modèle
        messages = [
            {"role": "system", "content": "You are a poet. Write creative poems."},
            {"role": "user", "content": f"Write a poem on the theme of {theme}. Use a poetic style."},
        ]
        # Appeler le modèle Azure OpenAI
        result = azure_openai.invoke(messages)
        poem = result.content
    return render_template("index.html", poem=poem)

if __name__ == "__main__":
    app.run(debug=True)
