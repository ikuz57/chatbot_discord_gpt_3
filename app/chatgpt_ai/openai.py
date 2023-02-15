import os

import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("CHATGPT_API_KEY")


def chatgpt_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=0.4,
        max_tokens=300,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.5,
    )
    response_dict = response.get("choices")
    if response_dict and len(response_dict) > 0:
        prompt_response = response_dict[0]["text"]
    return prompt_response
