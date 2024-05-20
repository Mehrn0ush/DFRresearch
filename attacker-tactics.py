# Author: Mehrnoush Vaseghipanah   
# Research paper
def perform_reconnaissance(defender_posture, attacker_resources, attacker_motivation):
  """
  Simulates attacker reconnaissance activities.

  Args:
      defender_posture (float): Overall defender posture value (0-1)
      attacker_resources (int): Level of attacker resources (0-100)
      attacker_motivation (int): Level of attacker motivation (0-100)

  Returns:
      dict: Information gathered about the target network (e.g., IP addresses, services, vulnerabilities)

  Explanation:
      - Higher defender posture makes reconnaissance more difficult (increased detection, deception).
      - More attacker resources allow for more sophisticated techniques (advanced scanning, social engineering).
      - Higher attacker motivation leads to more thorough reconnaissance efforts.
  """
  recon_info = {}  # Dictionary to store gathered information

  # Adjust weights and membership functions as needed
  posture_weight = 0.4
  resource_weight = 0.3
  motivation_weight = 0.3

  posture_value = 1 - defender_posture  # Inverted for attacker's perspective
  resource_value = get_fuzzy_score(attacker_resources, (0, 50, 80, 100))
  motivation_value = get_fuzzy_score(attacker_motivation, (0, 20, 70, 100))

  # Simulate gathering information based on success chance (adjust logic)
  success_chance = posture_weight * posture_value + resource_weight * resource_value + motivation_weight * motivation_value
  if random.random() < success_chance:
      # Example information gathering (modify as needed)
      recon_info["ip_addresses"] = ["10.0.1.1", "10.0.1.20"]
      recon_info["services"] = ["SSH", "HTTP"]
      recon_info["vulnerabilities"] = ["CVE-2023-1234", "CVE-2024-5678"]

  return recon_info


def develop_resources(attacker_resources, attacker_motivation):
  """
  Simulates attacker resource development activities (e.g., acquiring tools, malware).

  Args:
      attacker_resources (int): Level of attacker resources (0-100)
      attacker_motivation (int): Level of attacker motivation (0-100)

  Returns:
      int: Increased attacker resources (0-100)

  Explanation:
      - Existing resources influence the ability to acquire new ones (e.g., funds for tools).
      - Higher motivation might lead to more aggressive resource acquisition (risky tactics).
  """
  resource_increase = 0

  # Adjust weights and membership functions as needed
  resource_weight = 0.7
  motivation_weight = 0.3

  resource_value = get_fuzzy_score(attacker_resources, (0, 20, 50, 80, 100))
  motivation_value = get_fuzzy_score(attacker_motivation, (0, 40, 70, 100))

  # Simulate resource increase based on success chance (adjust logic)
  success_chance = resource_weight * resource_value + motivation_weight * motivation_value
  if random.random() < success_chance:
      resource_increase = random.randint(5, 15)  # Example resource increase

  return attacker_resources + resource_increase




def gain_initial_access(defender_posture, attacker_resources, recon_info):
  """
  Simulates attacker attempts to gain initial access to the target network.

  Args:
      defender_posture (float): Overall defender posture value (0-100)
      attacker_resources (int): Level of attacker resources (0-100)
      recon_info (dict): Information gathered during reconnaissance

  Returns:
      bool: True if initial access is successful, False otherwise

  Explanation:
      - Higher defender posture makes initial access more difficult.
      - More attacker resources allow for more sophisticated techniques (exploits, social engineering).
      - Reconnaissance information can guide targeted attacks and increase success chances.
  """

  
  # Adjust weights and membership functions as needed
  posture_weight = 0.4
  resource_weight = 0.3
  recon_info_weight = 0.3

  posture_value = 1 - defender_posture  # Inverted for attacker's perspective
  resource_value = get_fuzzy_score(attacker_resources, (0, 50, 80, 100))

  # Consider information value (e.g., number of vulnerabilities) for recon_info_weight
  recon_info_value = 0  # Adjust calculation based on recon_info content
  if recon_info:
      recon_info_value = len(recon_info.get("vulnerabilities", []))  # Example using vulnerabilities

  access_chance = posture_weight * posture_value + resource_weight * resource_value + recon_info_weight * recon_info_value

  return random.random() < access_chance



