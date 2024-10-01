import requests
from bs4 import BeautifulSoup
from openai import OpenAI
from src.utils.helpers import truncate_text, load_api_key

client = OpenAI(api_key=load_api_key())

def process_website_and_answer(url, query):
    # Fetch website content
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extract text from the website
    text = soup.get_text()
    
    # Prepare the prompt for GPT-4
    prompt = f"Based on the following website content, answer this question: {query}\n\nWebsite content:\n{truncate_text(text)}"
    
    # Get answer from GPT-4
    response = client.chat.completions.create(
        model="gpt-4-0125-preview",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that answers questions based on website content."},
            {"role": "user", "content": prompt}
        ]
    )
    
    return response.choices[0].message.content