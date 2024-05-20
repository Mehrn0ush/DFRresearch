#Author: Mehrnoush Vaseghipanah
#Research paper
def harden(training, awareness):
  """
  Simulates hardening activities that improve overall cybersecurity posture using fuzzy logic.

  Args:
      training: (int) Level of defender training (0-100)
      awareness: (int) Level of defender awareness (0-100)

  Returns:
      float: Increased cybersecurity value based on training and awareness
  """
  low_train = (0, 20, 50)  # Triangular membership function for low training
  mid_train = (30, 60, 90)  # Triangular membership function for medium training
  high_train = (70, 100, 100)  # Triangular membership function for high training

  low_exp = (0, 2, 5)  # Triangular membership function for low awareness
  mid_exp = (3, 7, 10)  # Triangular membership function for medium awareness
  high_exp = (8, 10, 10)  # Triangular membership function for high awareness

  train_value = min(max(0, (training - low_train[0]) / (mid_train[0] - low_train[0])), 1) \
               if low_train[0] < mid_train[0] else min(max(0, (high_train[1] - training) / (high_train[1] - mid_train[1])), 1)
  exp_value = min(max(0, (awareness - low_exp[0]) / (mid_exp[0] - low_exp[0])), 1) \
              if low_exp[0] < mid_exp[0] else min(max(0, (high_exp[1] - awareness) / (high_exp[1] - mid_security[1])), 1)

  hardening_factor = (train_value + exp_value) / 2  # Combine training and awareness for hardening effectiveness

  # Increase cybersecurity based on hardening_factor (adjust as needed)
  cybersecurity_increase = random.uniform(0.02 * hardening_factor, 0.1 * hardening_factor)  # Increase between 2% and 10% based on hardening_factor

  return cybersecurity_increase


def detect(cybersecurity):
  """
  Simulates detection activities that might identify ongoing attacks using fuzzy logic.

  Args:
      cybersecurity: (float) Defender's current cybersecurity level

  Returns:
      bool: True if detection is successful, False otherwise
  """
  low_security = (0, 20, 50)  # Triangular membership function for low cybersecurity
  mid_security = (30, 60, 90)  # Triangular membership function for medium cybersecurity
  high_security = (70, 100, 100)  # Triangular membership function for high cybersecurity

  security_value = min(max(0, (cybersecurity - low_security[0]) / (mid_security[0] - low_security[0])), 1) \
                   if low_security[0] < mid_security[0] else min(max(0, (high_security[1] - cybersecurity) / (high_security[1] - mid_security[1])), 1)

  # Higher cybersecurity leads to higher chance of successful detection (adjust as needed)
  detection_chance = security_value**2  # Square security_value for a steeper increase in detection chance

  return random.random() < detection_chance


def isolate(cybersecurity, attacker_strength):
  """
  Simulates isolation activities that limit attacker movement within the network using fuzzy logic.

  Args:
      cybersecurity: (float) Defender's current cybersecurity level
      attacker_strength: (float) Attacker's strength

  Returns:
      float: Reduced attacker strength due to isolation
  """
  low_security = (0, 20, 50)  # Triangular membership function for low cybersecurity
  mid_security = (30, 60, 90)  # Triangular membership function for medium cybersecurity
  high_security = (70, 100, 100)  # Triangular membership function for high cybersecurity

  low_strength = (0, 20, 50)  
  low_strength = (0, 20, 50)  # Triangular membership function for low attacker strength
  mid_strength = (30, 60, 90)  # Triangular membership function for medium attacker strength
  high_strength = (70, 100, 100)  # Triangular membership function for high attacker strength

  security_value = min(max(0, (cybersecurity - low_security[0]) / (mid_security[0] - low_security[0])), 1) \
                   if low_security[0] < mid_security[0] else min(max(0, (high_security[1] - cybersecurity) / (high_security[1] - mid_security[1])), 1)
  strength_value = min(max(0, (attacker_strength - low_strength[0]) / (mid_strength[0] - low_strength[0])), 1) \
                  if low_strength[0] < mid_strength[0] else min(max(0, (high_strength[1] - attacker_strength) / (high_strength[1] - mid_security[1])), 1)

  isolation_effectiveness = (security_value + (1 - strength_value)) / 2  # Combine security and low attacker strength for isolation effectiveness

  # Reduce attacker strength based on isolation_effectiveness (adjust as needed)
  strength_reduction = random.uniform(0, isolation_effectiveness * 0.3)  # Reduce up to 30% based on isolation effectiveness

  return attacker_strength - strength_reduction



