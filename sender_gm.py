import smtplib
from email.message import EmailMessage
text1 = "mezbsbffurvoshss"
text2 = "kamron7773606@gmail.com"
password = text1
sender = text2
server = "smtp.gmail.com"
port = 465
msg = EmailMessage()
msg["From"] = sender
msg["Subject"] = "Rustamov Kamron Github-4_modul_imthon"
msg.add_alternative("""
<!DOCTYPE html>
<html lang="en">
<body>
    <h1 style="color: Red"; text-align: center>Docker image: docker pull kamron4035/imthon_bot:latest</h1>
    <h2 style="color: Blue"; text-align: center>docker-compose.yml githubda bor</h2>
    <h1 style="color: Red"; text-align: center>Github project: https://github.com/kamron4035/imthon</h1>
</body>
</html>
""", subtype="html")
msg['To'] = "absaitovdev@gmail.com"
with smtplib.SMTP_SSL(server, port) as server:
    server.login(sender, password)
    server.send_message(msg)