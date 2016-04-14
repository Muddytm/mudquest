import discord
import json

import new_or_load


def welcome():
    return ("Welcome to MudRPG! Type \"!mudrpg new\" to start a new session, "
            " \"!mudrpg load\" to continue, or \"!mudrpg exit\" to exit.")


def goodbye():
    return ("MudRPG session has ended. Buh-bye!")


async def run(client, message):
    """Hub of actions for MudRPG."""
    msg = message.content.replace("!mudrpg", "").strip()
    data_loc = "mudrpg/game_data.json"

    data = json.load(open(data_loc, "r"))

    # !mudrpg start
    if msg == "start" and not data["running"]:
        await client.send_message(message.channel, welcome())

        data["running"] = True
        with open(data_loc, "w+") as file:
            json.dump(data, file)

    if data["running"]:
        # !mudrpg end
        if msg == "exit":
            await client.send_message(message.channel, goodbye())

            data["running"] = False
            with open(data_loc, "w+") as file:
                json.dump(data, file)

        if data["gamestate"] == "new_or_load":
            new_or_load.main(client, message, data)
