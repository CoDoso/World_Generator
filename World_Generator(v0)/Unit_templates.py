import Gen_Values as Base

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
# -------------------------------------------------------------------------------------------------------------------
#                                            '---[ Human ]---'
#
Human_Knight = {
    "Knight": {
        "Name": "Knights",
        "Damage": Base.Knight_Damage,
        "Defense": Base.Knight_Defense + 10,
        "Pursuit": Base.Knight_Pursuit,
        "Upkeep": 5
    }
}
Human_Archer = {
    "Archer": {
        "Name": "Longbow_Archers",
        "Damage": Base.Archer_Damage + 10,
        "Defense": Base.Archer_Defense - 5,
        "Pursuit": Base.Archer_Pursuit + 2,
        "Upkeep": 2
    }
}
Human_Mage = {
    "Mage": {
        "Name": "Wizards",
        "Damage": Base.Mage_Damage,
        "Defense": Base.Mage_Defense,
        "Pursuit": Base.Mage_Pursuit,
        "Upkeep": 4
    }
}
Human_Cavalry = {
    "Cavalry": {
        "Name": "Heavy_Cavalry",
        "Damage": Base.Cavalry_Damage + 10,
        "Defense": Base.Cavalry_Defense + 50,
        "Pursuit": Base.Cavalry_Pursuit - 20,
        "Upkeep": 7
    }
}
# -------------------------------------------------------------------------------------------------------------------
#                                            '---[ Elf ]---'
#
Elven_Knight = {
    "Knight": {
        "Name": "Elf_Knights",
        "Damage": Base.Knight_Damage + 10,
        "Defense": Base.Knight_Defense - 10,
        "Pursuit": Base.Knight_Pursuit + 5,
        "Upkeep": 3
    }
}
Elven_Archer = {
    "Archer": {
        "Name": "Forest_Archers",
        "Damage": Base.Archer_Damage,
        "Defense": Base.Archer_Defense + 10,
        "Pursuit": Base.Archer_Pursuit - 2,
        "Upkeep": 2
    }
}
Elven_Mage = {
    "Mage": {
        "Name": "High_Mage",
        "Damage": Base.Mage_Damage + 30,
        "Defense": Base.Mage_Defense + 10,
        "Pursuit": Base.Mage_Pursuit + 5,
        "Upkeep": 5
    }
}
Elven_Cavalry = {
    "Cavalry": {
        "Name": "Elk_Riders",
        "Damage": Base.Cavalry_Damage - 10,
        "Defense": Base.Cavalry_Defense - 35,
        "Pursuit": Base.Cavalry_Pursuit,
        "Upkeep": 2
    }
}
# -------------------------------------------------------------------------------------------------------------------
#                                            '---[ Orc ]---'
#
Orc_Knight = {
    "Knight": {
        "Name": "Orc_Berserker",
        "Damage": Base.Knight_Damage + 40,
        "Defense": Base.Knight_Defense,
        "Pursuit": Base.Knight_Pursuit + 5,
        "Upkeep": 4
    }
}
Orc_Archer = {
    "Archer": {
        "Name": "Orc_Rangers",
        "Damage": Base.Archer_Damage - 5,
        "Defense": Base.Archer_Defense + 10,
        "Pursuit": Base.Archer_Pursuit + 5,
        "Upkeep": 2
    }
}
Orc_Mage = {
    "Mage": {
        "Name": "Shaman",
        "Damage": Base.Mage_Damage - 10,
        "Defense": Base.Mage_Defense,
        "Pursuit": Base.Mage_Pursuit,
        "Upkeep": 4
    }
}
Orc_Cavalry = {
    "Cavalry": {
        "Name": "Wolf_Riders",
        "Damage": Base.Cavalry_Damage + 15,
        "Defense": Base.Cavalry_Defense - 25,
        "Pursuit": Base.Cavalry_Pursuit,
        "Upkeep": 3
    }
}
# -------------------------------------------------------------------------------------------------------------------
#                                            '---[ Dwarf ]---'
#
Dwarven_Knight = {
    "Knight": {
        "Name": "Dwarven_Soldier",
        "Damage": Base.Knight_Damage - 10,
        "Defense": Base.Knight_Defense + 25,
        "Pursuit": Base.Knight_Pursuit + 5,
        "Upkeep": 3
    }
}
Dwarven_Archer = {
    "Archer": {
        "Name": "Spear_Cannon",
        "Damage": Base.Archer_Damage + 35,
        "Defense": Base.Archer_Defense + 25,
        "Pursuit": Base.Knight_Pursuit,
        "Upkeep": 8
    }
}
Dwarven_Mage = {
    "Mage": {
        "Name": "Magic_Engineer",
        "Damage": Base.Mage_Damage,
        "Defense": Base.Mage_Defense,
        "Pursuit": Base.Mage_Pursuit,
        "Upkeep": 5
    }
}
Dwarven_Cavalry = {
    "Cavalry": {
        "Name": "Goat_Riders",
        "Damage": Base.Cavalry_Damage,
        "Defense": Base.Cavalry_Defense - 25,
        "Pursuit": Base.Cavalry_Pursuit,
        "Upkeep": 2
    }
}
# -------------------------------------------------------------------------------------------------------------------
#                                            '---[ Fallen ]---'
#
Fallen_Knight = {
    "Knight": {
        "Name": "Fallen_Knight",
        "Damage": Base.Knight_Damage - 5,
        "Defense": Base.Knight_Defense - 25,
        "Pursuit": Base.Knight_Pursuit + 10,
        "Upkeep": 2
    }
}
Fallen_Archer = {
    "Archer": {
        "Name": "Crossbowmen",
        "Damage": Base.Archer_Damage + 15,
        "Defense": Base.Archer_Defense,
        "Pursuit": Base.Archer_Pursuit,
        "Upkeep": 4
    }
}
Fallen_Mage = {
    "Mage": {
        "Name": "Elder_Wizard",
        "Damage": Base.Mage_Damage + 40,
        "Defense": Base.Mage_Defense,
        "Pursuit": Base.Mage_Pursuit + 5,
        "Upkeep": 6
    }
}
Fallen_Cavalry = {
    "Cavalry": {
        "Name": "Ghost_Riders",
        "Damage": Base.Cavalry_Damage - 10,
        "Defense": Base.Cavalry_Defense - 25,
        "Pursuit": Base.Cavalry_Pursuit + 5,
        "Upkeep": 2
    }
}
