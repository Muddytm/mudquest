"""Gamestate wherein you choose to save or load a file."""


import discord
import enemies
import json


def make_enemy(enemy, data):
    """Populate enemy dict with enemy data."""
    data["enemy"] = {}
    data["enemy"]["name"] = enemy.name
    data["enemy"]["description"] = enemy.description
    data["enemy"]["HP"] = enemy.HP


async def main(client, message, data):
    """Hub of actions for turn-based battle."""
    if "enemy" not in data:
        make_enemy(enemies.Skellyton, data)

    if "enemy" in data:
        if message.content == "name":
            await client.send_message(message.channel, data["enemy"]["name"])
        elif message.content == "description"
            await client.send_message(message.channel,
                                      data["enemy"]["description"])
        elif message.content == "HP"
            await client.send_message(message.channel, str(data["enemy"]["HP"]))
