import discord
from discord.ext import commands
from discord.utils import get
import requests

TOKEN = # YOUR TOKEN
TRN_URL = 'https://public-api.tracker.gg/v2/apex/standard/profile/'

client = commands.Bot(command_prefix='+')
Client = discord.Client()


# Client Events & Commands
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('Ranking for Fun'))
    print('Bot online')


# Command usage error
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Use !help <command> to see proper command usage.')


# Command usage help
@client.command()
async def rankhelp(ctx):
    embed = discord.Embed(title="ApexRankBot", description="Rank command usage")
    embed.add_field(name="+rankme", value="Adds your Apex Legends rank as a role in the server\n\n***+rankme platform username***"
                                          "\nplatforms: origin, xbl, psn\nExample: +rankme origin username")
    await ctx.channel.send(content=None, embed=embed)


# Adding rank to nickname
@client.command(pass_context=True)
async def rankme(ctx, platform, username):
    
    url = f'{TRN_URL}' + platform + '/' + username
    headers = {
        'trn-api-key': "# YOUR TRN API KEY HERE",
        'cache-control': "no-cache"
    }
    response = requests.request("GET", url, headers=headers)
    response_dict = response.json()

    rank = response_dict['data']['segments'][0]['stats']['rankScore']['metadata']['rankName']
    rank_num = response_dict['data']['segments'][0]['stats']['rankScore']['rank']
    rank_image = response_dict['data']['segments'][0]['stats']['rankScore']['metadata']['iconUrl']
    pred_image = "https://trackercdn.com/cdn/apex.tracker.gg/ranks/apex.png"

    print(rank, rank_num)
    member = ctx.message.author

    if 'Bronze' in rank:
        role = get(member.guild.roles, name='Bronze')
        await member.add_roles(role)
        await ctx.send(f"{ctx.author.mention}, your rank has been assigned as ***{rank}***\n{rank_image}")
    elif 'Silver' in rank:
        role = get(member.guild.roles, name='Silver')
        await member.add_roles(role)
        await ctx.send(f"{ctx.author.mention}, your rank has been assigned as ***{rank}***\n{rank_image}")
    elif 'Gold' in rank:
        role = get(member.guild.roles, name='Gold')
        await member.add_roles(role)
        await ctx.send(f"{ctx.author.mention}, your rank has been assigned as ***{rank}***\n{rank_image}")
    elif 'Platinum' in rank:
        role = get(member.guild.roles, name='Platinum')
        await member.add_roles(role)
        await ctx.send(f"{ctx.author.mention}, your rank has been assigned as ***{rank}***\n{rank_image}")
    elif 'Diamond' in rank:
        role = get(member.guild.roles, name='Diamond')
        await member.add_roles(role)
        await ctx.send(f"{ctx.author.mention}, your rank has been assigned as ***{rank}***\n{rank_image}")
    elif 'Master' in rank:
        role = get(member.guild.roles, name='Master')
        if role == get(member.guild.roles, name='Master'):
            if rank_num < 501:
                role = get(member.guild.roles, name='Apex Predator')
                await member.add_roles(role)
                await ctx.send(f"{ctx.author.mention}, your rank has been assigned as ***{role}*** ***#{rank_num}***\n{pred_image}")
        else:
            await member.add_roles(role)
            await ctx.send(f"{ctx.author.mention}, your rank has been assigned as ***{role}***\n{pred_image}")


# Run the client
client.run(TOKEN)
