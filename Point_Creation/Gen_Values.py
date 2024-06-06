worldsize_input_x = int(input("Insert X size for the World size: "))
worldsize_input_y = int(input("\nInsert Y size for the World size: "))
worldsize = worldsize_input_x * worldsize_input_y

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
