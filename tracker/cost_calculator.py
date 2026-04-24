class CostCalculator:
    def __init__(self):
        # Cost per token (dummy pricing)
        self.input_token_rate = 0.0001
        self.output_token_rate = 0.0002

    def calculate_cost(self, input_tokens, output_tokens):
        input_cost = input_tokens * self.input_token_rate
        output_cost = output_tokens * self.output_token_rate
        total_cost = input_cost + output_cost
        return total_cost