def execute_malware(defender_posture, attacker_resources, initial_access_point):
  """
  Simulates attacker attempts to execute malware on the target system.

  Args:
      defender_posture (float): Overall defender posture value (0-100)
      attacker_resources (int): Level of attacker resources (0-100)
      initial_access_point (str): Point of initial access (e.g., IP address)

  Returns:
      bool: True if execution is successful, False otherwise

  Explanation:
      - Higher defender posture increases malware detection chances (endpoint detection and response).
      - More attacker resources allow for more advanced and evasive malware.
      - The initial access point might influence the success chance (easier execution on vulnerable systems).
  """

  # Adjust weights and membership functions as needed
  posture_weight = 0.5
  resource_weight = 0.3
  access_point_weight = 0.2

  posture_value = 1 - defender_posture  # Inverted for attacker's perspective
  resource_value = get_fuzzy_score(attacker_resources, (0, 20, 50, 80, 100))

  # Consider access point vulnerability (adjust logic)
  access_point_value = 0.5  # Example: moderate vulnerability
  if initial_access_point == "vulnerable_system":
      access_point_value = 0.8  # Higher success chance for vulnerable systems

  execution_chance = posture_weight * posture_value + resource_weight * resource_value + access_point_weight * access_point_value

  return random.random() < execution_chance


def establish_persistence(defender_posture, attacker_resources, executed_code):
  """
  Simulates attacker attempts to establish persistence on the target system.

  Args:
      defender_posture (float): Overall defender posture value (0-100)
      attacker_resources (int): Level of attacker resources (0-100)
      executed_code (bool): Whether malware execution was successful

  Returns:
      bool: True if persistence is established, False otherwise

  Explanation:
      - Higher defender posture makes persistence establishment more difficult (detection, removal).
      - More attacker resources allow for more sophisticated persistence mechanisms.
      - Successful code execution is a prerequisite for establishing persistence.
  """

  # Adjust weights and membership functions as needed
  posture_weight = 0.5
  resource_weight = 0.3
  execution_weight = 0.2

  posture_value = 1 - defender_posture  # Inverted for attacker's perspective
  resource_value = get_fuzzy_score(attacker_resources, (0, 30, 60, 90, 100))
  execution_value = 1 if executed_code else 0  # 0 if no code execution

  persistence_chance = posture_weight * posture_value + resource_weight * resource_value + execution_weight * execution_value

  return random.random() < persistence_chance


def escalate_privileges(defender_posture, attacker_resources, established_persistence):
  """
  Simulates attacker attempts to escalate privileges on the target system.

  Args:
      defender_posture (float): Overall defender posture value (0-100)
      attacker_resources (int): Level of attacker resources (0-100)
      established_persistence (bool): Whether persistence is established

  Returns:
      bool: True if privilege escalation is successful, False otherwise

  Explanation:
      - Higher defender posture makes privilege escalation more difficult (secure configurations, least privilege).
      - More attacker resources allow for more advanced techniques (exploiting vulnerabilities, lateral movement).
      - Established persistence is a prerequisite for attempting privilege escalation.
  """

  # Adjust weights and membership functions as needed
  posture_weight = 0.5
  resource_weight = 0.3
  persistence_weight = 0.2

  posture_value = 1 - defender_posture  # Inverted for attacker's perspective
  resource_value = get_fuzzy_score(attacker_resources, (0, 40, 70, 100))
  persistence_value = 1 if established_persistence else 0  # 0 if no persistence

  escalation_chance = posture_weight * posture_value + resource_weight * resource_value + persistence_weight * persistence_value

  return random.random() < escalation_chance


def evade_defenses(defender_posture, attacker_resources, established_persistence):
  """
  Simulates attacker attempts to evade defender detection and analysis tools.

  Args:
      defender_posture (float): Overall defender posture value (0-100)
      attacker_resources (int): Level of attacker resources (0-100)
      established_persistence (bool): Whether persistence is established

  Returns:
      bool: True if defenses are successfully evaded, False otherwise

  Explanation:
      - Higher defender posture makes defense evasion more difficult (advanced detection, sandboxing).
      - More attacker resources allow for more sophisticated techniques (rootkits, fileless malware).
      - Established persistence is a prerequisite for needing to evade defenses.
  """

  # Adjust weights and membership functions as needed
  posture_weight = 0.6
  resource_weight = 0.2
  persistence_weight = 0.2

  posture_value = 1 - defender_posture  # Inverted for attacker's perspective
  resource_value = get_fuzzy_score(attacker_resources, (0, 20, 50, 80, 100))
  persistence_value = 1 if established_persistence else 0  # 0 if no persistence

  evasion_chance = posture_weight * posture_value + resource_weight * resource_value + persistence_weight * persistence_value

  return random.random() < evasion_chance


