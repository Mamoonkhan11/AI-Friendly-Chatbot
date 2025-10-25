# Helper: Utility functions for chatbot logic

import os
import random

# Logging function
def log_chat(user_message: str, bot_message: str, file_path="data/chat_history.txt"):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, "a", encoding="utf-8") as f:
        f.write(f"You: {user_message}\nBot: {bot_message}\n\n")


# Emoji selector based on keywords/mood
def select_emoji(user_input: str) -> str:
    text = user_input.lower()
    if any(word in text for word in ["happy", "good", "great", "fun"]):
        return random.choice(["😄", "😊", "✨"])
    elif any(word in text for word in ["sad", "bad", "angry", "upset"]):
        return random.choice(["😢", "🙁", "😔"])
    elif any(word in text for word in ["wow", "amazing", "awesome"]):
        return "🤩"
    else:
        return random.choice(["🙂", "🌸", "🤖"])