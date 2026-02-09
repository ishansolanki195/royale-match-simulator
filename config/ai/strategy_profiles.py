class StrategyProfile:
    def __init__(self, name):
        self.name = name

    def get_playstyle(self):
        return self.name


AGGRESSIVE = StrategyProfile("aggressive")
DEFENSIVE = StrategyProfile("defensive")
BALANCED = StrategyProfile("balanced")
