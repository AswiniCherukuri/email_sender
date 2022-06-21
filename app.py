from email_sender import send_email


#configurations
host = "smtp.gmail.com"
port = 587
sender_mail = "example@gmail.com"
sender_mail_password = "example"

#read emails form text file
with open("emails_list.txt", "r") as f:
    emails = [line.rstrip() for line in f]

print(emails)

# Add file path
attach_file_name = ""

#call send email function
response = send_email(host, port, sender_mail, sender_mail_password, emails)
print(response)

