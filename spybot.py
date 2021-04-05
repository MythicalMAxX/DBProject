from discord.ext import commands
import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", password="14147714", database="vinamradb")

mycursor = mydb.cursor()

TOKEN = "ODI4Mjc2MTc3NDI0MjIwMjAw.YGnOTQ.unqxZ1gvGdaRLcAf71Pf-pIeoSM"
client = commands.Bot(command_prefix="")


with open("bad_words.txt") as file:
    bad_words = [bad_word.strip().lower() for bad_word in file.readlines()]
@client.event
async def on_message(message):
    message_content = message.content.strip().lower()
    for bad_word in bad_words:
        if bad_word in message_content:
            await message.channel.send("{}, your message has been censored.".format(message.author.mention))
            await message.delete()



@client.event
async def on_ready():
    print("bot is ready to takeoff")




client.run(TOKEN)