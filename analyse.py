from __future__ import annotations
from scipy.stats import pearsonr
from pickle import load
import numpy as np
import matplotlib.pyplot as plt
from os.path import join

all_scores = [[], [], [], [], []]
did_agree = [[], [], [], [], []]
for ending in (f"_{i+1}" for i in range(3)):
    with open(join("data", f"all_scores{ending}.pickle"), 'rb') as f:
        all_scores = [a+b for a, b in zip(all_scores, load(f))]

    with open(join("data", f"did_agree{ending}.pickle"), 'rb') as f:
        did_agree = [a+b for a, b in zip(did_agree, load(f))]

print([sum(a) for a in all_scores])
mean_scores = [sum(a)/len(a) for a in all_scores]
print([f"{s:.2f}" for s in mean_scores])
print([(1.96 * np.std(a)/np.sqrt(len(a)))/len(a) for a in all_scores])
print([sum(a) for a in did_agree])
did_agree_percentage = [sum(a)/len(a) for a in did_agree]
print([f"{p*100:.2f}%" for p in did_agree_percentage])
print([(1.96 * np.std(a)/np.sqrt(len(a)))/len(a) for a in did_agree])


def plot(data: list[float], title: str):
    plt.xticks(range(5))
    plt.plot(data)
    plt.title(title)
    plt.savefig(join("plots", f"{title.replace(' ', '_')}.png"))
    plt.clf()


plot(mean_scores, "Mean Score")
plot(did_agree_percentage, "Agreeness")


# Calculate Pearson's Correlation
corr = pearsonr(mean_scores, did_agree_percentage)[0]
print('Pearsons correlation: %.3f' % corr)
