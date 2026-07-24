from anthropic import Anthropic
import os
import json

client = Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

a = []
while True:
    x = input("Mood? or type done ")
    if x == "done":
        break

    a.append({"role": "user", "content": x})
    
    try:
        response = client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=200,
            messages=a,
            system="You are a supportive mood journal assistant. Give short, plain text advice and encouragement based on how the user feels. No markdown, no tables, no emojis.")
        answer = response.content[0].text
        print("Got answer:", answer[:50])
    except Exception as e:
        print("Error:", e)
        continue

    a.append({"role": "assistant", "content": answer})

    try:
        with open("mood.json", "r") as f:
            mood1 = json.load(f)
    except FileNotFoundError:
        mood1 = []

    mood1.append({"user": x, "claude": answer})

    with open("mood.json", "w") as f:
        json.dump(mood1, f)
    
    print(json.dumps(mood1, indent=2))