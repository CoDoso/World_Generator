import Unit_templates as Unit
import random
import json
import os


def create_points(Settings: dict):
    x: int = 0
    y: int = 1

    points: list = []
    Remaining_Wonders: list = Settings["Terrain"]["Wonders"]

    for i in range(Settings["Grid"]["x"] * Settings["Grid"]["y"]):
        # Location & ID Calculation
        i += 1
        if x < Settings["Grid"]["x"]:
            x += 1
        else:
            x = 1
            y += 1
        SubGridLocation: int = random.randint(1, 9)

        # Biome Assigning
        if True:
            # Biome
            Grassland_Chance: int = 30
            Forest_Chance: int = 40  # Base Chances
            Sand_Chance: int = 35
            New_Biome: str = ""
            # Elevation
            Flat_Chance: float = 17.5 * 2
            Hills_Chance: float = 22.5 * 2
            Steep_Chance: float = 20 * 2  # Base Chances
            Water_Chance: float = 25 * 2
            Uninhabitable_Chance: float = 15 * 2
            New_Elevation: str = ""
            TerrainName: str = "NoWater"
            Connections: list = []
            Wonders: list = []

            for item in points:
                # Neighboring point directly North
                if item['Point']['Coordinates']['y'] == y - 1 and item['Point']['Coordinates']['x'] == x:
                    Connections.append(item['Point']['Point_ID'])

                # Neighboring point directly to the West
                if item['Point']['Coordinates']['x'] == x - 1 and item['Point']['Coordinates']['y'] == y:
                    Connections.append(item['Point']['Point_ID'])

                # Adjust chances based on neighboring points
                if item['Point']['Coordinates']['y'] == y - 1 or item['Point']['Coordinates']['x'] == x - 1:
                    if item['Point']['Terrain']['Biome'] == "Grassland":
                        Grassland_Chance += 10
                        Forest_Chance -= 5
                        Sand_Chance -= 5
                    elif item['Point']['Terrain']['Biome'] == "Forest":
                        Grassland_Chance -= 5
                        Forest_Chance += 15
                        Sand_Chance -= 10
                    elif item['Point']['Terrain']['Biome'] == "Sand":
                        Grassland_Chance -= 5
                        Forest_Chance -= 5
                        Sand_Chance += 10

                    if item['Point']['Terrain']['Elevation'] == "Flat":
                        Flat_Chance += 5
                        Hills_Chance += 7.5
                        Steep_Chance -= 20
                        Water_Chance += 7.5
                    elif item['Point']['Terrain']['Elevation'] == "Hills":
                        Flat_Chance += 5
                        Hills_Chance += 12.5
                        Steep_Chance += 7.5
                        Water_Chance -= 20
                        Uninhabitable_Chance -= 5
                    elif item['Point']['Terrain']['Elevation'] == "Steep":
                        Flat_Chance -= 30
                        Hills_Chance += 20
                        Steep_Chance += 20
                        Water_Chance -= 10
                    elif item['Point']['Terrain']['Elevation'] == "Water":
                        Flat_Chance += 10
                        Hills_Chance -= 15
                        Steep_Chance -= 20
                        Water_Chance += 30
                        Uninhabitable_Chance -= 5
                        TerrainName = "River"
                    elif item['Point']['Terrain']['Elevation'] == "Uninhabitable":
                        Uninhabitable_Chance += 5
                        Sand_Chance += 5
                        Grassland_Chance += 5
                        Forest_Chance -= 10
                        Water_Chance -= 5

            # Ensures there's no negative chances
            Grassland_Chance = max(Grassland_Chance, 0)
            Forest_Chance = max(Forest_Chance, 0)
            Sand_Chance = max(Sand_Chance, 0)
            Flat_Chance = max(Flat_Chance, 0)
            Hills_Chance = max(Hills_Chance, 0)
            Steep_Chance = max(Steep_Chance, 0)
            Water_Chance = max(Water_Chance, 0)
            Uninhabitable_Chance = max(Uninhabitable_Chance, 0)

            Biome_Chance = random.randint(1, Sand_Chance + Forest_Chance + Grassland_Chance)
            Elevation_Chance = random.randint(1,
                                              int(Uninhabitable_Chance + Water_Chance + Steep_Chance + Hills_Chance + Flat_Chance))

            if (Biome_Chance / 2) < Grassland_Chance:
                New_Biome = Settings["Terrain"]["Biomes"][0]
            elif (Biome_Chance / 2) < Forest_Chance + Grassland_Chance:
                New_Biome = Settings["Terrain"]["Biomes"][1]
            elif (Biome_Chance / 2) < Sand_Chance + Forest_Chance + Grassland_Chance:
                New_Biome = Settings["Terrain"]["Biomes"][2]

            if Elevation_Chance < Flat_Chance:  # This assigns the Biome and Elevation
                New_Elevation = Settings["Terrain"]["Elevations"][0]
            elif Elevation_Chance < Hills_Chance + Flat_Chance:
                New_Elevation = Settings["Terrain"]["Elevations"][1]
                if random.randint(0, 20) == 10:
                    for Wonder in Remaining_Wonders:
                        if Wonder == {"High Hills": {"Type": "Military", "Modifier": "ToDo [Local] Fort Level +1"}}:
                            Wonders.append(Wonder)
                            Remaining_Wonders.remove(Wonder)  # Great Falls Monument(Wonder) creation
                            print(f"High Hills ID: {i}")
            elif Elevation_Chance < Steep_Chance + Hills_Chance + Flat_Chance:
                New_Elevation = Settings["Terrain"]["Elevations"][2]
            elif Elevation_Chance < Water_Chance + Steep_Chance + Hills_Chance + Flat_Chance:
                New_Elevation = Settings["Terrain"]["Elevations"][3]
                if TerrainName != "River":
                    TerrainName = "Source"
            elif Elevation_Chance < Uninhabitable_Chance + Water_Chance + Steep_Chance + Hills_Chance + Flat_Chance:
                New_Elevation = Settings["Terrain"]["Elevations"][4]
            else:
                New_Elevation = Settings["Terrain"]["Elevations"][random.randint(0, 4)]
                New_Biome = Settings["Terrain"]["Biomes"][random.randint(0, 2)]

            if (New_Elevation == "Steep" or New_Elevation != "Water") and TerrainName == "River":
                if New_Elevation == "Steep":
                    TerrainName = "Waterfall"
                    if random.randint(0, 20) == 10:
                        for Wonder in Remaining_Wonders:
                            if Wonder == {
                                "Great Falls": {"Type": "Symbolic", "Modifier": "ToDo [Faction] Prestige +10"}}:
                                Wonders.append(Wonder)
                                Remaining_Wonders.remove(Wonder)  # Great Falls Monument(Wonder) creation
                                print(f"Great Falls ID: {i}")
                else:
                    TerrainName = "NoWater"
        # Resource Calculations
        if True:
            # Ores
            if True:
                Chance = random.randint(1, 10)
                Iron: int = 0
                Coal: int = 0
                Copper: int = 0
                Tin: int = 0
                # Iron & Coal
                if True:
                    # Iron
                    IronValues = [random.randint(1, 10)]
                    while True:
                        New_Value = random.randint(1, 10)
                        if New_Value not in IronValues:  # 20%
                            IronValues.append(New_Value)
                        if len(IronValues) == 2:
                            break

                    if Chance in IronValues:
                        Iron += random.randint(5, 25)
                    # Coal
                    CoalValues = [random.randint(1, 10)]
                    while True:
                        New_Value = random.randint(1, 10)
                        if New_Value not in CoalValues:  # 30%
                            CoalValues.append(New_Value)
                        if len(CoalValues) == 3:
                            break
                    if Chance in CoalValues:
                        Coal += random.randint(6, 25)

                # Copper & Tin
                if Iron == 0 and Coal == 0:
                    # Copper
                    CopperValues = [random.randint(1, 10)]
                    while True:
                        New_Value = random.randint(1, 10)
                        if New_Value not in CopperValues:  # 30% (2x Chance because of the 50% for Iron or Coal)
                            CopperValues.append(New_Value)  # If my math is not mathing lmk pls
                        if len(CopperValues) == 6:
                            break
                    if Chance in CopperValues:
                        Copper += random.randint(5, 25)
                    # Tin
                    TinValues = [random.randint(1, 10)]
                    while True:
                        New_Value = random.randint(1, 10)
                        if New_Value not in TinValues:  # 20% (2x Chance because of the 50% for Iron or Coal)
                            TinValues.append(New_Value)
                        if len(TinValues) == 4:
                            break
                    if Chance in TinValues:
                        Tin += random.randint(6, 25)

            Score: int = 0
            Fertile_Land: int = 0
            Forestry_Land: int = 0
            Wild_Hunt: int = 0
            Berrys: int = 0  # Base Values
            Mushrooms: int = 0  # This is for convenience
            Mana_Crystals: int = 0  # (If you want a game were every province has Gold this makes it possible)
            Gems: int = 0
            Gold: int = 0

            Chance: int = random.randint(1, 100)

            # Gold
            GoldValues = [random.randint(1, 100)]
            while True:
                New_Value = random.randint(1, 10)
                if New_Value not in GoldValues:  # 20%
                    GoldValues.append(New_Value)
                if len(GoldValues) == 3:
                    break
            if Chance in GoldValues:
                Gold += random.randint(1, 10)

            match New_Biome:
                case "Grassland":
                    Score += 3
                    Fertile_Land += random.randint(10, 30)
                    Wild_Hunt += random.randint(3, 15)
                    Berrys += random.randint(1, 10)
                case "Forest":
                    Score += 2
                    Forestry_Land += random.randint(10, 30)  # The Resource Generation
                    Wild_Hunt += random.randint(3, 20)
                    Berrys += random.randint(1, 15)
                    Mushrooms += random.randint(2, 10)
                case "Sand":
                    Score += 1
                    if New_Elevation == "Water":
                        if random.randint(0, 20) == 10:
                            for Wonder in Remaining_Wonders:
                                if Wonder == {"Desert Floodplains": {"Type": "Economic",
                                                                     "Modifier": "ToDo [Local] +15 Fertile Lands"}}:
                                    Wonders.append(Wonder)
                                    Remaining_Wonders.remove(Wonder)  # Desert Floodplains creation
                                    print(f"Desert Floodplains ID: {i}")

            match New_Elevation:
                case "Flat":
                    Score += 5
                case "Hills":
                    Score += 3
                case "Steep":
                    Score += 1
                    # Mana Crystals
                    ManaValues = [random.randint(1, 100)]
                    while True:
                        New_Value = random.randint(1, 10)
                        if New_Value not in ManaValues:  # 20%
                            ManaValues.append(New_Value)
                        if len(ManaValues) == 5:
                            break
                    if Chance in ManaValues:
                        Mana_Crystals += random.randint(1, 10)
                    # Gems
                    GemsValues = [random.randint(1, 100)]
                    while True:
                        New_Value = random.randint(1, 10)
                        if New_Value not in GemsValues:  # 20%
                            GemsValues.append(New_Value)
                        if len(GemsValues) == 8:
                            break
                    if Chance in GemsValues:
                        Gems += random.randint(1, 5)
                case "Water":
                    Score += 5
                    # River Gold
                    if TerrainName == "River":
                        GoldValues = [random.randint(1, 100)]
                        while True:
                            New_Value = random.randint(1, 10)
                            if New_Value not in GoldValues:  # 20%
                                GoldValues.append(New_Value)
                            if len(GoldValues) == 3:
                                break
                        if Chance in GoldValues:
                            Gold += random.randint(1, 10)

        if New_Elevation == "Uninhabitable":
            # These Points are too hostile for life to inhabit the land
            # Lore wise these Places are remanence of Ancient Battles that drenched the Land in
            # blood and despair.
            # Unlike Mountains or Oceans these are however passable
            # They are also very easy to defend (through Defender Bonuses unique to this terrain)
            if random.randint(0, 25) == 10:
                for Wonder in Remaining_Wonders:
                    if Wonder == {"Volcano Field": {"Type": "Symbolic",
                                                    "Modifier": "ToDo [Both] Allow Volcano Eruption Event & *2 Attrition"}}:
                        Wonders.append(Wonder)
                        Score = int(Score / 2)
                        Remaining_Wonders.remove(Wonder)  # Volcano Field Wonder creation
                        print(f"Volcano Field ID: {i}")

            New_Point = {
                "Point": {
                    "Point_ID": i,
                    "Connections": Connections,
                    "Coordinates": {  # These coordinates are calculable and are a
                        "x": x,  # way to reduce the size of the Data recorded
                        "y": y,  # If we however change World-Gen all previous games will be lost
                        "SubGrid_Location": SubGridLocation
                    },
                    "Terrain": {
                        "TerrainName": TerrainName,
                        "Biome": New_Biome,
                        "Elevation": New_Elevation,
                        "Army Limit": Score * 20  # Grassland = 60, Forest = 40, Sand = 20
                        # If the Army on this Point is larger than the Limit the Army will start taking Damage
                        # every single turn called "Attrition" inspiration EU4
                    },
                    # The difference between Wonders and Buildings is Wonders
                    # are based on Terrain and get destroyed if those change
                    "Wonders": Wonders,
                }
            }
        else:
            Resources = [{"Building Slots": 5 * Score}]
            Resource_List = ["Fertility", "Forestry", "Iron", "Coal", "Copper", "Tin", "Wild Hunt", "Berrys",
                             "Mushrooms", "Mana Crystals", "Gems", "Gold"]
            for rs in Resource_List:
                match rs:  # This is to check if the Resource exists in that Point
                    case "Fertility":
                        if Fertile_Land != 0:
                            Resources.append({"Fertile Land": Fertile_Land})
                    case "Forestry":
                        if Forestry_Land != 0:
                            Resources.append({"Forestry Land": Forestry_Land})
                    case "Iron":  # and if not don't put it into the Data
                        if Iron != 0:
                            if random.randint(0, int(Settings["Grid"]["x"] * Settings["Grid"]["y"] * 0.085)) == 5:
                                for Wonder in Remaining_Wonders:
                                    if Wonder == {
                                        "Great Iron Deposit": {"Type": "Economic", "Modifier": "[Local] +30 Iron"}}:
                                        Wonders.append(Wonder)
                                        Iron += 30
                                        Remaining_Wonders.remove(Wonder)
                                        print(f"Great Iron Deposit ID: {i}")
                            Resources.append({"Iron": Iron})
                    case "Coal":
                        if Coal != 0:
                            if random.randint(0, int(Settings["Grid"]["x"] * Settings["Grid"]["y"] * 0.085)) == 5:
                                for Wonder in Remaining_Wonders:
                                    if Wonder == {
                                        "Great Coal Deposit": {"Type": "Economic", "Modifier": "[Local] +30 Coal"}}:
                                        Wonders.append(Wonder)
                                        Coal += 30
                                        Remaining_Wonders.remove(Wonder)
                                        print(f"Great Coal Deposit ID: {i}")
                            if New_Biome == "Sand" and random.randint(0, int(
                                    Settings["Grid"]["x"] * Settings["Grid"]["y"] * 0.085)) == 5:
                                for Wonder in Remaining_Wonders:
                                    if Wonder == {
                                        "Senlows Coal Deposit": {"Type": "Economic", "Modifier": "[Local] +50 Coal"}}:
                                        Wonders.append(Wonder)
                                        Coal += 50
                                        Remaining_Wonders.remove(Wonder)
                                        print(f"Senlows Coal Deposit ID: {i}")
                            Resources.append({"Coal": Coal})
                    case "Copper":
                        if Copper != 0 and {"Bronze Mountain": {"Type": "Economic",
                                                                "Modifier": "[Local] +40 Copper & Tin"}} not in Wonders:
                            if random.randint(0, int(Settings["Grid"]["x"] * Settings["Grid"]["y"] * 0.085)) == 5:
                                for Wonder in Remaining_Wonders:
                                    if Wonder == {
                                        "Great Copper Deposit": {"Type": "Economic", "Modifier": "[Local] +30 Copper"}}:
                                        Wonders.append(Wonder)
                                        Copper += 30
                                        Remaining_Wonders.remove(Wonder)
                                        print(f"Great Copper Deposit ID: {i}")
                                        Resources.append({"Copper": Copper})
                            elif random.randint(0, 20) == 5 and Tin != 0:
                                for Wonder in Remaining_Wonders:
                                    if Wonder == {
                                        "Bronze Mountain": {"Type": "Economic", "Modifier": "[Local] +40 Copper&Tin"}}:
                                        Wonders.append(Wonder)
                                        Remaining_Wonders.remove(Wonder)
                                        Copper += 40
                                        Tin += 40
                                        print(f"Bronze Mountain ID: {i}")
                                        Resources.append({"Copper": Copper})
                            else:
                                Resources.append({"Copper": Copper})
                    case "Tin":
                        if Tin != 0 and {"Bronze Mountain": {"Type": "Economic",
                                                             "Modifier": "[Local] +40 Copper & Tin"}} not in Wonders:
                            if random.randint(0, int(Settings["Grid"]["x"] * Settings["Grid"]["y"] * 0.085)) == 5:
                                for Wonder in Remaining_Wonders:
                                    if Wonder == {
                                        "Great Tin Deposit": {"Type": "Economic", "Modifier": "ToDo [Local] +30 Tin"}}:
                                        Wonders.append(Wonder)
                                        Tin += 30
                                        Remaining_Wonders.remove(Wonder)
                                        print(f"Great Tin Deposit ID: {i}")
                            Resources.append({"Tin": Tin})

                    case "Wild Hunt":
                        if Wild_Hunt != 0:
                            Resources.append({"Wild Hunt": Wild_Hunt})
                    case "Berrys":
                        if Berrys != 0:
                            Resources.append({"Berrys": Berrys})
                    case "Mushrooms":
                        if Mushrooms != 0:
                            Resources.append({"Mushrooms": Mushrooms})
                    case "Mana Crystals":
                        if Mana_Crystals != 0:
                            Resources.append({"Mana Crystals": Mana_Crystals})
                    case "Gems":
                        if Gems != 0:
                            Resources.append({"Gems": Gems})
                    case "Gold":
                        if Gold != 0:
                            Resources.append({"Gold": Gold})

            New_Point = {
                "Point": {
                    "Point_ID": i,
                    "Connections": Connections,
                    "Coordinates": {  # These coordinates are calculable and are a
                        "x": x,  # way to reduce the size of the Data recorded
                        "y": y,  # If we however change World-Gen all previous games will be lost
                        "SubGrid_Location": SubGridLocation,
                    },
                    "Terrain": {
                        "Biome": New_Biome,
                        "Elevation": New_Elevation,
                        "TerrainName": TerrainName
                    },
                    "Resources": Resources,
                    "Wonders": Wonders,  # are based on Terrain and get destroyed if those change
                }
            }
        points.append(New_Point)

    return points


