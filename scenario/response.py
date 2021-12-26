from typing import Dict, List, Tuple, Any
import re
import deepl
import os
import json

from df_engine.core import Actor, Context
from df_engine.core.keywords import TRANSITIONS, RESPONSE
import df_engine.conditions as cnd
import df_engine.labels as lbl
import requests

from annotators.main import annotate

from scenario.main import LANG

# 1. ----------GLOBAL FLOW----------
def check_language(ctx: Context, actor: Actor, *args, **kwargs) -> bool:
    global LANG
    request = ctx.last_request.lower()

    if re.search(r"\b(german)\b|\b(deutsch)\b|\b(de)\b", request):
        LANG = "DE"
        return True
    elif re.search(r"\b(english)\b|\b(englisch)\b|\b(en)\b", request):
        LANG = "EN"
        return True
    else:
        return False


def bot_introduction(ctx: Context, actor: Actor) -> Any:
    global LANG
    response = """
Hello I'm your personal financial bi-lingual chat-bot.
I speak 'English and 'German'. Whenever you want to change the language
type the keyword 'german' or 'english' to switch the language.
You can go back to this bot introduction anywhere in the chat workflow by typing 'start'.

I have the following financial skills:
    - Check your balance
    - Deposit money
    - Transfer money
    - Chatting about financial topics
    - Showing current share prices (yfinance API)

Off-topic skill:
    - Information about the creator of the bot.
"""
    if LANG == "EN":
        return response
    elif LANG == "DE":
        translator = deepl.Translator(os.getenv("DEEPL_AUTH_KEY"))
        return translator.translate_text(response, target_lang="DE")

def bot_introduction_loop(ctx: Context, actor: Actor) -> Any:
    global LANG
    response = "\n"
    if LANG == "EN":
        response += "I'm afraid I didn't understand you, please try again.\n"
        response += bot_introduction(ctx, actor)
    elif LANG == "DE":
        response += "Ich habe Sie leider nicht verstanden, bitte versuchen Sie es nochmals.\n"
        response += bot_introduction(ctx, actor)
    return response


def transition_check_balance_flow(ctx: Context, actor: Actor, *args, **kwargs) -> bool:
    global LANG
    request = ""

    if LANG=="DE":
        translator = deepl.Translator(os.getenv("DEEPL_AUTH_KEY"))
        request = str(translator.translate_text(ctx.last_request, target_lang="EN-US")).lower()
    elif LANG == "EN":
        request = ctx.last_request.lower()

    return re.search(r"\b(check)\b|\b(checking)\b|\b(balance)\b", request)!=None # True if found, else None if False


# 2. ----------CHECK BALANCE FLOW----------

def check_balance_node1_response(ctx: Context, actor: Actor, *args, **kwargs) -> Any:
    global LANG

    # Opening JSON file
    f = open("mock_assets/banks_account_balances.json")
 
    # returns JSON object as
    # a dictionary
    data = json.load(f)
 
    # Closing file
    f.close()

    response = data

    if LANG=="DE":
        translator = deepl.Translator(os.getenv("DEEPL_AUTH_KEY"))
        return translator.translate_text(response, target_lang="EN-US")
    elif LANG == "EN":
        return response