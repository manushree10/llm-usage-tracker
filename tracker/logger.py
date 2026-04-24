import json
import os
from datetime import datetime


class UsageLogger:
    def __init__(self, file_path="data/usage_log.json"):
        self.file_path = file_path

        if not os.path.exists(self.file_path):
            with open(self.file_path, "w") as f:
                json.dump([], f)

    def log(self, prompt, input_tokens, output_tokens, cost):
        log_entry = {
            "prompt": prompt,
            "input_tokens": input_tokens,
            "output_tokens": output_tokens,
            "total_tokens": input_tokens + output_tokens,
            "cost": cost,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        with open(self.file_path, "r") as f:
            data = json.load(f)

        data.append(log_entry)

        with open(self.file_path, "w") as f:
            json.dump(data, f, indent=4)