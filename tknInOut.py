from agno.run.agent import RunOutput

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

def calcoloTokenInOut(
    run_output: RunOutput
) :
    """
    Funzione utilizzata per calcolare l'utilizzo ed il costo dei token di input, output e di cache
    """
    model = run_output.model
    tknInput = run_output.metrics.input_tokens
    tknOutput = run_output.metrics.output_tokens
    tknCache = run_output.metrics.cache_read_tokens

    costoInToken= tknInput*geminiModel[model]["inToken"]/1000000
    costoOutToken = tknOutput*geminiModel[model]["outToken"]/1000000
    costoCacheToken = tknCache*geminiModel[model]["cacheToken"]/1000000
    with open("cost.txt", "a") as f:
        f.write(f"Costo token input per {tknInput} token: {costoInToken} "
                f"Costo token output per {tknOutput} token: {costoOutToken} "
                f"Costo token cache per {tknCache} token: {costoCacheToken} \n")