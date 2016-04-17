"""Class for a simpleton character class."""


class Simpleton:

    def __init__(self):
        self.name = "Simpleton"
        self.description = ("Simpletons hail from Simpleville, a place where "
                            "nothing of note has even been accomplished and "
                            "where originality is nonexistant.")
        self.HP = 20

    def act(self, action):
        """Perform an action.

        return: (text, damage, self_damage, self_heal, miss_chance)"""
        if action == "punch":
            text = ("You throw a punch!")
            damage = 5
            miss_chance = 25
            return [text, damage, None, None, miss_chance]
