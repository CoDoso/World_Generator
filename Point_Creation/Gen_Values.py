# -------------------------------------------------------------------------------------------------------------------
#                                            '---[ Points ]---'
#
# Worldsize
worldsize_input_x = int(input("Insert X size for the World size: "))
worldsize_input_y = int(input("Insert Y size for the World size: "))
worldsize = worldsize_input_x * worldsize_input_y
#
# Point Data
rows_left = worldsize_input_y
points = []
Biomes = ["Grassland", "Forest", "Sand"]
Elevations = ["Flat", "Hills", "Steep", "Water", "Uninhabitable"]
Natural_Wonders = [
    # Military
    {"High Hills": {"Type": "Military", "Modifier": "ToDo [Local] Fort Level +1"}},  # 0
    # Symbolic
    {"Great Falls": {"Type": "Symbolic", "Modifier": "ToDo [Faction] Prestige +10"}},  # 1
    {"Volcano Field": {"Type": "Symbolic", "Modifier": "ToDo [Both] Allow Volcano Eruption Event & *2 Attrition"}},  # 2
    # Economic
    {"Bronze Mountain": {"Type": "Economic", "Modifier": "ToDo [Local] +40 Copper&Tin"}},  # 3
    {"Desert Floodplains": {"Type": "Economic", "Modifier": "ToDo [Local] +15 Fertile Lands"}},  # 4
    {"Senlows Coal Deposit": {"Type": "Economic", "Modifier": "ToDo [Local] +50 Coal"}},  # 5
    {"Great Iron Deposit": {"Type": "Economic", "Modifier": "ToDo [Local] +30 Iron"}},  # 6
    {"Great Coal Deposit": {"Type": "Economic", "Modifier": "ToDo [Local] +30 Coal"}},  # 7
    {"Great Copper Deposit": {"Type": "Economic", "Modifier": "ToDo [Local] +30 Copper"}},  # 8
    {"Great Tin Deposit": {"Type": "Economic", "Modifier": "ToDo [Local] +30 Tin"}}]  # 9
# Modifier: Faction Variable(Global Modifiers or "Local"(the Point)) Increase | (Modifiers Inspiration: EU4)
Remaining_Wonders = Natural_Wonders
#
# -------------------------------------------------------------------------------------------------------------------
#                                           '---[ Factions ]---'
# Faction Diversity
faction_amount = int(input("Amount of Factions at Gamestart: "))
#
# Races
Races = ["Human", "Elf", "Dwarf", "Orc", "Fallen"]
#
# Faction Data
factions = []
#
# -------------------------------------------------------------------------------------------------------------------
#                                           '---[ Modifiers ]---'
# Economy
City_Creation_cost = 350  # Cost to build a City in a Point
Tax_Multiplier = 1
Production_Efficiency = 1
Tariff_Multiplier = 1
# Technology
Research_Speed = 100
Research_Queues = 1  # Like in Call of Dragons
# Military
Army_Efficiency = 100  # Eu4 Morale
Army_Damage_Dealt = 100  # Eu4 Discipline

Levy_Multiplier = 1  # similar to Eu4 "Manpower" Modifiers
Levy_Damage = 25
Levy_Defense = 30  # Levy's   (Stats similar to CK3)
Levy_Pursuit = 0

Knight_Damage = 60
Knight_Defense = 110  # Knight
Knight_Pursuit = 0

Archer_Damage = 75
Archer_Defense = 20  # Archer
Archer_Pursuit = 5

Mage_Damage = 80
Mage_Defense = 15    # Mage
Mage_Pursuit = 5

Cavalry_Damage = 60
Cavalry_Defense = 75  # Cav
Cavalry_Pursuit = 25

# Diplomatic
Reputation = 50
Prestige = 0  # Affect likeness to Ally, Relations, etc
Max_Allies = 3
