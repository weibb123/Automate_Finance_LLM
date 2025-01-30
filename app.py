import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta
import streamlit as st
from openai import OpenAI
import os
import time
from dotenv import load_dotenv

load_dotenv()

# client OPENAI
client = OpenAI(api_key=os.getenv("GLHF_API_KEY"), base_url="https://glhf.chat/api/openai/v1")

# strategy-functions
def calculate_200dma(ticker):
    """description:
        calculate 200 day moving average of a stock
        Args: Ticker (str) - stock ticker
        Returns: 200 day moving average (float)
    """
    try:
        data = yf.download(ticker, period="400d", progress=False)
        if len(data) < 200:
            return None, None
        data["200dma"] = data["Close"].rolling(window=200).mean()

        # get last valid values
        last_valid = data[['Close', '200dma']].dropna().iloc[-1]
        return float(last_valid['Close'].iloc[0]), float(last_valid['200dma'].iloc[0])
    
    except Exception as e:
        st.error(f"Error: {e}")
        return None, None

def get_fundamentals(ticker):
    """
    description: fetch fundamental data
    Args: Ticker (str) - stock ticker
    Returns: Free Cash Flow Yield (float), Debt-to-Equity Ratio (float)
    """
    try:
        stock = yf.Ticker(ticker)
        
        # get Free Cash Flow (FCF) and Market Cap
        market_cap = stock.info['marketCap']

        # calculate FCF yield
        free_cashflow = stock.cashflow.iloc[0,0]
        market_cap = stock.info['marketCap']

        fcf_yield = (free_cashflow/market_cap) * 100
        fcf_yield = round(fcf_yield, 2)

        # calculate debt/equity ratio
        total_debt = stock.balancesheet.iloc[4, 0]
        total_equity = stock.balancesheet.iloc[12, 0]
        debt_ratio = total_debt / total_equity

        return fcf_yield, debt_ratio
    except Exception as e:
        st.error(f"Error: {e}")
        return None, None

# Streamlit UI
st.title("Long-Term Stock Analysis Bot")
option = st.selectbox("Select stock ticker (e.g., 'Analyze AAPL')",
                      ("AAPL", "GOOGL", "AMZN", "MSFT", "NVDA", "TSLA", 'IVA'))

if option:
    try:
        # Run analysis
        with st.spinner(f"Analyzing {option}..."):
            price, dma200 = calculate_200dma(option)
            fcf_yield, debt_ratio = get_fundamentals(option)
            
            analysis = {
                'ticker': option,
                'price': round(price, 2) if price else 'N/A',
                '200DMA': round(dma200, 2) if dma200 else 'N/A',
                'fcf_yield': round(fcf_yield, 2),
                'debt_ratio': round(debt_ratio, 2),
                'recommendation': 'BUY' if all([
                    price and dma200 and price > dma200,
                    fcf_yield > 5,
                    debt_ratio < 1
                ]) else 'HOLD/SELL'
            }

        # Display results
        with st.chat_message("assistant"):
            st.subheader(f"{analysis['ticker']} Analysis")
            st.write(f"**Price**: ${analysis['price']}")
            st.write(f"**200-DMA**: ${analysis['200DMA']}")
            st.write(f"**FCF Yield**: {analysis['fcf_yield']}%")
            st.write(f"**Debt/Equity**: {analysis['debt_ratio']}")
            st.success(f"Recommendation: {analysis['recommendation']}")
        
        # waiting for LLM summary
        st.write("Generating expert summary...")

        # Generate LLM summary
        response = client.chat.completions.create(
            model="hf:deepseek-ai/DeepSeek-V3",
            messages=[{
                "role": "user",
                "content": f"""
                You are expert in algorithmic Trading. 
                Explain this stock analysis in simple terms: {str(analysis)}.
                Focus on:
                - Price vs 200DMA relationship
                - Financial health indicators (FCF Yielda and Debt/Equity)
                - Clear recommendation explanation
                at most 3 sentences.
                """
            }]
        )
        with st.chat_message("assistant"):
            st.write("**Expert Summary:**")
            st.text(response.choices[0].message.content)

    except Exception as e:
        st.error(f"Analysis failed: {str(e)}")