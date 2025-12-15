# Momentum: Agentic AI Loan Orchestrator 🏦 🚀

> **A "Zero-Touch" Intelligent Banking Assistant built for the EY Techathon 6.0.**
>
> *Compressing the 5-day personal loan process into 3 minutes using Multi-Agent Orchestration.*

---

## 📖 Executive Summary
**Momentum** is a next-generation banking solution that replaces rigid, rule-based chatbots with an **Agentic AI Architecture**. Instead of simple scripted responses, Momentum employs a team of specialized autonomous agents—**Sales, Verification, and Underwriting**—that collaborate to handle the entire loan lifecycle.

From real-time identity verification (PAN Check) to instant credit decisioning and dynamic legal document generation (Sanction Letter), Momentum automates the "Decisioning" and "Documentation" layers of banking, offering a frictionless experience for digital-native customers.

## 🌟 Key Features
* **🤖 Multi-Agent Orchestration:** A modular system where specialized agents handle specific tasks (Parsing, Risk, Legal) independently.
* **⚡ Zero-Touch Sanctions:** Fully automated "Happy Path" that issues a legally binding PDF Sanction Letter in <180 seconds.
* **🛡️ Real-Time Security:** Client-side Regex validation (`[A-Z]{5}[0-9]{4}[A-Z]{1}`) blocks invalid PAN entries instantly.
* **🧠 Intelligent Underwriting:** Autonomous logic gates that assess credit scores and loan limits without human bias.
* **📄 Dynamic PDF Generation:** Uses `ReportLab` to programmatically draw and issue unique contracts for every user.

## 🛠️ Tech Stack
| Component | Technology | Description |
| :--- | :--- | :--- |
| **Frontend** | HTML5, CSS3, JavaScript | Responsive Chat UI with Tata Capital branding. |
| **Backend** | Python 3.10, Flask | The central brain managing the Agentic State Machine. |
| **Server** | Gunicorn | Production-grade WSGI server for concurrency. |
| **Logic** | Custom Agent Classes | Modular Python classes simulating LangGraph nodes. |
| **Docs** | ReportLab | Engine for high-speed, dynamic PDF creation. |
| **Deployment** | Render (Backend) + Netlify (Frontend) | Cloud-native, stateless architecture for scalability. |

## 🏗️ Architecture
The system follows a **Hub-and-Spoke Agentic Model**:

1.  **Client Layer:** Captures user intent via a secure Chat Interface.
2.  **Orchestrator Layer (Flask):** The "Manager" that routes tasks to the correct agent.
3.  **Agent Layer:**
    * **🕵️ Verification Agent:** Validates Identity (PAN) & fetches Credit Score.
    * **⚖️ Underwriting Agent:** Applies Bank Policy Rules (Risk Assessment).
    * **📝 Sanction Agent:** Drafts the PDF contract.
4.  **Data Layer:** In-Memory Mock Database (simulating Core Banking System).

## 🚀 How to Run Locally

### Prerequisites
* Python 3.8+
* Pip

### Installation
1.  **Clone the Repository**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/TataCapital_Agentic_AI.git](https://github.com/YOUR_USERNAME/TataCapital_Agentic_AI.git)
    cd TataCapital_Agentic_AI
    ```

2.  **Setup Backend**
    ```bash
    cd backend
    pip install -r requirements.txt
    ```

3.  **Run the AI Server**
    ```bash
    python app.py
    ```
    *You should see: `Running on http://127.0.0.1:5000`*

4.  **Launch Frontend**
    * Navigate to the `frontend` folder.
    * Open `index.html` in any browser.
    * *Start chatting with Momentum!*

## 🧪 Testing the Prototype (The "Happy Path")
To see the full automated sanctioning flow, use these details during the demo:

* **Name:** `Rahul` (Simulates a pre-approved customer)
* **PAN Number:** `ABCDE1234F` (Valid format required)
* **Loan Amount:** `400000` (Within his limit)
* **Result:** 🟢 **Instant Approval + PDF Download**

*Try entering a low credit score user (e.g., "Priya") or an invalid PAN to see the rejection and validation logic in action.*

## 👥 Team
* **[Your Name]** - Lead Developer & Architect
* **[Team Member 2]** - Frontend & UX
* **[Team Member 3]** - Research & Documentation

---
*Built with ❤️ for the EY Techathon 6.0*