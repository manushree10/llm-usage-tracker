import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
import json

from tracker.usage_tracker import UsageTracker
from tracker.cost_calculator import CostCalculator
from tracker.llm_wrapper import tracked_llm_call
from tracker.exceptions import BudgetExceededError


# 🔹 Sidebar (DEFINE BUDGET FIRST)
st.sidebar.title("⚙️ Settings")

budget = st.sidebar.number_input(
    "Set Budget ($)",
    min_value=0.001,
    value=0.02,
    step=0.001
)


# 🔥 Initialize tracker (ONLY ONCE, CORRECT WAY)
if "tracker" not in st.session_state or st.session_state.tracker.budget != budget:
    st.session_state.tracker = UsageTracker(budget=budget)


calculator = CostCalculator()

st.title("💰 LLM Usage Tracker Dashboard")


# 🔹 User Input
prompt = st.text_area("Enter your prompt:")


# 🔹 Button
if st.button("Generate Response"):

    if prompt.strip() == "":
        st.warning("Please enter a prompt")
    else:
        try:
            result = tracked_llm_call(
                st.session_state.tracker,
                calculator,
                prompt
            )

            st.success("✅ Response Generated")

            st.write("### 🤖 Response")
            st.write(result["response"])

            st.write("### 📊 Usage Details")
            st.write(f"Input Tokens: {result['input_tokens']}")
            st.write(f"Output Tokens: {result['output_tokens']}")
            st.write(f"Cost: {result['cost']}")

        except BudgetExceededError as e:
            st.error(str(e))


# 🔹 Show overall usage
st.write("## 📈 Overall Usage")

tracker = st.session_state.tracker

col1, col2, col3 = st.columns(3)

col1.metric("Total Tokens", tracker.total_tokens)
col2.metric("Total Cost ($)", round(tracker.total_cost, 5))
col3.metric("Remaining Budget ($)", round(tracker.get_remaining_budget(), 5))


# 🔹 Usage Graph
st.write("## 📊 Usage Visualization")

try:
    with open("data/usage_log.json", "r") as f:
        data = json.load(f)

    if len(data) > 0:
        costs = [entry["cost"] for entry in data]
        st.line_chart(costs)
    else:
        st.info("No usage data yet")

except:
    st.warning("No log file found")