import discord
import json

from mudquest.Battle import Battle
from mudquest.Menu import Menu


class Game:

    def __init__(self):
        self.state = "menu"
        self.running = False
        self.name = None
        self.path = None
        self.enemy = {}
        self.hero = {}
        self.turn = None

    def welcome(self):
        return ("Welcome to MudQuest! Type \"new\" to start a new session, "
                " \"load\" to continue, or \"exit\" to exit.")

    def goodbye(self):
        return ("MudQuest session has ended. Buh-bye!")

    async def run(self, client, message):
        """Hub of actions for MudQuest."""
        msg = message.content

        if not self.running and msg == "start":
            await client.send_message(message.channel, self.welcome())
            self.running = True

        if self.running:
            if msg == "exit":
                await client.send_message(message.channel, self.goodbye())
                self.running = False
                return

            if self.state == "menu":
                await Menu().main(self, client, message)

            if self.state == "battle":
                await Battle().main(self, client, message)
