from awpy import DemoParser
import json


class DemToJson:

    def __init__(self, demo_path):
        self.demo_path = demo_path

    def dem_to_json(self):
        parser = DemoParser(demofile=self.demo_path, parse_rate=128, parse_frames=True)
        data = parser.parse()
        with open("match_data1.json", "w") as file:
            json.dump(data, file, indent=4)
        return


demo_path = "/Users/vitaliy/Documents/demoscraper/faceitgames/natus-vincere-vs-outsiders-m2-inferno.dem"
dem_to_json_instance = DemToJson(demo_path)
dem_to_json_instance.dem_to_json()