def steal_credentials(defender_posture, attacker_resources, established_persistence, privileged):
  """
  Simulates attacker attempts to steal credentials on the target system.

  Args:
      defender_posture (float): Overall defender posture value (0-100)
      attacker_resources (int): Level of attacker resources (0-100)
      established_persistence (bool): Whether persistence is established
      privileged (bool): Whether attacker has escalated privileges

  Returns:
      dict (optional): Stolen credentials (username and password) if successful, None otherwise

  Explanation:
      - Higher defender posture makes credential access more difficult (strong passwords, multi-factor authentication).
      - More attacker resources allow for more sophisticated techniques (password spraying, phishing).
      - Established persistence is a prerequisite for attempting credential access.
      - Privileged access increases the success chance of finding valuable credentials.
  """

  # Adjust weights and membership functions as needed
  posture_weight = 0.5
  resource_weight = 0.3
  persistence_weight = 0.1
  privilege_weight = 0.1

  posture_value = 1 - defender_posture  # Inverted for attacker's perspective
  resource_value = get_fuzzy_score(attacker_resources, (0, 30, 60, 90, 100))
  persistence_value = 1 if established_persistence else 0  # 0 if no persistence
  privilege_value = 1 if privileged else 0  # 0 if not privileged

  access_chance = posture_weight * posture_value + resource_weight * resource_value + persistence_weight * persistence_value + privilege_weight * privilege_value

  if random.random() < access_chance:
      # Example stolen credentials (modify as needed)
      return {"username": "user1", "password": "password123"}
  else:
      return None


def enumerate_systems(defender_posture, attacker_resources, established_persistence, privileged):
  """
  Simulates attacker attempts to discover additional systems on the target network.

  Args:
      defender_posture (float): Overall defender posture value (0-100)
      attacker_resources (int): Level of attacker resources (0-100)
      established_persistence (bool): Whether persistence is established
      privileged (bool): Whether attacker has escalated privileges

  Returns:
      list (optional): List of discovered system names if successful, None otherwise

  Explanation:
      - Higher defender posture makes system discovery more difficult (network segmentation, access controls).
      - More attacker resources allow for more advanced techniques (lateral movement tools).
      - Established persistence is a prerequisite for needing to discover additional systems.
      - Privileged access increases the ability to access and enumerate systems.
  """

  # Adjust weights and membership functions as needed
  posture_weight = 0.6
  resource_weight = 0.2
  persistence_weight = 0.1
  privilege_weight = 0.1

  posture_value = 1 - defender_posture  # Inverted for attacker's perspective
  resource_value = get_fuzzy_score(attacker_resources, (0, 20, 50, 80, 100))
  persistence_value = 1 if established_persistence else 0  # 0 if no persistence
  privilege_value = 1 if privileged else 0  # 0 if not privileged

  discovery_chance = posture_weight * posture_value + resource_weight * resource_value + persistence_weight * persistence_value + privilege_weight * privilege_value

  if random.random() < discovery_chance:
      # Example discovered systems (modify as needed)
      return ["server1", "client2", "printer3"]
  else:
      return None


