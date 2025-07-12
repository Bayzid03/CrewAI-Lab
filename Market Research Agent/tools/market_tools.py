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