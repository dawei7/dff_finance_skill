from typing import Any
from df_engine.core import Actor, Context


def loop_checker(ctx: Context,loopchecker=True) -> Any:
    if ctx.misc.get("language_not_changed") == True and ctx.last_label == ctx.misc.get("previous_label") and loopchecker:
        response = """
I'm afraid I didn't understand you, please try it again.
"""
    else:
        response = """
"""
    
    return response