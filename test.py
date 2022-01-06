
import plotly.express as px
import yfinance as yf

msft = yf.Ticker("MSFT")

# get stock info

df = msft.history(period="max")


fig = px.line(df, x='Date', y="Close")
fig.show()

