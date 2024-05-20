#Author: Mehrnoush Vaseghipanah
# Research Paper
import random
from collections import namedtuple
import matplotlib.pyplot as plt


# Define player preferences (namedtuple)
PlayerPreference = namedtuple("PlayerPreference", ["preference1", "preference2", "preference3", "preference4", "preference5", "preference6", "preference7", "preference8", "preference9", "preference10", "preference11", "preference12", "preference13", "preference14", "preference15", "preference16"])
PlayerPreference_D = namedtuple("PlayerPreference_D", ["preference1", "preference2", "preference3", "preference4", "preference5", "preference6"])

# Fuzzy membership function (example - triangular)
def membership(value, low, medium, high):
    if value <= low:
        return 1
    elif low < value <= medium:
        return (medium - value) / (medium - low)
    elif medium < value <= high:
        return (value - medium) / (high - medium)
    else:
        return 0


# Player utility function (without readiness influence)
def player_utility(preferences, opponent_preferences, preference_weights):
    total_utility = 0
    # Loop through each preference and calculate utility
    for i in range(len(preferences)):
        if i>5:
            i = i%5
        attack_pref_value = preferences[i]
        defense_pref_value = opponent_preferences[i]
        weight = preference_weights[i]
        utility = membership(attack_pref_value, low=0.25, medium=0.5, high=0.75) * (1 - membership(defense_pref_value, low=0.25, medium=0.5, high=0.75))
        total_utility += weight * utility
    return total_utility


# Define preference functions (replace with your specific logic)
def define_preferences_readiness(readiness_utilities):
    low_bound = 0.2
    high_bound = 0.8
    # Not used in utility calculation (placeholders can remain)
    attacker_preferences = PlayerPreference(*[random.uniform(low_bound, high_bound) for _ in range(16)])
    defender_preferences = PlayerPreference_D(*[random.uniform(low_bound, high_bound) for _ in range(6)])
    return attacker_preferences, defender_preferences

def define_preferences_investigation(readiness_utilities):
    low_bound = 0.3
    high_bound = 0.7
    # Investigation preferences independent of readiness (replace with your logic)
    attacker_preferences = PlayerPreference(*[random.uniform(low_bound, high_bound) for _ in range(16)])
    defender_preferences = PlayerPreference_D(*[random.uniform(low_bound, high_bound) for _ in range(6)])
    return attacker_preferences, defender_preferences


# Simulation loop (separate for readiness and investigation)
num_simulations = 100
attacker_utilities = []
defender_utilities = []

# Investigation Phase Simulation
phase = "investigation"
for _ in range(num_simulations):
    attacker_preferences, defender_preferences = define_preferences_investigation(define_preferences_readiness(None))  # No readiness influence

    # Calculate utilities for attacker and defender
    attacker_utility = player_utility(attacker_preferences, defender_preferences, [1.0] * 16)  # Assuming equal weights
    defender_utility = player_utility(defender_preferences, attacker_preferences, [1.0] * 6)  # Assuming equal weights

    attacker_utilities.append(attacker_utility)
    defender_utilities.append(defender_utility)

# Function to calculate cumulative percentages
def calculate_cumulative_percentages(preference_values):
  cumulative_percentages = []
  total_value = sum(preference_values)
  current_sum = 0
  for value in preference_values:
    current_sum += value
    cumulative_percentages.append(current_sum / total_value * 100)
  return cumulative_percentages

# Extract preference values for Pareto chart
attacker_pref_values = [getattr(attacker_preferences, f"preference{i+1}") for i in range(16)]
defender_pref_values = [getattr(defender_preferences, f"preference{i+1}") for i in range(6)]

# Calculate cumulative percentages
attacker_cumulative_percentages = calculate_cumulative_percentages(attacker_pref_values)
defender_cumulative_percentages = calculate_cumulative_percentages(defender_pref_values)


# Plotting - Pareto Chart
plt.figure(figsize=(10, 6))
plt.bar(range(len(attacker_pref_values)), attacker_pref_values, color='skyblue', label='Attacker Preference')
plt.twinx()
plt.plot(range(len(attacker_pref_values)), attacker_cumulative_percentages, color='red', linestyle='--', label='Attacker Cumulative (%)')

plt.xticks(range(len(attacker_pref_values)), [f"F {i+1}" for i in range(len(attacker_pref_values))], rotation=45, ha='right')
plt.xlabel('Preference Factors')
plt.ylabel('Preference Value')
plt.title('Pareto Chart - Investigation Phase Preferences')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()  # Uncomment to display the Pareto chart

# Plotting - Utility Histograms
plt.figure(figsize=(10, 6))
plt.hist(attacker_utilities, bins=20, alpha=0.7, label='Attacker Utility')
plt.hist(defender_utilities, bins=20, alpha=0.7, label='Defender Utility')
plt.xlabel('Player Utility')
plt.ylabel('Frequency')
plt.title('Utility Distribution (Investigation Phase)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()  # Uncomment to display the utility histograms

# Plotting - Scatter Plot
plt.figure(figsize=(8, 6))
plt.scatter(attacker_utilities, defender_utilities)
plt.xlabel('Attacker Utility')
plt.ylabel('Defender Utility')
plt.title('Attacker vs. Defender Utility (Investigation Phase)')
plt.grid(True)
plt.tight_layout()
plt.show()  # Uncomment to display the scatter plot


