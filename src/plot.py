import math
import matplotlib.pyplot as plt

def plot_hist(df, col, r, b):
    plt.hist(df[col], bins = b, range = r, edgecolor='black', alpha=0.7)
    plt.xlabel(col)
    plt.ylabel("Frequency")
    plt.title(f"Distribution of {col} Among Students")