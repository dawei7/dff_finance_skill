from df_engine.core import Context,Actor
from .basic import *
import annotators.check_accounts as check_accounts # Import all custom condition functions
from typing import Any

def annotate(ctx: Context, actor: Actor, scope="basic") -> Any:


    if scope == "basic":
        ctx = check_language(ctx)
        ctx = previous_label(ctx)

        return ctx
    
def transfer_bank(ctx: Context,request,banks) -> Any:
    ctx.misc.setdefault("transfer_banks",banks)
    ctx.misc["transfer_amount"] = re.findall(r"[1-9]\d*",request)[0]

    return ctx


