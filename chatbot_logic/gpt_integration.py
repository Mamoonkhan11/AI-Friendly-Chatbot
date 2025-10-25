# API Logic for GPT Integration

import os
from dotenv import load_dotenv
from openai import OpenAI

# Load .env file
load_dotenv()

# Get the API key from environment
api_key = os.getenv("OPENAI_API_KEY")


# Initialize OpenAI client
client = OpenAI(api_key=api_key)

def gpt_response(user_input: str) -> str:
    
    #Send user input to GPT and return the response.
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are Lyra, a friendly AI assistant that uses emojis occasionally."},
                {"role": "user", "content": user_input}
            ]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Sorry, I couldn't get an answer: {str(e)}"