from df_engine.core import Context
from .basic import *

def annotate(ctx: Context):
    ctx = check_language(ctx)
    ctx = previous_label(ctx)
    return ctx
