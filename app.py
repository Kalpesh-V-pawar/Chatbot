import random

def chatbot():
    print("Chatbot: Hello! I'm a basic chatbot. Type 'exit' to end the conversation.")
    print("Chatbot: How can I help you today?")

    # Predefined responses
    responses = {
        "hello": "Hi there! How can I assist you?",
        "how are you": "I'm just a program, but I'm doing great! Thanks for asking.",
        "what is your name": "I am your friendly chatbot!",
        "help": "Sure! I can answer your questions or chat with you. What do you need help with?",
        "bye": "Goodbye! Have a great day!",
    }

    while True:
        # Get user input
        user_input = input("You: ").strip().lower()

        # Exit condition
        if user_input == "exit":
            print("Chatbot: Goodbye! It was nice talking to you.")
            break

        # Get response or default reply
        response = responses.get(user_input, "I'm sorry, I don't understand that.")
        print(f"Chatbot: {response}")

# Run the chatbot
if __name__ == "__main__":
    chatbot()
  
