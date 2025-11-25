# StockSentimentAnalysis - Task 1: Data Acquisition & EDA

This guide provides step-by-step instructions to complete Task 1 using a modular approach.

## Overview
You will:
1.  Fetch stock and news data.
2.  Clean and process the data.
3.  Perform Exploratory Data Analysis (EDA).
4.  Organize your code into reusable modules in `src/`.

---

## Step 1: Data Acquisition

### 1.1 Fetch Stock Data
**Goal**: Get historical stock prices for your target stocks (e.g., AAPL, TSLA).
**Action**:
1.  Open `src/data_loader.py`.
2.  Implement `fetch_stock_data` using `yfinance`.
    *   *Hint*: `yfinance.download(ticker, start=start_date, end=end_date)` returns a DataFrame.
3.  Create a notebook `notebooks/01_Data_Collection.ipynb`.
4.  Import your function:
    ```python
    import sys
    import os
    sys.path.append(os.path.abspath('../src'))
    from data_loader import fetch_stock_data
    ```
5.  Fetch data for a stock (e.g., 'AAPL' from '2020-01-01' to '2023-01-01') and save it to `data/raw/stock_prices.csv`.

### 1.2 Fetch News Data
**Goal**: Get financial news headlines.
**Action**:
1.  **Option A (yfinance)**: `yfinance` has a `.news` attribute, but it only gives recent news.
2.  **Option B (NewsAPI)**: Requires an API key. Good for historical data if you have a paid plan, otherwise limited.
3.  **Option C (Dataset)**: If you have the FNSPID dataset or a CSV provided for the challenge, use that.
4.  Implement `load_raw_data` in `src/data_loader.py` to load your news CSV/JSON.
5.  Load the news data in your notebook and save the raw version to `data/raw/news_data.csv` (or keep as JSON).

---

## Step 2: Data Preparation

### 2.1 Clean & Process News Data
**Goal**: Standardize the news data for analysis.
**Action**:
1.  Create a new notebook `notebooks/02_Data_Processing.ipynb`.
2.  Load your raw news data.
3.  **Flatten JSON**: If your data is nested JSON, extract: `headline`, `publisher`, `url`, `date`.
4.  **Convert Dates**: Ensure the `date` column is a datetime object.
    ```python
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    ```
    *   *Tip*: Normalize to keep only the date part (YYYY-MM-DD) if you want to match with daily stock prices.
5.  **Drop Duplicates**: Remove duplicate headlines.
6.  **Save**: Save the cleaned DataFrame to `data/processed/news_processed.csv`.

### 2.2 Align Stock Data
1.  Load `data/raw/stock_prices.csv`.
2.  Ensure the index or date column is in datetime format.
3.  Save to `data/processed/stock_prices_processed.csv`.

---

## Step 3: Exploratory Data Analysis (EDA)

**Goal**: Visualize patterns in the data using your `eda_utils` module.

### 3.1 Implement EDA Utils
**Action**:
1.  Open `src/eda_utils.py`.
2.  Implement `plot_headline_length_distribution`:
    *   Calculate length: `df['headline'].str.len()`.
    *   Plot histogram using `plt.hist()` or `sns.histplot()`.
3.  Implement `plot_publisher_counts`:
    *   Count values: `df['publisher'].value_counts().head(top_n)`.
    *   Plot bar chart.
4.  Implement `plot_publication_frequency`:
    *   Group by date and count.
    *   Plot line chart.

### 3.2 Run EDA in Notebook
**Action**:
1.  Create `notebooks/03_EDA.ipynb`.
2.  Import your processed data and your `eda_utils` functions.
3.  **Headline Analysis**:
    ```python
    from eda_utils import plot_headline_length_distribution
    plot_headline_length_distribution(news_df)
    ```
    *   *Markdown*: Explain what the distribution tells you. Are most headlines short or long?
4.  **Publisher Analysis**:
    ```python
    from eda_utils import plot_publisher_counts
    plot_publisher_counts(news_df)
    ```
    *   *Markdown*: Who are the top publishers?
5.  **Time Series**:
    ```python
    from eda_utils import plot_publication_frequency
    plot_publication_frequency(news_df)
    ```
    *   *Markdown*: Do you see spikes in news volume? Can you correlate them with known market events?

---

## Step 4: Version Control

**Action**:
1.  **Commit your work**:
    ```bash
    git add .
    git commit -m "feat: Complete Task 1 data pipeline and EDA"
    ```
2.  **Push**:
    ```bash
    git push origin task-1-eda
    ```

You are now ready for Task 2!
