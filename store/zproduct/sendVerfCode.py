import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def sendCodeVerefication(zestoreMail:str, zestorePass:str, client:str, code:str, fullName:str):
    try:
        print(f'{type(zestoreMail)} =>{zestoreMail}')
        message = MIMEMultipart()
        message['From'] = zestoreMail
        message['To'] = client
        message['Subject'] = 'Zestore Account Verification'
        content = f'''
                    Hello {fullName}
                    Here Is Your Verification Code
                    `{code}`
                    Best,
                    Zestore
                    '''
        message.attach(MIMEText(content, 'plain'))
        server = smtplib.SMTP('smtp.gmail.com', 25)
        server.connect('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(zestoreMail, zestorePass)
        toSend = message.as_string()
        server.sendmail(zestoreMail, client, toSend)
        server.quit()
    except Exception as e:
        print(f"ERROR: {e}")