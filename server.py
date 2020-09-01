from flask import Flask, render_template, redirect, request, url_for
import requests
from blueprints.stock import stock

app = Flask(__name__)
app.register_blueprint(stock)

@app.route("/")
def index():
  return render_template("home.html")

def fetch_price(ticker):
  data = requests.get("https://financialmodelingprep.com/api/v3/stock/real-time-price/{}".format(ticker.upper()), params={"apikey": "7ee6a284877bac2cf363374463688fcd"}).json() 
  return data["price"]   