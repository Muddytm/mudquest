"""Gamestate wherein you choose to save or load a file."""

import discord
import json


async def main(client, message, data):
    """Hub of actions for new_or_load gamestate."""

    msg = message.content.replace("!mudrpg", "").strip()

    # !mudrpg new
    if msg == "new":
        data["gamestate"] = "battle"
        data["session"]["name"] = message.author.name
        data["session"]["class"] = "simpleton"
        with open("mudrpg/game_data.json", "w+") as file:
            json.dump(data, file)

        await client.send_message(message.channel, "Your class is: simpleton")

    # !mudrpg load
    elif msg == "load":
        pass
