import json
import re
from df_engine.core import Actor, Context
from .condition_util import clean_request

f = open("mock_assets/banks_account_balances.json")
banks = json.load(f,encoding='utf-8')
f.close()

def check_available_banks():
    my_banks = "\n"
    for bank in banks.keys():
        my_banks+=f"- {bank}\n"

    return my_banks

def check_balances(ctx:Context):
    my_banks = ["".join(x) for x in re.findall(r"\b(all)\b|\b(All)\b|\b(UBS)\b|\b(Credit Suisse)\b|\b(Raiffeisen)\b|\b(Zuercher Kantonalbank)\b|\b(Postfinance)\b", clean_request(ctx, no_translation=True, lower=False))]

    if "all" in my_banks or "ALL" in my_banks:
        my_banks = ["UBS","Credit Suisse","Raiffeisen", "Zuercher Kantonalbank","Raiffeisen"]

    if my_banks == []:
        my_response = "\nYou have not chosen any bank, please try it again.\n\n"
    else:
        my_response= "\nYou have balances on the following bank accounts:\n\n"

        for bank in my_banks:
            my_response += f"{bank}:\n"
            for k, v in banks[bank].items():
                my_response += f"{k}: {v:,}\n"
            my_response += "\n"

    return my_response

def tranfer_money(ctx:Context):

    my_banks = ["".join(x) for x in re.findall(r"\b(UBS)\b|\b(Credit Suisse)\b|\b(Raiffeisen)\b|\b(Zuercher Kantonalbank)\b|\b(Postfinance)\b", clean_request(ctx, no_translation=True, lower=False))]
    my_amount = ["".join(x) for x in re.findall(r"[1-9]\d*",clean_request(ctx, no_translation=True, lower=False))]

    ctx.misc["transfer_banks"] = my_banks
    try:
        ctx.misc["transfer_amount"] = int(my_amount[0])
    except:
        ctx.misc["transfer_amount"] = None

    my_amount = ctx.misc.get("transfer_amount")

    try:
        my_response = f"\nAre you sure, that you want to transfer CHF {my_amount} from {my_banks[0]} to {my_banks[1]}?"
        my_response += "\nTo confirm the transaction please type 'yes' otherwise 'no'. To go back to the banks overview type 'back'."
        my_response += "\n-------------------------------------------------------------------------------------------"
    except:
        my_response ="\nSomething went wrong"

    return my_response

def transfer_money_confirm(ctx:Context):

    if re.search(r"\b(yes)\b",clean_request(ctx)) != None:
        try:
            my_response = ""
            my_banks = ctx.misc.get("transfer_banks")
            my_amount = ctx.misc.get("transfer_amount")


            withdraw_bank = my_banks[0]
            deposit_bank = my_banks[1]

            if banks[withdraw_bank]["Amount"]-my_amount>=0:
                banks[withdraw_bank]["Amount"] -= my_amount
                banks[deposit_bank]["Amount"] += my_amount

                my_response += f"\nSuccess! You tranferred CHF {my_amount} from {withdraw_bank} to {deposit_bank}.\n"
                my_response += "\nNew balances:\n\n"
                for bank in [withdraw_bank,deposit_bank]:
                    my_response += f"{bank}:\n"
                    for k, v in banks[bank].items():
                        my_response += f"{k}: {v:,}\n"
                    my_response += "\n Press any key to go back to the bank overview or press 'start to go back to the start'"

            else:
                my_response+= "\nVery sorry! The amount of the withdraw bank is too low. Please choose another amount"

            my_response += "\n-------------------------------------------------------------------------------------------"
    
        except:
            my_response ="\nSomething went wrong."

    else:
        my_response = "\n Alright. You didn't confirm."
        my_response += "\n Press any key to go back to the bank overview or press 'start to go back to the start'"

    return my_response