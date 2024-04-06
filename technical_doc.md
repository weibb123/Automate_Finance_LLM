1. download ollama

2. pip install langchain or upgrade, make sure it has langchain_community

3. pull the model you want to use.. ex: mistral-7b, ollama pull mistral

4. ```llm = Ollama(model="mistral")

llm.invoke("tell me a joke")``` -> serve the model as endpoint, for local use

{'input': 'summarise the stock price movement for AAPL for the last 7 days\n\n', 'text': [{'ticker': 'AAPL', 'days': 7}]}


function calling -> ollamafunction

