from google.adk.agents.llm_agent import Agent
from google.genai import types
root_agent = Agent(
    model='gemini-3.5-flash',
    name='root_agent',
    description='A helpful assistant for user questions.',
    instruction='Answer user questions to the best of your knowledge',
    generate_content_config=types.GenerateContentConfig(  
            temperature=0.3, # lower = more consistent support answers 
            max_output_tokens=800 
            ) 
)
