from ollama_client import ask_model

def main():
    print("🤖 Local AI Fun-Fact Assistant")
    print("Type 'exit' to quit\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("Goodbye 👋")
            break
            

        answer = ask_model(user_input)
        print(f"AI: {answer}\n")

if __name__ == "__main__":
    main()