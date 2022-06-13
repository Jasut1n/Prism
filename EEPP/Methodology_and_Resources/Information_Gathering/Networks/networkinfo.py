#!/bin/python3
import shodan
import optparse
import subprocess

def main():
	query = str(input("Enter IP | Port | Organization: \n"))
	res = api.search(query)
	for service in res['matches']:
		print(service['ip_str'] + '   |   ' + str(service['port']) + '   |   ' + str(service['org']))

api = shodan.Shodan("SgU9XuO5BDy96qba0sHQ3bODnwovj5ns")

if __name__ == "__main__":
   try:
      main()
   except KeyboardInterrupt:
      # do nothing here
      pass
