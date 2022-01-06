import json
import re
import plotly.express as px
import yfinance as yf

from df_engine.core import Actor, Context
from .condition_util import clean_request


def shares_info(ctx:Context):
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


def get_ticker(ctx:Context):
    request = ctx.last_request
    try:
        msft = yf.Ticker(request)
        df = msft.history(period="max")
        fig = px.line(df, x=df.index, y="Close")
        fig.show() # Opens a separate Browser window
        return "\nSuccess, see scatter plot in separate browser window."
    except:
        return "Failed, please type a valid ticker symbol."