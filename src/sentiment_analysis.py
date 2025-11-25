from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd

# Initialize the analyzer ONCE at the top of the file
# This is much faster than creating a new 'analyzer' for every single row
analyzer = SentimentIntensityAnalyzer()


def get_sentiment_score(text):
    """
    Calculates the compound sentiment score for a text string.
    Returns a float between -1 (Most Negative) and +1 (Most Positive).
    """
    try:
        # Check if text is valid (not empty or NaN)
        if not isinstance(text, str):
            return 0.0

        # .polarity_scores returns a dictionary: {'neg': 0.0, 'neu': 1.0, 'pos': 0.0, 'compound': 0.0}
        # We only care about 'compound' for the trend
        scores = analyzer.polarity_scores(text)
        return scores["compound"]

    except Exception as e:
        # If anything breaks, return neutral (0.0) rather than crashing the whole program
        return 0.0
