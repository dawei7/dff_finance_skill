import json


f = open("mock_assets/banks_account_balances.json")
banks = json.load(f,encoding='utf-8')
f.close()

def check_available_banks():
    my_banks = "\n"
    for bank in banks.keys():
        my_banks+=f"{bank}\n"

    return my_banks