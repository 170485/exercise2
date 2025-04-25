"""
Monmouthshire Land Authority
-*- coding: utf-8 -*-
Created on Mon Mar 15 09:22:02 2025
Author: RMSI
"""
import numpy as np
import matplotlib.pyplot as plt

# Parameters for exponential growth
t_max = 100  # total time range in years
k = 0.1      # growth rate

# Function to simulate AI exponential growth
def ai_growth(t, k):
    return np.exp(k * t)

# Generate values for plotting
t_values = np.linspace(0, t_max, 500)
ai_values = ai_growth(t_values, k)

# Hypothetical maximum human IQ value
human_iq_max = 250

# Calculate when AI reaches human IQ level (singularity)
# Using the formula: exp(k * t) = human_iq_max
# Solving for t:
t_singularity = np.log(human_iq_max) / k

# Plotting the AI growth curve
plt.figure(figsize=(8, 6))
plt.plot(t_values, ai_values, label="AI Growth", color='b')
plt.axhline(y=human_iq_max, color='g', linestyle='--', label="Max Human IQ (250)")
plt.axvline(x=t_singularity, color='r', linestyle='--', label=f"Singularity in {t_singularity:.2f} years")
plt.title("Exponential Growth Simulation of AI Until Singularity")
plt.xlabel("Time (years)")
plt.ylabel("AI Intelligence (relative capacity)")
plt.legend()
plt.grid(True)
plt.show()

# Display singularity time
print(f"Singularity reaches human IQ after {t_singularity:.2f} years.")
