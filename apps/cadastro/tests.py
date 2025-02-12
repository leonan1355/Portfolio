import smtplib

EMAIL = "leonan.ferreira.dev@hotmail.com"
PASSWORD = "ykdsmvpsdsnsojtv"  # Pegando do .env

try:
    server = smtplib.SMTP("smtp.office365.com", 587)
    server.starttls()
    server.login(EMAIL, PASSWORD)
    print("SMTP funcionando!")
    server.quit()
except Exception as e:
    print(f"Erro: {e}")
