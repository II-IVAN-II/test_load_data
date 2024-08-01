# ECOR 1042 Lab 3 - Team submission
# Remember to include docstring and type annotations for your functions

# Update "" to list all students contributing to the team work
__author__ = "Ivan, Vision and Zuhayr"

# Update "" with your team (e.g. T102)
__team__ = "T37"


#==========================================#
# Place your character_occupation_list function after this line

def character_occupation_list(file_name: str, occupation: str) -> list[dict]:
    """
    >>> character_occupation_list ('characters-mat.csv', 'AT')
    [{'Strength': 13, 'Agility': 2, 'Stamina': 6, 'Personality': 7,
    'Intelligence': 8, 'Luck': 0.67, 'Armor': 8, 'Weapon': 'Staff'},
    {another element},
    …
    ]
    """
    in_file = open(file_name, 'r')
    first_line = True
    table_header = None
    new_list = []

    for line in in_file:
        line = line.strip().split(',')
        if first_line:
            first_line = False
            table_header = line
        else:
            if line[0] == occupation:
                new = {}
                new[table_header[1]] = int(line[1])
                new[table_header[2]] = (line[2])
                new[table_header[3]] = int(line[3])
                new[table_header[4]] = float(line[4])
                new[table_header[5]] = int(line[5])
                new[table_header[6]] = float(line[6])
                new[table_header[7]] = int(line[7])
                new[table_header[8]] = line[8]
                new_list.append(new)

    in_file.close()
    return new_list
#==========================================#
# Place your character_strength_list function after this line


def character_strength_list(file_name: str, strength_range: tuple[int, int]) -> list[dict]:
    """
    >>> character_strength_list ('characters-mat.csv', (8, 11))
    [{'Occupation': 'AT', 'Agility': 9, 'Stamina': 8, 'Personality': 8,
    'Intelligence': 15, 'Luck': 0.72, 'Armor': 10, 'Weapon': 'Staff'},
    {'Occupation': 'AT', 'Agility': 9, 'Stamina': 3, 'Personality': 9,
    'Intelligence': 15, 'Luck': 0.5, 'Armor': 10, 'Weapon': 'Club'},
    {another element},
    …
    ]
    """
    min_strength, max_strength = strength_range
    in_file = open(file_name, 'r')
    first_line = True
    table_header = None
    new_list = []

    for line in in_file:
        line = line.strip().split(',')
        if first_line:
            first_line = False
            table_header = line
        else:
            strength = int(line[1])
            if min_strength <= strength <= max_strength:
                new = {}
                new[table_header[0]] = line[0]
                new[table_header[2]] = (line[2])
                new[table_header[3]] = int(line[3])
                new[table_header[4]] = float(line[4])
                new[table_header[5]] = int(line[5])
                new[table_header[6]] = float(line[6])
                new[table_header[7]] = int(line[7])
                new[table_header[8]] = line[8]
                new_list.append(new)

    in_file.close()
    return new_list

#==========================================#
# Place your character_luck_list function after this line


def character_luck_list(file_name: str, luck_given: float) -> list[dict]:
    """
    character_luck_list ('characters-mat.csv', 0.4)
    [{'Occupation': 'AT', 'Strength': 12, 'Agility': 3, 'Stamina': 7,
    'Personality': 13, 'Intelligence': 11, 'Armor': 8, 'Weapon': 'Staff'},
    {'Occupation': 'AT', 'Strength': 19, 'Agility': 9, 'Stamina': 9,
    'Personality': 10, 'Intelligence': 12, 'Armor': 10, 'Weapon': 'Dagger'},
    {another element},
     …
     ]
    """
    in_file = open(file_name, 'r')
    first_line = True
    table_header = None
    new_list = []

    for line in in_file:
        line = line.strip().split(',')
        if first_line:
            first_line = False
            table_header = line
        else:
            if float(line[6]) < luck_given:
                new = {}
                new[table_header[0]] = line[0]
                new[table_header[1]] = int(line[1])
                new[table_header[2]] = (line[2])
                new[table_header[3]] = int(line[3])
                new[table_header[4]] = float(line[4])
                new[table_header[5]] = int(line[5])
                new[table_header[7]] = int(line[7])
                new[table_header[8]] = line[8]
                new_list.append(new)
    in_file.close()
    return new_list

#==========================================#
# Place your character_weapon_list function after this line


