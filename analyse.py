from pickle import load
import numpy as np
import matplotlib.pyplot as plt
from os.path import join


with open(join("data", "all_scores.pickle"), 'rb') as f:
    all_scores = load(f)

with open(join("data", "did_agree.pickle"), 'rb') as f:
    did_agree = load(f)

print([sum(a) for a in all_scores])
mean_scores = [sum(a)/len(a) for a in all_scores]
print([f"{s:.2f}" for s in mean_scores])
print([(1.96 * np.std(a)/np.sqrt(len(a)))/len(a) for a in all_scores])
print([sum(a) for a in did_agree])
did_agree_percentage = [sum(a)/len(a) for a in did_agree]
print([f"{p*100:.2f}%" for p in did_agree_percentage])
print([(1.96 * np.std(a)/np.sqrt(len(a)))/len(a) for a in did_agree])

plt.plot(mean_scores)
plt.show()

plt.plot(did_agree_percentage)
plt.show()
