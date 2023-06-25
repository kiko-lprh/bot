import discord
import respuestas 
from discord.activity import Activity

async def send_message(message,user_message,is_private):
    try:
        respuesta = respuestas.procesar_respuestas(user_message)
        await message.author.send(respuesta) if is_private else await message.channel.send(respuesta)
    except Exception as error_:
        print(error_)     

def run_bot():
    #TOKEN = 'get a token from discord'
    client = discord.Client()
    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.streaming, name="choose activity"))

    @client.event
    async def on_message(message):
        #makes it so that the bot can't use its own messages
        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str (message.channel)

        print(f"{username} said: '{user_message}' on the {channel} channel")

        if user_message[0] == "?":
            user_message = user_message[1:]
            await send_message(message,user_message,is_private=True)
        else:
            await send_message(message,user_message,is_private=False)

    client.run(TOKEN)
    

