import random

def chatbot():
    print("Chatbot: Hello! I'm an advanced chatbot. Type 'exit' to end the conversation.")
    print("Chatbot: How can I help you today?")

    
    # Predefined responses
    responses = {
        "hello": ["Hi there! How can I assist you?", "Hello! What's on your mind?", "Hey! How can I help you?"],
        "how are you": ["I'm doing great! Thanks for asking.", "I'm just a program, but I feel fantastic!", "I'm here to help!"],
        "what is your name": ["I am your friendly chatbot!", "You can call me ChatBot.", "I don't have a fancy name, but I'm here for you!"],
        "help": ["Sure! Ask me anything.", "I'm here to assist you. What do you need help with?", "Let me know how I can help you."],
        "bye": ["Goodbye! Have a great day!", "See you later! Take care.", "Bye! It was nice talking to you."],
        "what can you do": ["I can answer simple questions, chat with you, and make your day better!", 
                            "I'm here to provide information and entertain you. Ask me anything!", 
                            "I can chat with you, help you learn, and answer basic queries."],
        "tell me a joke": ["Why don’t scientists trust atoms? Because they make up everything!", 
                           "Why did the math book look sad? Because it had too many problems.", 
                           "What do you call fake spaghetti? An impasta!"],
        "who created you": ["I was created by a Python enthusiast!", "Someone smart and curious made me.", "I was built using Python, and here I am!"],
        "what is python": ["Python is a popular programming language known for its simplicity and versatility.", 
                           "Python is a programming language used for web development, data science, AI, and more.", 
                           "Python is like a Swiss Army knife for programming!"],
    }

    while True:
        # Get user input
        user_input = input("You: ").strip().lower()

        # Exit condition
        if user_input == "exit":
            print("Chatbot: Goodbye! It was nice talking to you.")
            break

        # Get response or default reply
        if user_input in responses:
            response = random.choice(responses[user_input])
        else:
            response = "I'm sorry, I don't understand that. Can you try asking something else?"

        print(f"Chatbot: {response}")

# Run the chatbot
if __name__ == "__main__":
    chatbot()
