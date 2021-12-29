from typing import Dict, List, Tuple, Any
import re
import deepl
import os
import json
import logging

from df_engine.core import Actor, Context



logger = logging.getLogger(__name__)

translator = deepl.Translator(os.getenv("DEEPL_AUTH_KEY")) # DEEPL API


# 1. ----------GLOBAL FLOW----------
def check_banks(ctx: Context, actor: Actor, *args, **kwargs) -> bool:
    language = ctx.misc.get("language")
    request = ""

    if language =="DE":
        request = str(translator.translate_text(ctx.last_request, target_lang="EN-US")).lower()
    elif language == "EN":
        request = ctx.last_request.lower()

    return re.search(r"\b(check)\b|\b(checking)\b|\b(balance)\b|\b(deposit)\b|\b(withdraw)\b|\b(transfer)\b", request)!=None # True if found, else None if False