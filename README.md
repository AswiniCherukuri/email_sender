# Email sender

This python script send emails to all the mail addresses given in text file (emails.txt). Mail contains email body, html content and attachment (test_file)

It contains two files:

Steps involved:
1. Put all the receiver email addresses in emails.txt file
2. Give attachment file as test_file ( (it should be either txt or pdf)
3. Created the below python files:
   1. app.py -> It read all the configurations and call the helper function (send_email) from email_sender.py
   2. email_sender.py -> It has email sending logic 
4. Run "python app.py" in command line



