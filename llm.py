# generate_mcqs.py
import os
import google.generativeai as genai
from dotenv import load_dotenv
import re

# Load environment variables from .env file
load_dotenv()

# Retrieve the Gemini API key
GEMINI_API_KEY = os.getenv("GEMINI_FLASH_API")
genai.configure(api_key=GEMINI_API_KEY)

# Initialize the Gemini model
def output(prompt):
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)

    if response and response.candidates:
        text_content = response.candidates[0].content.parts[0].text
        output_text = text_content
        # print(f'Response: {text_content}')
    else:
     print("No response or candidates found.")

    

    return output_text

# Function to generate MCQs using the Gemini model
