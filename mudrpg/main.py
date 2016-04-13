import discord
import json


async def run(client, message):
    msg = message.content.replace("!mudrpg", "").strip()
    data_loc = "mudrpg/game_data.json"

    data = json.load(open(data_loc, "r"))

    if msg == "start" and not data["running"]:
        await client.send_message(message.channel, welcome())

        data["running"] = True
        with open(data_loc, "w+") as file:
            json.dump(data, file)
    elif msg == "end" and data["running"]:
        await client.send_message(message.channel, goodbye())

        data["running"] = False
        with open(data_loc, "w+") as file:
            json.dump(data, file)


def welcome():
    return ("Welcome to MudRPG! Type \"!mudrpg new\" to start a new session, or"
            " \"!mudrpg load\" to continue.")


def goodbye():
    return ("MudRPG session has ended. Buh-bye!")
