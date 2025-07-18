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
  
  analysis_task = Task(
      description="""Analyze the collected data to identify key trends and patterns.
      Create visualization and prepare the data for reporting. """,
      agent = data_analyst
  )

  insight_task = Task(
      description="""Provide industry concept and insights based on the analysis.
      Highlights key findings and their implications.""",
      agent = industry_expert
  )

  crew = Crew(
      agents = [research_manager, data_analyst, industry_expert],
      tasks = [research_task, analysis_task, insight_task],
      verbose = True
  )

  result = crew.kickoff()

  save_report(result)
  print("Market research completed and saved to market_research_report.json")

if __name__ = "__main__":
  main()
