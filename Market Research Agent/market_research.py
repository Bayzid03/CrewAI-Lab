from crewai import Crew, Task
from agents.research_agents import ResearchAgents
from tools.market_tools import MarketTools
from utils.helpers import process_news_data, create_stock_plot, save_report
import os
from dotenv import load_dotenv

load_dotenv()