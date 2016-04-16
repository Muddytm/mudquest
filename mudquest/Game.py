import discord
import json

from mudrpg import battle
from mudrpg import new_or_load


class Game:

    def __init__(self):
        self.state = "menu"
        self.running = False
        self.name = None
        self.class = None
        self.enemy = {}
        self.hero = {}
        self.turn = None

    def welcome():
        return ("Welcome to MudQuest! Type \"new\" to start a new session, "
                " \"load\" to continue, or \"exit\" to exit.")

    def goodbye():
        return ("MudQuest session has ended. Buh-bye!")

    async def run(self, client, message):
        """Hub of actions for MudQuest."""
        msg = message.content

        if not self.running and msg == "start":
            await client.send_message(message.channel, welcome())
            self.running = True

        if self.running:
            if msg == "exit":
                await client.send_message(message.channel, goodbye())
                self.running = False
                return

            if self.state == "menu":
                await menu.main(self, client, message)

            if self.state == "battle":
                await battle.main(self, client, message)
