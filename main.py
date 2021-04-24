import discord
from discord.ext import commands
from discord import Webhook, AsyncWebhookAdapter
import aiohttp 

token = input('Enter your bot token... ')
roleID = int(input('Enter the role ID... '))
channelID = int(input('Enter the channel ID... '))
webhook1 = input("Enter webhook link 1... ")
webhook2 = input("Enter webhook link 2... ")
webhook3 = input("Enter webhook link 3... ")
spam_webhooks = [webhook1, webhook2, webhook3]
client = commands.Bot(command_prefix=';', intents=discord.Intents.all())
client.remove_command("help")


@client.event
async def on_ready():
  print("Running, type ;spam in the channel to start the spamming. ")

@client.command(pass_context=True)
async def spam(ctx):
  channel = client.get_channel(channelID)
  for url in spam_webhooks: 
    while True:
      try:
        async with aiohttp.ClientSession() as session:
          webhook = Webhook.from_url(url, adapter=AsyncWebhookAdapter(session))
          monkey = discord.utils.get(ctx.guild.roles, id=roleID)
          await webhook.send(f"{monkey.mention}")
          await channel.send(f'{monkey.mention}')
      except:
        pass
  


client.run(token)













