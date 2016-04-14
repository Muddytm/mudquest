"""Gamestate wherein you choose to save or load a file."""

import discord
import json


async def main(client, message, data):
    """Hub of actions for new_or_load gamestate."""

    # !mudrpg new
    if msg == "new":
        data["gamestate"] = "battle"
        with open("mudrpg/game_data.json", "w+") as file:
            json.dump(data, file)

        data["session"][message.author.name]
        await client.send_message(message.channel, "Your class is: simpleton")

    # !mudrpg load
    elif msg == "load":
        pass
