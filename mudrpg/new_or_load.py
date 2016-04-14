"""Gamestate wherein you choose to save or load a file."""

import discord
import json


async def main(client, message, data):
    """Hub of actions for new_or_load gamestate."""

    # !mudrpg new
    if msg == "new":
        # TODO: put stuff here
        data["gamestate"] = "battle"
    elif msg == "load":
        pass