def move_laterally(defender_posture, attacker_resources, established_persistence, privileged, discovered_systems):
  """
  Simulates attacker attempts to move laterally within the target network.

  Args:
      defender_posture (float): Overall defender posture value (0-100)
      attacker_resources (int): Level of attacker resources (0-100)
      established_persistence (bool): Whether persistence is established
      privileged (bool): Whether attacker has escalated privileges
      discovered_systems (list): List of discovered systems (optional)

  Returns:
      str (optional): Name of the system attacker moved to if successful, None otherwise

  Explanation:
      - Higher defender posture makes lateral movement more difficult (network segmentation, access controls).
      - More attacker resources allow for more sophisticated techniques (exploiting vulnerabilities, stolen credentials).
      - Established persistence is a prerequisite for needing to move laterally.
      - Privileged access increases the ability to move laterally.
      - Discovered systems provide targets for lateral movement.
  """

  # Adjust weights and membership functions as needed
  posture_weight = 0.6
  resource_weight = 0.2
  persistence_weight = 0.1
  privilege_weight = 0.1

  posture_value = 1 - defender_weight  # Inverted for attacker's perspective
  resource_value = get_fuzzy_score(attacker_resources, (0, 10, 40, 70, 100))
  persistence_value = 1 if established_persistence else 0  # 0 if no persistence
  privilege_value = 1 if privileged else 0  # 0 if not privileged

  # Consider the number of discovered systems (adjust logic)
  discovered_weight = 0.1
  discovered_value = 0 if not discovered_systems else len(discovered_systems)

  movement_chance = posture_weight * posture_value + resource_weight * resource_value + persistence_weight * persistence_value + privilege_weight * privilege_value + discovered_weight * discovered_value

  if random.random() < movement_chance:
      # Example selecting a system to move to (modify as needed)
      if discovered_systems:
          return random.choice(discovered_systems)
      else:
          return None  # No movement if no discovered systems
  else:
      return None


def collect_data(defender_posture, attacker_resources, established_persistence, privileged):
  """
  Simulates attacker attempts to collect data from the target system(s).

  Args:
      defender_posture (float): Overall defender posture value (0-100)
      attacker_resources (int): Level of attacker resources (0-100)
      established_persistence (bool): Whether persistence is established
      privileged (bool): Whether attacker has escalated privileges

  Returns:
      str (optional): Description of collected data if successful, None otherwise

  Explanation:
      - Higher defender posture makes data collection more difficult (data encryption, activity monitoring).
      - More attacker resources allow for more sophisticated techniques (exfiltrating large datasets).
      - Established persistence is a prerequisite for needing to collect data.
      - Privileged access increases the ability to access and collect sensitive data.
  """

  # Adjust weights and membership functions as needed
  posture_weight = 0.6
  resource_weight = 0.2
  persistence_weight = 0.1
  privilege_weight = 0.1

  posture_value = 1 - defender_posture  # Inverted for attacker's perspective
  resource_value = get_fuzzy_score(attacker_resources, (0, 20, 50, 80, 100))
  persistence_value = 1 if established_persistence else 0  # 0 if no persistence
  privilege_value = 1 if privileged else 0  # 0 if not privileged

  collection_chance = posture_weight * posture_value + resource_weight * resource_value + persistence_weight * persistence_value + privilege_weight * privilege_value

  if random.random() < collection_chance:
      # Example collected data (modify as needed)
      return "Collected financial records"
  else:
      return None


def establish_command_and_control(defender_posture, attacker_resources, established_persistence):
  """
  Simulates attacker attempts to establish command and control (C2) communication with the target system.

  Args:
      defender_posture (float): Overall defender posture value (0-100)
      attacker_resources (int): Level of attacker resources (0-100)
      established_persistence (bool): Whether persistence is established

  Returns:
      bool: True if C2 communication is established, False otherwise

  Explanation:
      - Higher defender posture makes C2 communication more difficult (network traffic monitoring, detection).
      - More attacker resources allow for more sophisticated techniques (encrypted channels, dynamic C2 servers).
      - Established persistence is a prerequisite for needing C2 communication.
  """

  # Adjust weights and membership functions as needed
  posture_weight = 0.6
  resource_weight = 0.2
  persistence_weight = 0.2

  posture_value = 1 - defender_posture  # Inverted for attacker's perspective
  resource_value = get_fuzzy_score(attacker_resources, (0, 30, 60, 90, 100))
  persistence_value = 1 if established_persistence else 0  # 0 if no persistence

  c2_chance = posture_weight * posture_value + resource_weight * resource_value + persistence_weight * persistence_value

  return random.random() < c2_chance


