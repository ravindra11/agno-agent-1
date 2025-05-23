from agno.agent import Agent
from agno.models.openai import OpenAIChat


agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    description = "You are an enthusiastic news reporter with a flair for storytelling",
    markdown = True
)

agent.print_response("tell me about a breaking news story from US tarrifs.", stream=True)