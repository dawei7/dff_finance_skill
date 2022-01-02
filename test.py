import json
import locale
locale.setlocale(locale.LC_ALL, 'de_CH')

"""
f = open("mock_assets/banks_account_balances.json")
banks = json.load(f,encoding='utf-8')
f.close()

my_banks = "\n"

for bank in banks.keys():
    my_banks+=f"{bank}\n"

print(my_banks)

"""

f = open("mock_assets/banks_account_balances.json")
banks = json.load(f,encoding='utf-8')
f.close()

bank = banks["UBS"]

for k, v in bank.items():
    print(f"{k}: {v:,}")

