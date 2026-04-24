# 💰 LLM Usage Tracker

A reusable Python library and dashboard to track LLM usage, calculate costs, and enforce budget limits.

---

## 🚀 Features

- ✅ Token tracking (input & output)
- ✅ Cost calculation
- ✅ Budget enforcement (blocks requests when exceeded)
- ✅ JSON logging system
- ✅ Streamlit dashboard (interactive UI)
- ✅ Usage visualization

---

## 🧠 How It Works

1. User sends a prompt
2. Tokens are calculated
3. Cost is computed
4. Budget is checked
5. Request is allowed or blocked
6. Usage is logged

---

## 📂 Project Structure
llm-usage-tracker/
│
├── tracker/
│ ├── usage_tracker.py
│ ├── cost_calculator.py
│ ├── llm_wrapper.py
│ ├── logger.py
│ ├── exceptions.py
│
├── dashboard/
│ └── app.py
│
├── demo/
│ ├── normal_usage.py
│ └── budget_exceeded.py
│
├── data/
│ └── usage_log.json
│
└── README.md

## ▶️ Run Locally

```bash
pip install -r requirements.txt
streamlit run dashboard/app.py

🧪 Tech Stack
Python
Streamlit
JSON (logging)
🔥 Future Improvements
Real LLM API integration (OpenAI)
Database logging
Multi-user support
Advanced analytics dashboard
👨‍💻 Author

Manushree N
