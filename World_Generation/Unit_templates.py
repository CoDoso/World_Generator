# Military
Global_Combat_Moral: int = 100
Global_Combat_Efficiency: int = 100
Global_Combat_EXP_Decay: float = 0.5

# Armys
Army_Morale: float = 100        # Eu4 Morale, low after a long March but high after a Victory or Training session | Max: Variable
Army_Efficiency: float = 100    # Combat "Readiness", low after a long march but high after a good nights rest    | Max: Variable
Army_Experience: float = 20     # Eu4 Army Professionalism, but for an individual Army                            | Max: 100
Army_EXP_Decay: float = 0.5     # Amount of Experience an Army looses every turn                                  | Min: 0.1

# Units
Levy_Multiplier: float = 1
Levy_Damage: float = 25
Levy_Defense: float = 30  # Levy
Levy_Pursuit: float = 0

Knight_Damage: float = 60
Knight_Defense: float = 100  # Knight
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

# -------------------------------------------------------------------------------------------------------------------
#                                            '---[ Unit Templates ]---'
#
Scout = {
    "Scout": {
        "Name": "Scout",
        "Damage": 10,
        "Defense": 15,
        "Pursuit": 5,
        "Upkeep": 1
    }
}
#
Levy = {
    "Levy": {
            "Name": "Levy",
            "Damage": 25,
            "Defense": 40,
            "Pursuit": 0,
            "Upkeep": 0.5
        }
}
# -------------------------------------------------------------------------------------------------------------------
#                                            '---[ Human ]---'
#
Human_Knight = {
    "Knight": {
        "Name": "Knights",
        "Damage": Knight_Damage,
        "Defense": Knight_Defense + 10,
        "Pursuit": Knight_Pursuit,
        "Upkeep": 5
    }
}
Human_Archer = {
    "Archer": {
        "Name": "Longbow_Archers",
        "Damage": Archer_Damage + 10,
        "Defense": Archer_Defense - 5,
        "Pursuit": Archer_Pursuit + 2,
        "Upkeep": 2
    }
}
Human_Mage = {
    "Mage": {
        "Name": "Wizards",
        "Damage": Mage_Damage,
        "Defense": Mage_Defense,
        "Pursuit": Mage_Pursuit,
        "Upkeep": 4
    }
}
Human_Cavalry = {
    "Cavalry": {
        "Name": "Heavy_Cavalry",
        "Damage": Cavalry_Damage + 10,
        "Defense": Cavalry_Defense + 50,
        "Pursuit": Cavalry_Pursuit - 20,
        "Upkeep": 6.5
    }
}
# -------------------------------------------------------------------------------------------------------------------
#                                            '---[ Elf ]---'
#
Elven_Knight = {
    "Knight": {
        "Name": "Elf_Knights",
        "Damage": Knight_Damage + 10,
        "Defense": Knight_Defense - 10,
        "Pursuit": Knight_Pursuit + 5,
        "Upkeep": 3
    }
}
Elven_Archer = {
    "Archer": {
        "Name": "Forest_Archers",
        "Damage": Archer_Damage,
        "Defense": Archer_Defense + 10,
        "Pursuit": Archer_Pursuit - 2,
        "Upkeep": 2
    }
}
Elven_Mage = {
    "Mage": {
        "Name": "High_Mage",
        "Damage": Mage_Damage + 30,
        "Defense": Mage_Defense + 10,
        "Pursuit": Mage_Pursuit + 5,
        "Upkeep": 5
    }
}
Elven_Cavalry = {
    "Cavalry": {
        "Name": "Elk_Riders",
        "Damage": Cavalry_Damage - 10,
        "Defense": Cavalry_Defense - 35,
        "Pursuit": Cavalry_Pursuit,
        "Upkeep": 2
    }
}
# -------------------------------------------------------------------------------------------------------------------
#                                            '---[ Orc ]---'
#
Orc_Knight = {
    "Knight": {
        "Name": "Orc_Berserker",
        "Damage": Knight_Damage + 40,
        "Defense": Knight_Defense,
        "Pursuit": Knight_Pursuit + 5,
        "Upkeep": 4
    }
}
Orc_Archer = {
    "Archer": {
        "Name": "Orc_Rangers",
        "Damage": Archer_Damage - 5,
        "Defense": Archer_Defense + 10,
        "Pursuit": Archer_Pursuit + 5,
        "Upkeep": 2
    }
}
Orc_Mage = {
    "Mage": {
        "Name": "Shaman",
        "Damage": Mage_Damage - 10,
        "Defense": Mage_Defense,
        "Pursuit": Mage_Pursuit,
        "Upkeep": 4
    }
}
Orc_Cavalry = {
    "Cavalry": {
        "Name": "Wolf_Riders",
        "Damage": Cavalry_Damage + 15,
        "Defense": Cavalry_Defense - 25,
        "Pursuit": Cavalry_Pursuit,
        "Upkeep": 3
    }
}
# -------------------------------------------------------------------------------------------------------------------
#                                            '---[ Dwarf ]---'
#
Dwarven_Knight = {
    "Knight": {
        "Name": "Dwarven_Soldier",
        "Damage": Knight_Damage - 10,
        "Defense": Knight_Defense + 25,
        "Pursuit": Knight_Pursuit + 5,
        "Upkeep": 3
    }
}
Dwarven_Archer = {
    "Archer": {
        "Name": "Spear_Cannon",
        "Damage": Archer_Damage + 35,
        "Defense": Archer_Defense + 25,
        "Pursuit": Knight_Pursuit,
        "Upkeep": 7
    }
}
Dwarven_Mage = {
    "Mage": {
        "Name": "Magic_Engineer",
        "Damage": Mage_Damage,
        "Defense": Mage_Defense,
        "Pursuit": Mage_Pursuit,
        "Upkeep": 5
    }
}
Dwarven_Cavalry = {
    "Cavalry": {
        "Name": "Goat_Riders",
        "Damage": Cavalry_Damage,
        "Defense": Cavalry_Defense - 25,
        "Pursuit": Cavalry_Pursuit,
        "Upkeep": 2
    }
}
# -------------------------------------------------------------------------------------------------------------------
#                                            '---[ Fallen ]---'
#
Fallen_Knight = {
    "Knight": {
        "Name": "Fallen_Knight",
        "Damage": Knight_Damage - 5,
        "Defense": Knight_Defense - 25,
        "Pursuit": Knight_Pursuit + 10,
        "Upkeep": 2
    }
}
Fallen_Archer = {
    "Archer": {
        "Name": "Crossbowmen",
        "Damage": Archer_Damage + 15,
        "Defense": Archer_Defense,
        "Pursuit": Archer_Pursuit,
        "Upkeep": 4
    }
}
Fallen_Mage = {
    "Mage": {
        "Name": "Elder_Wizard",
        "Damage": Mage_Damage + 40,
        "Defense": Mage_Defense,
        "Pursuit": Mage_Pursuit + 5,
        "Upkeep": 6
    }
}
Fallen_Cavalry = {
    "Cavalry": {
        "Name": "Ghost_Riders",
        "Damage": Cavalry_Damage - 10,
        "Defense": Cavalry_Defense - 25,
        "Pursuit": Cavalry_Pursuit + 5,
        "Upkeep": 2
    }
}
