----
### Step 1: Update the File

1.  Open **`docs/01_Setup_and_EDA.md`** in VS Code.
2.  **Delete everything** inside.
3.  **Copy and Paste** the following block:

<!-- end list -->

````markdown
# 📑 Technical Report: Environment Setup & Exploratory Data Analysis (EDA)

**Project:** Stock Sentiment Analysis Pipeline
**Author:** Miftah (Agentic AI Developer)
**Date:** November 2025
**Version:** 1.0.0

---

## 1. Executive Summary of Phase 1
The objective of the initial phase was to establish a reproducible development environment and assess the integrity, quality, and distribution of the financial news dataset (1.4 million rows). This document details the infrastructure setup, data validation steps, and critical statistical insights that informed the downstream modeling strategy.

---

## 2. Infrastructure & Environment Configuration

To ensure **reproducibility** and **dependency isolation**, the project follows strict software engineering standards.

### 2.1 Virtual Environment Strategy
A dedicated Python virtual environment was initialized to prevent dependency conflicts with the system runtime.

```bash
# Architecture: Windows / Git Bash
python -m venv venv
source venv/Scripts/activate
````

### 2.2 Dependency Management (`requirements.txt`)

The following core libraries were selected for specific architectural reasons:

  * **Pandas:** High-performance dataframe manipulation.
  * **TA-Lib (Binary):** Chosen over standard TA-Lib for C++ compatibility on Windows environments without MSVC build tools.
  * **VADER Sentiment:** Selected for its specialized lexicon optimized for short-text social/financial media (handling caps, punctuation, and intensity) compared to TextBlob.
  * **YFinance:** Utilized for retrieving historical market data for validation.

-----

## 3\. Data Integrity & Preprocessing

### 3.1 Dataset Specifications

  * **Source:** Financial News Corpus (CSV)
  * **Volume:** \~1,407,000 observations
  * **Features:** Headline, Date, Publisher, Stock Ticker.

### 3.2 Timezone Normalization (Critical Fix)

During the ingestion layer, a schema mismatch was detected:

  * **News Data:** ISO-8601 format with UTC offsets (e.g., `2020-06-05 14:30:00+00:00`).
  * **Market Data:** Naive Datetime (e.g., `2020-06-05`).

**Resolution:** An ETL transformation step was implemented to normalize all timestamps to `datetime64[ns]` and strip timezone awareness (`dt.tz_localize(None)`), ensuring accurate inner joins during the correlation phase.

-----

## 4\. Exploratory Data Analysis (EDA) Findings

### 4.1 Temporal Distribution & Data Sparsity

**Observation:** A time-series visualization revealed significant data sparsity between **2011 and 2018**, followed by an exponential surge in data volume during **2019-2020**.

**Strategic Implication:**

  * Model training and correlation analysis must be restricted to the **2019-2020 epoch**.
  * Analyzing the sparse period (2011-2018) would introduce statistical noise and bias the correlation results due to insufficient sample size per day.

### 4.2 Semantic Analysis (N-Grams)

A Bigram (2-gram) frequency analysis was performed using `CountVectorizer` to understand the *nature* of the text.

**Top Key Phrases:**

1.  `"earnings per"`
2.  `"price target"`
3.  `"estimates q1"`
4.  `"insider trading"`

**Insight:** The corpus is highly **Quantitative and Event-Driven**. It focuses on hard financial metrics (Earnings calls, Analyst ratings) rather than general macroeconomic sentiment (e.g., "Economy is crashing").
**Hypothesis:** This suggests that VADER sentiment scores will likely track *short-term volatility* effectively, as these headlines represent material information.

### 4.3 Headline Statistics

  * **Length Distribution:** Follows a near-normal distribution centered at **60-80 characters**.
  * **Outliers:** Minimal outliers detected. No truncation or padding was required for the NLP pipeline.

-----

## 5\. Conclusion & Next Steps

The EDA phase confirmed that the dataset is clean, structurally sound, and rich in event-driven financial text. The timezone discrepancies were resolved via the ETL pipeline.

**Transition to Phase 2:**
The analysis justifies the use of **Daily Aggregation** for sentiment scoring, as the high volume of news in 2020 allows for a statistically significant "Daily Mood" metric to be correlated against Daily Stock Returns.

````

---
