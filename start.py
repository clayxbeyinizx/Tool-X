import os
import sys
import time
os.system("clear")
screen="""
-----------------------------------------
\033[1m[Bilgi]\033[92m Selam, Ben ClayX Bu Toolda Sizin isinize yarayacak toollar gosterilmistir
-----------------------------------------
\033[1m[Kullanim]\033[0m Baslamak icin 1 veya 2 yi secin
-----------------------------------------
[!]Bu Uygulamada Yuklediginiz Toollar Yalnız Bu Toolda Kullanılabilir 
-----------------------------------------
"""
print (screen)
banner="""
\033[1m1) Termuxu Guncelle
\033[1m2) Tool Kit +10
"""
print (banner)
login=int(input("Seçiniz: "))
if login==1:
   time.sleep(0.56)
   print ("[√] İşlem Tamamlandı")
   time.sleep(0.80)
   print ("[√] Termux Guncelleniyor")
   os.system("pkg install && pkg update && pkg upgrade && pkg install curl && pkg install pip && pkg install pip2 && pkg install pip3 && pkg install unstable-repo pkg install python && pkg install python2 && pkg install python3")
   time.sleep(0.80)
   print ("[√] İşlem Tamamlandi")
   os.system("clear")
   os.system("python toolstarting.py")
elif login==2:
    os.system("clear")
    print("""
-----------------------------------------
    1)Sms Bombası Hard
    2)Router Sploit
    3)Insta Spam 2.1
    4)Admin Panel
    5)Cam Hacker
    6)Trojan
    7)Sql Map
    8)wifi hack
    9)yubasms
    10)Exit
-----------------------------------------
                         """)
login2=int(input("Seçiniz: "))    
if login2==1:
    os.system("clear")
    os.system("cd")
    os.system("git clone https://github.com/umutkaratools/SMS-ATTACK")
    os.system("clear")
    time.sleep(0.80)
    print ("[√]Işlem Tamamlandi ")
    os.system("python toolstarting.py")
elif login2==2:
    os.system("clear")
    os.system("cd")
    os.system("git clone https://github.com/ethicalhackeragnidhra/Router-Sploit")
    os.system("clear")
    time.sleep(0.80)
    print ("[√]Işlem Tamamlandi ")
    os.system("python toolstarting.py")
elif login2==3:
    os.system("clear")
    os.system("cd")
    os.system("git clone https://github.com/ethicalhackeragnidhra/Router-Sploit")
    os.system("clear")
    time.sleep(0.80)
    print ("[√]Işlem Tamamlandi ")
    os.system("python toolstarting.py")
elif login2==4:
    os.system("clear")
    os.system("cd")
    os.system("git clone https://github.com/alexhacker313/Admin-Panel-Finder")
    os.system("clear")
    time.sleep(0.80)
    print ("[√]Işlem Tamamlandi ")
    os.system("python toolstarting.py")
elif login2==5:
    os.system("clear")
    os.system("cd")
    os.system("git clone https://github.com/AngelSecurityTeam/Cam-Hackers")
    os.system("clear")
    time.sleep(0.80)
    print ("[√]Işlem Tamamlandi ")
    os.system("python toolstarting.py")
elif login2==6:
    os.system("clear")
    os.system("cd")
    time.sleep(0.80)
    print ("[!] Error[404] ")
    time.sleep(0.50)
    os.system("python toolstarting.py")
elif login2==7:
    os.system("clear")
    os.system("cd && cd")
    os.system("git clone https://github.com/The404Hacking/sqlmap")
    os.system("clear")
    time.sleep(0.80)
    print ("[√]Işlem Tamamlandi ")
    os.system("python toolstarting.py")
elif login2==8:
    os.system("clear")
    os.system("cd")
    os.system("git clone https://github.com/esc0rtd3w/wifi-hacker")
    os.system("clear")
    time.sleep(0.80)
    print ("[√]Işlem Tamamlandi ")
    os.system("python toolstarting.py")
elif login2==9:
    os.system("clear")
    os.system("cd")
    os.system("git clone https://github.com/yuba-0/yubasms")
    os.system("clear")
    time.sleep(0.80)
    print ("[√]Işlem Tamamlandi ")
    os.system("python toolstarting.py")
elif login2==10:
    os.system("cd")
    os.system("ls")


