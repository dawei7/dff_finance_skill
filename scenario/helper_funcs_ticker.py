import json
import re
import plotly.express as px
import yfinance as yf
import wikipediaapi

from df_engine.core import Actor, Context
from .condition_util import clean_request
from scenario.transformers import qa

# General instance
wiki = wikipediaapi.Wikipedia('en')


def overview_ticker(ctx:Context):
    my_response ="""I am your stock scatter plot assistant; please type any public traded stock with the corresponding "ticket symbol".
To start with, here are some exemplatory corporations with corresponding ticker symbol:
----------------------------------------------------
Ticker Symbol | Corporation
----------------------------------------------------
F             | Ford Motor Company
AAPL          | Apple Inc.
AMD	          | Advanced Micro Devices, Inc.
T	          | AT&T Inc.
LCID	      | Lucid Group, Inc.
PLTR	      | Palantir Technologies Inc.
NVDA	      | NVIDIA Corporation
MSFT	      | Microsoft Corporation
PFE	          | Pfizer Inc.
BABA	      | Alibaba Group Holding Limited
TSLA	      | Tesla, Inc.
UBER	      | Uber Technologies, Inc.
INTC	      | Intel Corporation
"""
    return my_response


def plot_ticker(ctx:Context):
    request = ctx.last_request
    try:
        ticker = yf.Ticker(request)
        ctx.misc["ticker_name"] = ticker.info["longName"]
        df = ticker.history(period="max")
        fig = px.line(df, x=df.index, y="Close", )
        fig.show() # Opens a separate Browser window
        return """
Success, see scatter plot in separate browser window.
If you like you can ask the bot in a free QA about the chosen company (Distillbert & Wikipedia)
"""
    except:
        return """
Failed, please type a valid ticker symbol."""


def QA_ticker(ctx:Context,question):

    try:
        ticker_name = ctx.misc.get("ticker_name")
        page = wiki.page(ticker_name)
        context = page.summary
        result = qa(question,context)
        return "\n"+result["answer"]
    except:
        return f"""
Wiki article for {ticker_name} not found. Please try another ticker."""