def character_weapon_list(file_name: str, weapon: str) -> list[dict]:
    """
    >>> character_weapon_list ('characters-mat.csv', 'Staff')
    [{'Occupation': 'AT', 'Strength': 13, 'Agility': 2, 'Stamina': 6,
    'Personality': 7, 'Intelligence': 8, 'Luck': 0.67, 'Armor': 8},
    {another element},
    …
    ]
    """
    in_file = open(file_name, 'r')
    first_line = True
    table_header = None
    new_list = []

    for line in in_file:
        line = line.strip().split(',')
        if first_line:
            first_line = False
            table_header = line
        else:
            if line[-1] == weapon:
                new = {}
                new[table_header[0]] = line[0]
                new[table_header[1]] = int(line[1])
                new[table_header[2]] = int(line[2])
                new[table_header[3]] = int(line[3])
                new[table_header[4]] = int(line[4])
                new[table_header[5]] = int(line[5])
                new[table_header[6]] = float(line[6])
                new[table_header[7]] = int(line[7])
                new_list.append(new)

    in_file.close()
    return new_list

#==========================================#
# Place your load_data function after this line


def load_data(file_name: str, pair_of_values: tuple) -> list[dict]:
    """
    >>> load_data('characters-mat.csv', ('Weapon', 'Staff'))
    [{'Occupation': 'AT', 'Strength': 13, 'Agility': 2, 'Stamina': 6,
    'Personality': 7, 'Intelligence': 8, 'Luck': 0.67, 'Armor': 8},
    {another element},
     …
    ]

    >>> load_data('characters-mat.csv', ('All', -1))
    [{'Occupation': 'AT', 'Strength': 13, 'Agility': 2, 'Stamina': 6,
     'Personality': 7, 'Intelligence': 8, 'Luck': 0.67, 'Armor': 8,
     'Weapon': 'Staff'},
    {another element},
    …
    ]

    >>> load_data('characters-mat.csv', ('Agility', 2))
    Invalid Value //Message displayed on the terminal
    [] //Return value
    >>> load_data('characters-mat.csv', ('Stamina', -1))
    Invalid Value //Message displayed on the terminal
    [] //Return value

"""
    from load_data import character_occupation_list, character_strength_list, character_luck_list, character_weapon_list
    in_file = open(file_name, 'r')
    first_line = True
    table_header = None
    new_list = []
    (key, value) = pair_of_values

    for line in in_file:
        line = line.strip().split(',')
        if first_line:
            first_line = False
            table_header = line
        else:
            if key == 'All':
                new = {}
                new[table_header[0]] = line[0]
                new[table_header[1]] = int(line[1])
                new[table_header[2]] = int(line[2])
                new[table_header[3]] = int(line[3])
                new[table_header[4]] = int(line[4])
                new[table_header[5]] = int(line[5])
                new[table_header[6]] = float(line[6])
                new[table_header[7]] = int(line[7])
                new[table_header[8]] = line[8]
                new_list.append(new)

            elif key == 'Occupation':
                return character_occupation_list(file_name, value)

            elif key == 'Strength':
                return character_strength_list(file_name, value)

            elif key == 'Luck':
                return character_luck_list(file_name, value)

            elif key == 'Weapon':
                return character_weapon_list(file_name, value)

    in_file.close()
    return new_list

#==========================================#
# Place your calculate_health function after this line


def calculate_health(characters: list[dict]) -> list[dict]:
    """
     calculate_health([{'Strength': 13, 'Agility': 2, 'Stamina': 6,
     'Personality': 7, 'Intelligence': 8, 'Luck': 0.6,
     'Armor': 8, 'Weapon': 'Staff'},
     {another element},
     …
     ])
    [{'Strength': 13, 'Agility': 2, 'Stamina': 6, 'Personality': 7,
     'Intelligence': 8, 'Luck': 0.6, 'Armor': 8, 'Weapon': 'Staff',
     'Health': 28.75},
    {another element},
    …
    ]
"""
    for character in characters:
        agility = character.get('Agility', 0)
        stamina = character.get('Stamina', 0)
        personality = character.get('Personality', 0)
        intelligence = character.get('Intelligence', 0)
        # Default to 1 to avoid division by zero
        armor = character.get('Armor', 1)

        health = ((agility + stamina + personality +
                  intelligence) / armor) * 10
        character['Health'] = health

    return characters

# Do NOT include a main script in your submission