def create_factions(Settings: dict):
    factions: list = []
    armys: list = []

    New_Race: str = ""
    Name: str = ""
    New_Capital: list = [0, 0]
    List_of_Capitals: list = []
    List_of_Races: list = []
    Faction_Units: list = []
    Behavior: str = ""

    Allowed_Races_count: int = int(Settings["Factions"]["Faction_amount"] / 3)  # 16 Faction = 5 Races (Small World)

    def create_Army(Owner_ID: int, x: int, y: int, Type: str, Units: list, Armys_len: int):
        Army = {
            "Army": {
                "Type": Type,
                "Army_ID": Armys_len + 1,
                "Owner_ID": Owner_ID,
                "Coordinates": {"x": x, "y": y},
                "Units": Units,
                "Stats": {
                    "Morale": Unit.Army_Morale,
                    "Efficiency": Unit.Army_Efficiency,
                    "Experience": Unit.Army_Experience,
                    "Exp. Decay": Unit.Army_EXP_Decay,
                }
            }
        }
        return Army

    for i in range(1, Settings["Factions"]["Faction_amount"] + 1):
        New_Capital: list = [int(random.randint(1, Settings["Grid"]["x"])),
                             int(random.randint(1, Settings["Grid"]["y"]))]
        while New_Capital in List_of_Capitals:
            New_Capital: list = [int(random.randint(1, Settings["Grid"]["x"])),
                                 int(random.randint(1, Settings["Grid"]["y"]))]

        New_Race = Settings["Factions"]["Races"][random.randint(0, len(Settings["Factions"]["Races"]) - 1)]
        if New_Race not in List_of_Races:
            if len(List_of_Races) == Allowed_Races_count:
                New_Race = List_of_Races[random.randint(0, len(List_of_Races) - 1)]
            else:
                List_of_Races.append(New_Race)

        match New_Race:
            case "Human":
                Behavior = ["Economic", "Expansionist", "Innovative"][random.randint(0, 2)]
                Faction_Units = [Unit.Human_Knight, Unit.Human_Archer, Unit.Human_Mage, Unit.Human_Cavalry]
                armys.append(
                    create_Army(i, New_Capital[0], New_Capital[1], "Combat", [[4, Unit.Levy], [3, Faction_Units[1]]],
                                len(armys)))  # 4 Levy, 3 Archer | Upkeep: 8)
            case "Elf":
                Behavior = "Diplomatic"
                Faction_Units = [Unit.Elven_Knight, Unit.Elven_Archer, Unit.Elven_Mage, Unit.Elven_Cavalry]
                armys.append(create_Army(i, New_Capital[0], New_Capital[1], "Combat",
                                         [[1, Faction_Units[0]], [2, Faction_Units[1]], [1, Faction_Units[3]]],
                                         len(armys)))  # 1 Knight, 2 Archer, 1 Cavalry | Upkeep: 8
            case "Dwarf":
                Behavior = "Economic"
                Faction_Units = [Unit.Dwarven_Knight, Unit.Dwarven_Archer, Unit.Dwarven_Mage, Unit.Dwarven_Cavalry]
                armys.append(
                    create_Army(i, New_Capital[0], New_Capital[1], "Combat", [[2, Unit.Levy], [1, Faction_Units[1]]],
                                len(armys)))  # 2 Levy, 1 Archer | Upkeep: 8
            case "Orc":
                Behavior = "Militaristic"
                Faction_Units = [Unit.Orc_Knight, Unit.Orc_Archer, Unit.Orc_Mage, Unit.Orc_Cavalry]
                armys.append(create_Army(i, New_Capital[0], New_Capital[1], "Combat",
                                         [[2, Faction_Units[0]], [1, Faction_Units[1]]],
                                         len(armys)))  # 2 Knights, 1 Archer | Upkeep: 10
            case "Fallen":
                Behavior = "Expansionist"
                Faction_Units = [Unit.Fallen_Knight, Unit.Fallen_Archer, Unit.Fallen_Mage, Unit.Fallen_Cavalry]
                armys.append(create_Army(i, New_Capital[0], New_Capital[1], "Combat",
                                         [[1, Faction_Units[2]], [1, Faction_Units[3]]],
                                         len(armys)))  # 1 Mage, 1 Cavalry | Upkeep: 8

        if i == 1:
            Behavior = "Player"

        Faction = {
            "Faction": {
                "Details": {
                    "Name": Name,
                    "ID": i,
                    "Race": New_Race,
                    "Behavior": Behavior,
                    "Units": Faction_Units,
                    "Capital": [New_Capital[0], New_Capital[1]]
                },
                "Modifiers": {
                    "Tech_IDs": [],
                    "Temporary": [],  # Modifier + Turns left
                    "Stats": []  # to safe Lines every Modifier that isn't in here is the Worlds default Value
                }
            }
        }
        factions.append(Faction)
        armys.append(create_Army(i, New_Capital[0], New_Capital[1], "Scout", [[1, Unit.Scout]], len(armys)))

    return [factions, armys]


