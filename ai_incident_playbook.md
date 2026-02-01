# Incident Response Playbook: Unauthorized AI Data Exposure

### **PHASE 1: Identification**
- Confirm exactly what data was entered into the unapproved AI (e.g., source code, client emails, or financial data).
- Identify the AI tool’s data retention policy (Does it store inputs for training?).

### **PHASE 2: Containment**
- **Disable Access:** Block the domain at the corporate firewall level immediately.
- **Revoke Tokens:** If the AI had access to the company Google Drive or Slack, revoke its OAuth tokens instantly.

### **PHASE 3: Eradication & Legal**
- **Deletion Request:** Formally request the AI vendor to delete the specific prompts/data (required under GDPR/AI Act).
- **Compliance Check:** Determine if the leak triggers a "72-hour notification" requirement to the regulator.

### **PHASE 4: Recovery & Prevention**
- Move the employee to a "Sanctioned AI" (e.g., Enterprise ChatGPT) so they can work safely.
- Conduct a "Post-Mortem" meeting to update the Acceptable Use Policy.
