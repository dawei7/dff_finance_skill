from typing import Dict, List, Tuple, Any
import re
import deepl
import os
import json
import logging

from df_engine.core import Actor, Context



logger = logging.getLogger(__name__)

translator = deepl.Translator(os.getenv("DEEPL_AUTH_KEY")) # DEEPL API

# 0. ----------GENERAL----------
def clean_request(ctx: Context)-> Any:
    language = ctx.misc.get("language")
    request = ""

    if language =="DE":
        request = str(translator.translate_text(ctx.last_request, target_lang="EN-US")).lower()
    elif language == "EN":
        request = ctx.last_request.lower()
    
    return request


# 1. ----------GLOBAL FLOW----------
def check_banks(ctx: Context, actor: Actor) -> bool:

    return re.search(r"\b(check)\b|\b(checking)\b|\b(balance)\b|\b(deposit)\b|\b(withdraw)\b|\b(transfer)\b", clean_request(ctx))!=None # True if found, else None if False


# 2. ----------CHECK ACCOUNTS FLOW----------
# 2.2
def check_balance(ctx: Context, actor: Actor) -> Any:
    
    return re.search(r"\b(check)\b|\b(checking)\b|\b(balance)\b|\b(deposit)\b|\b(withdraw)\b|\b(transfer)\b", clean_request(ctx))!=None # True if found, else None if False

# 2.3
def tranfer_money(ctx: Context, actor: Actor) -> Any:
    pass

# 2.4
def deposit_money(ctx: Context, actor: Actor) -> Any:
    pass

#2.5
def withdraw_money(ctx: Context, actor: Actor) -> Any:
    pass