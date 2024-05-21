#Author: Mehrnoush Vaseghipanah
#Research paper
import random
import pandas as pd

# Fuzzy Membership Functions (example using simple linear functions)
attacker_type_values = {
    "Script Kiddie": 0.5,
    "Disgruntled Insider": 0.7,
    "Organized Crime": 0.8,
    "Nation-State Actor": 1.0
}
def attack_intensity(malicious_score):
    return malicious_score * 1.5

def maliciousness(attacker_type, category):
    """
    This function models the attacker's maliciousness based on attacker type and category (SME or SMB).

    Args:
        attacker_type (float): A value between 0 and 1 representing the attacker type.
        category (str): The category of the defender (SME or SMB).

    Returns:
        float: A value between 0 and 1 representing the attacker's malicious intent.
    """
    if attacker_type not in attacker_type_values:
        raise ValueError("Invalid attacker type. Please refer to valid options.")
    attacker_value = attacker_type_values[attacker_type]
    if category == "SME":
        # Consider SMEs might attract less targeted attacks
        return attacker_value * 1.5
    elif category == "SMB":
        return attacker_value * 2
    else:
        raise ValueError("Invalid category. Choose 'SME' or 'SMB'.")

def defense_effectiveness(resources, workload, category):
    """
    This function calculates how effective the defender's resources are against the attack workload,
    considering category-specific factors.

    Args:
        resources (float): A value between 0 and 1 representing the defender's resources.
        workload (float): The total attack workload.
        category (str): The category of the defender (SME or SMB).

    Returns:
        float: A value between 0 and 1 representing the defense effectiveness.
    """
    if resources < 0.5:
        return resources
    else:
        if category == "SME":
            # SMEs might have less robust defenses
            return 1 - (1 - resources) * (0.7 - workload * 0.2)
        elif category == "SMB":
            return 1 - (1 - resources) * (0.8 - workload * 0.2)  # Diminishing returns
        else:
            raise ValueError("Invalid category. Choose 'SME' or 'SMB'.")

# Function to estimate CVSS base score based on attack type and impact (replace with logic for specific metrics)
def estimate_cvss_base(attack_type, impact):
    # This is a simplified example. A real implementation would use CVSS metrics and scoring criteria.
    if attack_type == "DDoS":
        if impact == "High":
            return 7.0  # High impact for overwhelming system resources
        else:
            return 0.0  # Low impact for DDoS attacks on confidentiality or integrity
    elif attack_type == "SQL Injection" and impact == "High":
        return 9.0  # High severity for successful data exfiltration
    elif attack_type == "SQL Injection" and impact == "Medium":
        return 7.0  # Medium severity for potential data exposure
    else:
        return 0.0  # Example low severity for other scenarios

# Function to translate CVSS score to impact label
def cvss_to_impact_label(cvss_score):
    if cvss_score >= 7.0:
        return "High"
    elif cvss_score >= 4.0:
        return "Medium"
    else:
        return "Low"

def attack_round(attacker_pool, defender_resources,irrational_behavior):
    """
    This function simulates a single round of attack and defense actions.

    Args:
        attacker_pool (list): A list representing the attacker pool (types of attackers with probabilities).
        defender_resources (float): A value between 0 and 1 representing the defender's resources.

    Returns:
        dict: A dictionary containing the results of the attack round.
    """

    # Simulate attacker actions
    attack_results = []
    for attacker_type, probability in attacker_pool:
      if random.random() < probability:  # Simulate attacker selection based on probability
        # Introduce irrational behavior with a chance (e.g., 10%)
        if random.random() < irrational_behavior:
          malicious_score = random.uniform(0, 1)  # Random maliciousness for irrational attackers
        else:
          malicious_score = maliciousness(attacker_type, category)
        attack_type = random.choice(["DDoS", "SQL Injection"])
        attack_strength = attack_intensity(malicious_score)
        potential_impact = random.choice(["High", "Medium", "Low"])  # Random impact for now
        cvss_base_score = estimate_cvss_base(attack_type, potential_impact)
        attack_results.append({
            "attack_type": attack_type,
            "maliciousness": malicious_score,
            "attack_strength": attack_strength,
            "potential_impact": potential_impact,
            "cvss_base_score": cvss_base_score
        })

    # Calculate total attack workload
    total_workload = sum(result["attack_strength"] for result in attack_results)

    # Calculate defense effectiveness considering workload
    defense_modifier = defense_effectiveness(defender_resources, total_workload, category)

    # Simulate impact on metrics (consider CVSS scores and potential impacts)
    impact_availability = max(0, sum(result["attack_strength"] for result in attack_results) - defense_modifier * 0.6)
    impact_confidentiality = 0
    impact_integrity = 0
    for result in attack_results:
        if result["attack_type"] == "SQL Injection":
            # Consider defense effectiveness on impact for successful attacks
            impact_modifier = 1 - defense_modifier  # Higher defense reduces impact
            if result["potential_impact"] == "High":
                impact_confidentiality = max(impact_confidentiality, result["cvss_base_score"] * impact_modifier)
                impact_integrity = max(impact_integrity, result["cvss_base_score"] * impact_modifier)
            elif result["potential_impact"] == "Medium":
                impact_confidentiality = max(impact_confidentiality, result["cvss_base_score"] * 0.5 * impact_modifier)
                impact_integrity = max(impact_integrity, result["cvss_base_score"] * 0.5 * impact_modifier)
        # Handle DDoS impact specifically
        elif result["attack_type"] == "DDoS":
            if result["potential_impact"] == "High":
                impact_availability = 0.8  # Set a high value for high-impact DDoS (assuming severe disruption)
            else:
                impact_availability = max(0, impact_availability - result["attack_strength"] * defense_modifier * 0.2)  # Lower impact for low/medium DDoS


    # Return the attack round results
    return {
        "attack_results": attack_results,
        "total_workload": total_workload,
        "impact_availability": impact_availability,
        "impact_confidentiality": impact_confidentiality,
        "impact_integrity": impact_integrity
    }


