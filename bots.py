import discord # type: ignore
import responses
import os
TOKEN = os.getenv('DISCORD_TOKEN')

async def send_message(message,user_message,is_private):

    try:
        response = responses.handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception:
        print(Exception)



def run_discord_bot():
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)


    @client.event
    async def on_ready():
        print(f'{client.user} is running!')
    


    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        username=str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)
        
        await send_message(message,user_message=user_message,is_private=False)

    client.run(TOKEN)