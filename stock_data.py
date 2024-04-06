import yfinance as yf
import json
from datetime import datetime


def get_stock(ticker, days):
    """description: fetch stock data
    Args:
    ticker: (str)
    days: (int)

    Example usage
    get_stock("AAPL", 30)

    Returns
    JSON object of stock data

    """
    try:
        # fetch data
        data = yf.download(ticker, period=f"{days}d", interval="1d")
        
        # format datetime -> dd/mm/yyyy format
        data.index = data.index.strftime("%m/%d/%Y")

        # convert to JSON format
        data_json = data.to_json(orient="index")

        stock = json.loads(data_json)

        return stock
    except Exception as e:
        return {"error": str(e)}