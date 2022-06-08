from twitchio.ext import commands
import random

token=''

class Bot(commands.Bot):

    def __init__(self):
        # Initialise our Bot with our access token, prefix and a list of channels to join on boot...
        # prefix can be a callable, which returns a list of strings or a string...
        # initial_channels can also be a callable which returns a list of strings...
        super().__init__(token='oauth:'+token, prefix='?', initial_channels=['#chickenswithaview'])

    async def event_ready(self):
        # Notify us when everything is ready!
        # We are logged in and ready to chat and use commands...
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')

    async def event_message(self, message):
        # Messages with echo set to True are messages sent by the bot...
        # For now we just want to ignore them...
        if message.echo:
            return

        # Print the contents of our message to console...
        print(message.content)

        # Since we have commands and are overriding the default `event_message`
        # We must let the bot know we want to handle and invoke our commands...
        await self.handle_commands(message)

    @commands.command()
    async def roo(self, ctx: commands.Context):
        # Here we have a command hello, we can invoke our command with our prefix and command name
        # e.g ?hello
        # We can also give our commands aliases (different names) to invoke with.

        # Send a hello back!
        # Sending a reply back to the channel is easy... Below is an example.
        await ctx.send(f'Cock a doodle doo @{ctx.author.name}!')

    @commands.command()
    async def hello(self, ctx: commands.Context):
        # Here we have a command hello, we can invoke our command with our prefix and command name
        # e.g ?hello
        # We can also give our commands aliases (different names) to invoke with.

        # Send a hello back!
        # Sending a reply back to the channel is easy... Below is an example.
        await ctx.send(f'Hello hello {ctx.author.name}!')

    @commands.command()
    async def joke(self, ctx: commands.Context):
        # Here we have a command hello, we can invoke our command with our prefix and command name
        # e.g ?hello
        # We can also give our commands aliases (different names) to invoke with.

        # Send a hello back!
        # Sending a reply back to the channel is easy... Below is an example.
        jokes=['What do sick chickens get? Human-pox', \
            'Why did the rooster never come home to his hen? He was free range',\
            'What do you call a great chicken? Impeckable', \
            'What day of the week are chickens afraid of? Fry-day', \
            'What do young chickens like to watch? Chick flicks', \
            'How do chickens like their eggs? Hatched', \
            'How do you know if an egg joke is good? If it cracks you up', \
            'What do you do with a shy chick? Try get it to come out of its shell', \
            'What do you think of these egg jokes? They aren’t all what they cracked up to be',\
            'Why did the chick cross the road? For cheep thrills', \
            'What do you call a bird who’s too afraid to fly? A chicken',\
            'What do chickens study at college? Egg-onomics',\
            'What’s a hen’s favorite type of movie? A chick flick',\
            'What do you call a mischievous egg? A practical yolker',\
            'What time do chickens wake up in the morning? At the cluck of dawn']

        int=random.randint(0, (len(jokes)-1))
        await ctx.send(f'{jokes[int]}!')



bot = Bot()
bot.run()