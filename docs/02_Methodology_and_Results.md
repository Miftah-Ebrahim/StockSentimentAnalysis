# 📑 Technical Report: Methodology & Final Results

**Project:** Stock Sentiment Analysis Pipeline
**Phase:** Feature Engineering & Statistical Inference
**Author:** Miftah (Aspiring Agentic AI Developer)
**Date:** November 2025

---

## 1. Quantitative Feature Engineering (Technical Analysis)
To model market momentum and trends, we implemented standard technical indicators using `TA-Lib`. These features serve as the "Ground Truth" for market movement against which sentiment is tested.

### 1.1 Trend Indicators
* **Simple Moving Average (SMA):** Calculated over **20-day** (Short-term) and **50-day** (Medium-term) windows.
    * *Logic:* Smooths out daily price volatility to identify the underlying trend direction.
* **MACD (Moving Average Convergence Divergence):**
    * *Parameters:* Fast=12, Slow=26, Signal=9.
    * *Purpose:* Used to identify trend reversals and buy/sell signals based on momentum crossovers.

### 1.2 Momentum Indicators
* **Relative Strength Index (RSI):**
    * *Window:* 14 days.
    * *Thresholds:* Overbought (>70) and Oversold (<30).
    * *Application:* Identifies conditions where mean reversion is likely, filtering out false sentiment signals.

---

## 2. Qualitative Feature Engineering (Sentiment Analysis)
We employed Natural Language Processing (NLP) to quantify the unstructured text data.

### 2.1 Model Selection: VADER vs. TextBlob
We selected **VADER (Valence Aware Dictionary and sEntiment Reasoner)** over TextBlob.
* **Reasoning:** VADER is rule-based and specifically tuned for social media and financial headlines. It understands capitalization (e.g., "BUY NOW"), punctuation (e.g., "!!!"), and degree modifiers (e.g., "extremely good"), which are common in financial news tickers.

### 2.2 Aggregation Strategy
* **Granularity:** Daily.
* **Method:** Mean Aggregation.
* *Process:* All headlines for a specific stock ticker on a specific date were scored individually, then averaged to produce a single `daily_sentiment_score` (-1 to +1).

---

## 3. Correlation Analysis & Results

### 3.1 Data Alignment
A strict inner join was performed between the **Aggregated Sentiment Data** and **Daily Stock Returns**.
* **Overlap Period:** 2019-2020 (Due to data availability).
* **Sample Size:** Validated across high-volume tickers (AAPL, NVDA, etc.).

### 3.2 Statistical Findings
A Pearson Correlation Matrix was generated to test the hypothesis: *Does positive sentiment correlate with positive daily returns?*

* **Correlation Coefficient:** `0.17`
* **Statistical Interpretation:**
    * There is a **positive linear relationship**, but it is **weak**.
    * The coefficient indicates that while news is a contributing factor to price movement, it is heavily diluted by other market factors (macroeconomics, volume, algorithmic trading).

### 3.3 Visual Evidence
* **Heatmap:** Confirmed the 0.17 correlation.
* **Time-Series Overlay:** Visual inspection of AAPL and NVDA charts showed that extreme sentiment spikes (very high/low scores) often preceded short-term price corrections, aligning with RSI overbought/oversold signals.

---

## 4. Final Conclusion
The project successfully demonstrated an automated pipeline for ingesting, processing, and correlating unstructured text data with structured financial data.

**Recommendation:**
This sentiment signal should **not** be used as a standalone trading trigger. Instead, it should be deployed as a **Feature in a larger Machine Learning Ensemble** (e.g., Random Forest or LSTM) combined with the calculated Technical Indicators (RSI, MACD) to predict probability of movement.