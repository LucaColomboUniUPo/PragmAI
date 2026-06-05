from google import genai

client = genai.Client()

with open("./markdown/exampleContext.md", "r", encoding="utf-8")as f:
    context_example = f.read()

with open("./markdown/exampleRole.md", "r", encoding="utf-8")as f:
    role_example = f.read()

with open("./markdown/exampleTask.md", "r", encoding="utf-8")as f:
    task_example = f.read()

def createMD(conversation: str) -> str:
    """
        DA RICHIAMARE ALLA FINE DELLA CONVERSAZIONE per creare due file markdown.
        Uno che rappresenterà il contesto della conversazione, l'altro il ruolo dell'agente
        nella conversazione.
        Ricevere in input l'intera conversazione
    """
    
    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=f"""
            Devi analizzare questa conversazione: {conversation}
            In base ai dati emersi generare tredue file formati come segue:

            ===PRIMO BLOCCO===
            contenente il file da mandare come contesto. Prendere esempio da questo testo: {context_example}

            ===SECONDO BLOCCO===
            contente il file da mandare dove si dice il ruolo dell'agente nella conversazione. Prendere esempio da questo: {role_example}
            ===TERZO BLOCCO===
            contenente soltanto le task che deve eseguire. Seguire l'esempio dato: {task_example}
            Separare il primo, il secondo ed il terzo blocco categoricamente con questa stringa: ===SEPARA QUI===
            Generare prima il primo blocco, poi la stringa di separazione, poi il secondo blocco, poi la stringa di separazione e poi il terzo blocco
        """
    )

    text = response.text

    if "===SEPARA QUI===" in text:
        div = text.split("===SEPARA QUI===")
        context = div[0].strip()
        role = div[1].strip()
        task = div[2].strip()

        with open("./markdown/context.md", "w", encoding="utf-8")as f:
            f.write(context)

        with open("./markdown/role.md", "w", encoding="utf-8")as f:
            f.write(role)

        with open("./markdown/task.md", "w", encoding="utf-8")as f:
            f.write(task)