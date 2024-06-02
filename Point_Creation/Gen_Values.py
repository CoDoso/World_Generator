worldsize_input_x = int(input("Insert X size for the World size: "))
worldsize_input_y = int(input("\nInsert Y size for the World size: "))
worldsize = worldsize_input_x * worldsize_input_y

rows_left = worldsize_input_y
points = []
Biomes = ["Grassland", "Forest", "Sand"]
Elevations = ["Flat", "Hills", "Steep", "Water", "Uninhabitable"]
Natural_Wonders = [
    # Military
    {"High Hills": {"Type": "Military", "Modifier": "ToDo [Local] Fort Level +1"}},
    # Symbolic
    {"Great Falls": {"Type": "Symbolic", "Modifier": "ToDo [Faction] Prestige +10"}},
    {"Volcano Field": {"Type": "Symbolic", "Modifier": "ToDo [Both] Allows Volcano Eruption Event & *2 Attrition"}},
    # Economic
    {"Desert Floodplains": {"Type": "Economic", "Modifier": "ToDo [Local] +15 Fertile Lands"}},
    {"Senlows Coal Deposit": {"Type": "Economic", "Modifier": "ToDo [Local] +50 Coal"}},
    {"Great Iron Deposit": {"Type": "Economic", "Modifier": "ToDo [Local] +30 Iron"}},
    {"Great Coal Deposit": {"Type": "Economic", "Modifier": "ToDo [Local] +30 Coal"}},  # ToDo
    {"Great Copper Deposit": {"Type": "Economic", "Modifier": "ToDo [Local] +30 Copper"}},
    {"Great Tin Deposit": {"Type": "Economic", "Modifier": "ToDo [Local] +30 Tin"}},
    {"Bronze Mountain": {"Type": "Economic", "Modifier": "ToDo [Local] +40 Copper&Tin"}}]
# Modifier: Faction Variable(Global Modifiers or "Local"(the Point)) Increase | (Modifiers Inspiration: EU4)
Remaining_Wonders = Natural_Wonders
