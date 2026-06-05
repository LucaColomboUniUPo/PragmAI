from dotenv import load_dotenv
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


# Parte necessaria per permettere all'agente di essere eseguito su AgnoOS
agent_os = AgentOS(agents=[convAgent.convAgent, startConvAgent.startAgent])
app = agent_os.get_app()