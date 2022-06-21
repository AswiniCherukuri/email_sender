# Email sender

This python script send emails to all the mail addresses given in text file (emails.txt). Mail contains email body, html content and attachment (test_file)

Steps involved:
* Put all the receiver email addresses in emails.txt file
* Given attachment file as test_file ( (it should be either txt or pdf)
* Created the below python files:
   1. app.py -> It reads all the configurations and call the helper function (send_email) from email_sender.py
   2. email_sender.py -> It has email sending logic 
* Run "python app.py" in command line 



