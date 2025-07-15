import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from typing import List, Dict
import json
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def process_news_data(news_articles: List[Dict]) -> pd.DataFrame:
    """Process news articles into a pandas DataFrame."""
    if not news_articles:
        logger.warning("No news articles provided")
        return pd.DataFrame()
    
    processed_data = []
    for article in news_articles:
        if isinstance(article, dict):
            processed_data.append({
                'title': article.get('title', ''),
                'description': article.get('description', ''),
                'published_at': article.get('publishedAt', ''),
                'source': article.get('source', {}).get('name', '')
            })
        else:
            logger.warning(f"Skipping invalid article format: {type(article)}")
    
    return pd.DataFrame(processed_data)

def create_stock_plot(stock_data: pd.DataFrame, symbol: str) -> str:
    """Create a plotly figure for stock data."""
    if stock_data.empty:
        logger.warning(f"No stock data available for {symbol}")
        return ""
    
    try:
        fig = go.Figure()
        fig.add_trace(go.Candlestick(
            x=stock_data.index,
            open=stock_data['Open'],
            high=stock_data['High'],
            low=stock_data['Low'],
            close=stock_data['Close'],
            name=symbol
        ))
        
        fig.update_layout(
            title=f'{symbol} Stock Price',
            yaxis_title='Price',
            xaxis_title='Date'
        )
        
        return fig.to_json()
    except Exception as e:
        logger.error(f"Error creating stock plot for {symbol}: {str(e)}")
        return ""
