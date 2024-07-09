import Generator as Generator
import Data
import yaml
import os


if __name__ == "__main__":
    Generator.create_points()
    Generator.create_factions()
    if input("Compile?:  ") == "Y":

        Factions = []
        Points = []

        with open("factions.yml", 'r') as file:
            data = yaml.safe_load(file)
            for item in data:
                Factions.append(item)

        with open("points.yml", 'r') as file:
            data = yaml.safe_load(file)
            for item in data:
                Points.append(item)

        Game_Data = {
            "Factions": Factions,
            "Armys": "",
            "Points": Points,
            "Citys": ""
        }

        with open(f"safes/{str(input('Insert File Name: '))}.yml", 'w') as data:
            yaml.safe_dump(Game_Data, data, default_flow_style=False, sort_keys=False)

        os.remove("points.yml")
        os.remove("factions.yml")
