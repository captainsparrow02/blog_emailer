from bs4 import BeautifulSoup
import requests

def extract_content(url):

	response = requests.get(url)
	content = response.content
	soup = BeautifulSoup(content, 'html.parser')

	tag = soup.find('div', attrs= {'class':'post'})
	heading, mainBody, date= content_parser(tag)
	link = get_href(tag)

	return (heading, mainBody, link, date)

	
		

def get_href(tag):
	c = str(tag.h2.a)
	start = c.index('"')
	end = c[start+1:].index('"')
	return c[start+1:end]

def content_parser(content):
	content = content.text.strip()
	body_content = content.split('\n')
	heading = body_content[0]
	date = body_content[-1]
	mainBody = body_content[1:len(body_content)-2]

	try:

		visibleLength = int(len(mainBody[2])*0.5)
		content = ''.join(mainBody[:2])
		content += mainBody[2][:visibleLength]+"..."

	except:
		x = len(mainBody)
		visibleLength = int(x*0.1)
		content = ''.join(mainBody[:visibleLength+1])

	return (heading, content, date)



		
if __name__ == '__main__':
	url = 'https://seths.blog/'
	for content in extract_content(url):
		print(content)
		print()