def deceive(cybersecurity):
  """
  Simulates deception activities that mislead attackers using fuzzy logic.

  Args:
      cybersecurity: (float) Defender's current cybersecurity level

  Returns:
      float: Reduced attacker strength due to deception
  """
  low_security = (0, 20, 50)  # Triangular membership function for low cybersecurity
  mid_security = (30, 60, 90)  # Triangular membership function for medium cybersecurity
  high_security = (70, 100, 100)  # Triangular membership function for high cybersecurity

  security_value = min(max(0, (cybersecurity - low_security[0]) / (mid_security[0] - low_security[0])), 1) \
                   if low_security[0] < mid_security[0] else min(max(0, (high_security[1] - cybersecurity) / (high_security[1] - mid_security[1])), 1)

  # Higher cybersecurity leads to higher deception effectiveness (adjust as needed)
  deception_effectiveness = security_value**1.5  # Square root for a moderate increase in effectiveness with higher security

  return random.uniform(0, deception_effectiveness * 0.1)  # Reduce attacker strength up to 10% based on deception effectiveness


def evict(cybersecurity, attacker_strength):
  """
  Simulates eviction activities that remove the attacker from the system using fuzzy logic.

  Args:
      cybersecurity: (float) Defender's current cybersecurity level
      attacker_strength: (float) Attacker's strength

  Returns:
      float: Reduced attacker strength (0 if eviction successful)
  """
  low_security = (0, 20, 50)  # Triangular membership function for low cybersecurity
  mid_security = (30, 60, 90)  # Triangular membership function for medium cybersecurity
  high_security = (70, 100, 100)  # Triangular membership function for high cybersecurity

  low_strength = (0, 20, 50)  # Triangular membership function for low attacker strength
  mid_strength = (30, 60, 90)  # Triangular membership function for medium attacker strength
  high_strength = (70, 100, 100)  # Triangular membership function for high attacker strength

  security_value = min(max(0, (cybersecurity - low_security[0]) / (mid_security[0] - low_security[0])), 1) \
                   if low_security[0] < mid_security[0] else
  min(max(0, (high_security[1] - cybersecurity) / (high_security[1] - mid_security[1])), 1)
  strength_value = min(max(0, (attacker_strength - low_strength[0]) / (mid_strength[0] - low_strength[0])), 1) \
                  if low_strength[0] < mid_strength[0] else min(max(0, (high_strength[1] - attacker_strength) / (high_security[1] - mid_security[1])), 1)

  eviction_chance = security_value * (1 - strength_value)  # Higher security and lower attacker strength lead to higher eviction chance

  # Reduce attacker strength to 0 if successful eviction (adjust as needed)
  if random.random() < eviction_chance:
    return 0
  else:
    return attacker_strength


def restore(cybersecurity):
  """
  Simulates recovery activities to restore system functionality after an attack using fuzzy logic.

  Args:
      cybersecurity: (float) Defender's cybersecurity level before the attack

  Returns:
      float: Reduced cybersecurity value due to recovery effort
  """
  low_security = (0, 20, 50)  # Triangular membership function for low cybersecurity before attack
  mid_security = (30, 60, 90)  # Triangular membership function for medium cybersecurity before attack
  high_security = (70, 100, 100)  # Triangular membership function for high cybersecurity before attack

  security_value = min(max(0, (cybersecurity - low_security[0]) / (mid_security[0] - low_security[0])), 1) \
                   if low_security[0] < mid_security[0] else min(max(0, (high_security[1] - cybersecurity) / (high_security[1] - mid_security[1])), 1)

  # Higher pre-attack cybersecurity reduces recovery effort (adjust as needed)
  recovery_effort = 1 - security_value**0.5  # Square root for a moderate decrease in effort with higher pre-attack security

  # Reduce cybersecurity between 2% and 5% based on recovery effort
  cybersecurity_reduction = random.uniform(0.02 * recovery_effort, 0.05 * recovery_effort)

  return cybersecurity - cybersecurity_reduction



