import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
from openai import OpenAI

# Carrega as variáveis do .env
load_dotenv()
EMAIL_USUARIO = os.getenv("EMAIL_USUARIO")
EMAIL_SENHA = os.getenv("EMAIL_SENHA")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Cliente da OpenAI
client = OpenAI(api_key=OPENAI_API_KEY)

# Gera mensagem motivacional com a IA
def gerar_mensagem():
    resposta = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Você é um gerador de mensagens motivacionais."},
            {"role": "user", "content": "Crie uma mensagem motivacional de até 3 linhas para o dia de hoje."}
        ]
    )
    return resposta.choices[0].message.content

# Envia o e-mail
def enviar_email(mensagem, destinatario):
    msg = EmailMessage()
    msg["Subject"] = "Mensagem do Dia 🌞"
    msg["From"] = EMAIL_USUARIO
    msg["To"] = destinatario
    msg.set_content(mensagem)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(EMAIL_USUARIO, EMAIL_SENHA)
        smtp.send_message(msg)

# Execução
if __name__ == "__main__":
    mensagem = gerar_mensagem()
    enviar_email(mensagem, "lucian.bonifacio@gmail.com")  # Troque aqui!
    print("E-mail enviado com sucesso!")