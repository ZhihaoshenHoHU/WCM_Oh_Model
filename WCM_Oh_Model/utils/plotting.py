import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy import stats

def plot_sm(SM, ypred, save_path=None):
    sns.set(style="whitegrid")
    fig, ax = plt.subplots(figsize=(5, 5))

    sns.scatterplot(x=SM, y=ypred, ax=ax)

    slope, intercept, r, _, _ = stats.linregress(SM, ypred)
    ax.plot(SM, intercept + slope * SM, 'r')

    ax.plot([0, 0.6], [0, 0.6], 'k-')
    ax.set_xlim(0, 0.6)
    ax.set_ylim(0, 0.6)

    ax.set_xlabel("Observed SM")
    ax.set_ylabel("Estimated SM")

    ax.text(0.05, 0.9, f"R={r:.2f}", transform=ax.transAxes)

    if save_path:
        plt.savefig(save_path, dpi=300)

    plt.show()