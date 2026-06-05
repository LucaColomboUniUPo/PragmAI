from google import genai

client = genai.Client()

with open("./markdown/task.md", "r", encoding="utf-8") as f:
    task = f.read()

def tracker_task(last_messages: str) -> str:
    """
        Usa sempre questo tool per validare il progresso dell'utente rispetto ai task 
        didattici. Restituisce l'ultimo task completato e cosa manca per procedere.
        Richiede come input 'last_messages' (una stringa con gli ultimi scambi del dialogo).
    """
    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=f"""
            Agisci come un log di sistema per un'apprendimento linguistico.
            Task totali: {task}
    
            Analizza la cronologia recente: {last_messages}
    
            Indica:
            1. L'ID dell'ultimo task COMPLETATO con successo.
            2. Eventuali task saltati.
            3. Cosa deve fare l'utente per sbloccare il task successivo.
    
            Sii brevissimo, massimo 30 parole.
        """
    )
    return response.text