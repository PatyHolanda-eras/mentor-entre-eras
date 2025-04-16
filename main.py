from flask import Flask, request, Response
import openai
import os

app = Flask(__name__)

openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/webhook", methods=["POST"])
def webhook():
    incoming_msg = request.values.get("Body", "").strip()
    if not incoming_msg:
        return Response("No message received", status=400)

    # Chamada ao GPT com comportamento de mentor casual
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": (
                    "Você é um mentor virtual chamado Entre Eras. "
                    "Fale como uma pessoa amiga, com linguagem casual e inspiradora. "
                    "Sempre que possível, recomende links úteis — especialmente vídeos do YouTube e cursos online. "
                    "Indique se o conteúdo é gratuito ou pago. "
                    "Adapte a resposta conforme o tipo de pergunta. "
                    "Não fale como assistente de IA. Seja um mentor humano e direto."
                )
            },
            {"role": "user", "content": incoming_msg}
        ]
    )

    reply = response['choices'][0]['message']['content']

    # Retorno formatado para Twilio (resposta em XML/texto)
    return Response(reply, mimetype="text/plain"), 200


if __name__ == "__main__":
    # Porta padrão para Render (10000)
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
