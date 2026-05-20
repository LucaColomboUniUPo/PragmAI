from dotenv import load_dotenv
from agno.agent import Agent
from agno.run.agent import RunOutput
from agno.db.sqlite import SqliteDb
from agno.models.google import Gemini
from agno.os import AgentOS
load_dotenv()

# I prezzi sono stati segnati tenendo conto della cifra più alta delle due disponibili 
# Da tenere d'occhio il fatto che se si parla di audio i costi aumentano 
geminiModel = {
    "gemini-2.5-flash":{
        "inToken": 0.30,
        "outToken": 2.50,
        "cacheToken": 0.03
    },
    "gemini-3.1-pro-preview":{
        "inToken": 4,
        "outToken": 18,
        "cacheToken": 0.40
    },
    "gemini-3-flash-preview":{
        "inToken": 0.50,
        "outToken": 3,
        "cacheToken": 0.05
    }
}

# Estraggo i dati che servono per il System Prompting
with open("./markdown/context.md", "r", encoding="utf-8") as f:
    context_prompt = f.read()
with open("./markdown/cameriere.md", "r", encoding="utf-8") as f:
    cameriere_prompt = f.read()

# Funzione che calcola l'utilizzo dei token ed il loro relativo costo
def calcoloTokenInOut(
    run_output: RunOutput
) ->None:
    costoInToken= (run_output.metrics.input_tokens * geminiModel[convAgent.model.id]["inToken"])/1000000
    costoOutToken = run_output.metrics.output_tokens * geminiModel[convAgent.model.id]["outToken"]/1000000
    costoCacheToken = run_output.metrics.cache_read_tokens * geminiModel[convAgent.model.id]["cacheToken"]/1000000
    with open("cost.txt", "a") as f:
        f.write(f"Costo token input per {run_output.metrics.input_tokens} token: {costoInToken} "
                f"Costo token output per {run_output.metrics.output_tokens} token: {costoOutToken} "
                f"Costo token cache per {run_output.metrics.cache_read_tokens} token: {costoCacheToken} \n")


# Agente che permette la conversazione
convAgent = Agent(
    model=Gemini(id="gemini-3.1-pro-preview"),
    db=SqliteDb(db_file="tmp/agno_demo.db"),  # necessario per la cronologia
    add_history_to_context=True,
    instructions=[context_prompt],
    description=cameriere_prompt,
    markdown=True,
    num_history_runs=5,
    post_hooks=[calcoloTokenInOut],
)

# Parte necessaria per permettere all'agente di essere eseguito su AgnoOS
agent_os = AgentOS(agents=[convAgent])
app = agent_os.get_app()