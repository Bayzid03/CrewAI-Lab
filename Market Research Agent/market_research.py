from crewai import Crew, Task
from agents.research_agents import ResearchAgents
from tools.market_tools import MarketTools
from utils.helpers import process_news_data, create_stock_plot, save_report
import os
from dotenv import load_dotenv

load_dotenv()

def main():
  # Initialize Tools
  market_tools = MarketTools()
  tools = market_tools.create_tools()

  # Initialize Agents
  research_agents = ResearchAgents(tools)
  research_manager = research_agents.create_research_manager()
  data_analyst = research_agents.create_data_analyst()
  industry_expert = reseach_agents.create_industry_expert()
  
  # Define tasks
  research_task = Task(
      description="""Gather market news and stock data for the specified company.
      Focus on recent developments, market trends, and financial performance.""",
      agent=research_manager
  )
