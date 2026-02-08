from ai_manager import generate_narrative

player_input = input("> ")

narrative = generate_narrative(player_input)
print(narrative)