import json
import zipfile
from seleniumbase import SB
import os
import urllib.request
from modules.allkeyshop import claimAllkeyshop
from modules.coingecko import claimCoinGecko
from modules.msi import claimmsi

try:
    secret = json.load(open("secret.json", "r"))
except:
    raise Exception("secret.json nav atrasts")

funcs = {"Allkeyshop": claimAllkeyshop, "CoinGecko": claimCoinGecko, "MSI": claimmsi}

to_run = []

def toggle_run(func, arr):
    if func in arr:
        arr.remove(func)
    else:
        arr.append(func)

def prompt(to_run):
    global funcs
    os.system("cls")
    print("Izvēlieties, kuras balvas savākt.")
    for i in range(len(funcs)):
        print(str(i+1) + ") " + list(funcs.keys())[i] + ("✅" if list(funcs.values())[i] in to_run else "❌"))
    choice = input("Ievadiet ciparu, burtu S (sākt) vai burtu A (sākt un savākt visu): ").lower().strip()
    match choice:
        case "s":
            start(to_run)
        case "a":
            for i in list(funcs.values()):
                toggle_run(i, to_run)
            start(to_run)
        case _:
            try:
                choice = int(choice)
                toggle_run(list(funcs.values())[choice-1], to_run)
            except:
                pass
            prompt(to_run)

def start(sites):
    if claimAllkeyshop in sites and not os.path.exists("allkeyshop"):
        urllib.request.urlretrieve("https://clients2.google.com/service/update2/crx?response=redirect&os=linux&arch=x64&os_arch=x86_64&nacl_arch=x86-64&prod=chromium&prodchannel=unknown&prodversion=91.0.4442.4&lang=en-US&acceptformat=crx2,crx3&x=id%3Dbibdjkcebiliphphjbnkngdjgeklgcdf%26installsource%3Dondemand%26uc", "aks.zip")
        with zipfile.ZipFile("aks.zip", 'r') as zip_ref:
            zip_ref.extractall("allkeyshop")
        os.remove("aks.zip")
    with SB(uc_cdp=True, extension_dir=("allkeyshop" if claimAllkeyshop in sites else None)) as sb:
        for i in sites:
            i(sb, secret)

prompt(to_run)
