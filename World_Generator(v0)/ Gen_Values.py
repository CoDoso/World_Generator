# -------------------------------------------------------------------------------------------------------------------
#                                            '---[ Points ]---'
#
# Worldsize
worldsize_input_x: int = int(input("Insert X size for the World size: "))
worldsize_input_y: int = int(input("Insert Y size for the World size: "))
worldsize: int = worldsize_input_x * worldsize_input_y
#
# Point Data
rows_left: int = worldsize_input_y
points: list = []
Biomes: list = ["Grassland", "Forest", "Sand"]
Elevations: list = ["Flat", "Hills", "Steep", "Water", "Uninhabitable"]
Natural_Wonders: list = [
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
Remaining_Wonders: list = Natural_Wonders
#
Natural_Buildings: bool = False
Mountains: bool = False   # These 3 are not implemented yet
Oceans: bool = False
#
# -------------------------------------------------------------------------------------------------------------------
#                                           '---[ Factions ]---'
# Faction Diversity
faction_amount: int = int(input("Amount of Factions at Gamestart: "))
#
# Races
Races: list = ["Human", "Elf", "Dwarf", "Orc", "Fallen"]
#
# Faction Data
factions: list = []
#
# -------------------------------------------------------------------------------------------------------------------
#                                           '---[ Armys ]---'
armys: list = []
#
# -------------------------------------------------------------------------------------------------------------------
#                                           '---[ Modifiers ]---'
# Economy
City_build_cost: float = 350  # Cost to build/Expand a City in a new Point
Tax_Multiplier: float = 1
Production_Efficiency: float = 1
Tariff_Multiplier: float = 1

# Technology
Research_Speed: float = 100
Research_Queues: int = 1

# Military
Army_Morale: float = 100        # Eu4 Morale, low after a long March but high after a Victory or Training session | Max: 100
Army_Efficiency: float = 100    # Combat "Readiness", low after a Fight but high after a good nights rest         | Max: 100
Army_Experience: float = 20     # Eu4 Army Professionalism, but for an individual Army                            | Max: 100
Army_EXP_Decay: float = 0.5     # Amount of Experience an Army looses every turn

# Army_Damage_Dealt: float = (Army_Morale + Army_Efficiency) * (Army_Experience * 0.375) + 1)  # min 0, max 275
#                                   # min 0, max 200              # min 1, max 1.375

Levy_Multiplier: float = 1
Levy_Damage: float = 25
Levy_Defense: float = 30  # Levy
Levy_Pursuit: float = 0

Knight_Damage: float = 60
Knight_Defense: float = 100  # Knight ()
Knight_Pursuit: float = 0

Archer_Damage: float = 75
Archer_Defense: float = 20  # Archer
Archer_Pursuit: float = 5

Mage_Damage: float = 80
Mage_Defense: float = 15    # Mage
Mage_Pursuit: float = 5

Cavalry_Damage: float = 60
Cavalry_Defense: float = 75  # Cav
Cavalry_Pursuit: float = 25

# Diplomatic
Reputation: int = 50
Prestige: int = 0      # Affects likeness to Ally, Relations, etc
Max_Allies: int = 3
