from tracker.exceptions import BudgetExceededError
from tracker.logger import UsageLogger

def dummy_llm(prompt):
    """
    Simulates an LLM response
    """
    return "This is a generated response for: " + prompt


def tracked_llm_call(tracker, calculator, prompt):
    """
    Wrapper function that:
    - Simulates token usage
    - Checks budget
    - Updates tracker
    """

    # 🔹 Initialize logger
    logger = UsageLogger()

    # 🔹 Step 1: Simulate token usage
    input_tokens = len(prompt.split())
    output_tokens = 20  # fixed for simplicity

    # 🔹 Step 2: Calculate cost
    cost = calculator.calculate_cost(input_tokens, output_tokens)

    # 🔹 Step 3: Check budget BEFORE making request
    if tracker.total_cost + cost > tracker.budget:
        raise BudgetExceededError()

    # 🔹 Step 4: Call dummy LLM
    response = dummy_llm(prompt)

    # 🔹 Step 5: Update usage
    tracker.add_usage(input_tokens + output_tokens, cost)

    # 🔥 Step 6: Log the usage (ADD HERE)
    logger.log(prompt, input_tokens, output_tokens, cost)

    return {
        "response": response,
        "input_tokens": input_tokens,
        "output_tokens": output_tokens,
        "cost": cost
    }