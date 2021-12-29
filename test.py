import json

f = open("mock_assets/banks_account_balances.json")
banks = json.load(f,encoding='utf-8')
f.close()

my_banks = "\n"

for bank in banks.keys():
    my_banks+=f"{bank}\n"

print(my_banks)