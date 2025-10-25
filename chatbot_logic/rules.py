# rules based fallback responses

import datetime

def rule_based_response(user_input: str) -> str:
    text = user_input.lower()
    if any(word in text for word in ["hi", "hello", "hey"]):
        return "Hello! 😊 How can I help you today?"
    elif "time" in text:
        return f"The current time is {datetime.datetime.now().strftime('%H:%M')} ⏰"
    elif "date" in text:
        return f"Today's date is {datetime.datetime.now().strftime('%Y-%m-%d')} 📅"
    elif "bye" in text:
        return "Goodbye! 👋 See you soon!"
    return None
