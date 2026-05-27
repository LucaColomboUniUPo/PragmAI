from google import genai

client = genai.Client()

task = {
    "T1": "Il cameriere saluta il cliente, chiede se ha prenotato, propone un tavolo.",
    "T2": "Il cameriere accompagna al tavolo, consegna il menù, propone qualcosa da bere nell'attesa.",
    "T3": "Il cameriere chiede se il cliente è pronto, risponde a domande sui piatti, prende l'ordine e lo conferma.",
    "T4": "Il cameriere porta i piatti ordinati e augura buon appetito.",
    "T5": "Il cameriere verifica che tutto sia di gradimento. Risponde a eventuali richieste aggiuntive.",
    "T6": "Il cameriere propone dessert e/o caffè.",
    "T7": "Il cameriere porta il conto quando richiesto e gestisce il pagamento.",
    "T8": "Ringraziamenti e saluti reciproci. La conversazione si chiude."
}

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