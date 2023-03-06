import openai
import discord
from discord.ext import commands


discordtoken = "PASTE DISCORD BOT TOKEN"
openai.api_key = "PASTE OPENAI KEY"

allowed_users = ["User1#0001",
				 "User50#1023",
				 "User11#0232"]

def query(userprompt):
    response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=userprompt,
                max_tokens=1024,
                n=1,
                stop=None,
                temperature=0.5
                )
    return response.choices[0].text.strip()

def imgquery(userprompt):
	response = openai.Image.create(prompt=userprompt,
									n=1,
									size="512x512")
	image_url = response['data'][0]['url']
	embed = discord.Embed(title = "Dalle Image", color = 0xff0000)
	embed.set_image(url=image_url)
	return embed

intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(intents=intents, command_prefix="&")

@client.event
async def on_ready():
		print("Bot launched as {0.user}.".format(client))

@client.event
async def on_message(message):
	if message.content[0] == "&" or message.content[0] == "!":
		requester = str(message.author)
		if requester in allowed_users:
			try:
				prompt = message.content[1:]
				if message.content[0] == "!":
					await message.channel.send(embed=imgquery(prompt))
					pass
				else:
					await message.channel.send(query(prompt))
			except IndexError:
				pass
			except openai.error.InvalidRequestError:
				await message.channel.send("I cannot draw " + prompt + ".")
		else:
			await message.channel.send("You are not on the whitelist " + requester[:-5] + ".")
		
client.run(discordtoken)

