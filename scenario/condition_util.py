from typing import Any
from df_engine.core import Actor, Context

import os
import deepl

# Deepl API
translator = deepl.Translator(os.getenv("DEEPL_AUTH_KEY")) # DEEPL API

# Clean request, translate German iunto English
def clean_request(ctx: Context, no_translation=False, lower=True)-> Any:

    request = ""

    if no_translation:
        language = "EN"
    else:
        language = ctx.misc.get("language")

    if lower:
        if language=="DE":
            request = str(translator.translate_text(ctx.last_request, target_lang="EN-US")).lower()
        elif language=="EN":
            request = str(ctx.last_request.lower())
    elif not lower:
        if language=="DE":
            request = str(translator.translate_text(ctx.last_request, target_lang="EN-US"))
        elif language=="EN":
            request = str(ctx.last_request)
    
    return request