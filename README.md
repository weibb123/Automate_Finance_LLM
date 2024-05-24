# Automate_Finance_LLM

## Description

Project Title: Automate Finance with LLM

Developed a cutting-edge finance automation tool using Ollama, LangChain, and OpenAI, integrating with Yahoo Finance to retrieve and process real-time financial data

Designed and implemented a full-stack application, utilizing Streamlit for the front-end and leveraging Ollama(Mistral-7b) to automate financial analysis


## Table of Contents
- [Demo Video](#Demo-Video)
  - [Tech Stack](#Tech-Stack)
  - [Usage](#usage)
- [Next Step](#Next-Step)

![image](https://github.com/weibb123/Automate_Finance_LLM/assets/84426364/8100d88b-7ace-4328-9ae4-f1739b02da65)

## Demo Video
https://github.com/weibb123/Automate_Finance_LLM/assets/84426364/660d004c-d342-41be-b409-845baf791133

## Tech Stack
This demo make uses of Ollama, LangChain, openai, yahoofinance, and streamlit.

**Ollama**: Local host LLM. For this demo, mistral-7b was used.
```
ollama pull mistral
```

**LangChain**: To extract scheme from user's query and wrapper for openai and Ollama function calling

**openai**: For creating openai model server for Ollama(local model server). For Ollama, model is hosted via in specific ip address.

```
client = OpenAI(api_key="ollama", base_url="http://localhost:11434/v1")
```

**yahoofinance**: To download financial data of stocks and period.

**Streamlit**: For app frontend

## Usage
To run it locally, make sure to download ollama and do

```
ollama pull mistral
```

then run the app locally

```
streamlit run app.py
```

## Next Step
With LLM to automate finances, it is possible to generate an entire profile for a company.

Create training data for deep learning model to predict stocks

## Reference 
Nicholas Renotte - AI engineer at IBM

Inspired by Nicholas Renotte for demonstrating how to create fake openai server with llama.cpp. Although llama.cpp is hard to setup locally, this demo make uses of Ollama to use mistral-7b.

https://ollama.com/blog/openai-compatibility - Ollama Blog Post on openai client

