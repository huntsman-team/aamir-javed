#!/usr/bin/python
# coding=utf-8
# Originally Written By:Jam Shahrukh
# Source : Python2"
# Donot Recode It. 

#Import module
try:
    import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,uuid,cookielib,getpass,mechanize,requests
    from multiprocessing.pool import ThreadPool
    from requests.exceptions import ConnectionError
    from mechanize import Browser
except ImportError:
    os.system('pip2 install requests')
    os.system('pip2 install mechanize')
    os.system('python2 aamir.py')

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
\033[1;97m███████ \033[1;91m███████ \033[1;93m███    ███ \033[1;95m██ \033[1;96m██████ 
\033[1;97m██   ██ \033[1;91m██   ██ \033[1;93m████  ████ \033[1;95m██ \033[1;96m██   ██ 
\033[1;97m███████ \033[1;91m███████ \033[1;93m██ ████ ██ \033[1;95m██ \033[1;96m██████  
\033[1;97m██   ██ \033[1;91m██   ██ \033[1;93m██  ██  ██ \033[1;95m██ \033[1;96m██   ██ 
\033[1;97m██   ██ \033[1;91m██   ██ \033[1;93m██      ██ \033[1;95m██ \033[1;96m██   ██\033[1;90mKING
\033[1;94m══════════════════════════════════════════════
\033[1;90m➣ OWNER  : \033[1;97mAAMIR JAVED
\033[1;90m➣ Fb-Team: \033[1;97mHUNTSMAN KINGS OF FACEBOOK
\033[1;90m➣ Github : \033[1;97mhttps://github.com/huntsman-team
\033[1;94m══════════════════════════════════════════════ """
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
			
#Menu
def menu():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		os.system('clear')
		print"[!] Token Not Found"
		os.system('rm -rf login.txt')
		time.sleep(1)
		os.system('python2 aamir.py')
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		z = a['name']
		id = a['id']
	except KeyError:
		os.system('clear')
		print"[!] Account Is On Checkpoint"
		os.system('rm -rf login.txt')
		time.sleep(1)
		os.system('python2 aamir.py')
	except requests.exceptions.ConnectionError:
		print"[!] No Connection"
		time.sleep(1)
		('python2 aamir.py')
	os.system("clear")
	print banner
	print "|[✓] Name: "+z
	print "|[✓] ID  : "+id
	print (47*"-")
	print "[1] Clone With 4 Pass Mode."
	print "[2] Clone With 2 Pass Mode."
	print "[3] Extract Tools."
	print "[4] Lock Profile Tool."
	print "[5] Auto Del Tools."
	print "[6] Update Tool."
	print "[7] Follow Me On Facebook."
	print "[8] Logout"
	print ('                  ')
	men()

def men():
	rana = raw_input("Choose Option >>  ")
	if rana =="":
		print " Wrong Input"
		men()
	elif rana =="1":
	    os.system('clear')
	    jam('[!] Please Wait While Page Is Loding.')
	    sani('HUNTSMAN TEAM-100%...')
	    os.system('python2 crack.py')
	elif rana =="2":
	    os.system('clear')
	    jam('[!] Please Wait While Page Is Loding.')
	    sani('HUNTSMAN TEAM-100%...')
	    os.system('python2 fast.py')
	    time.sleep(1)
	elif rana =="3":
		grab()
	elif rana =="4":
		os.system('clear')
	        sani('HUNTSMAN TEAM-100%...')
		os.system('python locked.py')
		time.sleep(1)
	elif rana =="5":
		bot()
	elif rana =="6":
		os.system('clear')
		print banner
		jam('[✓] Please Wait While Tool Is Updating')
		os.system('git pull origin master')
		jam('[✓] Tool Has Been Update Successfully')
		jam('[✓] Please Wait While Update Is Setting Up On Your Mobile Phone')
		time.sleep(3)
		os.system('cd .. && rm -rf aamir-javed')
		os.system('git clone https://github.com/huntsman-team/aamir-javed')
		os.system('cd sani && python2 aamir.py')
	elif rana =="7":
		os.system('xdg-open https://www.facebook.com/aamir.bahtti.311')
		menu()
	elif rana =="8":
		os.system('rm -rf login.txt')
		jam('[✓] Logged Out Successfully')
		os.system('python2 aamir.py')
	else:
		print "[!] Wrong Input"
		men()
	
##### Grab #####
def grab():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"[!] Token Not Found"
		os.system('rm -rf login.txt')
		time.sleep(1)
		os.system('python2 aamir.py')
	os.system('clear')
	print banner
	print "[1] Extract Numeric IDs From Public ID."
	print "[2] Extract Email's From Public ID."
	print "[3] Extract Phone Number From Public ID."
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
	elif grm =="0":
		menu()
	else:
		print "[!] Wrong input"
		grab_menu()
		


##### Extract IDs From Public Id #####
def idfromfriend():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"[!] Token Not Found"
		os.system('rm -rf login.txt')
		time.sleep(1)
		('python2 aamir.py')
	try:
		os.mkdir('/sdcard/ids')
	except OSError:
		pass
	try:
		os.system('clear')
		print banner
		idt = raw_input("[+] Input ID : ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"[✓] Account Name : "+op["name"]
		except KeyError:
			print"[!] Friend Not Found"
			raw_input("Press Enter To Back ")
			grab()
		r=requests.get("https://graph.facebook.com/"+idt+"?fields=friends.limit(5000)&access_token="+toket)
		z=json.loads(r.text)
		jam('[✓] Getting Friends Numeric IDs...')
		print"--------------------------------------"
		bz = open('/sdcard/ids/aamir_file.txt','w')
		for a in z['friends']['data']:
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


##### EMAIL FROM Friend#####
def emailfromfriend():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"[!] Token Not Found"
		os.system('rm -rf login.txt')
		time.sleep(1)
		os.system('python2 aamir.py')
	try:
		os.mkdir('/sdcard/Email.txt')
	except OSError:
		pass
	try:
		os.system('clear')
		print banner
		idt = raw_input("[+] Input ID : ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"[✓] Account Name : "+op["name"]
		except KeyError:
			print"[!] Account Not Found"
			raw_input("\nPress Enter To Back ")
			grab()
		r = requests.get('https://graph.facebook.com/'+idt+'/friends?access_token='+toket)
		a = json.loads(r.text)
		jam('[✓] Getting Emails From')
		print 40*"\033[1;97m-"
		bz = open('save/email.txt','w')
		for i in a['data']:
			x = requests.get("https://graph.facebook.com/"+i['id']+"?access_token="+toket)
			z = json.loads(x.text)
			try:
				emfromfriend.append(z['email'])
				bz.write(z['email'] + '\n')
				print ("\r\033[1;97m[ \033[1;97m"+str(len(emfromfriend))+"\033[1;97m ]\033[1;97m  \033[1;97m"+z['email']+" | "+z['name']+"\n"),;sys.stdout.flush();time.sleep(0.0001)
			except KeyError:
				pass
		bz.close()
		print "----------------------------------"
		print '\r[✓] Successfully Extracted Mails'
		print"\r[✓] Total Mail Founded : "+str(len(emfromfriend))
		done = raw_input("\r\033[1;97m[✓] \033[1;97mSave File With Name\033[1;97m :\033[1;97m ")
		print("\r[✓] File Has Been Saved As : save/"+done)
		raw_input("\nPress Enter  To Back ")
		grab()
	except IOError:
		print"[!] Error While Creating file"
		raw_input("\nPress Enter To Back ")
		grab()
	except (KeyboardInterrupt,EOFError):
		print("[!] Process Has Been Stopped")
		raw_input("\nPress Enter To Back ")
		grab()
	except KeyError:
		print('[!] Error')
		raw_input("\nPress Enter To Back ")
		grab()
	except requests.exceptions.ConnectionError:
		print"\033[1;97m[✖] No Connection"
		time.sleep(1)
		grab()
		


##### Number From Public Id #####
def numberfromfriend():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"[!] Token Not Found"
		os.system('rm -rf login.txt')
		time.sleep(1)
		os.system('python2 aamir.py')
	try:
		os.mkdir('/sdcard/Number.txt')
	except OSError:
		pass
	try:
		os.system('clear')
		print banner
		idt = raw_input("[+] Input ID : ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"[✓] Account Name : "+op["name"]
		except KeyError:
			print"[!] Friend Not Found"
			raw_input("\nPress Enter To Back ")
			grab()
		r = requests.get('https://graph.facebook.com/'+idt+'/friends?access_token='+toket)
		a = json.loads(r.text)
		jam('[✓] Getting All Numbers')
		print 40*"\033[1;97m-"
		bz = open('save/number.txt','w')
		for i in a['data']:
			x = requests.get("https://graph.facebook.com/"+i['id']+"?access_token="+toket)
			z = json.loads(x.text)
			try:
				nofromfriend.append(z['mobile_phone'])
				bz.write(z['mobile_phone'] + '\n')
				print ("\r\033[1;97m[ \033[1;97m"+str(len(nofromfriend))+"\033[1;97m ]\033[1;97m \033[1;97m"+z['mobile_phone']+" | "+z['name']+"\n"),;sys.stdout.flush();time.sleep(0.001)
			except KeyError:
				pass
		bz.close()
		print "-----------------------------------"
		print"\r[✓] Total Number Founded : "+str(len(nofromfriend))
		done = raw_input("\r[?] Save File With Name: ")
		print("\r[✓] File Has Been Saved As save/"+done)
		raw_input("\nPress Enter To Back ")
		grab()
	except IOError:
		print"[!] Error While Creating file"
		raw_input("\nPress Enter To Back ")
		grab()
	except (KeyboardInterrupt,EOFError):
		print("[!]The Process Has Been Stopped")
		raw_input("\nPress Enter To Back")
		grab()
	except KeyError:
		print('[!] Error')
		raw_input("\nPress Enter To Back ")
		grab()
	except requests.exceptions.ConnectionError:
		print"\n[✖] No Connection"
		time.sleep(1)
		grab()

##### MENU BOT #####
#----------------------------------------#
def bot():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(1)
		os.system('python2 aamir.py')
	os.system('clear')
	print banner
	print "[1] Auto Delete Posts."
	print "[2] Auto Accept Friend Requests."
	print "[3] Auto Unfriend All."
	print "[0] Back."
	print ('         ')
	bot_menu()
	
def bot_menu():
	bots = raw_input("\nChoose Option >> ")
	if bots =="":
		print "[!] Wrong Input"
		bot_menu()
	elif bots =="1":
		deletepost()
	elif bots =="2":
		accept()
	elif bots =="3":
		unfriend()
	elif bots =="0":
		menu()
	else:
		print "[!] Wrong Input"
		bot_menu()
		


##### Auto Delt Post #####
def deletepost():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
		nam = requests.get('https://graph.facebook.com/me?access_token='+toket)
		lol = json.loads(nam.text)
		name = lol['name']
	except IOError:
		print"[!] Token Not Found"
		os.system('rm -rf login.txt')
		time.sleep(0.1)
		os.system('python2 aamir.py')
	os.system('clear')
	print banner
	print("[✓] Account Name : "+nama)
	jam("[✓] The Process Has Been Started")
	print (40*"-")
	asu = requests.get('https://graph.facebook.com/me/feed?access_token='+toket)
	asus = json.loads(asu.text)
	for p in asus['data']:
		id = p['id']
		piro = 0
		url = requests.get('https://graph.facebook.com/'+id+'?method=delete&access_token='+toket)
		ok = json.loads(url.text)
		try:
			error = ok['error']['message']
			print '\033[1;97m[\033[1;97m'+id[:10].replace('\n',' ')+'...'+'\033[1;97m] \033[1;97m[!] Failed'
		except TypeError:
			print '\033[1;97m[\033[1;97m'+id[:10].replace('\n',' ')+'...'+'\033[1;97m \033[1;97[✓] [Deleted]'
			piro += 1
		except requests.exceptions.ConnectionError:
			print"\033[1;91m[!] Connection Error"
			raw_input("\nPress Enter To Back ")
			bot()
	print (40*"-")
	print"[✓] The Process Has Been Completed. "
	raw_input("\nPress Enter To Back ")
	bot()
	
##### ACCEPT FRIEND #####
def accept():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"[!] Token Not Found"
		os.system('rm -rf login.txt')
		time.sleep(1)
		os.system('python2 aamir.py')
	os.system('clear')
	print banner
	limit = raw_input("[+] Enter Limit To Accept Requests : ")
	r = requests.get('https://graph.facebook.com/me/friendrequests?limit='+limit+'&access_token='+toket)
	teman = json.loads(r.text)
	if '[]' in str(teman['data']):
		print"No friend Request"
		raw_input("Press Enter To Back ")
		bot()
	jam('[✓] The Process Has Been Start')
	print (40*"-")
	for i in teman['data']:
		gas = requests.post('https://graph.facebook.com/me/friends/'+i['from']['id']+'?access_token='+toket)
		a = json.loads(gas.text)
		if 'error' in str(a):
			print "[!] [Failed] | "+i['from']['name']
		else:
			print "[!] [Accepted] |  "+i['from']['name']
	print (40*"-")
	print"[✓] The Process Has Been Completed."
	raw_input("\nPress Enter To Back ")
	bot()
	
##### UNFRIEND ####
def unfriend():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"[!] Token Not Found"
		os.system('rm -rf login.txt')
		time.sleep(1)
		os.system('python2 aamir.py')
	os.system('clear')
	print banner
	jam('[✓] The Process Has Been Started.')
	print "[✓] Press CTRL Z to Stop Process."
	print (50*"-")
	try:
		pek = requests.get('https://graph.facebook.com/me/friends?access_token='+toket)
		cok = json.loads(pek.text)
		for i in cok['data']:
			name = i['name']
			id = i['id']
			requests.delete("https://graph.facebook.com/me/friends?uid="+id+"&access_token="+toket)
			print "[✓] [Unfriended] | "+name
	except IndexError: pass
	except KeyboardInterrupt:
		print "[!]The Process Has Been Stopped"
		raw_input("\n Press Enter To Back ")
		bot()
	print"[✓] The Process Has Been Completed."
	raw_input("Press Enter To Back ")
	bot()
	
if __name__ == '__main__':
	menu()
