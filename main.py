from dotenv import load_dotenv
from agno.team.team import Team
from agno.team.mode import TeamMode
from agno.agent import Agent
from agno.run.agent import RunOutput
from agno.db.sqlite import SqliteDb
from agno.models.google import Gemini
from agno.os import AgentOS
from tool.taskTool import tracker_task
from tknInOut import calcoloTokenInOut
import startConvAgent
import convAgent
load_dotenv()

team = Team(
    name="PragmAI",
    mode=TeamMode.route,
    model=Gemini(id="gemini-2.5-flash-lite"),
    members=[convAgent.convAgent, startConvAgent.startAgent],
    add_history_to_context=True,
    db=SqliteDb(db_file="tmp/team.db"),
    instructions="Prima esegui startAgent, poi quando viene richiamato il tool di fine dialogo richiama convAgent"
)

# Parte necessaria per permettere all'agente di essere eseguito su AgnoOS
agent_os = AgentOS(agents=[convAgent.convAgent, startConvAgent.startAgent], teams=[team])
app = agent_os.get_app()