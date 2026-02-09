from ai.decision_engine import DecisionEngine

def start_battle():
    engine = DecisionEngine()
    game_state = {
        "available_moves": ["attack", "defend", "wait"]
    }

    for turn in range(5):
        action = engine.decide(game_state)
        print(f"Turn {turn + 1}: AI chooses to {action}")
