import random
import discord
from bot_logic import gen_pass
from bot_logic2 import *
# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Listo, estás dentro siendo {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith("Commands"):
        await message.channel.send("ok")
    elif message.content.startswith('hello'):
        await message.channel.send("Hi!")
    elif message.content.startswith('bye'):
        await message.channel.send("\\U0001f642")
    elif message.content.startswith('$How are you?'):
        await message.channel.send("Doing fine, thanks for asking.")
    elif message.content.startswith('WATCH OUT, A BOMB!'):
        await message.channel.send("WHERE?!")
    elif message.content.startswith('ITS GONNA EXPLODE!!'):
        await message.channel.send("BOMBOCLA- *BOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOM*")
    elif message.content.startswith('Generame una contraseña aleatoria.'):
        await message.channel.send(f"Password: {gen_pass(100)}")
    elif message.content.startswith("Generame un número aleatorio."):
        number = random.randint(1,100)
        await message.channel.send(number)
    elif message.content.startswith('👍'):
        await message.channel.send("👍")
    elif message.content.startswith('❗'):
        await message.channel.send("❓")
    elif message.content.startswith('💬'):
        await message.channel.send("💯")
    elif message.content.startswith('Mi canal de Youtube?'):
        await message.channel.send("https://www.youtube.com/@Jaimotorola3000")
    elif message.content.startswith(f'Eres chino?'):
        await message.channel.send("https://avatars.steamstatic.com/e468b72c990461c95b9cf194deff2cbb4aa8ef05_full.jpg")
        await message.channel.send("Si.")
    elif message.content.startswith(f"¿Cara o Sello?"):
        image_url, message_text = (flip_coin())
        await message.channel.send(image_url)
        await message.channel.send(message_text)
    else:
        await message.channel.send(message.content)
client.run("Aquí iría el token.")