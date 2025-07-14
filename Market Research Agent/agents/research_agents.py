from crewai import Agent
from langchain.tools import Tool
from typing import List

class ResearchAgents:
    def __init__(self, tools: List[Tool]):
        self.tools = tools

    def create_research_manager(self) -> Agent:
        """Creates the Research Manager agent that coordinates the research process."""
        return Agent(
            role='Research Manager',
            goal='Coordinate and oversee the market research process',
            backstory="""You are an experienced Research Manager with expertise in 
            coordinating market research projects. Your role is to ensure all research 
            activities are properly organized and executed.""",
            verbose=True,
            tools=self.tools,
            allow_delegation=True,
            memory=True
        )

    def create_data_analyst(self) -> Agent:
        """Creates the Data Analyst agent that processes and analyzes market data."""
        return Agent(
            role='Data Analyst',
            goal='Process and analyze market data to identify trends and insights',
            backstory="""You are a skilled Data Analyst with expertise in processing 
            financial data and identifying market trends. You excel at cleaning data 
            and creating meaningful visualizations.""",
            verbose=True,
            tools=self.tools,
            memory=True
        )

    def create_industry_expert(self) -> Agent:
        """Creates the Industry Expert agent that provides domain-specific insights."""
        return Agent(
            role='Industry Expert',
            goal='Provide industry-specific insights and context to market data',
            backstory="""You are a seasoned Industry Expert with deep knowledge of 
            market dynamics and industry trends. You help interpret data in the 
            context of broader market conditions.""",
            verbose=True,
            tools=self.tools,
            memory=True
        )
