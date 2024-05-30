import json

try:
    with open('match_data.json', 'r') as file:
        data = json.load(file)

    round_data = data.get("gameRounds")
    if round_data:
        for round_info in round_data:
            rounds = round_info.get("roundNum")
            for kill_info in round_info.get("kills", []):
                attacker_name = kill_info.get("attackerName")
                victim_name = kill_info.get("victimName")
                weapon = kill_info.get("weapon")
                print(f'Round: {rounds}, Attacker: {attacker_name}, Victim: {victim_name}, Weapon: {weapon}')

except FileNotFoundError:
    print("The file 'match_data.json' was not found.")
except json.JSONDecodeError:
    print("Error decoding JSON. Ensure the file contains valid JSON.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
