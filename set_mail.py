
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText



def html_content(heading, mainBody, link):
	content = ''
	content += f"<h1 style='text-align: center;'> {heading} </h1><br>"
	content += f"<h4>{mainBody}<a href='{link}'>more</a></h4>"
	
	return content

def mail_construct(FROM, TO, mailContent):
	heading, mainBody, link, date = mailContent
	msg = MIMEMultipart()
	msg['Subject'] = "Seths Blog " + date
	msg['From'] = FROM
	msg['To'] = TO
	
	content = html_content(heading, mainBody, link)

	msg.attach(MIMEText(content, 'html')) 

	return msg.as_string()