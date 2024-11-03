from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage
import os

api_key = os.environ["mistral_api_key"]
model = "codestral-mamba-latest" # Use "mistral-tiny" for "Mistral-7B-v0.2"

client = MistralClient(api_key=api_key)

messages = [
    ChatMessage(role="user", content="Explain Vietnam law")
]

# No streaming
chat_response = client.chat(
    model=model,
    messages=messages,
)
print(chat_response.choices[0].message.content)

# With streaming
# for chunk in client.chat_stream(model=model, messages=messages):
#     if chunk.choices[0].delta.content:
#         print(chunk.choices[0].delta.content, end="")