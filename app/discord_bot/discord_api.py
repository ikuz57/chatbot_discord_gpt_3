import logging
import os

import discord
import openai
from dotenv import load_dotenv

from app.chatgpt_ai.openai import chatgpt_response

load_dotenv()

dis_token = os.getenv("DISCORD_TOKEN")
logging.basicConfig(
    level=logging.INFO,
    filemode="w",
    filename="bot.log",
    format="%(asctime)s %(levelname)s %(message)s",
    encoding="utf-8",
)


class MyClient(discord.Client):
    """
    This class is a Discord bot that uses the OpenAI GPT-3 API to generate
    responses. It takes in user input and uses it to generate a response.
    It also keeps track of the context of the conversation by storing the
    dialogue in a variable. If the dialogue gets too long, it will reset
    the context.
    """
    context = ""

    async def on_ready(self):
        logging.info("Successfully logged in")

    async def on_message(self, message):
        if message.author == self.user:
            return
        command, prompt = None, None

        if message.content.startswith("/ai"):
            command = message.content.split(" ")[0]
            prompt = message.content.replace("/ai", "")[1::]
            logging.info(f"command:{command}, prompt:{prompt}\n")

        if message.content.startswith("/ai_clear"):
            command = message.content.split(" ")[0]
            logging.info(f"command:{command}")

        if command == "/ai_clear":
            self.context = ""
            await message.channel.send(
                "You cleaned up the dialogue, "
                "Now I don't remember what we were talking about."
            )

        if command == "/ai":
            logging.info(self.context)
            try:
                if self.context == "":
                    bot_response = chatgpt_response(prompt=prompt)
                    self.context += prompt + "\n" + bot_response + "\n"
                else:
                    self.context += prompt + "\n"
                    if len(self.context.split()) >= 2700:
                        logging.info("переполнение")
                        self.context = self.context[-2700]
                    bot_response = chatgpt_response(prompt=self.context)
                    self.context += bot_response + "\n"
                await message.channel.send(bot_response)
            except discord.errors.HTTPException:
                await message.channel.send(
                    "Sorry, we received an empty "
                    "message, can we try again?"
                )
            except openai.error.ServiceUnavailableError:
                await message.channel.send(
                    "Error on the server or it's not available, come on "
                    "let's try again?"
                )
            except openai.error.InvalidRequestError:
                await message.channel.send(
                    "Clean up the dialogue (/ai_clear), and let's try again?"
                )


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
