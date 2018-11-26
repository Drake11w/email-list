import smtplib
import re
from robobrowser import RoboBrowser
import time
from bs4 import BeautifulSoup
import json

br = RoboBrowser()

br.open('https://www.google.com/search?biw=2048&bih=750&ei=mY_7W4bDPIeUtQW0y7uIBw&q=%22%40gmail.com%22+motorcycle+drag+racing+youtube&oq=%22%40gmail.com%22+motorcycle+drag+racing+youtube&gs_l=psy-ab.12...413909.418189..419846...1.0..0.70.398.6......0....1..gws-wiz.......35i302i39.4d3oJ_34kOs')
email_list = []
i = 1
try:
	for i in range(50):
		i = i + 1
		texts = br.find_all('span', {'class' : 'st'})
		for text in texts:
			emails = re.findall(r"([a-zA-Z0-9_.+-]+@)", str(text))
			#print text
			for email in emails:
				data = email + "gmail.com"
				email_list.append(data)
				print data
		nextpage = br.find_all('a')
		time.sleep(1)
		for page in nextpage:
			if page.text.strip().encode('utf-8') == str(i):
				br.follow_link(page)
except:
	print "broke"
	
print email_list	
#r"[a-zA-Z0-9._]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,5}"
#print str(text)

with open('data.txt', 'w') as outfile:  
    json.dump(email_list, outfile, separators = (",", ": "))
