def chatbot():
    print("Hello! I'm ChatBot 🤖. Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower()

        if user_input == "bye":
            print("ChatBot: Goodbye! Have a great day 👋")
            break
        elif "hello" in user_input or "hi" in user_input:
            print("ChatBot: Hi there! How can I help you?")
        elif "how are you" in user_input:
            print("ChatBot: I'm just a program, but I'm doing great! 😃")
        elif "your name" in user_input:
            print("ChatBot: I'm a simple Python ChatBot!")
        elif "time" in user_input:
            from datetime import datetime
            print("ChatBot: Current time is", datetime.now().strftime("%H:%M:%S"))
        else:
            print("ChatBot: Sorry, I don’t understand that.")

if __name__ == "__main__":
    chatbot()