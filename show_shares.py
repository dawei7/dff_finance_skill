
import plotly.express as px
import yfinance as yf

msft = yf.Ticker("MSFT")

# get stock info

df = msft.history(period="max")

fig = px.line(df, x=df.index, y="Close")
fig.show()

