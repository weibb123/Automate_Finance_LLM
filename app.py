from openai import OpenAI
import streamlit as st
from stock_data import get_stock
from langchain.chains import create_extraction_chain
from langchain_experimental.llms.ollama_functions import OllamaFunctions

# intialize llm function calling
model = OllamaFunctions(model="mistral")

#create client
client = OpenAI(api_key="ollama", base_url="http://localhost:11434/v1")

# structure to extract
schema = {
    "properties": {
        "ticker": {"type": "string"},
        "days": {"type": "integer"},
    },
    # "required": ["ticker", "days"],
}

# title of app
st.title("Automate Finance LLM")
prompt = st.chat_input("Pass your prompt here")

# if user types a prompt hits enter
if prompt:
    st.chat_message("user").markdown(prompt)

    # Function calling LLM call
    chain = create_extraction_chain(schema, model)
    extract_response = chain.invoke(prompt) # extract ticker, days from prompt using llm

    try:
        prices = get_stock(extract_response['text'][0]['ticker'], extract_response['text'][0]['days']) # prices is JSON object with dates, prices...
        st.chat_message("AI").markdown(prices)

        # query = user's question + the extracted prices
        query = extract_response['input'] + "\n" + str(prices)

        # produce summary
        whole_response = client.chat.completions.create(
            model="mistral",
            messages=[{"role": "user", "content": query}],
            stream = True
        )

        with st.chat_message("AI"):
            completed_message = ""
            message = st.empty()
            for chunk in whole_response:
                if chunk.choices[0].delta.content is not None:
                    # because output involves money sign, $, streamlit treats it as latex which cause weird text.
                    completed_message += str(chunk.choices[0].delta.content).replace("$", "\\$")
                    message.markdown(completed_message)
            

    except Exception as e:
        st.chat_message("AI").markdown("Bot is incorrect. Check if you have sepcify stock and days")