import random

def model_based_defense(security_data, threat_models):
  """
  Simulates model-based threat detection and mitigation using fuzzy logic with triangular membership functions.

  Args:
      security_data (dict): Dictionary containing security data points.
      threat_models (list): List of threat models (dictionaries with attributes).

  Returns:
      list: List of potential threats identified and corresponding mitigation actions.
  """

  potential_threats = []
  mitigation_actions = []

  for threat_model in threat_models:
    # Calculate model score based on fuzzy logic with triangular membership functions
    model_score = calculate_model_score(security_data, threat_model["data_points"], threat_model["membership_functions"])

    # Simulate threshold-based detection
    if model_score > threat_model["threshold"]:
      potential_threats.append(threat_model["name"])

      # Simulate mitigation action selection based on threat model (replace with logic)
      mitigation_actions.append("Simulate mitigation action for " + threat_model["name"])

  # Introduce randomness to simulate potential false positives
  if random.random() < 0.1:  # Adjust probability as needed
    potential_threats.append("False Positive")
    mitigation_actions.append("No mitigation required")

  return potential_threats, mitigation_actions

# Function to calculate model score using fuzzy logic with triangular membership functions
def calculate_model_score(security_data, data_points, membership_functions):
  """
  Calculates a score based on security data points, threat model data points, and membership functions.

  Args:
      security_data (dict): Dictionary containing security data points.
      data_points (dict): Dictionary containing data points for the threat model.
      membership_functions (dict): Dictionary containing membership functions for each data point.

  Returns:
      float: Model score between 0 and 1.
  """

  total_score = 0
  for data_point, weight in data_points.items():
    # Retrieve membership function and security data point value
    membership_func = membership_functions[data_point]
    data_point_value = security_data.get(data_point, 0)

    # Calculate membership degree using triangular membership function (replace with your specific implementation)
    membership_degree = triangular_membership_function(data_point_value, membership_func["low"], membership_func["mid"], membership_func["high"])

    # Combine membership degree with weight
    score = membership_degree * weight
    total_score += score

  # Normalize score between 0 and 1
  normalized_score = total_score / (max(data_points.values()) * sum(data_points.values()))
  return normalized_score

# Example triangular membership function (replace with your specific implementation)
def triangular_membership_function(x, low, mid, high):
  """
  Calculates the membership degree for a triangular membership function.

  Args:
      x (float): Value to evaluate.
      low (float): Lower bound of the triangle.
      mid (float): Middle value of the triangle (peak).
      high (float): Upper bound of the triangle.

  Returns:
      float: Membership degree between 0 and 1.
  """

  if x <= low:
    return 0
  elif low < x <= mid:
    return (x - low) / (mid - low)
  elif mid < x <= high:
    return (high - x) / (high - mid)
  else:
    return 0

# Example usage (replace with actual security data, threat models, and membership functions)
security_data = {
  "unusual_network_traffic": True,
  "attempted_login_from_unknown_ip": False,
  "file_access_anomaly": True
}

threat_models = [
    {
  "name": "Insider Threat",
  "data_points": {
    "unusual_network_traffic": 0.3,
    "attempted_login_from_unknown_ip": 0.2,
    "file_access_anomaly": 0.5
  },
  "membership_functions": {
    "unusual_network_traffic": {"low": 0.1, "mid": 0.5, "high": 0.8},
    "attempted_login_from_unknown_ip": {"low": 0, "mid": 0.2, "high": 0.5},
    "file_access_anomaly": {"low": 0.3, "mid": 0.7, "high": 1.0}
  },
  "threshold": 0.8  # Required threshold for threat detection
}
]


# Example usage (replace with actual security data)
security_data = {
  "unusual_network_traffic": True,
  "attempted_login_from_unknown_ip": False,
  "file_access_anomaly": True
}

potential_threats, mitigation_actions = model_based_defense(security_data, threat_models)
print(f"Potential threats identified: {potential_threats}")
print(f"Mitigation actions: {mitigation_actions}")
