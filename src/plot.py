import math
import matplotlib.pyplot as plt

def plot_hist(df, col, r, b):
    fig, ax = plt.subplots()
    ax.hist(df[col], bins=b, range=r, edgecolor='black', alpha=0.7)
    ax.set_xlabel(col)
    ax.set_ylabel("Frequency")
    ax.set_title(f"Distribution of {col} Among Students")
    return ax