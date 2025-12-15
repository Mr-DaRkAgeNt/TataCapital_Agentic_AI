from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os

# --- IMPORT OUR NEW AGENTS ---
from agents import SalesAgent, VerificationAgent, UnderwritingAgent

app = Flask(__name__)
CORS(app)

# Initialize Agents
sales_bot = SalesAgent()
verifier_bot = VerificationAgent()
underwriter_bot = UnderwritingAgent()

# Global State (In-Memory Database for the session)
chat_context = {}

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_input = data.get("message", "").strip()
    user_id = data.get("user_id", "guest")

    # Initialize context if new
    if user_id not in chat_context:
        chat_context[user_id] = {"step": "welcome", "name": None, "user_data": None}
    
    state = chat_context[user_id]

    # --- AGENT LOGIC FLOW ---

    # 1. Welcome Phase
    if state["step"] == "welcome":
        state["step"] = "get_name"
        return jsonify({"response": sales_bot.get_greeting()})

    # 2. Identification Phase
    if state["step"] == "get_name":
        name = user_input.capitalize()
        result = verifier_bot.verify_user(name)
        
        if result["status"] == "not_found":
            return jsonify({"response": "I couldn't find that name in our system. Try 'Rahul' or 'Priya'."})
        
        state["name"] = name
        state["user_data"] = result["data"]
        
        # NEW STEP: Ask for PAN
        state["step"] = "ask_pan"
        return jsonify({"response": f"Hello {name}! To proceed, please enter your **PAN Card Number** for verification."})

    # 3. PAN Verification Phase (NEW)
    if state["step"] == "ask_pan":
        pan_number = user_input.upper()
        
        # Check if PAN format is valid (Regex)
        if not verifier_bot.validate_pan(pan_number):
            return jsonify({"response": "Invalid PAN format. It should look like 'ABCDE1234F'. Please try again."})

        # Check Credit Score AFTER PAN check
        score = state["user_data"]["credit_score"]
        if score < 700:
            state["step"] = "rejected"
            return jsonify({"response": f"Thank you. Based on your PAN details, your Credit Score is {score}. Unfortunately, we cannot proceed at this time."})

        state["step"] = "ask_amount"
        return jsonify({"response": f"PAN Verified ✅. Your Credit Score is {score} (Excellent). \nHow much loan amount do you need?"})

    # 4. Negotiation Phase
    if state["step"] == "ask_amount":
        amount = sales_bot.parse_amount(user_input)
        if not amount:
            return jsonify({"response": "Please enter a valid numeric amount (e.g., 500000)."})

        decision = underwriter_bot.evaluate_loan(state["user_data"], amount, state["name"])

        if decision["decision"] == "APPROVE":
            state["step"] = "done"
            pdf_link = f"http://localhost:5000/download/{decision['pdf_file']}" 
            return jsonify({
                "response": f"Congratulations! Your loan of ₹{amount} is INSTANTLY APPROVED.",
                "action": "show_pdf",
                "link": pdf_link
            })
        
        elif decision["decision"] == "NEED_DOCS":
            state["step"] = "upload_slip"
            state["pending_amount"] = amount
            return jsonify({"response": f"This amount exceeds your instant limit of ₹{decision['limit']}. \nPlease upload your **Salary Slip** to proceed."})
        
        else: # REJECT
            state["step"] = "done"
            return jsonify({"response": f"Sorry, we cannot approve this amount. {decision['reason']}"})

    # 5. Document Upload Phase
    if state["step"] == "upload_slip":
        if "upload" in user_input.lower() or "sent" in user_input.lower():
            amount = state["pending_amount"]
            from sanction_generator import generate_pdf
            pdf_file = generate_pdf(state["name"], amount)
            pdf_link = f"http://localhost:5000/download/{pdf_file}"
            state["step"] = "done"
            return jsonify({
                "response": "Document Verified Successfully! Loan Sanctioned.",
                "action": "show_pdf",
                "link": pdf_link
            })
        else:
            return jsonify({"response": "Please type 'uploaded' after submitting your document."})

    return jsonify({"response": "Session reset. Say 'Hi' to start over."})

@app.route('/download/<filename>')
def download(filename):
    return send_from_directory('static', filename)

if __name__ == '__main__':
    if not os.path.exists('static'):
        os.makedirs('static')
    app.run(debug=True, port=5000)