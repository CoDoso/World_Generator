import Gen_Values as Game
from matplotlib import pyplot


def visualize():

    # Biomes
    b_g = 0
    b_f = 0
    b_s = 0
    # Elevation
    e_f = 0
    e_h = 0
    e_s = 0
    e_w = 0
    e_u = 0

    for item in Game.points:

        for Wonder in list(item['Point']['Monuments']['Wonders']):
            if Wonder == {"Great Falls": {"Type": "Touristic", "Modifier": "ToDo [Global] Prestige +10"}}:
                print("Great Falls Detected in "
                      f"X:{item['Point']['Coordinates']['x']} : Y:{item['Point']['Coordinates']['y']}")

        if item['Point']['Terrain']['Biome'] == "Grassland":
            b_g += 1
        elif item['Point']['Terrain']['Biome'] == "Forest":
            b_f += 1
        elif item['Point']['Terrain']['Biome'] == "Sand":
            b_s += 1

        if item['Point']['Terrain']['Elevation'] == "Flat":
            e_f += 1
        elif item['Point']['Terrain']['Elevation'] == "Hills":
            e_h += 1
        elif item['Point']['Terrain']['Elevation'] == "Steep":
            e_s += 1
        elif item['Point']['Terrain']['Elevation'] == "Water":
            e_w += 1
        elif item['Point']['Terrain']['Elevation'] == "Uninhabitable":
            e_u += 1

    b_data = [b_g, b_f, b_s]
    e_data = [e_f, e_h, e_s, e_w, e_u]

    fig = pyplot.figure(figsize=(10, 7))

    # pyplot.pie(b_data, labels=Game.Biomes)
    # pyplot.show()

    pyplot.pie(e_data, labels=Game.Elevations)
    pyplot.show()
