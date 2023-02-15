# chatbot_discord_cgpt
This is a Discord bot that uses the OpenAI GPT-3 API to generate responses. It takes user input and uses it to generate a response. It also keeps track of the context of the conversation by storing the conversation in a variable. But due to the 4097 token limit, if the dialogue gets too long, the context will be reset.

## Installation
1. clone
2. install virtual environment
3. install dependencies from requirmenets.txt
4. Create and populate the .env, like .example.env
5. Run run.py

## Commands
1. "/ai you_request" - all requests to the bot come after /ai
2. "/ai_clear" - clear the dialogue history. The bot sometimes gets stuck on one topic.

## Settings GPT_3 in chatgpt_api/openai.py
1. engine="text-davinci-003"
https://platform.openai.com/docs/api-reference/models/list
2. prompt=prompt
3. temperature=0.4
https://platform.openai.com/docs/api-reference/completions/create#completions/create-temperature
4. max_tokens=300
5. top_p=1
https://platform.openai.com/docs/api-reference/completions/create#completions/create-top_p
6. frequency_penalty=0
https://platform.openai.com/docs/api-reference/completions/create#completions/create-frequency_penalty
7. presence_penalty=0.5
https://platform.openai.com/docs/api-reference/completions/create#completions/create-presence_penalty

## Taken from here:
https://youtu.be/wdgVv4UP08c