import Generator as Generator
import json
import os


if __name__ == "__main__":
    Generator.create_points()
    Generator.create_factions()
    if input("Compile?:  ") == "Y":

        Factions = []
        Points = []
        Armys = []

        with open("factions.json", 'r') as file:
            for item in file:
                Factions.append(item)

        with open("points.json", 'r') as file:
            for item in file:
                Points.append(item)

        with open("armys.json", 'r') as file:
            for item in file:
                Armys.append(item)

        Game_Data = {
            "Factions": Factions,
            "Armys": Armys,
            "Points": Points,
            "Citys": ""
        }

        with open(f"safes/{str(input('Insert File Name: '))}.json", 'w') as data:
            json.dump(Game_Data, data)

        os.remove("points.json")
        os.remove("factions.json")
        os.remove("armys.json")
