import requests,os,sys,time
from time import sleep
print ('Tools By ALgi FH')

nomor = input('Target :')
print ('Target Locked...')
jm = int(input('Attack :'))

for i in range(jm):
      req=requests.get("https://amfcode.my.id/api/spamsms",params={"phone":nomor}).text
      if "mengirim" in req:
            print ('Fetch Database')
      else:
            print ('Done...')



