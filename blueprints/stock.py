from flask import Blueprint, render_template 
import requests

stock = Blueprint("stock", __name__, url_prefix="/stocks")

@stock.route("/<string:ticker>")
def view_stock(ticker):
  stock_price = fetch_price(ticker)
  return render_template("stock/stock_quote.html", ticker=ticker, stock_price=stock_price)

def fetch_price(ticker):
  data = requests.get("https://financialmodelingprep.com/api/v3/stock/real-time-price/{}".format(ticker.upper()), params={"apikey": "7ee6a284877bac2cf363374463688fcd"}).json() 
  return data["price"]  