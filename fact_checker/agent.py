from dotenv import load_dotenv
from google.adk.agents import Agent
from google.adk.apps.app import App
from google.adk.tools import google_search
from google.genai import types

# Load environment variables from .env file
load_dotenv(override=True)

root_agent = Agent(
    name="Facts",
    model="gemini-3.5-flash", # Gemini 3.5 flash at the time of writing
    instruction="""You are a fact checker. 
    You will be skeptical about anything that is said to you. 
    You will search the web and verify the given information 
    if it does not match you will respond with the latest 
    and factual information.""",
    description="An Agent to provide only facts about a given topic using Google Search.",
    generate_content_config=types.GenerateContentConfig(
        temperature=0.1 
    ),
    tools=[google_search],
)

app = App(name="fact_checker", root_agent=root_agent)
