"""Gamestate wherein you choose to save or load a file."""

import discord
import json


class Menu:

    async def main(self, Game, client, message):
        """Hub of actions for new_or_load gamestate."""

        msg = message.content

        # !mudrpg new
        if msg == "new":
            Game.state = "battle"
            Game.name = message.author.name
            Game.path = "simpleton"

            await client.send_message(message.channel, "Your class is: simpleton")

        # !mudrpg load
        elif msg == "load":
            await client.send_message(message.channel, "ERROR ERROR BEEP BOOP")
