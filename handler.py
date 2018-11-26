import json
import smtplib
import time

username = 
password = 


def alertMe(email):
	gmail_user = username
	gmail_password = password

	sent_from = gmail_user  
	to = email  
	subject = "Here's a Motorcycle related Youtube video that I think you may enjoy"  

	body = "https://youtu.be/6lQ3SUkdSKo"

	email_text = """
	From: %s 
	To: %s  
	Subject: %s 

	%s
	""" % (sent_from, to, subject, body)

	try:  
		server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
		server.ehlo()
		server.login(gmail_user, gmail_password)
		server.sendmail(sent_from, to, email_text)
		server.close()

		print "email sent to: " + email
	except:  
		print ('Something went wrong...')


##########################################################################


text_file = open("data.txt", "r")
data = json.load(text_file)

emails = list(set(data))
emails_copy = []
for email in emails:
	emails_copy.append(email)

text_file = open("used_emails.txt", "r")
used_emails = json.load(text_file)

print len(emails)

for email in emails_copy:
	if email in used_emails:
		emails.remove(email)

for email in emails:
	used_emails.append(email)
		
print len(used_emails)
print len(emails)

time.sleep(2)
	
for email in emails:
	alertMe(email)
	
with open('used_emails.txt', 'w') as outfile:  
    json.dump(used_emails, outfile, separators = (",", ": "))

