from flask import Flask, request, jsonify
import openai

# Configurez votre clé API OpenAI
openai.api_key = "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"

app = Flask(__name__)

@app.route('/generate', methods=['POST'])
def generate_poem():
    user_prompt = request.json.get('prompt', '')
    try:
        # Génération de texte avec OpenAI
        response = openai.Completion.create(
            engine="text-davinci-003",  # Modèle puissant pour le texte
            prompt=f"Compose un poème basé sur le thème : {user_prompt}",
            max_tokens=150,  # Limitez la longueur du poème
            temperature=0.7  # Contrôle de la créativité
        )
        poem = response.choices[0].text.strip()
        return jsonify({"poem": poem})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
