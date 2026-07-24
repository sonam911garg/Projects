from anthropic import Anthropic
import os

client = Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))
a = []

while True:  
    x = input("Question? ")
    if x == "exit":
        break
    a.append({"role": "user", "content": x})

    response = response = client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=200,
            messages=a,
            system="You are a sarcastic assistant who responds to everything with sarcasm and dry humor."
        )

    answer = response.content[0].text
    a.append({"role": "assistant", "content": answer})
    print("Claude:", answer)