# Define attacker pools with adjusted probabilities for SMEs and SMBs
SME_attacker_pool = [
    ("Script Kiddie", 0.7),  # Higher probability for SMEs
    ("Disgruntled Insider", 0.2),
    ("Organized Crime", 0.1)
]
SMB_attacker_pool = [
    ("Script Kiddie", 0.5),
    ("Disgruntled Insider", 0.2),
    ("Organized Crime", 0.1),
    ("Nation-State Actor", 0.2)  # Lower probability for SMEs
]

Outputs = []
# Loop through simulations for SMEs and SMBs
for category in ["SME", "SMB"]:
    if category == "SME":
        resources = 0.2  # Define SME resources (value between 0 and 1)
        num_simulations = 100  # Number of simulation rounds for SMEs
    else:
        resources = 1  # Define SMB resources (value between 0 and 1)
        num_simulations = 100  # Number of simulation rounds for SMBs

    for _ in range(num_simulations):
        # Simulate attack round for current category
        results = attack_round(eval(category + "_attacker_pool"), resources,irrational_behavior=0.8)
        Outputs.append(results)



Outputs_updated = []

for output in Outputs:
  output_dict = {}
  try:
    output_dict['attack_results_SME_attack_type']        = output['attack_results'][0]['attack_type']
    output_dict['attack_results_SME_maliciousness']      = output['attack_results'][0]['maliciousness']
    output_dict['attack_results_SME_attack_strength']    = output['attack_results'][0]['attack_strength']
    output_dict['attack_results_SME_potential_impact']   = output['attack_results'][0]['potential_impact']
    output_dict['attack_results_SME_cvss_base_score']    = output['attack_results'][0]['cvss_base_score']

    output_dict['attack_results_SMB_attack_type']        = output['attack_results'][0]['attack_type']
    output_dict['attack_results_SMB_maliciousness']      = output['attack_results'][0]['maliciousness']
    output_dict['attack_results_SMB_attack_strength']    = output['attack_results'][0]['attack_strength']
    output_dict['attack_results_SMB_potential_impact']   = output['attack_results'][0]['potential_impact']
    output_dict['attack_results_SMB_cvss_base_score']    = output['attack_results'][0]['cvss_base_score']

  except:
    output_dict['attack_results_SME_attack_type']        = 0
    output_dict['attack_results_SME_maliciousness']      = 0
    output_dict['attack_results_SME_attack_strength']    = 0
    output_dict['attack_results_SME_potential_impact']   = 0
    output_dict['attack_results_SME_cvss_base_score']    = 0

    output_dict['attack_results_SMB_attack_type']        = 0
    output_dict['attack_results_SMB_maliciousness']      = 0
    output_dict['attack_results_SMB_attack_strength']    = 0
    output_dict['attack_results_SMB_potential_impact']   = 0
    output_dict['attack_results_SMB_cvss_base_score']    = 0
  output_dict['total_workload']         = output['total_workload']
  output_dict['impact_availability']    = output['impact_availability']
  output_dict['impact_confidentiality'] = output['impact_confidentiality']
  output_dict['impact_integrity']       = output['impact_integrity']

  Outputs_updated.append(output_dict)


Output_df = pd.DataFrame(Outputs_updated)
