from logic import get_answer

if __name__ == "__main__":
    print("Welcome to the Thoughtful AI Agent! Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("Goodbye!")
            break
        print("Agent: ", get_answer(user_input))