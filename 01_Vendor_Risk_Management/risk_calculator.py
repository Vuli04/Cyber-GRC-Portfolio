# GRC Vendor Risk Calculator - 5x5 Matrix
# Purpose: Automate the scoring of vendor risks based on Likelihood and Impact.

def calculate_risk(likelihood, impact):
    score = likelihood * impact
    
    if score >= 20:
        status = "CRITICAL (Red)"
        action = "Stop integration immediately. Executive review required."
    elif score >= 12:
        status = "HIGH (Orange)"
        action = "Implement mandatory mitigation controls before launch."
    elif score >= 5:
        status = "MEDIUM (Yellow)"
        action = "Monitor closely and document semi-annual reviews."
    else:
        status = "LOW (Green)"
        action = "Acceptable risk. Proceed with standard monitoring."
        
    return score, status, action

print("--- 2026 AI & Vendor Risk Scorer ---")
try:
    l = int(input("Enter Likelihood (1-5): "))
    i = int(input("Enter Impact (1-5): "))

    if 1 <= l <= 5 and 1 <= i <= 5:
        score, status, action = calculate_risk(l, i)
        print(f"\nTotal Risk Score: {score}")
        print(f"Risk Level: {status}")
        print(f"Required Action: {action}")
    else:
        print("Error: Please enter numbers between 1 and 5.")
except ValueError:
    print("Error: Invalid input. Please enter numbers only.")
