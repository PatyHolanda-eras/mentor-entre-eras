from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/webhook", methods=["POST"])
def webhook():
    incoming_msg = request.values.get("Body", "").strip()
    if not incoming_msg:
        return jsonify({"status": "no message"}), 400

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
           {"role": "system", "content": "Você é um mentor virtual educacional. Responda com linguagem casual, recomende vídeos do YouTube e indique se são gratuitos ou pagos."},
            {"role": "user", "content": incoming_msg}
        ]
    )

    reply = response['choices'][0]['message']['content']
    return reply, 200
