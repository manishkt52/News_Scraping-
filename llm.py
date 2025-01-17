import os
from groq import Groq
from dotenv import load_dotenv
load_dotenv(dotenv_path='.env')

# Load environment variables from the .env file
load_dotenv()

# Check if the API key is loaded correctly
API_KEY = os.getenv("GROQ_API")
if API_KEY is None:
    raise ValueError("API key not found. Make sure it is defined in the .env file.")
 # For debugging purposes
def output(prompt):
# Create a Groq client using the API key loaded from .env
    client = Groq(
        api_key=API_KEY  # Load API key from .env
    )

    # Send a request to the LLaMA model
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="llama-3.1-8b-instant",  # Specify the model
    )

    # Print the response from the API
    return(chat_completion.choices[0].message.content)