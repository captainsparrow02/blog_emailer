from blog_content import *
from set_mail import *
from send_mail import *


def main():
	url = 'https://seths.blog/'

	# Credentials
	fromMail = input("Enter Your Email: ")
	password = input("Enter Your Password: ")

	toMail = input("Enter the email of recipient: ")

	blogContent = extract_content(url)
	heading, mainBody, link, date = blogContent

	htmlContent = html_content(heading, mainBody, link)

	mailMessage = mail_construct(toMail, fromMail, blogContent)

	email(fromMail, toMail, password, mailMessage)

if __name__ == '__main__':
	main()
