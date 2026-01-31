# Vendor Risk Assessment: Zenith AI (Customer Support Agent)
**Date:** January 2026  
**Status:** 🔴 RED LIGHT (High Risk)  
**Assessor:** [Your Name]

---

## 1. Executive Summary
Zenith AI currently presents a **Critical Risk** profile due to unauthorized data residency and significant failures in access control. Implementation is **not recommended** until the remediation steps below are completed. Failure to address these could lead to GDPR fines (up to 4% of global turnover) and intellectual property leakage.

---

## 2. Risk Matrix
| Risk ID | Category | Description | Likelihood (1-5) | Impact (1-5) | Total Score |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **VR-01** | Privacy | Data stored in USA (No DPA in place) | 5 | 4 | **20 (High)** |
| **VR-02** | Security | Former employees retain system access | 5 | 5 | **25 (Critical)** |
| **VR-03** | AI Gov | Model training on customer data | 4 | 5 | **20 (High)** |

---

## 3. Key Findings & Impact
### Finding A: Technical Access Control Failure
The vendor's most recent SOC 2 report shows three exceptions regarding employee offboarding.
* **Impact:** A disgruntled ex-employee could sabotage the customer database or leak trade secrets.

### Finding B: AI Data Poisoning / IP Leakage
Zenith AI reserves the right to use input data for model training by default.
* **Impact:** Proprietary fintech algorithms could become part of a public AI model, destroying AeroFin’s competitive advantage.

---

## 4. Required Remediation (The "Next Steps")
1. **Contractual:** Sign a Data Processing Agreement (DPA) with Standard Contractual Clauses (SCCs).
2. **Technical:** Demand an "AI Opt-Out" confirmation to ensure zero data training.
3. **Operational:** Implement a monthly review of the vendor's user access logs.
