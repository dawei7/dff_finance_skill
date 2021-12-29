import re
from deepl.translator import Language

from df_engine.core import Context
from df_engine.core.keywords import MISC


def check_language(ctx: Context):
    request = ctx.last_request.lower()

    if "language" not in ctx.misc:
        ctx.misc["language"] = "EN"

    ctx.misc["language_not_changed"] = False
    
    if re.search(r"\b(german)\b|\b(deutsch)\b|\b(de)\b", request):
        ctx.misc["language"] = "DE"
    elif re.search(r"\b(english)\b|\b(englisch)\b|\b(en)\b", request):
        ctx.misc["language"] = "EN"
    else:
        ctx.misc["language_not_changed"] = True
    
    return ctx

def previous_label(ctx:Context):

    if ctx.last_label==None or ctx.last_label==("global","start"):
        ctx.misc["previous_label"] = ("global","bot_introduction") # Special case for first & second run
    else:
        ctx.misc["previous_label"] = ctx.last_label

    return ctx