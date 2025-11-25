# 📈 Financial News Sentiment & Stock Market Analysis

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Status](https://img.shields.io/badge/Status-Completed-success)
![Focus](https://img.shields.io/badge/Focus-Agentic%20AI%20%7C%20Business%20Ops-violet)

**Repository:** [https://github.com/Miftah-Ebrahim/StockSentimentAnalysis/](https://github.com/Miftah-Ebrahim/StockSentimentAnalysis/)

## 📌 Executive Summary
This project investigates the predictive power of **Financial News Sentiment** on **Stock Price Movements**. By engineering a pipeline that processes **1.4 million news headlines** and historical stock data for 6 major tech companies (AAPL, AMZN, GOOG, META, MSFT, NVDA), we aimed to quantify the relationship between "Market Mood" and "Market Returns".

**Key Finding:** We discovered a **Pearson correlation of 0.17** between daily news sentiment and stock returns. This indicates a **weak but positive signal**, suggesting that while sentiment alone cannot drive a trading strategy, it serves as a valuable secondary filter for quantitative models.

---

## 👤 Author
**Miftah** *Aspiring Agentic AI Developer for Business Ops* Focusing on building autonomous data pipelines and actionable business intelligence systems.

---

## 🛠️ Project Architecture

The analysis follows a standard Data Science lifecycle:
1.  **ETL (Extract, Transform, Load):** Ingesting raw CSVs and unifying date formats across timezones.
2.  **EDA (Exploratory Data Analysis):** Analyzing headline length, publisher frequency, and N-grams.
3.  **Feature Engineering (Quantitative):** Calculating SMA, RSI, and MACD using `TA-Lib` and `PyNance`.
4.  **Feature Engineering (Qualitative):** Scoring headlines (-1 to +1) using `VADER` Sentiment Analysis.
5.  **Statistical Inference:** Merging datasets on a daily timeline to calculate correlation.

### 📂 Directory Structure
```text
├── data/
│   ├── raw/                # Original CSV files (Gitignored for security/size)
│   └── processed/          # Cleaned data with Sentiment Scores (Gitignored)
├── notebooks/
│   ├── 01_Data_Collection.ipynb    # Data Loading & Merging
│   ├── 03_EDA.ipynb                # Text Analysis & Visualization
│   ├── 04_Technical_Analysis.ipynb # Computing RSI, SMA, MACD
│   ├── 05_Sentiment_Analysis.ipynb # VADER Sentiment Scoring
│   └── 06_Final_Report.ipynb       # Final Executive Report & Charts
├── src/
│   ├── technical_analysis.py       # Modular script for indicators
│   └── sentiment_analysis.py       # Modular script for VADER logic
├── requirements.txt                # Python dependencies
└── README.md                       # Project Documentation

⚠️ Data Access Policy
Note: To ensure compliance with data redistribution policies and repository size limits, the raw dataset (1.4M rows) and processed CSVs are not included in this repository. To run this project locally, please add your own financial news dataset (CSV) and stock price data into the data/raw/ folder.

📊 Key Insights & Visualizations
1. Sentiment vs. Returns Correlation
We aggregated sentiment scores by day and merged them with daily stock returns.

Correlation Coefficient: 0.17

Interpretation: A positive coefficient confirms that happier news generally aligns with higher returns, though the relationship is noisy.

2. Technical Strategy
We implemented a trend-following strategy using Moving Averages and Momentum:

SMA (20 & 50): Used to identify Golden Cross / Death Cross trends.

RSI (14): Used to detect Overbought (>70) and Oversold (<30) conditions.

MACD: Used to confirm trend reversals.

⚙️ Installation & Usage
1. Clone the Repository

Bash

git clone [https://github.com/Miftah-Ebrahim/StockSentimentAnalysis.git](https://github.com/Miftah-Ebrahim/StockSentimentAnalysis.git)
cd StockSentimentAnalysis
2. Install Dependencies

Bash

pip install -r requirements.txt
3. Run the Pipeline Execute the notebooks in order:

Run 01_Data_Collection.ipynb to clean raw data.

Run 04_Technical_Analysis.ipynb to generate indicators.

Run 05_Sentiment_Analysis.ipynb to score 1.4M headlines.

Open 06_Final_Report.ipynb to view the final analysis.

Date: November 2025