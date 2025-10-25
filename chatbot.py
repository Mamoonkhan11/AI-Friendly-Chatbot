# Main chatbot application

import os
from dotenv import load_dotenv
from chatbot_logic.gpt_integration import gpt_response
from chatbot_logic.rules import rule_based_response
from chatbot_logic.utils import log_chat, select_emoji

# Load API key
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Path to chat history file
CHAT_HISTORY_FILE = "data/chat_history.txt"


def load_chat_history(file_path=CHAT_HISTORY_FILE):
    """Load previous chat history from file safely."""
    if not os.path.exists(file_path):
        # Ensure directory exists
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        return []
    
    chat_memory = []
    with open(file_path, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip()]  # skip blank lines

    # Parse safely to avoid IndexError
    for i in range(0, len(lines) - 1, 2):  # every two lines: You + Bot
        if not lines[i].startswith("You:") or not lines[i+1].startswith("Bot:"):
            continue
        user_line = lines[i].replace("You: ", "").strip()
        bot_line = lines[i+1].replace("Bot: ", "").strip()
        chat_memory.append({"user": user_line, "bot": bot_line})

    return chat_memory


def main():
    print("Welcome to Friendly AI Chatbot!")
    user_name = input("What's your name? ").strip() or "Friend"
    print(f"\nHello {user_name}! I'm Neura, your friendly AI assistant. 🌸")
    print("Type 'quit' to exit.\n")

    # Load previous chat history
    chat_memory = load_chat_history()

    # Print previous chat if exists
    if chat_memory:
        print("Previous conversation:\n")
        for chat in chat_memory:
            print(f"{user_name}: {chat['user']}")
            print(f"Neura: {chat['bot']}\n")

    # Chat loop
    while True:
        user_input = input(f"{user_name}: ").strip()
        if user_input.lower() in ["quit", "exit"]:
            print("Goodbye! Have a wonderful day! 👋")
            break

        # Check rule-based responses first
        response = rule_based_response(user_input)
        if not response:
            # GPT-powered intelligent response
            response = gpt_response(user_input)

        # Add mood emoji dynamically
        response += " " + select_emoji(user_input)

        # Print bot reply
        print(f"Neura: {response}\n")

        # Update memory
        chat_memory.append({"user": user_input, "bot": response})

        # Persist conversation to file
        log_chat(user_input, response, file_path=CHAT_HISTORY_FILE)


if __name__ == "__main__":
    main()