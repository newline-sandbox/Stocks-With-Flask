from flask import Flask, render_template, redirect, request, url_for
import requests

app = Flask(__name__)

@app.route("/")
def index():
  return render_template("home.html")

@app.route("/stocks/<string:ticker>")
def view_stock(ticker):
  stock_price = fetch_price(ticker)
  return render_template("stock_quote.html", ticker=ticker, stock_price=stock_price)

def fetch_price(ticker):
  data = requests.get("https://financialmodelingprep.com/api/v3/stock/real-time-price/{}".format(ticker.upper()), params={"apikey": "7ee6a284877bac2cf363374463688fcd"}).json() 
  return data["price"]   