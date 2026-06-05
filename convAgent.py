from agno.agent import Agent
from agno.db.sqlite import SqliteDb
from agno.models.google import Gemini
from tool.taskTool import tracker_task
from tknInOut import calcoloTokenInOut

# Estraggo i dati che servono per il System Prompting
with open("./markdown/context.md", "r", encoding="utf-8") as f:
    context_prompt = f.read()
with open("./markdown/role.md", "r", encoding="utf-8") as f:
    cameriere_prompt = f.read()

convAgent = Agent(
    model=Gemini(id="gemini-3.1-pro-preview"),
    db=SqliteDb(db_file="tmp/agno_demo.db"),  # necessario per la cronologia
    add_history_to_context=True,
    instructions=[context_prompt],
    description=cameriere_prompt,
    markdown=True,
    num_history_runs=5,
    post_hooks=[calcoloTokenInOut],
    tools=[tracker_task]
)