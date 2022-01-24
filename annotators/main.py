from df_engine.core import Context,Actor
from .basic import *
from typing import Any

def annotate(ctx: Context, actor: Actor, scope="basic") -> Any:

    # Check with every step
    if scope == "basic":
        ctx = check_language(ctx)
        ctx = previous_label(ctx)

        return ctx
    

