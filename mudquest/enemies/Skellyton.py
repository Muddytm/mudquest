"""Class for a skellyton enemy."""


class Skellyton:

    def __init__(self):
        self.name = "Skellyton"
        self.description = ("A common skellyton stereotype is that they are all"
                            " good at playing the flute. This is, of course, "
                            "false. They are excellent on the trombone, "
                            "however.")
        self.battle_text = ("You feel a spooky presence descend upon you..."
                            "a wild skellyton appears!")
        self.death_text = ("The skellyton whispers one last \"doot doot\" "
                           "before falling into a pile of bones. He\'s not "
                           "dead though...just unorganized for a bit.")
        self.HP = 20
        self.moves = ["Stare", "Bone Toss", "Super Mega Ultra Bone Toss",
                      "Boned-Aid"]

    def act(self, roll):
        """Perform an action based on random roll from 0 to 99.

        return: (text, damage, self_damage, self_heal, miss_chance)"""
        if roll < 20:
            text = ("The skellyton stares at you with eyes wide open. That "
                    "should be obvious, though. It\'s a skellyton.")
            damage = 0
            return [text, None, None, None, None]
        elif roll < 70:
            text = ("The skellyton throws a bone at you.")
            damage = 5
            miss_chance = 30
            return [text, damage, None, None, miss_chance]
        elif roll < 80:
            text = ("The skellyton tries to throw a bone at you but trips over "
                    "itself. Silly skellyton!")
            self_damage = 2
            return [text, None, self_damage, None, None]
        elif roll < 100:
            text = ("The skellyton sticks more bones to itself with duct tape.")
            self_heal = 4
            miss_chance = 10  # lol
            return [text, None, None, self_heal, miss_chance]
