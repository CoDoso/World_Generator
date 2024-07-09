import random
import yaml
import Gen_Values as Game


def create_points():
    x = 0
    y = 1

    for i in range(Game.worldsize):
        # Location & ID Calculation
        if True:
            i += 1
            if x < Game.worldsize_input_x:
                x += 1
            else:
                x = 1
                y += 1
            SubGridLocation = random.randint(1, 9)

        # Biome Assigning
        if True:

            # Biome
            Grassland_Chance = 30
            Forest_Chance = 40  # Base Chances
            Sand_Chance = 35
            New_Biome = ""

            # Elevation
            Flat_Chance = 17.5 * 2
            Hills_Chance = 22.5 * 2
            Steep_Chance = 20 * 2  # Base Chances
            Water_Chance = 25 * 2
            Uninhabitable_Chance = 15 * 2
            New_Elevation = ""
            Water_Status = "NoWater"
            Wonders = []

            for item in Game.points:
                if item['Point']['Coordinates']['y'] == y + 1:
                    if Game.worldsize_input_y / 3 < y < Game.worldsize_input_y / 2:
                        Grassland_Chance -= 10
                        Forest_Chance -= 20
                        Sand_Chance += 30
                    match item['Point']['Terrain']['Biome']:
                        case "Grassland":
                            Grassland_Chance += 10
                            Forest_Chance -= 5
                            Sand_Chance -= 5
                        case "Forest":
                            Grassland_Chance -= 5
                            Forest_Chance += 15
                            Sand_Chance -= 10
                        case "Sand":
                            if Game.worldsize_input_y / 3 < y < Game.worldsize_input_y / 2:
                                Grassland_Chance -= 30
                                Forest_Chance -= 40
                                Sand_Chance += 70
                            else:
                                Grassland_Chance -= 5
                                Forest_Chance -= 5
                                Sand_Chance += 10

                    match item['Point']['Terrain']['Elevation']:
                        case "Flat":
                            Flat_Chance += 5
                            Hills_Chance += 7.5
                            Steep_Chance -= 20
                            Water_Chance += 7.5
                        case "Hills":
                            Flat_Chance += 5
                            Hills_Chance += 12.5
                            Steep_Chance += 7.5
                            Water_Chance -= 20
                            Uninhabitable_Chance -= 5  # Chance Calculations for Terrain
                        case "Steep":
                            Flat_Chance -= 30
                            Hills_Chance += 20
                            Steep_Chance += 20
                            Water_Chance -= 10
                        case "Water":
                            Flat_Chance += 10
                            Hills_Chance -= 15
                            Steep_Chance -= 20
                            Water_Chance += 30
                            Uninhabitable_Chance -= 5
                            Water_Status = "River"
                        case "Uninhabitable":
                            Uninhabitable_Chance += 5
                            Sand_Chance += 5
                            Grassland_Chance += 5
                            Forest_Chance -= 10
                            Water_Chance -= 5

                if item['Point']['Coordinates']['x'] == x - 1:
                    match item['Point']['Terrain']['Biome']:
                        case "Grassland":
                            Grassland_Chance += 10
                            Forest_Chance -= 5
                            Sand_Chance -= 5
                        case "Forest":
                            Grassland_Chance -= 5
                            Forest_Chance += 15
                            Sand_Chance -= 10
                        case "Sand":
                            if Game.worldsize_input_y / 3 < y < Game.worldsize_input_y / 2:
                                Grassland_Chance -= 20
                                Forest_Chance -= 30
                                Sand_Chance += 50
                            else:
                                Grassland_Chance -= 5
                                Forest_Chance -= 5
                                Sand_Chance += 10
                    match item['Point']['Terrain']['Elevation']:
                        case "Flat":
                            Flat_Chance += 7.5
                            Steep_Chance -= 10
                            Water_Chance += 2.5
                        case "Hills":
                            Flat_Chance += 7.5
                            Hills_Chance += 10
                            Steep_Chance += 7.5
                            Water_Chance -= 20
                            Uninhabitable_Chance -= 5
                        case "Steep":
                            Flat_Chance -= 30
                            Hills_Chance += 20
                            Steep_Chance += 20
                            Water_Chance -= 10
                        case "Water":
                            Flat_Chance += 10
                            Hills_Chance -= 10
                            Steep_Chance -= 20
                            Water_Chance += 25
                            Uninhabitable_Chance -= 5
                            Water_Status = "River"
                        case "Uninhabitable":
                            Uninhabitable_Chance += 5
                            Sand_Chance += 5
                            Grassland_Chance += 5
                            Forest_Chance -= 10
                            Water_Chance -= 5

            if Grassland_Chance < 0:
                Grassland_Chance = 0
            if Forest_Chance < 0:
                Forest_Chance = 0
            if Sand_Chance < 0:
                Sand_Chance = 0

            if Flat_Chance < 0:  # This insures there's no negative Chance
                Flat_Chance = 0
            if Hills_Chance < 0:
                Hills_Chance = 0
            if Steep_Chance < 0:
                Steep_Chance = 0
            if Water_Chance < 0:
                Water_Chance = 0
            if Uninhabitable_Chance < 0:
                Uninhabitable_Chance = 0

            Biome_Chance = random.randint(1, Sand_Chance + Forest_Chance + Grassland_Chance)
            Elevation_Chance = random.randint(1,
                                              int(Uninhabitable_Chance + Water_Chance + Steep_Chance + Hills_Chance + Flat_Chance))

            if (Biome_Chance / 2) < Grassland_Chance:
                New_Biome = Game.Biomes[0]
            elif (Biome_Chance / 2) < Forest_Chance + Grassland_Chance:
                New_Biome = Game.Biomes[1]
            elif (Biome_Chance / 2) < Sand_Chance + Forest_Chance + Grassland_Chance:
                New_Biome = Game.Biomes[2]

            if Elevation_Chance < Flat_Chance:  # This assigns the Biome and Elevation
                New_Elevation = Game.Elevations[0]
            elif Elevation_Chance < Hills_Chance + Flat_Chance:  # ToDo: Wonders
                New_Elevation = Game.Elevations[1]
                if random.randint(0, 20) == 10:
                    for Wonder in Game.Remaining_Wonders:
                        if Wonder == {"High Hills": {"Type": "Military", "Modifier": "ToDo [Local] Fort Level +1"}}:
                            Wonders.append(Wonder)
                            Game.Remaining_Wonders.remove(Wonder)  # Great Falls Monument(Wonder) creation
                            print(f"High Hills ID: {i}")
            elif Elevation_Chance < Steep_Chance + Hills_Chance + Flat_Chance:
                New_Elevation = Game.Elevations[2]
            elif Elevation_Chance < Water_Chance + Steep_Chance + Hills_Chance + Flat_Chance:
                New_Elevation = Game.Elevations[3]
                if Water_Status != "River":
                    Water_Status = "Source"
            elif Elevation_Chance < Uninhabitable_Chance + Water_Chance + Steep_Chance + Hills_Chance + Flat_Chance:
                New_Elevation = Game.Elevations[4]
            else:
                New_Elevation = Game.Elevations[random.randint(0, 4)]
                New_Biome = Game.Biomes[random.randint(0, 2)]

            if (New_Elevation == "Steep" or New_Elevation != "Water") and Water_Status == "River":
                if New_Elevation == "Steep":
                    Water_Status = "Waterfall"
                    if random.randint(0, 20) == 10:
                        for Wonder in Game.Remaining_Wonders:
                            if Wonder == {
                                "Great Falls": {"Type": "Symbolic", "Modifier": "ToDo [Faction] Prestige +10"}}:
                                Wonders.append(Wonder)
                                Game.Remaining_Wonders.remove(Wonder)  # Great Falls Monument(Wonder) creation
                                print(f"Great Falls ID: {i}")
                else:
                    Water_Status = "NoWater"

        # Resource Calculations
        if True:

            # Ores
            if True:
                Chance = random.randint(1, 10)
                Iron = 0
                Coal = 0
                Copper = 0
                Tin = 0

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

            Score = 0
            Fertile_Land = 0
            Forestry_Land = 0
            Wild_Hunt = 0
            Berrys = 0  # Base Values
            Mushrooms = 0  # This is for convenience
            Mana_Crystals = 0  # (If you want a game were every province has Gold this makes it possible)
            Gems = 0
            Gold = 0

            Chance = random.randint(1, 100)

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
                            for Wonder in Game.Remaining_Wonders:
                                if Wonder == {"Desert Floodplains": {"Type": "Economic",
                                                                     "Modifier": "ToDo [Local] +15 Fertile Lands"}}:
                                    Wonders.append(Wonder)
                                    Game.Remaining_Wonders.remove(Wonder)  # Desert Floodplains creation
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
                    if Water_Status == "River":
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
                for Wonder in Game.Remaining_Wonders:
                    if Wonder == {"Volcano Field": {"Type": "Symbolic",
                                                    "Modifier": "ToDo [Both] Allow Volcano Eruption Event & *2 Attrition"}}:
                        Wonders.append(Wonder)
                        Score = int(Score / 2)
                        Game.Remaining_Wonders.remove(Wonder)  # Volcano Field Wonder creation
                        print(f"Volcano Field ID: {i}")

            New_Point = {
                "Point": {
                    "Point_ID": i,
                    "Coordinates": {  # These coordinates are calculable and are a
                        "x": x,  # way to reduce the size of the Data recorded
                        "y": y  # If we however change World-Gen all previous games will be lost
                        "SubGrid_Location": SubGridLocation
                    },
                    "Terrain": {
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
            Resources = [
                {"Building Slots": 5 * Score}
            ]

            Resource_List = ["Fertility", "Forestry", "Iron", "Coal", "Copper", "Tin", "Wild Hunt", "Berrys",
                             # This is for convenience
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
                            if random.randint(0, int(Game.worldsize * 0.085)) == 5:
                                for Wonder in Game.Remaining_Wonders:
                                    if Wonder == {"Great Iron Deposit": {"Type": "Economic",
                                                                         "Modifier": "ToDo [Local] +30 Iron"}}:
                                        Wonders.append(Wonder)
                                        Iron += 30
                                        Game.Remaining_Wonders.remove(Wonder)
                                        print(f"Great Iron Deposit ID: {i}")
                            Resources.append({"Iron": Iron})
                    case "Coal":
                        if Coal != 0:
                            if random.randint(0, int(Game.worldsize * 0.085)) == 5:
                                for Wonder in Game.Remaining_Wonders:
                                    if Wonder == {"Great Coal Deposit": {"Type": "Economic",
                                                                         "Modifier": "ToDo [Local] +30 Coal"}}:
                                        Wonders.append(Wonder)
                                        Coal += 30
                                        Game.Remaining_Wonders.remove(Wonder)
                                        print(f"Great Coal Deposit ID: {i}")
                            if New_Biome == "Sand" and random.randint(0, int(Game.worldsize * 0.085)) == 5:
                                for Wonder in Game.Remaining_Wonders:
                                    if Wonder == {"Senlows Coal Deposit": {"Type": "Economic",
                                                                           "Modifier": "ToDo [Local] +50 Coal"}}:
                                        Wonders.append(Wonder)
                                        Coal += 30
                                        Game.Remaining_Wonders.remove(Wonder)
                                        print(f"Senlows Coal Deposit ID: {i}")
                            Resources.append({"Coal": Coal})
                    case "Copper":
                        if Copper != 0:
                            if random.randint(0, int(Game.worldsize * 0.085)) == 5:
                                for Wonder in Game.Remaining_Wonders:
                                    if Wonder == {"Great Copper Deposit": {"Type": "Economic",
                                                                           "Modifier": "ToDo [Local] +30 Copper"}}:
                                        Wonders.append(Wonder)
                                        Copper += 30
                                        Game.Remaining_Wonders.remove(Wonder)
                                        print(f"Great Copper Deposit ID: {i}")
                                        Resources.append({"Copper": Copper})
                            elif random.randint(0, 20) == 5 and Tin != 0:
                                for Wonder in Game.Remaining_Wonders:
                                    if Wonder == {"Bronze Mountain": {"Type": "Economic",
                                                                      "Modifier": "ToDo [Local] +40 Copper&Tin"}}:
                                        Wonders.append(Wonder)
                                        Game.Remaining_Wonders.remove(Wonder)
                                        Copper += 40
                                        Tin += 40
                                        print(f"Bronze Mountain ID: {i}")
                                        Resources.append({"Copper": Copper})
                            else:
                                Resources.append({"Copper": Copper})
                    case "Tin":
                        if Tin != 0:
                            if random.randint(0, int(Game.worldsize * 0.085)) == 5:
                                for Wonder in Game.Remaining_Wonders:
                                    if Wonder == {"Bronze Mountain": {"Type": "Economic",
                                                                      "Modifier": "ToDo [Local] +40 Copper&Tin"}}:
                                        break
                                    if Wonder == {
                                        "Great Tin Deposit": {"Type": "Economic", "Modifier": "ToDo [Local] +30 Tin"}}:
                                        Wonders.append(Wonder)
                                        Tin += 30
                                        Game.Remaining_Wonders.remove(Wonder)
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
                    "Connections": "",
                    "Coordinates": {  # These coordinates are calculable and are a
                        "x": x,  # way to reduce the size of the Data recorded
                        "y": y,  # If we however change World-Gen all previous games will be lost
                        "SubGrid_Location": SubGridLocation,
                    },
                    "Terrain": {
                        "Biome": New_Biome,
                        "Elevation": New_Elevation,
                        "Water_Status": Water_Status
                    },
                    "Resources": Resources,
                    "Wonders": Wonders,  # are based on Terrain and get destroyed if those change
                }
            }

        Game.points.append(New_Point)

    with open("points.yml", 'w') as f:
        yaml.safe_dump(Game.points, f, default_flow_style=False, sort_keys=False)


def create_factions():
    New_Race = ""
    New_Capital = [0, 0]
    List_of_Capitals = []
    List_of_Races = []

    Allowed_Races = int(Game.faction_amount / 3)  # 16 Faction = 5 Races (Small World)

    for i in range(1, Game.faction_amount + 1):
        while New_Capital in List_of_Capitals:
            New_Capital = [random.randint(1, Game.worldsize_input_x), random.randint(1, Game.worldsize_input_y)]

        while New_Race not in List_of_Races and len(List_of_Races) == Allowed_Races:
            New_Race = Game.Races[int(random.randint(0, len(Game.Races)))]

        if i == 1:
            Behavior = "Player"
        else:
            Behavior = "AI"

        match New_Race:
            case "Human":
                Behavior = "Technological"
            case "Elf":
                Behavior = "Diplomatic"
            case "Dwarf":
                Behavior = "Economic"
            case "Orc":
                Behavior = "Militaristic"
            case "Fallen":
                Behavior = "Militaristic"

        Faction = {
            "Faction": {
                "Faction Name": "Name",
                "Faction_ID": i,
                "Faction_Behavior": Behavior,  # Player, etc
                "Race": "",
                New_Race: {},
                "Temporary_Modifiers": {},  # Modifier + Turns left
                "Modifiers": {}  # to safe Lines every Modifier that isn't in here is the default Value
            }
        }

        Game.factions.append(Faction)

    with open("factions.yml", 'w') as f:
        yaml.safe_dump(Game.factions, f, default_flow_style=False, sort_keys=False)
