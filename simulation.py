import matplotlib.pyplot as plt
import numpy as np

# Parameters
p_strike = 0.55
n_rolls = 10
n_sims = 10000

# Simulation
simulated_strikes = np.random.binomial(n_rolls, p_strike, size=n_sims)
prob_6_plus = (simulated_strikes >= 6).mean()
print(f"Estimated probability of 6 or more strikes: {prob_6_plus:.3f}")

# Histogram data
counts, _ = np.histogram(simulated_strikes, bins=np.arange(-0.5, 11.5, 1))

# Colors: green for <6, orange for >=6
bar_colors = ["#1b9e77"] * 6 + ["#d95f02"] * 5

plt.bar(range(11), counts, color=bar_colors, edgecolor="black")
plt.xticks(range(11))
plt.xlabel("Strikes in ten rolls")
plt.ylabel("Frequency (out of 10 000)")
plt.title("Distribution of strikes (p = 0.55, 10 rolls, 10 000 sims)")
plt.tight_layout()
plt.show()
