#! /usr/bin/python

from subprocess import check_output as check

print("""
  ______             _______                   __          
 |___  /            |__   __|                 / _|         
    / / ___  _ __   ___| |_ __ __ _ _ __  ___| |_ ___ _ __ 
   / / / _ \| '_ \ / _ \ | '__/ _` | '_ \/ __|  _/ _ \ '__|
  / /_| (_) | | | |  __/ | | | (_| | | | \__ \ ||  __/ |   
 /_____\___/|_| |_|\___|_|_|  \__,_|_| |_|___/_| \___|_|   
                                                           
                Author: Batuhan Türkarslan
                GitHub: https://github.com/TURKZEN                                                           
""")

domain = input("Domain : ")
ns1 = input("NS1 : ")
ns2 = input("NS2 : ")



output1 = check(["dig","@{}".format(ns1),domain,"axfr"])

output1 = output1.decode()
output1 = output1.split()
output1 = output1[::-1]

output2 = check(["dig","@{}".format(ns2),domain,"axfr"])

output2 = output2.decode()
output2 = output2.split()
output2 = output2[::-1]

if output1[0] == "failed.":
    print("[-] NS1'de Zone Transfer Açığı Bulunamadı !")
else:
    print("[+] NS1'de Zone Transfer Açığı Bulundu !")

if output2[0] == "failed.":
    print("[-] NS2'de Zone Transfer Açığı Bulunamadı !")
else:
    print("[+] NS2'de Zone Transfer Açığı Bulundu !")

