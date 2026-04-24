class BudgetExceededError(Exception):
    def __init__(self, message="❌ Budget exceeded! Request blocked."):
        super().__init__(message)