def exfiltrate_data(defender_posture, attacker_resources, established_persistence, data_collected):
  """
  Simulates attacker's attempt to exfiltrate data from the target system(s).

  Args:
      defender_posture (float): Overall defender posture value (0-100)
      attacker_resources (int): Level of attacker resources (0-100)
      established_persistence (bool): Whether persistence is established
      data_collected (str): Description of data collected (if any)

  Returns:
      bool: True if exfiltration is successful, False otherwise
  """

  # Adjust weights as needed
  posture_weight = 0.6
  resource_weight = 0.3
  persistence_weight = 0.1

  posture_value = 1 - defender_posture  # Inverted for attacker's perspective
  resource_value = get_fuzzy_score(attacker_resources, (0, 20, 50, 80, 100))
  persistence_value = 1 if established_persistence else 0  # 0 if no persistence

  # Consider collected data type in success chance (optional)
  data_weight = 0.0  # Adjust weight and modify logic as needed
  data_value = 0.5 if data_collected == "Financial Records" else 0  # Example logic

  exfiltration_chance = (posture_weight * posture_value +
                        resource_weight * resource_value +
                        persistence_weight * persistence_value +
                        data_weight * data_value)

  return random.random() < exfiltration_chance

# Example usage (assuming data_collected is populated from a previous function)
if exfiltrate_data(70, 80, True, data_collected):
  print("Data exfiltration successful!")
else:
  print("Data exfiltration failed.")





def deliver_impact(defender_posture, attacker_resources, established_persistence, collected_data):
  """
  Simulates attacker attempts to deliver impact on the target system(s).

  Args:
      defender_posture (float): Overall defender posture value (0-100)
      attacker_resources (int): Level of attacker resources (0-100)
      
  established_persistence (bool): Whether persistence is established
  collected_data (str): Description of collected data (optional)

  Returns:
      str (optional): Description of the impact if successful, None otherwise

  Explanation:
      - Higher defender posture makes it harder for attackers to deliver impact (incident response, backups).
      - More attacker resources allow for more destructive techniques (data deletion, ransomware).
      - Established persistence is a prerequisite for needing to deliver impact.
      - Collected data can inform the type of impact (e.g., financial disruption if financial data is collected).
  """

  # Adjust weights and membership functions as needed
  posture_weight = 0.6
  resource_weight = 0.2
  persistence_weight = 0.1
  data_weight = 0.1

  posture_value = 1 - defender_posture  # Inverted for attacker's perspective
  resource_value = get_fuzzy_score(attacker_resources, (0, 40, 70, 90, 100))
  persistence_value = 1 if established_persistence else 0  # 0 if no persistence
  data_value = 0.5 if collected_data else 0  # Lower impact without collected data

  impact_chance = posture_weight * posture_value + resource_weight * resource_value + persistence_weight * persistence_value + data_weight * data_value

  if random.random() < impact_chance:
      # Example impact descriptions (modify as needed)
      if collected_data == "Collected financial records":
          return "Financial data exfiltrated"
      else:
          return "System disruption caused"
  else:
      return None


def calculate_defender_posture(training, awareness, hardening_level):
  """
  Calculates a single value representing the overall defender posture.

  Args:
      training: (int) Level of defender training (0-100)
      awareness: (int) Level of defender awareness (0-100)
      hardening_level: (float) Effectiveness of recent hardening activities

  Returns:
      float: Overall defender posture value (0-1)
  """
  # Adjust weights and membership functions as needed
  training_weight = 0.3
  awareness_weight = 0.3
  hardening_weight = 0.4

  training_value = get_fuzzy_score(training, (0, 20, 50, 80, 100))  # Example membership function for training
  awareness_value = get_fuzzy_score(awareness, (0, 30, 60, 90, 100))  # Example membership function for awareness
  hardening_value = hardening_level  # Already a normalized value (0-1)

  posture = training_weight * training_value + awareness_weight * awareness_value + hardening_weight * hardening_value

  return posture
  
  
  def get_fuzzy_score_template(value, membership_function_params):
  """
  Calculates the membership degree of a value in a triangular fuzzy set for factors in collect_data.

  Args:
      value (float): The value to evaluate (e.g., defender posture).
      membership_function_params (tuple): Tuple containing (lower bound, middle value, upper bound).

  Returns:
      float: Membership degree between 0 and 1.
  """

  lower_bound, mid_value, upper_bound = membership_function_params

  if value <= lower_bound:
    return 1  # Easier to collect with lower values (e.g., defender posture)
  elif lower_bound < value <= mid_value:
    return (mid_value - value) / (mid_value - lower_bound)
  elif mid_value < value <= upper_bound:
    return 0  # More difficult to collect with higher values
  else:
    return 0


