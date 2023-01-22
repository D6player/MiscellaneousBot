import discord
import random

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
id_guild = 397889512174518283
id_channel = 675414098024071169
global channel
global submiter
global submits
submits = {}

def there_are_submits():
	global submits
	n = 0
	for k in submits:
		n += len(submits[k])

	return n > 0

async def send_submit():
	global submits
	global submiter
	global channel

	submiter = random.choice(list(submits.keys()))
	v = random.choice(submits[submiter])
	submits[submiter].remove(v)
	
	await channel.send(v)


@client.event
async def on_ready():
	global channel
	GUILD = client.get_guild(id_guild)
	channel = GUILD.get_channel(id_channel)
	print(f'Working as {client.user}')

@client.event
async def on_message(message):
	global submits
	global submiter
	global channel

	if message.content == 'go':
		if there_are_submits():
			await send_submit()
		else:
			message.reply('No more submits')

		return
	elif message.content == 'reveal':
		await channel.send(f'The submiter is <@{submiter}>')
		return

	if message.channel.type == discord.ChannelType.private:
		for attachment in message.attachments:
			aux = submits.get(message.author.id, [])
			aux.append(attachment.proxy_url)
			submits[message.author.id] = aux


client.run('MTA2NjY5MTU2MDIwMjMwOTYzMg.GVeyaq.z3d4VcD-iosLk17wOxy0mJWf9Cac5L8h4dH80k')
