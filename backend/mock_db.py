# Simulating a Bank Database
users = {
    "Rahul": {"credit_score": 750, "limit": 500000},  # Happy Path
    "Priya": {"credit_score": 650, "limit": 200000},  # Reject Path (Low Score)
    "Amit":  {"credit_score": 720, "limit": 300000}   # Edge Case (Needs Slip)
}

def get_user_data(name):
    return users.get(name, None)