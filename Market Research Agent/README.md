# Market Research Automation using CrewAI

This project implements an automated market research system using CrewAI agents. The system consists of multiple specialized AI agents that work together to gather, analyze, and present market insights.

## Features

- Automated market data collection from multiple sources
- Data analysis and processing
- Market trend identification
- Automated report generation with visualizations

## Setup

1. Install Python 3.9 or higher
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env` file with your API keys:
   ```
   GOOGLE_API_KEY=your_google_api_key
   NEWS_API_KEY=your_newsapi_key
   ```

## Project Structure

- `agents/`: Contains the CrewAI agent definitions
- `tools/`: Custom tools for data collection and processing
- `utils/`: Utility functions and helpers
- `market_research.py`: Main script to run the market research automation

## Usage

Run the main script:
```bash
python market_research.py
```

## Requirements

- Python 3.9+
- CrewAI framework
- LangChain
- Pandas
- Gemini API
- Various data source APIs (NewsAPI, Yahoo Finance, etc.) 