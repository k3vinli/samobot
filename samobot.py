import discord
import pickle
import re
class SamoBot(discord.Bot):

    def __init__(self, terms, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.connections = {}
        self.terms = terms
        if "brainrot_count" in kwargs:
            self.brainrot_count = kwargs["brainrot_count"]
        else:
            self.brainrot_count = {}
        
        if "my_id" in kwargs:
            self.my_id = int(kwargs["my_id"])
        else:
            self.my_id = None

    async def on_ready(self):
        print(f'We have logged in as {self.user.name}. ID: {self.user.id}')

    async def on_voice_state_update(self, member, before, after):
        
        if member.id != self.user.id and member.id == self.my_id:
            print(member.id)
            if member.voice is not None:
                print(member.guild.id)
                vc = await member.voice.channel.connect()
                self.connections.update({member.guild.id: vc})
            if member.voice is None:
                await self.connections[member.guild.id].disconnect()

    async def on_message(self, message: discord.Message):
        if message.author.id != self.user.id:
            x = message.content.split(' ')
            channel = message.channel
            for i in self.terms:

                matched = re.search(i, message.content, re.IGNORECASE)
                if matched:
                    self.brainrot_count[message.author.id] = self.brainrot_count.get(message.author.id, 0) + 1
                    await channel.send(f"🚨brainrot term found🚨 '{matched.group(0)}' typed by @{message.author.name}  number of brainrot: {self.brainrot_count[message.author.id]}", )
                    with open("saved_brainrot.pkl", 'wb') as f:
                        pickle.dump(self.brainrot_count, f)
                    

            
        # # bot joins/leaves a voice channel on user join/leaving
        # channel = before.channel or after.channel

        # if before.channel is None and after.channel is not None:
        #     await self.join(channel)
        #     print(type(channel))

        # if before.channel is not None and after.channel is None:
        #     await self.leave()

