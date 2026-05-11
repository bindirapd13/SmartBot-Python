import json
import random

# Load intents file
with open('intents.json') as file:
    data = json.load(file)

print("AI Chatbot is running! Type 'quit' to stop.")

while True:
    user_input = input("You: ").lower()

    # Exit condition
    if user_input == "quit":
        print("Chatbot: Goodbye!")
        break

    found = False

    # Check patterns
    for intent in data["intents"]:
        for pattern in intent["patterns"]:

            # Improved matching
            if pattern.lower() in user_input:
                response = random.choice(intent["responses"])
                print("Chatbot:", response)
                found = True
                break

        if found:
            break

    # Default response
    if not found:
        print("Chatbot: Sorry, I don't understand. Please try another question.")