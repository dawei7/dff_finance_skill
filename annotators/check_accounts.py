def check_balances(ctx,assets):
    ctx.misc.setdefault("banks",assets)
    return ctx