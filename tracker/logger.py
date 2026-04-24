import json
import os
from datetime import datetime


class UsageLogger:
    def __init__(self):
        # 🔥 Correct absolute path
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.file_path = os.path.join(base_dir, "data", "usage_log.json")

        # Ensure file exists
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

        # Read existing data
        with open(self.file_path, "r") as f:
            data = json.load(f)

        # Append new log
        data.append(log_entry)

        # Write back
        with open(self.file_path, "w") as f:
            json.dump(data, f, indent=4)
