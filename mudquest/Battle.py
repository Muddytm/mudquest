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
        Game.enemy["death_text"] = enemy.death_text
        Game.enemy["HP"] = enemy.HP
        Game.enemy["moves"] = enemy.moves


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
            Game.turn = "hero"
            await client.send_message(message.channel,
                                      Game.enemy["battle_text"])

        if Game.hero == {}:
            self.make_hero(Simpleton(), Game)

        if Game.turn == "hero":
            if msg == "check":
                text = ("Studying the " + Game.enemy["name"] + "...")
                await client.send_message(message.channel, text)
                text = ("Name: " + Game.enemy["name"])
                await client.send_message(message.channel, text)
                text = ("Lore: " + Game.enemy["description"])
                await client.send_message(message.channel, text)
                text = ("HP: " + str(Game.enemy["HP"]))
                await client.send_message(message.channel, text)
                text = ("Moves: " + str(Game.enemy["moves"]))
                await client.send_message(message.channel, text)
            elif msg == "punch":
                ability_data = Simpleton().act("punch")
                await client.send_message(message.channel, ability_data[0])

                roll = random.randint(0, 99)
                if roll > ability_data[4]:
                    Game.enemy["HP"] -= ability_data[1]
                    dmg_text = (Game.enemy["name"] + " took "
                                "" + str(ability_data[1]) + " damage!")
                    hp_text = (Game.enemy["name"] + " now has "
                               "" + str(Game.enemy["HP"]) + " HP.")
                    await client.send_message(message.channel, dmg_text)
                    await client.send_message(message.channel, hp_text)
                else:
                    await client.send_message(message.channel, "...missed!")

            Game.turn = "enemy"

        if Game.turn == "enemy":
            roll = random.randint(0, 99)
            ability_data = Skellyton().act(roll)
            await client.send_message(message.channel, ability_data[0])

            if ability_data[1]:
                if ability_data[4]:
                    roll = random.randint(0, 99)
                    if roll > ability[4]:
                        Game.hero["HP"] -= ability_data[1]
                        dmg_text = (Game.name + " took "
                                    "" + str(ability_data[1]) + " damage!")
                        hp_text = (Game.name + " now has "
                                   "" + str(Game.hero["HP"]) + " HP.")
                        await client.send_message(message.channel, dmg_text)
                        await client.send_message(message.channel, hp_text)
            elif ability_data[2]:
                Game.enemy["HP"] -= ability_data[2]
                self_dmg_text = (Game.enemy["name"] + " took "
                                 "" + str(ability_data[2]) + " damage!")
                await client.send_message(message.channel, self_dmg_text)
            elif ability_data[3]:
                if ability_data[4]:
                    roll = random.randint(0, 99)
                    if roll > ability[4]:
                        Game.enemy["HP"] += ability_data[3]
                        heal_text = (Game.enemy["name"] + " healed for "
                                     "" + str(ability_data[3]) + " HP!")
                        await client.send_message(message.channel, heal_text)

        Game.turn = "hero"

        await client.send_message(message.channel, "" + Game.name + "\'s turn.")
