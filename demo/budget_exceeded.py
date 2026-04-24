from tracker.usage_tracker import UsageTracker
from tracker.cost_calculator import CostCalculator
from tracker.llm_wrapper import tracked_llm_call

tracker = UsageTracker(budget=0.005)  # very small budget
calculator = CostCalculator()

prompts = [
    "Explain AI",
    "Explain ML",
    "Explain Deep Learning"
]

for i, prompt in enumerate(prompts):
    print(f"\n🔹 Request {i+1}")
    
    try:
        result = tracked_llm_call(tracker, calculator, prompt)
        print("Response:", result["response"])
        print("Cost:", result["cost"])
        print("Remaining Budget:", tracker.get_remaining_budget())

    except Exception as e:
        print(e)
        break