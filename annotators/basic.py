import re

from df_engine.core import Context


def check_language(ctx: Context):
    request = ctx.last_request.lower()

    if re.search(r"\b(german)\b|\b(deutsch)\b|\b(de)\b", request):
        ctx.misc["language"] = "DE"
        return ctx
    elif re.search(r"\b(english)\b|\b(englisch)\b|\b(en)\b", request):
        ctx.misc["language"] = "EN"
        return ctx
    else:
        return ctx