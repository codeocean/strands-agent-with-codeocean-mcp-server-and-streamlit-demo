import os
from strands.models.anthropic import AnthropicModel
from dotenv import load_dotenv
load_dotenv()

model = AnthropicModel(
    client_args={
        "api_key": os.getenv("ANTRHROPIC_API_KEY", ""),
    },
    max_tokens=4096,
    model_id="claude-sonnet-4-20250514",
)
