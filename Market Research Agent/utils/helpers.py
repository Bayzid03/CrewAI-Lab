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
