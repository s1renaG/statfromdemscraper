import json
import pandas as pd

def get_attacker_data(json_file):
    try:
        with open(json_file, 'r') as file:
            data = json.load(file)
        attacker_data = []
        round_data = data.get("gameRounds")
        if round_data:
            for round_info in round_data:
                round_num = round_info.get("roundNum")
                for kill_info in round_info.get("kills", []):
                    attacker_name = kill_info.get("attackerName")
                    victim_name = kill_info.get("victimName")
                    weapon = kill_info.get("weapon")
                    attacker_data.append({
                        "round": round_num,
                        "attacker": attacker_name,
                        "victim": victim_name,
                        "weapon": weapon
                    })
        return attacker_data
    except FileNotFoundError:
        print("The file 'match_data.json' was not found.")
    except json.JSONDecodeError:
        print("Error decoding JSON. Ensure the file contains valid JSON.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


attacker_data = get_attacker_data('match_data.json')
if attacker_data:
    df = pd.DataFrame(attacker_data)
    df.to_csv('killfeed.csv', mode='w', index=False, header=False)
