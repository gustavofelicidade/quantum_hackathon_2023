import os
import openai

openai_api_key = "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"

# openai.organization = "YOUR_ORG_ID"
openai.api_key = os.getenv(openai_api_key)
openai.Model.list()