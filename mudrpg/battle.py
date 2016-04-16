"""Gamestate wherein you choose to save or load a file."""


import discord
import json
import random
from mudrpg.classes.Simpleton import Simpleton
from mudrpg.enemies.Skellyton import Skellyton


def make_enemy(enemy, data):
    """Populate enemy dict with enemy data."""
    data["enemy"] = {}
    data["enemy"]["name"] = enemy.name
    data["enemy"]["description"] = enemy.description
    data["enemy"]["battle_text"] = enemy.battle_text
    data["enemy"]["HP"] = enemy.HP


def make_hero(hero, data):
    """Populate enemy dict with enemy data."""
    data["hero"] = {}
    data["hero"]["name"] = hero.name
    data["hero"]["description"] = hero.description
    data["hero"]["HP"] = hero.HP


async def main(client, message, data):
    """Hub of actions for turn-based battle."""

    msg = message.content.replace("!mudrpg", "").strip()

    if "enemy" not in data:
        make_enemy(Skellyton(), data)
        await client.send_message(message.channel, data["enemy"]["battle_text"])

    if "hero" not in data:
        make_hero(Simpleton(), data)

    data["turn"] = "hero"

    if "enemy" in data and "hero" in data:
        if data["turn"] == "hero":
            if msg == "name":
                await client.send_message(message.channel, data["enemy"]["name"])
            elif msg == "description":
                await client.send_message(message.channel,
                                          data["enemy"]["description"])
            elif msg == "HP":
                await client.send_message(message.channel, str(data["enemy"]["HP"]))
            elif msg == "punch":
                ability_data = Simpleton().act("punch")
                await client.send_message(message.channel, ability_data[0])

                rand = random.randint(0, 99)
                if rand > ability_data[4]:
                    data["enemy"]["HP"] -= ability_data[1]
                    dmg_text = (data["enemy"]["name"] + " took "
                                "" + str(ability_data[1]) + " damage!")
                    hp_text = (data["enemy"]["name"] + " now has "
                               "" + data["enemy"]["HP"] + " HP.")
                    await client.send_message(message.channel, dmg_text)
                    await client.send_message(message.channel, hp_text)


    with open(data_loc, "w+") as file:
        json.dump(data, file)
