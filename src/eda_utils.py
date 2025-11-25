import matplotlib.pyplot as plt
import seaborn as sns


def plot_headline_length_distribution(df, column="headline"):
    """
    Plots the distribution of headline lengths.

    Args:
        df (pd.DataFrame): DataFrame containing headlines.
        column (str): Name of the headline column.
    """
    # TODO: Calculate lengths and plot histogram.
    pass


def plot_publisher_counts(df, column="publisher", top_n=10):
    """
    Plots the top N publishers by article count.

    Args:
        df (pd.DataFrame): DataFrame containing publisher info.
        column (str): Name of the publisher column.
        top_n (int): Number of top publishers to show.
    """
    # TODO: Count values and plot bar chart.
    pass


def plot_publication_frequency(df, date_column="date"):
    """
    Plots the number of articles published over time.

    Args:
        df (pd.DataFrame): DataFrame containing publication dates.
        date_column (str): Name of the date column.
    """
    # TODO: Group by date (e.g., daily or monthly) and plot line chart.
    pass
