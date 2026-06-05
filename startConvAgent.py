from dotenv import load_dotenv
from agno.agent import Agent
from agno.run.agent import RunOutput
from agno.db.sqlite import SqliteDb
from agno.models.google import Gemini
from agno.os import AgentOS
from tool.createMD import createMD
from tknInOut import calcoloTokenInOut
load_dotenv()

with open("./markdown/instrStart.md", "r", encoding="utf-8") as f:
    instrPrompt = f.read()

startAgent = Agent(
    model=Gemini(id="gemini-3.1-pro-preview"),
    db=SqliteDb(db_file="tmp/agno_demo.db"),  # necessario per la cronologia
    add_history_to_context=True,
    instructions=[instrPrompt],
    markdown=True,
    num_history_runs=5,
    tools=[createMD],
    post_hooks=[calcoloTokenInOut]
)