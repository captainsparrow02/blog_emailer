import smtplib

def email(fromMail, toMail, password, message):
	SERVER = 'smtp.gmail.com'
	PORT = 587
	FROM = fromMail
	TO = toMail
	PASS = password

	print("------Initiating server-------")
	server = smtplib.SMTP(SERVER, PORT)

	server.set_debuglevel(0)
	server.ehlo()
	server.starttls()
	try:
		server.login(FROM, PASS)
		server.sendmail(FROM, TO, message)
		print("Email Sent")
	except smtplib.SMTPAuthenticationError:
		print("!!!!!!!! Authentication failed !!!!!!!!!")
		print("Please enter valid EmailId/Password.")
	

	
	print("---------Closing Server----------")
	server.quit()