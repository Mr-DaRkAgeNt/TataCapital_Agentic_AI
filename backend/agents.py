import re
from mock_db import get_user_data
from sanction_generator import generate_pdf

class SalesAgent:
    """Handles interaction and gathering requirements."""
    def get_greeting(self):
        return "Welcome to Tata Capital! I am your AI Loan Assistant. \nTo begin, please tell me your First Name (e.g., Rahul, Priya)."

    def parse_amount(self, text):
        try:
            # Extract the first valid number found in text
            return int(''.join(filter(str.isdigit, text)))
        except:
            return None

class VerificationAgent:
    """Connects to the 'Mock' Bureau/CRM to get data."""
    def verify_user(self, name):
        data = get_user_data(name)
        if not data:
            return {"status": "not_found", "message": "User not found."}
        return {"status": "found", "data": data}

    def validate_pan(self, pan_number):
        # Basic Regex for PAN: 5 Letters, 4 Digits, 1 Letter (e.g., ABCDE1234F)
        pattern = r"[A-Z]{5}[0-9]{4}[A-Z]{1}"
        if re.match(pattern, pan_number.upper()):
            return True
        return False

class UnderwritingAgent:
    """The Brain: Applies the rules (Logic Gates)."""
    def evaluate_loan(self, user_data, amount, user_name):
        credit_score = user_data["credit_score"]
        limit = user_data["limit"]

        # RULE 1: Credit Score Check
        if credit_score < 700:
            return {
                "decision": "REJECT",
                "reason": f"Credit Score ({credit_score}) is below 700."
            }

        # RULE 2: Amount within Limit (Happy Path)
        if amount <= limit:
            pdf_file = generate_pdf(user_name, amount)
            return {
                "decision": "APPROVE",
                "pdf_file": pdf_file,
                "limit": limit
            }

        # RULE 3: Amount < 2x Limit (Edge Case)
        elif amount <= (2 * limit):
            return {
                "decision": "NEED_DOCS",
                "reason": "Amount exceeds pre-approved limit.",
                "limit": limit
            }

        # RULE 4: Amount > 2x Limit (Hard Reject)
        else:
            return {
                "decision": "REJECT",
                "reason": "Loan amount is too high for current profile."
            }
