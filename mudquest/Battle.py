"""Gamestate wherein you choose to save or load a file."""


import discord
import json
import random
from mudquest.classes.Simpleton import Simpleton
from mudquest.enemies.Skellyton import Skellyton


class Battle:

    def make_enemy(self, enemy, Game):
        """Populate enemy dict with enemy data."""
        Game.enemy["name"] = enemy.name
        Game.enemy["description"] = enemy.description
        Game.enemy["battle_text"] = enemy.battle_text
        Game.enemy["HP"] = enemy.HP


    def make_hero(self, hero, Game):
        """Populate enemy dict with enemy data."""
        Game.hero["name"] = hero.name
        Game.hero["description"] = hero.description
        Game.hero["HP"] = hero.HP


    async def main(self, Game, client, message):
        """Hub of actions for turn-based battle."""

        msg = message.content

        if Game.enemy == {}:
            self.make_enemy(Skellyton(), Game)
            await client.send_message(message.channel,
                                      Game.enemy["battle_text"])

        if Game.hero == {}:
            self.make_hero(Simpleton(), Game)

        Game.turn = "hero"

        if Game.turn == "hero":
            if msg == "name":
                await client.send_message(message.channel, Game.enemy["name"])
            elif msg == "description":
                await client.send_message(message.channel,
                                          Game.enemy["description"])
            elif msg == "HP":
                await client.send_message(message.channel,
                                          str(Game.enemy["HP"]))
            elif msg == "punch":
                ability_data = Simpleton().act("punch")
                await client.send_message(message.channel, ability_data[0])

                rand = random.randint(0, 99)
                if rand > ability_data[4]:
                    Game.enemy["HP"] -= ability_data[1]
                    dmg_text = (Game.enemy["name"] + " took "
                                "" + str(ability_data[1]) + " damage!")
                    hp_text = (Game.enemy["name"] + " now has "
                               "" + str(Game.enemy["HP"]) + " HP.")
                    await client.send_message(message.channel, dmg_text)
                    await client.send_message(message.channel, hp_text)
