# Mentor Virtual Entre Eras

Este projeto é um MVP de mentor virtual via WhatsApp, utilizando:

- Flask (Python)
- OpenAI GPT
- Twilio (sandbox WhatsApp)
- Hospedado no Glitch

### Criadora
**Patrícia Ramos**

## Como usar

1. Clone este repositório no [Glitch](https://glitch.com/)
2. Crie um arquivo `.env` com base no `.env.example`
3. Preencha com suas credenciais do Twilio e OpenAI
4. Configure o webhook do Twilio apontando para `https://seu-projeto.glitch.me/webhook`
5. Envie uma mensagem via WhatsApp para o número do sandbox

O bot responderá com conteúdo educativo, vídeos, links e recomendações personalizadas 🎓
