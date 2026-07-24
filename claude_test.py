from anthropic import Anthropic
import os

client = Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))
history = []

while True:
    question = input("You: ")
    if question == "exit":
        break
    
    history.append({"role": "user", "content": question})
    
    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=200,
        messages=history
    )
    
    answer = response.content[0].text
    history.append({"role": "assistant", "content": answer})
    print("Claude:", answer)