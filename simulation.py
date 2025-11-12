import matplotlib.pyplot as plt
import numpy as np

# Simulate experiment
simulated_strikes = np.random.binomial(10, 0.55, size=1000)

# Histogram data
counts, bins = np.histogram(simulated_strikes, bins=np.arange(-0.5, 11.5, 1))

# Plot histogram with all bars in one color
plt.bar(range(11), counts, color="#1b9e77", edgecolor="black", label="0-5 strikes")

# Overlay highlight for bins 6 to 10
highlight_bins = np.arange(6, 11)
plt.bar(
    highlight_bins, counts[6:11], color="#d95f02", edgecolor="black", label="6+ strikes"
)

plt.xticks(range(11))
plt.xlabel("Strikes in ten rolls")
plt.ylabel("Frequency (out of 1 000)")
plt.title("Distribution of strikes (p = 0.55, 10 rolls, 1 000 sims)")
plt.legend()
plt.tight_layout()
plt.show()