def base_world_settings():
    return {
            "Grid": {
                "x": int(input("Insert X size for the World size: ")),
                "y": int(input("Insert Y size for the World size: "))
            },
            "Terrain": {
                "Biomes": ["Grassland", "Forest", "Sand"],
                "Elevations": ["Flat", "Hills", "Steep", "Water", "Uninhabitable"],
                "Wonders": [{"High Hills": {"Type": "Military", "Modifier": "ToDo [Local] Fort Level +1"}},
                            {"Great Falls": {"Type": "Symbolic", "Modifier": "ToDo [Faction] Prestige +10"}},
                            {"Volcano Field": {"Type": "Symbolic", "Modifier": "ToDo [Both] Allow Volcano Eruption Event & *2 Attrition"}},
                            {"Bronze Mountain": {"Type": "Economic", "Modifier": "ToDo [Local] +40 Copper&Tin"}},
                            {"Desert Floodplains": {"Type": "Economic", "Modifier": "ToDo [Local] +15 Fertile Lands"}},
                            {"Senlows Coal Deposit": {"Type": "Economic", "Modifier": "ToDo [Local] +50 Coal"}},
                            {"Great Iron Deposit": {"Type": "Economic", "Modifier": "ToDo [Local] +30 Iron"}},
                            {"Great Coal Deposit": {"Type": "Economic", "Modifier": "ToDo [Local] +30 Coal"}},
                            {"Great Copper Deposit": {"Type": "Economic", "Modifier": "ToDo [Local] +30 Copper"}},
                            {"Great Tin Deposit": {"Type": "Economic", "Modifier": "ToDo [Local] +30 Tin"}}],
                "Options": {
                    "Natural_Buildings": False,
                    "Mountains": False,
                    "Oceans": False
                }
            },
            "Factions": {
                "Races": ["Human", "Elf", "Dwarf", "Orc", "Fallen"],
                "Faction_amount": int(input("Amount of Factions at Gamestart: ")),
            }
    }


File_Name = str(input('Insert File Name: '))

while File_Name.startswith("bfo-"):
    File_Name = File_Name[4:]

file_num = 1
while os.path.exists(f"saves/{File_Name}.json"):
    if File_Name.endswith(f"({file_num})"):
        File_Name = File_Name[:-3]
    file_num += 1
    File_Name = f"{File_Name}({file_num})"
    print(File_Name)

with open(f"safes/bfo-{File_Name}.json", 'w') as f:  # bfo-World == build file of "World"
    json.dump(base_world_settings(), f)

with open(f"safes/bfo-{File_Name}.json", 'r') as file:
    build_data = json.load(file)

Points = create_points(build_data)
Factions_and_Armys = create_factions(build_data)

with open(f"safes/{File_Name}.json", 'w') as data:
    json.dump({"Settings": [], "Factions": Factions_and_Armys[0], "Armys": Factions_and_Armys[1], "Points": Points, "Citys": ""}, data, )

os.remove(f"safes/bfo-{File_Name}.json")
