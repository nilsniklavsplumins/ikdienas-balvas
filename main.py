import json
from seleniumbase import SB
import os
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
            for i in funcs:
                toggle_run(i, to_run)
            start(to_run)
        case "1":
            toggle_run(claimAllkeyshop, to_run)
            prompt(to_run)
        case "2":
            toggle_run(claimCoinGecko, to_run)
            prompt(to_run)
        case "3":
            toggle_run(claimmsi, to_run)
            prompt(to_run)
        case _:
            prompt(to_run)

def start(sites):
    with SB(uc_cdp=True, guest_mode=True) as sb:
        for i in sites:
            i(sb, secret)

prompt(to_run)
