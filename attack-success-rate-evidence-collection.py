#Author: Mehrnoush Vaseghipanah
# Research paper
import random

def generate_attacker_strength(difficulty):
  """
  Generates attacker strength based on difficulty level (1-low, 3-high).
  """
  return random.randint(10 * difficulty, 30 * difficulty)

def generate_defender_cybersecurity(training, awareness):
  """
  Calculates defender's cybersecurity readiness based on training and awareness.
  """
  cybersecurity = (training * 0.7) + (awareness * 0.3)
  return min(100, cybersecurity)  # Clamp value between 0 and 100

def generate_defender_forensics(experience, procedures):
  """
  Calculates defender's digital forensics readiness based on experience and procedures.
  """
  forensics = (experience * 0.8) + (procedures * 0.2)
  return min(100, forensics)  # Clamp value between 0 and 100

def simulate_attack(attacker_strength, defender_cybersecurity):
  """
  Simulates the attack and determines success based on attacker strength vs defender's cybersecurity.
  """
  breach_chance = attacker_strength / (defender_cybersecurity + 1)
  return random.random() < breach_chance  # Random value less than breach_chance indicates successful attack

def analyze_evidence(defender_forensics, evidence_complexity):
  """
  Simulates digital forensics investigation and determines evidence collection success.
  """
  collection_chance = defender_forensics / (evidence_complexity + 1)
  return random.random() < collection_chance  # Random value less than collection_chance indicates successful collection

def run_simulation(difficulty):
  """
  Runs a single simulation round with attacker and defender actions.
  """
  attacker_strength = generate_attacker_strength(difficulty)
  defender_cybersecurity = generate_defender_cybersecurity(training=80, awareness=70)  # Sample values
  defender_forensics = generate_defender_forensics(experience=60, procedures=90)  # Sample values

  # Simulate attack
  attack_successful = simulate_attack(attacker_strength, defender_cybersecurity)

  # Simulate forensics investigation (if attack successful)
  evidence_collected = None
  if attack_successful:
    evidence_complexity = random.randint(50, 80)  # Random complexity for evidence
    evidence_collected = analyze_evidence(defender_forensics, evidence_complexity)

  return attack_successful, evidence_collected

def main():
  # Run multiple simulations and track results
  num_simulations = 1000
  attack_success_count = 0
  evidence_collected_count = 0
  for _ in range(num_simulations):
    attack_successful, evidence_collected = run_simulation(difficulty=3)  # Sample difficulty
    attack_success_count += attack_successful
    if evidence_collected is not None:
      evidence_collected_count += evidence_collected

  # Print simulation results
  print("Simulation Results:")
  print(f"Attack Success Rate: {attack_success_count / num_simulations:.2f}")
  print(f"Evidence Collection Rate (on successful attacks): {evidence_collected_count / attack_success_count:.2f} (if applicable)")

if __name__ == "__main__":
  main()
