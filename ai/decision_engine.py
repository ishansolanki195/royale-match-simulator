import random
import time

class DecisionEngine:
    def decide(self, game_state):
        time.sleep(random.uniform(0.3, 1.0))
        return random.choice(game_state["available_moves"])
