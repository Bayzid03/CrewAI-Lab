from langchain.tools import Tool
from newsapi import NewsApiClient
import yfinance as yf
import pandas as pd
from typing import List, Dict
import os
from dotenv import load_dotenv

load_dotenv()

class MarketTools:
    def __init__(self):
        api_key = os.getenv('NEWS_API_KEY')
        if not api_key:
            raise ValueError("NEWS_API_KEY environment variable is required")
        self.newsapi = NewsApiClient(api_key=api_key)

    def get_market_news(self, query: str, days: int = 7) -> List[Dict]:
        """Get market news from NewsAPI."""
        if not query or not query.strip():
            return [{"error": "Query parameter is required"}]
        
        try:
            news = self.newsapi.get_everything(
                q=query,
                language='en',
                sort_by='relevancy',
                page_size=10
            )
            return news.get('articles', [])
        except Exception as e:
            return [{"error": f"Failed to fetch news: {str(e)}"}]

    def get_stock_data(self, symbol: str, period: str = "1mo") -> pd.DataFrame:
        """Get stock data from Yahoo Finance."""
        if not symbol or not symbol.strip():
            return pd.DataFrame({"error": ["Symbol parameter is required"]})
        
        try:
            stock = yf.Ticker(symbol.upper())
            hist = stock.history(period=period)
            if hist.empty:
                return pd.DataFrame({"error": [f"No data found for symbol {symbol}"]})
            return hist
        except Exception as e:
            return pd.DataFrame({"error": [f"Failed to fetch stock data: {str(e)}"]})

    def create_tools(self) -> List[Tool]:
        """Create and return a list of tools for the agents to use."""
        return[
            Tool(
                name="Get Market News",
                func=self.get_market_news,
                description="Get latest market news for a specific query. Input should be a search term."
            ),
            Tool(
                name="Get Stock Data",
                func=self.get_stock_data,
                description="Get historical stock data for a specific symbol. Input should be a stock symbol like 'AAPL' or 'MSFT'."
            )
        ]
