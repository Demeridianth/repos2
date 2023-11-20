
class Elf:
    def __init__(self, level, ability_scores=None):
        self.level = level
        self.ability_scores = {
            'str': 11, 'dex': 12, 'con': 10,
            'int': 16, 'wis': 14, 'cha': 13
        } if ability_scores is None else ability_scores
        self.hp = 10 + self.ability_scores['con']