from llama_cpp import Llama

# Load your local LLaMA model
llm = Llama(
    model_path="./models/mistral-7b-instruct.Q4_K_M.gguf",
    n_ctx=2048,
    n_threads=4,
    n_gpu_layers=0
)

# LLM wrapper for CrewAI compatibility
def local_llm(prompt: str) -> str:
    try:
        output = llm(prompt, max_tokens=500, stop=["</s>"])
        return output["choices"][0]["text"].strip()
    except Exception as e:
        print(f"LLM error: {e}")
        return "Error: LLM failed to generate a response."

class LocalLLMWrapper:
    def __init__(self, engine):
        self.engine = engine

    def complete(self, prompt: str) -> str:
        return self.engine(prompt)

llm_wrapper = LocalLLMWrapper(local_llm)

# Define Agents
from crewai import Agent

researcher = Agent(
    role="Trend Researcher",
    goal="Identify a trending topic in technology today",
    backstory="An AI that keeps up with the latest tech trends on social media and blogs.",
    llm=llm_wrapper
)

explainer = Agent(
    role="Tech Explainer",
    goal="Break down the topic into simple, easy-to-understand concepts",
    backstory="A technical educator with a knack for simplifying complex ideas.",
    llm=llm_wrapper
)

writer = Agent(
    role="Blog Writer",
    goal="Write a blog post using the explanation and trend summary",
    backstory="A tech blogger with a passion for making technical content accessible.",
    llm=llm_wrapper
)

# Define Tasks
from crewai import Task

task1 = Task(
    description="Find and summarize a trending technology topic from 2025.",
    agent=researcher,
    expected_output="1-paragraph summary of a tech trend."
)

task2 = Task(
    description="Explain the trend from Task 1 in simple terms for beginners.",
    agent=explainer,
    depends_on=[task1],
    expected_output="Beginner-friendly explanation of the trend."
)

task3 = Task(
    description="Write a full blog post using the explanation and summary.",
    agent=writer,
    depends_on=[task1, task2],
    expected_output="Structured blog post (intro, body, conclusion)."
)

# Create and run the Crew
from crewai import Crew

crew = Crew(
    agents=[researcher, explainer, writer],
    tasks=[task1, task2, task3],
    verbose=True
)

result = crew.kickoff()
print(result)
