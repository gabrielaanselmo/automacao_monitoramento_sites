import requests
import os
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sites = ["https://www.google.com", "https://www.thissitedoesnotexist.com"]


def send_email(subject, message):
    sender = os.environ['SENDER']
    password = os.environ['PASSWORD']
    receiver = os.environ['REMITTEE']

    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = receiver
    msg['Subject'] = subject

    msg.attach(MIMEText(message, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender, password)
        text = msg.as_string()
        server.sendmail(sender, receiver, text)
        server.quit()
        print("E-mail enviado com sucesso.")
    except Exception as e:
        print(f"Erro ao enviar e-mail: {e}")


def monitor_sites(sites):
    for site in sites:
        try:
            start_time = time.time()
            response = requests.get(site)
            response_time = time.time() - start_time
            status_code = response.status_code

            if status_code != 200 or response_time > 3:
                message = f"{site} falhou com o status {status_code} ou tempo de resposta alto ({response_time} segundos)."
                send_email("Alerta de Site", message)

        except requests.RequestException as e:
            send_email("Erro de Monitoramento de Site", f"Erro ao acessar {site}: {e}")


if __name__ == "__main__":
    monitor_sites(sites)
