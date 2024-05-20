#Author: Mehrnoush Vaseghipanah
#Research paper
import random
import numpy as np
import matplotlib.pyplot as plt

# Fuzzy membership functions (modify these functions)
def attacker_strategy(resources):
    if resources < 3:
        return 1
    elif resources >= 3 and resources <= 6:
        return (resources - 3) / 3
    else:
        return 0

def defender_strategy(resources):
    if resources < 3:
        return 0
    elif resources >= 3 and resources <= 6:
        return (resources - 3) / 3
    else:
        return 1

# Game parameters
n_attackers = 5
n_defenders = 10
n_resources = 5  # Total number of resources
n_generations = 100  # Number of generations

# Initialize populations
attacker_population = np.random.rand(n_attackers)
defender_population = np.random.rand(n_defenders)
defender_readiness = np.zeros(n_defenders)  # New variable for defender readiness

# Track average strategies and readiness for plotting
avg_attacker_strategy = []
avg_defender_strategy = []
avg_defender_readiness = []

# Simulation loop
for generation in range(n_generations):

    # Defender Readiness Phase
    def defender_readiness_update(resources, defender_population, defender_readiness, defense_strength_used):
        defender_readiness += defender_strategy(resources) * 0.001 - defense_strength_used * 0.0005  # Adjust factor based on desired impact

    defense_strength_used = np.zeros(n_defenders)  # Initialize array to track used defense strength

    defender_readiness_update(n_resources, defender_population, defender_readiness, defense_strength_used)

    # Payoffs (modify these functions)
    attacker_payoffs = np.zeros(n_attackers)
    defender_payoffs = np.zeros(n_defenders)
    for i in range(n_attackers):
        for j in range(n_defenders):
            attack_strength = attacker_strategy(attacker_population[i])
            defense_strength = defender_strategy(defender_population[j]) * defender_readiness[j]
            resources_gained = attack_strength * (1 - defense_strength) * n_resources / (n_attackers + n_defenders)
            resources_lost = defense_strength * attack_strength * n_resources / (n_attackers + n_defenders)
            attacker_payoffs[i] += resources_gained
            defender_payoffs[j] += n_resources / (n_attackers + n_defenders) - resources_lost

            # Update defense strength used
            defense_strength_used[j] = defense_strength

    # Selection (tournament selection)
    new_attacker_population = np.zeros(n_attackers)
    new_defender_population = np.zeros(n_defenders)
    for i in range(n_attackers):
        contestants = random.sample(range(n_attackers), 2)
        winner = np.argmax(attacker_payoffs[contestants])
        new_attacker_population[i] = attacker_population[contestants[winner]]
    for i in range(n_defenders):
        contestants = random.sample(range(n_defenders), 2)
        winner = np.argmax(defender_payoffs[contestants])
        new_defender_population[i] = defender_population[contestants[winner]]

    # Mutation
    for i in range(n_attackers):
        new_attacker_population[i] += np.random.rand() * 0.01
    for i in range(n_defenders):
        new_defender_population[i] += np.random.rand() * 0.01

    # Apply boundary conditions (0 to 1)
    new_attacker_population = np.clip(new_attacker_population, 0, 1)
    new_defender_population = np.clip(new_defender_population, 0, 1)

    # Update populations
    attacker_population = new_attacker_population
    defender_population = new_defender_population

    # Track average strategies and readiness
    avg_attacker_strategy.append(np.mean(attacker_population))
    avg_defender_strategy.append(np.mean(defender_population))
    avg_defender_readiness.append(np.mean(defender_readiness))

# Plot average strategies and readiness
plt.plot(range(n_generations), avg_attacker_strategy, label="Attacker Strategy")
plt.plot(range(n_generations), avg_defender_strategy, label="Defender Strategy")
plt.plot(range(n_generations), avg_defender_readiness, label="Defender Readiness")
plt.xlabel("Generation")
plt.ylabel("Average Value")
plt.title("Evolution of Attacker, Defender Strategies, and Defender Readiness")
plt.legend()
plt.show()

# Print final average strategies
print("Final Average Attacker Strategy:", np.mean(attacker_population))
print("Final Average Defender Strategy:", np.mean(defender_population))
print("Final Average Defender Readiness:", np.mean(avg_defender_readiness))
