import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText, MIMEBase
from email import encoders

def send_email(host, port, sender_mail, sender_mail_password, emails, attach_file_name):

    s = smtplib.SMTP(host,port)
    s.ehlo()
    s.starttls()
    s.login(sender_mail,sender_mail_password)
    for receiver_mail in emails:

        if receiver_mail is None:
            pass
        else:

            message = MIMEMultipart("alternative")
            message["Subject"] = "Testing"
            message["From"] = sender_mail
            message["To"] = receiver_mail


            plain_text = """"
            test email ......
            """
            html_text ="""
            <html>
            <body>
                <p>Hi<br>
                Sending email using python script <br>
                </p>
            </body>
            </html>
            """
            part_1 = MIMEText(plain_text,"plain")
            part_2 = MIMEText(html_text,"html")
            message.attach(part_1)
            message.attach(part_2)
            #attach_file_name = 'TP_python_prev.pdf'
            attach_file = open(attach_file_name, 'rb') # Open the file as binary mode
            payload = MIMEBase('application', 'octate-stream')
            payload.set_payload((attach_file).read())
            encoders.encode_base64(payload) #encode the attachment
            #add payload header with filename
            payload.add_header('Content-Decomposition', 'attachment', filename=attach_file_name)
            message.attach(payload)
            try:
                s.sendmail(sender_mail,receiver_mail,message.as_string())
                s.quit()
                return True
            except Exception as e:
                return False

    



