from anthropic import Anthropic
import os
import json
client = Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))
a = []

while True:  
    x = input("Ask about a Country? ")
    if x == "exit":
        break
    a.append({"role": "user", "content": x})

    response = client.messages.create(model="claude-sonnet-4-6",
    max_tokens=200,
            messages=a,
            system="Return ONLY valid JSON with no markdown, no backticks, no explanation. Just the raw JSON with fields: name, capital, population, language")
    print("API response received") 

    answer = response.content[0].text
    answer = answer.replace("```json", "").replace("```", "").strip()
    a.append({"role": "assistant", "content": answer})
    

    try:
        with open("countries.json", "r") as f:
            countries = json.load(f)
    except FileNotFoundError:
        countries = []

    countries.append(answer)

    with open("countries.json", "w") as f:
        json.dump(countries, f)

    with open("countries.json", "r") as f:
            print(f.read())
            parsed = json.loads(answer)
            print("Capital:", parsed["capital"])

    