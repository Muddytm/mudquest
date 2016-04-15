"""Gamestate wherein you choose to save or load a file."""


import discord
from mudrpg.enemies.Skellyton import Skellyton
import json


def make_enemy(enemy, data):
    """Populate enemy dict with enemy data."""
    data["enemy"] = {}
    data["enemy"]["name"] = enemy.name
    data["enemy"]["description"] = enemy.description
    data["enemy"]["HP"] = enemy.HP


async def main(client, message, data):
    """Hub of actions for turn-based battle."""

    msg = message.content.replace("!mudrpg", "").strip()

    if "enemy" not in data:
        make_enemy(Skellyton(), data)

    if "enemy" in data:
        if msg == "name":
            await client.send_message(message.channel, data["enemy"]["name"])
        elif msg == "description":
            await client.send_message(message.channel,
                                      data["enemy"]["description"])
        elif msg == "HP":
            await client.send_message(message.channel, str(data["enemy"]["HP"]))
