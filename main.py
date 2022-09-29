from discord.ext import commands
from models import User
bot = commands.Bot('.')

@bot.event
async def on_message(message):
    if message.author.id not in users.keys():
        users[message.author.id] = User(message.author.name)


@bot.listen()
async def on_message(message):
    for index, badword in enumerate(badwords):
        if badword in message.content.lower():
            users[message.author.id].__dict__[words[index]] += 1
            users[message.author.id].total += 1
    if users[message.author.id].total >= 10:
        for index, word in enumerate(words):
            msg += f"{word}: {users[message.author.id].__dict__[word]}\n"
        await message.author.send(msg)
        users[message.author.id].total = 0