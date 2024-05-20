#Author:  Mehrnoush Vaseghipanah
# Research papaer

import numpy as np
import random
import matplotlib.pyplot as plt

def cvss_to_severity(score):
  """
  Maps CVSS score to a severity level (color).
  """
  if score >= 7.0:
    return "Red (High)"
  elif score >= 4.0:
    return "Orange (Medium)"
  elif score >= 0.1:
    return "Green (low)"
  else:
    return "Gray (Unknown)"

def fuzzy_readiness(training, experience, vulnerability):
  """
  Simulates readiness using fuzzy logic (triangular membership functions).
  """
  low_train = (0, 20, 50)  # Triangular membership function for low training
  mid_train = (30, 60, 90)  # Triangular membership function for medium training
  high_train = (70, 100, 100)  # Triangular membership function for high training

  low_exp = (0, 2, 5)  # Triangular membership function for low experience
  mid_exp = (3, 7, 10)  # Triangular membership function for medium experience
  high_exp = (8, 10, 10)  # Triangular membership function for high experience

  low_vuln = (0, 0, 3)  # Triangular membership function for low vulnerability
  mid_vuln = (2, 5, 8)  # Triangular membership function for medium vulnerability
  high_vuln = (7, 10, 10)  # Triangular membership function for high vulnerability

  train_value = min(max(0, (training - low_train[0]) / (mid_train[0] - low_train[0])), 1) \
                if low_train[0] < mid_train[0] else min(max(0, (high_train[1] - training) / (high_train[1] - mid_train[1])), 1)
  exp_value = min(max(0, (experience - low_exp[0]) / (mid_exp[0] - low_exp[0])), 1) \
               if low_exp[0] < mid_exp[0] else min(max(0, (high_exp[1] - experience) / (high_exp[1] - mid_exp[1])), 1)
  vuln_value = min(max(0, (vulnerability - low_vuln[0]) / (mid_vuln[0] - low_vuln[0])), 1) \
                if low_vuln[0] < mid_vuln[0] else min(max(0, (high_vuln[1] - vulnerability) / (high_vuln[1] - mid_vuln[1])), 1)

  # Simple averaging for simplicity (more complex fuzzy rules can be implemented)
  readiness = (train_value + exp_value + (1 - vuln_value)) / 3
  return readiness

def simulate_game():
  """
  Simulates a single game between defenders and attackers.
  """
  defender_training = random.randint(70, 90)  # Simulate random training level
  defender_experience = random.randint(7, 10)  # Simulate random experience level
  attacker_capability = random.uniform(0.1, 10.0)  # Simulate random CVSS score

  defender_readiness = fuzzy_readiness(defender_training, defender_experience, attacker_capability)
  attacker_advantage = random.uniform(0.0, 1.0)  # Simulate random attacker advantage

  # Simple win/lose logic based on readiness and attacker advantage
  if defender_readiness > (attacker_advantage + 0.2):
    print(f"Defenders win! Readiness: {defender_readiness:.2f} (high), Vulnerability: {attacker_capability:.1f} ({cvss_to_severity(attacker_capability)})")
  else:
    print(f"Attackers win! Readiness: {defender_readiness:.2f}, Advantage: {attacker_advantage:.2f}, Vulnerability: {attacker_capability:.1f} ({cvss_to_severity(attacker_capability)})")

  return defender_training, defender_readiness, attacker_capability

# Run simulations and collect data
training_levels = []
readiness_values = []
attacker_capability_values = []
for _ in range(10):
  training, readiness, vulnerability = simulate_game()
  training_levels.append(training)
  readiness_values.append(readiness)
  attacker_capability_values.append(vulnerability)

# Normalization
readiness_values = readiness_values / np.max(readiness_values)
training_levels = training_levels / np.max(training_levels)
attacker_capability_values = attacker_capability_values/np.max(attacker_capability_values)
# Plot readiness vs training
plt.plot(training_levels, label="Defender Training", color='red')
plt.plot(readiness_values, label="Defender Readiness", color='Blue')
plt.plot(attacker_capability_values, label="Attacker Capability", color='green')
plt.xlabel("Defender Training Level")
plt.ylabel("Values")
plt.title("Defender Readiness & Attacker Capability vs. Training Level")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()



'''
Junior, mid and Senior Level	
    defender_training = random.randint(40, 90)
    defender_experience = random.randint(4, 10)
    attacker_vulnerability = random.uniform(0.1, 10.0)
mid and Senior Level	
    defender_training = random.randint(60, 90)
    defender_experience = random.randint(6, 10)
    attacker_vulnerability = random.uniform(0.1, 10.0)
Senior Level
    defender_training = random.randint(70, 90)
    defender_experience = random.randint(7, 10)
    attacker_vulnerability = random.uniform(0.1, 10.0)
'''
