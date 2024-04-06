# Automate_Finance_LLM

## Description
Connect to yahoofinance with text and automate finance using Ollama-mistral and mistral function calling

## Table of Contents
- [Demo Video](#Demo-Video)
  - [Tech Stack](#Tech-Stack)
  - [Subheading 1.2](#subheading-12)
- [Heading 2](#heading-2)
  - [Subheading 2.1](#subheading-21)

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





## Reference 
Nicholas Renotte - AI engineer at IBM

Inspired by Nicholas Renotte for demonstrating how to create fake openai server with llama.cpp. Although llama.cpp is hard to setup locally, this demo make uses of Ollama to use mistral-7b.

