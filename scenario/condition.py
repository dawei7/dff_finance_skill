from typing import Dict, List, Tuple, Any
import re
import json
import logging

from df_engine.core import Actor, Context

from .condition_util import clean_request

import annotators.main as ctx_setter


logger = logging.getLogger(__name__)



# 0. ----------GENERAL----------
def check_language(ctx: Context, actor: Actor) -> bool:
    request = ctx.last_request.lower()

    if re.search(r"\b(german)\b|\b(deutsch)\b|\b(de)\b", request) and not ctx.misc["language_not_changed"]:
        return True
    elif re.search(r"\b(english)\b|\b(englisch)\b|\b(en)\b", request) and not ctx.misc["language_not_changed"]:
        return True
    else:
        return False


# 1. ----------GLOBAL FLOW----------
def check_banks(ctx: Context, actor: Actor) -> bool:

    return re.search(r"\b(check)\b|\b(checking)\b|\b(balance)\b|\b(deposit)\b|\b(withdraw)\b|\b(transfer)\b", clean_request(ctx))!=None # True if found, else None if False


# 2. ----------CHECK ACCOUNTS FLOW----------
# 2.2
def check_balances(ctx: Context, actor: Actor) -> bool:
    
    # Just checking, in response it has to be rechecked
    request = clean_request(ctx,lower=False)
    
    #check and at least one bank
    return re.search(r"\b(show)\b",request) != None and re.search(r"\b(all)\b|\b(All)\b|\b(UBS)\b|\b(Credit Suisse)\b|\b(Raiffeisen)\b|\b(Zuercher Kantonalbank)\b|\b(Postfinance)\b", request) != None

# 2.3
def tranfer_money(ctx: Context, actor: Actor) -> bool:

    request = clean_request(ctx,no_translation=True,lower=False)
    
    #check and at least one bank
    if re.search(r"\b(transfer)\b",request) != None and re.search(r"[1-9]\d*",request) != None:
        banks = ["".join(x) for x in re.findall(r"\b(UBS)\b|\b(Credit Suisse)\b|\b(Raiffeisen)\b|\b(Zuercher Kantonalbank)\b|\b(Postfinance)\b", request)]
        if len(banks) == 2:
            return True

    return False


# 2.4
def deposit_money(ctx: Context, actor: Actor) -> Any:
    
    request = clean_request(ctx,no_translation=True,lower=False)
    
    #check and at least one bank
    if re.search(r"\b(deposit)\b",request) != None and re.search(r"[1-9]\d*",request) != None:
        banks = ["".join(x) for x in re.findall(r"\b(UBS)\b|\b(Credit Suisse)\b|\b(Raiffeisen)\b|\b(Zuercher Kantonalbank)\b|\b(Postfinance)\b", request)]
        if len(banks) == 1:
            return True

    return False


#2.5
def withdraw_money(ctx: Context, actor: Actor) -> Any:
    request = clean_request(ctx,no_translation=True,lower=False)
    
    #check and at least one bank
    if re.search(r"\b(withdraw)\b",request) != None and re.search(r"[1-9]\d*",request) != None:
        banks = ["".join(x) for x in re.findall(r"\b(UBS)\b|\b(Credit Suisse)\b|\b(Raiffeisen)\b|\b(Zuercher Kantonalbank)\b|\b(Postfinance)\b", request)]
        if len(banks) == 1:
            return True

    return False