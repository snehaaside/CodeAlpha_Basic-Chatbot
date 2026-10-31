"""
CodeAlpha Python Internship - Task 4: Basic Chatbot
A simple rule-based chatbot using if-elif, functions, loops and input/output.
"""


def get_response(user_input):
    """Return a predefined reply based on the user's message."""
    message = user_input.lower().strip()

    if message == "hello" or message == "hi":
        return "Hi!"
    elif message == "how are you":
        return "I'm fine, thanks!"
    elif message == "what is your name":
        return "I'm a simple rule-based chatbot."
    elif message == "help":
        return "Try typing: hello, how are you, what is your name, or bye."
    elif message == "bye":
        return "Goodbye!"
    else:
        return "Sorry, I don't understand that. Type 'help' to see what I can reply to."


def chatbot():
    """Run the chat loop until the user says bye."""
    print("Chatbot: Hello! Let's chat. (Type 'bye' to exit)")

    while True:
        user_input = input("You: ")
        reply = get_response(user_input)
        print("Chatbot:", reply)

        if user_input.lower().strip() == "bye":
            break


chatbot()
