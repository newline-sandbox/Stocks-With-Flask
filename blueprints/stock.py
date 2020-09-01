from flask import Blueprint, render_template 
import requests

stock = Blueprint("stock", __name__, url_prefix="/stocks")

def fetch_price(ticker):
  data = requests.get("https://financialmodelingprep.com/api/v3/stock/real-time-price/{}".format(ticker.upper()), params={"apikey": "7ee6a284877bac2cf363374463688fcd"}).json() 
  return data["price"]  