#!/bin/python3

from datetime import datetime
from json2html import *
from bs4 import BeautifulSoup as BS
from urllib.request import Request, urlopen
import urllib.request
import json
import os

# if password_choice == str("y") or password_choice == str("Y"):


cwd = os.getcwd()
now = datetime.now()
current_time = str(now.strftime("%Y-%m-%d-%H-%M-%S"))

hdr = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36', 
    'Accept-Language': 'en-US,en;q=0.8'
    }


input = input("Check username in data breach: ")
req = urllib.request.Request(
  'https://haveibeenpwned.com/unifiedsearch/' + input, 
    headers=hdr
    )


try:
	with urllib.request.urlopen(req) as resp:
		print("\nPwned | Founded data breach for your entered input")
		print("Saving all available data wait...")
		json = json.loads(resp.read().decode("utf-8"))
		#print(data) #print the result found
		#the_page = resp.code #remove # if you want to print the http status code
		#print(the_page) #remove # if you want to print the http status code
		html=(json2html.convert(json=json))
		print("\n\033[92m(\033[0m>\033[92m)\033[0m All founded data breached details are saved as "+ input + ".json to", cwd)
		print("\033[92m(\033[0m>\033[92m)\033[0m All founded data breached details are saved as "+ input + ".html to", cwd)
		saveFile = open(input + '.json', 'w')
		saveFile.write(str(json))
		saveFile.close()
		saveFile = open(input + '.html', 'w')
		saveFile.write(str(html))
		saveFile.close()



except Exception as e:
	pass
	print("\n\033[92mGood news — no pwnage found!\033[0m\n     No breached data")
print("\nScanning finished.")

