from typing import Dict, List, Tuple, Any
import re
import deepl
import os
import json

from df_engine.core import Actor, Context

from scenario.response_util import loop_checker
import scenario.helper_check_balance as helper_check_balance


# translator
translator = deepl.Translator(os.getenv("DEEPL_AUTH_KEY"))



# 0. ----------GENERAL----------




# 1. ----------GLOBAL FLOW----------

def bot_introduction(ctx: Context, actor: Actor) -> Any:
    language = ctx.misc.get("language")

    response = loop_checker(ctx)

    response += """
Hello I'm your personal financial bi-lingual chat-bot.
I speak 'English and 'German'. Whenever you want to change the language
type the keyword 'german' or 'english' to switch the language.
You can go back to this bot introduction anywhere in the chat workflow by typing 'start'.

I have the following financial skills:
    - Check your balance, transfer money, deposit/withdraw money (REGEX/ Local save)
    - Showing current share prices (REGEX/ yfinance API)
    - Chatting about financial topics (HuggingFace)

Off-topic skill:
    - Information about the creator of the bot. (ML/DL)
--------------------------------------------------------------------------------------------
"""
    if language == "EN" or language==None:
        return response
    elif language == "DE":
        return str(translator.translate_text(response, target_lang="DE"))

# 2. ----------CHECK BALANCE FLOW----------

def check_banks(ctx: Context, actor: Actor) -> Any:
    language = ctx.misc.get("language")

    response = loop_checker(ctx)
    response += """
You have balances on the following bank accounts:
- By typing the Bank's name, you can access your balance and interest rate.
- By typing two Bank's name, you can transfer money from one bank to another
- You can deposit money to a bank
- You can wihdraw money from a bank
-------------------------------------------------------------------------------------------
"""

    if language == "DE":
        return str(translator.translate_text(response, target_lang="DE")) + helper_check_balance.check_available_banks()
    elif language == "EN":
        return response + helper_check_balance.check_available_banks()