from tracker.usage_tracker import UsageTracker
from tracker.cost_calculator import CostCalculator
from tracker.llm_wrapper import tracked_llm_call

# 🔹 Step 1: Initialize tracker with budget
tracker = UsageTracker(budget=0.01)  # small budget
calculator = CostCalculator()

# 🔹 Step 2: Simulate multiple LLM calls
prompts = [
    "Hello, how are you?",
    "Explain machine learning in simple terms",
    "What is artificial intelligence?",
]

for i, prompt in enumerate(prompts):
    print(f"\n🔹 Request {i+1}")
    
    try:
        result = tracked_llm_call(tracker, calculator, prompt)
        
        print("Response:", result["response"])
        print("Input Tokens:", result["input_tokens"])
        print("Output Tokens:", result["output_tokens"])
        print("Cost:", result["cost"])
        print("Total Cost:", tracker.total_cost)
        print("Remaining Budget:", tracker.get_remaining_budget())

    except Exception as e:
        print(e)
        break