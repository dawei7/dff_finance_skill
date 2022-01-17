from typing import Dict, List, Tuple, Any
import re
import deepl
import os
import json

from df_engine.core import Actor, Context

from scenario.response_util import loop_checker
import scenario.helper_funcs_check_accounts as helper_funcs_check_accounts
import scenario.helper_funcs_ticker as helper_funcs_ticker
import scenario.helper_funcs_ask_the_bot_creator as helper_funcs_ask_the_bot_creator
from .condition_util import clean_request


# translator
translator = deepl.Translator(os.getenv("DEEPL_AUTH_KEY"))


# 0. ----------GENERAL----------
def clean_response(ctx: Context, response: str,loopchecker=True)-> Any:
    language = ctx.misc.get("language")

    clean_response = loop_checker(ctx,loopchecker=loopchecker)
    clean_response += response

    if language =="DE":
        return str(translator.translate_text(clean_response, target_lang="DE"))
    elif language =="EN":
        return clean_response

def clean_request(ctx: Context)-> str:
    language = ctx.misc.get("language")

    request = ctx.last_request

    if language =="DE":
        return str(translator.translate_text(request, target_lang="EN-US"))
    elif language =="EN":
        return request


# 1. ----------GLOBAL FLOW----------

def bot_introduction(ctx: Context, actor: Actor) -> Any:

    response = """
Hello I'm your personal financial bi-lingual chat-bot.
I speak 'English and 'German'. Whenever you want to change the language
type the keyword 'german' or 'english' to switch the language.
You can go back to this bot introduction anywhere in the chat workflow by typing 'start'.

I have the following financial skills:
    1. Check your balance, transfer money, deposit/withdraw money (REGEX/ Local save)
    2. Plot share tickers & QA of the company (yfinance API/ Plotly/ HuggingFace)

Other skill:
    3. If you like to get more information about me, query me (HuggingFace)
--------------------------------------------------------------------------------------------
"""
    return clean_response(ctx, response)

# 2. ----------CHECK ACCOUNTS FLOW----------

# 2.1
def check_banks(ctx: Context, actor: Actor) -> Any:

    response = "You have accounts on the following banks:\n"
    response += helper_funcs_check_accounts.check_available_banks()
    response += """
Instructions:
- By typing 'show' and one or more banks' name, you can access your banks' account details. If you type like "show all", all banks get listed.
- By typing 'transfer' two banks' name, you can transfer money from one bank to another
- By typing 'deposit' deposit money to a specified bank
- By typing 'withdraw' You can wihdraw money from a sceficied bank
-------------------------------------------------------------------------------------------
"""
    return clean_response(ctx, response)

# 2.2
def check_balances(ctx: Context, actor: Actor) -> Any:
    
    response = helper_funcs_check_accounts.check_balances(ctx)
    response += """Further possibilities:
- By typing 'back', you can go back to your banks' overview.
- By typing 'show' and one or more banks' name, you can access your banks' account details. If you type like "show all", all banks get listed.
- By typing 'transfer', two banks name and anb amount, you can transfer money from one bank to another.
- By typing 'deposit', a bank's name and an amount, you can deposit money to the specified bank.
- By typing 'withdraw', a bank's name and an amount, you can wihdraw money from a sceficied bank.
-------------------------------------------------------------------------------------------
"""


    return clean_response(ctx, response,loopchecker=False)

# 2.3
def transfer_money(ctx: Context, actor: Actor) -> Any:
    
    response = helper_funcs_check_accounts.tranfer_money(ctx)

    return clean_response(ctx, response)

def transfer_money_confirm(ctx: Context, actor: Actor) -> Any:
    
    response = helper_funcs_check_accounts.transfer_money_confirm(ctx)

    return clean_response(ctx, response)


# 2.4
def deposit_money(ctx: Context, actor: Actor) -> Any:
    
    response = helper_funcs_check_accounts.deposit_money(ctx)

    return clean_response(ctx, response)


def deposit_money_confirm(ctx: Context, actor: Actor) -> Any:
    
    response = helper_funcs_check_accounts.deposit_money_confirm(ctx)

    return clean_response(ctx, response)


#2.5
def withdraw_money(ctx: Context, actor: Actor) -> Any:
    
    response = helper_funcs_check_accounts.withdraw_money(ctx)

    return clean_response(ctx, response)

def withdraw_money_confirm(ctx: Context, actor: Actor) -> Any:
    
    response = helper_funcs_check_accounts.withdraw_money_confirm(ctx)

    return clean_response(ctx, response)

# 3.1
def overview_ticker(ctx: Context, actor: Actor) -> Any:

    response = helper_funcs_ticker.overview_ticker(ctx)

    return clean_response(ctx, response,loopchecker=False)

# 3.2
def plot_ticker(ctx: Context, actor: Actor) -> Any:
    
    response = helper_funcs_ticker.plot_ticker(ctx)

    return clean_response(ctx, response,loopchecker=False)

# 3.3
def QA_ticker(ctx: Context, actor: Actor) -> Any:
    
    response = helper_funcs_ticker.QA_ticker(ctx,clean_request(ctx))

    return clean_response(ctx, response,loopchecker=False)


# 4.1
def QA_start_ask_the_bot_creator(ctx: Context, actor: Actor) -> Any:
    
    response = helper_funcs_ask_the_bot_creator.QA_start_ask_the_bot_creator(ctx)

    return clean_response(ctx, response,loopchecker=False)


# 4.2
def QA_ask_the_bot_creator(ctx: Context, actor: Actor) -> Any:
    
    response = helper_funcs_ask_the_bot_creator.QA_ask_the_bot_creator(ctx,clean_request(ctx))

    return clean_response(ctx, response,loopchecker=False)