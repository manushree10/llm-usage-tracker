class UsageTracker:
    def __init__(self, budget):
        self.total_tokens = 0
        self.total_cost = 0.0
        self.budget = budget

    def add_usage(self, tokens, cost):
        self.total_tokens += tokens
        self.total_cost += cost

    def get_remaining_budget(self):
        return self.budget - self.total_cost

    def is_budget_exceeded(self):
        return self.total_cost >= self.budget

    def get_usage_summary(self):
        return {
            "total_tokens": self.total_tokens,
            "total_cost": self.total_cost,
            "remaining_budget": self.get_remaining_budget()
        }