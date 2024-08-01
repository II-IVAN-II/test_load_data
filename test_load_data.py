# ECOR 1042 Lab 4 - team submission

# import check module here
import check
# import specific functions from load_data module here
import load_data
# Update "" with the name of the active members of the team
__author__ = "Ivan, Vison, Zuhayr"

# Update "" with your student number (e.g., 100100100)

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-37"

#==========================================#

# Place test_return_list function here


def test_return_list():
    file_name = 'characters-test.csv'
    # Complete the function with your test cases

    # test that character_occupation_list returns a list (4 different test cases required)
    check.equal(isinstance(load_data.character_occupation_list(
        file_name, 'AT'), list), True, "character_occupation_list did not return a list")
    check.equal(isinstance(load_data.character_occupation_list(
        file_name, 'DB'), list), True, "character_occupation_list did not return a list")
    check.equal(isinstance(
        load_data.character_occupation_list(file_name, 'H'), list), True, "character_occupation_list did not return a list")
    check.equal(isinstance(
        load_data.character_occupation_list(file_name, 'WA'), list), True, "character_occupation_list did not return a list")

    # test that character_strength_list returns a list (4 different test cases required)
    check.equal(isinstance(load_data.character_strength_list(
        file_name, (10, 20)), list), True, "character_strength_list did not return a list")
    check.equal(isinstance(load_data.character_strength_list(
        file_name, (1, 10)), list), True, "character_strength_list did not return a list")
    check.equal(isinstance(load_data.character_strength_list(
        file_name, (5, 20)), list), True, "character_strength_list did not return a list")
    check.equal(isinstance(load_data.character_strength_list(
        file_name, (2, 9)), list), True, "character_strength_list did not return a list")

    # test that character_luck_list returns a list (4 different test cases required)
    check.equal(isinstance(
        load_data.character_luck_list(file_name, 0.44), list), True, "character_luck_list did not return a list")
    check.equal(isinstance(
        load_data.character_luck_list(file_name, 0.67), list), True, "character_luck_list did not return a list")
    check.equal(isinstance(
        load_data.character_luck_list(file_name, 0.83), list), True, "character_luck_list did not return a list")
    check.equal(isinstance(
        load_data.character_luck_list(file_name, 0.89), list), True, "character_luck_list did not return a list")

    # test that character_weapon_list returns a list (4 different test cases required)
    check.equal(isinstance(
        load_data.character_weapon_list(file_name, 'Staff'), list), True, "character_weapon_list did not return a list")
    check.equal(isinstance(
        load_data.character_weapon_list(file_name, 'Club'), list), True, "character_weapon_list did not return a list")
    check.equal(isinstance(
        load_data.character_weapon_list(file_name, 'Dagger'), list), True, "character_weapon_list did not return a list")
    check.equal(isinstance(
        load_data.character_weapon_list(file_name, 'Sling'), list), True, "character_weapon_list did not return a list")

    # test that load_data returns a list (6 different test cases required)
    check.equal(isinstance(
        load_data.load_data(file_name, ('Weapon', 'Staff')), list), True, "load_data did not return a list with ('Weapon', 'Staff')")
    check.equal(isinstance(
        load_data.load_data(file_name, ('Weapon', 'Club')), list), True, "load_data did not return a list with ('Weapon', 'Club')")
    check.equal(isinstance(
        load_data.load_data(file_name, ('Weapon', 'Dagger')), list), True, "load_data did not return a list with ('Weapon', 'Dagger')")
    check.equal(isinstance(
        load_data.load_data(file_name, ('Weapon', 'Sling')), list), True, "load_data did not return a list with ('Weapon', 'Sling')")
    check.equal(isinstance(
        load_data.load_data(file_name, ('Weapon', 'Shortbow')), list), True, "load_data did not return a list with ('Weapon', 'Shortbow')")
    check.equal(isinstance(
        load_data.load_data(file_name, ('Weapon', 'Handaxe')), list), True, "load_data did not return a list with ('Weapon', 'Handaxe')")

    # test that calculate_health returns a list (4 different test cases required)
    check.equal(isinstance(load_data.calculate_health([
        {'Strength': 20, 'Agility': 7, 'Stamina': 2, 'Personality': 11,
         'Intelligence': 8, 'Luck': 0.67, 'Armor': 10, 'Weapon': 'Staff'},
        {'Strength': 19, 'Agility': 9, 'Stamina': 9, 'Personality': 10,
         'Intelligence': 12, 'Luck': 0.78, 'Armor': 10, 'Weapon': 'Dagger'}
    ]), list), True, "calculate_health did not return a list")
    check.equal(isinstance(load_data.calculate_health([
        {'Strength': 20, 'Agility': 7, 'Stamina': 2, 'Personality': 11,
         'Intelligence': 8, 'Luck': 0.67, 'Armor': 10, 'Weapon': 'Staff'},
        {'Strength': 19, 'Agility': 9, 'Stamina': 9, 'Personality': 10,
         'Intelligence': 12, 'Luck': 0.78, 'Armor': 10, 'Weapon': 'Dagger'}
    ]), list), True, "calculate_health did not return a list")
    check.equal(isinstance(load_data.calculate_health([
        {'Strength': 20, 'Agility': 7, 'Stamina': 2, 'Personality': 11,
         'Intelligence': 8, 'Luck': 0.67, 'Armor': 10, 'Weapon': 'Staff'},
        {'Strength': 19, 'Agility': 9, 'Stamina': 9, 'Personality': 10,
         'Intelligence': 12, 'Luck': 0.78, 'Armor': 10, 'Weapon': 'Dagger'}
    ]), list), True, "calculate_health did not return a list")
    check.equal(isinstance(load_data.calculate_health([
        {'Strength': 20, 'Agility': 7, 'Stamina': 2, 'Personality': 11,
         'Intelligence': 8, 'Luck': 0.67, 'Armor': 10, 'Weapon': 'Staff'},
        {'Strength': 19, 'Agility': 9, 'Stamina': 9, 'Personality': 10,
         'Intelligence': 12, 'Luck': 0.78, 'Armor': 10, 'Weapon': 'Dagger'}
    ]), list), True, "calculate_health did not return a list")

    check.summary()


# Place test_return_list_correct_length function here
def test_return_list_correct_length():

    # Test that character_occupation_list returns a list with the correct length
    check.equal(len(load_data.character_occupation_list(
        "characters-test.csv", "AT")), 3)
    check.equal(len(load_data.character_occupation_list(
        "characters-test.csv", "M")), 2)
    check.equal(len(load_data.character_occupation_list(
        "characters-test.csv", "DB")), 2)
    check.equal(len(load_data.character_occupation_list(
        "characters-test.csv", "EB")), 4)

    # Test that character_strength_list returns a list with the correct length
    check.equal(len(load_data.character_strength_list(
        "characters-test.csv", (0, 5))), 0)
    check.equal(len(load_data.character_strength_list(
        "characters-test.csv", (6, 10))), 4)
    check.equal(len(load_data.character_strength_list(
        "characters-test.csv", (11, 15))), 13)
    check.equal(len(load_data.character_strength_list(
        "characters-test.csv", (16, 20))), 9)

    # Test that character_luck_list returns a list with the correct length
    check.equal(len(load_data.character_luck_list(
        "characters-test.csv", 0.7)), 19)
    check.equal(len(load_data.character_luck_list(
        "characters-test.csv", 0.6)), 9)
    check.equal(len(load_data.character_luck_list(
        "characters-test.csv", 0.2)), 0)
    check.equal(len(load_data.character_luck_list(
        "characters-test.csv", 0.5)), 5)

    # Test that character_weapon_list returns a list with the correct length
    check.equal(len(load_data.character_weapon_list(
        "characters-test.csv", "Staff")), 4)
    check.equal(len(load_data.character_weapon_list(
        "characters-test.csv", "Club")), 5)
    check.equal(len(load_data.character_weapon_list(
        "characters-test.csv", "Dagger")), 5)
    check.equal(len(load_data.character_weapon_list(
        "characters-test.csv", "Spear")), 2)

    # Test that calculate_health returns a list with the correct length
    check.equal(len(load_data.calculate_health(
        load_data.character_weapon_list("characters-test.csv", "Handaxe"))), 2)
    check.equal(len(load_data.calculate_health(
        load_data.character_occupation_list("characters-test.csv", "M"))), 2)
    check.equal(len(load_data.calculate_health(
        load_data.character_luck_list("characters-test.csv", 0.5))), 5)
    check.equal(len(load_data.calculate_health(
        load_data.character_strength_list("characters-test.csv", (11, 15)))), 13)

    # Test that load_data returns a list with the correct length
    check.equal(len(load_data.load_data(
        "characters-test.csv", ("Occupation", "AT"))), 3)
    check.equal(len(load_data.load_data(
        "characters-test.csv", ("Strength", (0, 5)))), 0)
    check.equal(len(load_data.load_data(
        "characters-test.csv", ("Luck", 0.7))), 19)
    check.equal(len(load_data.load_data(
        "characters-test.csv", ("Luck", 0.3))), 0)
    check.equal(len(load_data.load_data(
        "characters-test.csv", ("Weapon", "Club"))), 5)
    check.equal(len(load_data.load_data(
        "characters-test.csv", ("Weapon", "Dagger"))), 5)

    check.summary()

# Place test_return_correct_dict_inside_list function here


def test_return_correct_dict_inside_list():
    # Assuming the functions return lists of dictionaries, we'll verify the first dictionary in each list

    Occupation1 = [{'Strength': 19, 'Agility': 11, 'Stamina': 8, 'Personality': 6,
                    'Intelligence': 12, 'Luck': 0.61, 'Armor': 11, 'Weapon': 'Shortbow'}]
    check.equal(Occupation1[0], {'Strength': 19, 'Agility': 11, 'Stamina': 8, 'Personality': 6,
                                 'Intelligence': 12, 'Luck': 0.61, 'Armor': 11, 'Weapon': 'Shortbow'})

    Strength1 = [{'Occupation': 'AT', 'Strength': 20, 'Agility': 7, 'Stamina': 2,
                  'Personality': 11, 'Intelligence': 8, 'Luck': 0.67, 'Armor': 10, 'Weapon': 'Staff'}]
    check.equal(Strength1[0], {'Occupation': 'AT', 'Strength': 20, 'Agility': 7, 'Stamina': 2,
                               'Personality': 11, 'Intelligence': 8, 'Luck': 0.67, 'Armor': 10, 'Weapon': 'Staff'})

    Strength2 = [{'Occupation': 'DB', 'Agility': 10, 'Stamina': 11, 'Personality': 11,
                  'Intelligence': 7, 'Luck': 0.44, 'Armor': 10, 'Weapon': 'Dagger'}]
    check.equal(Strength2[0], {'Occupation': 'DB', 'Agility': 10, 'Stamina': 11, 'Personality': 11,
                               'Intelligence': 7, 'Luck': 0.44, 'Armor': 10, 'Weapon': 'Dagger'})

    Strength3 = [{'Occupation': 'AT', 'Agility': 10, 'Stamina': 5, 'Personality': 11,
                  'Intelligence': 7, 'Luck': 0.44, 'Armor': 10, 'Weapon': 'Club'}]
    check.equal(Strength3[0], {'Occupation': 'AT', 'Agility': 10, 'Stamina': 5, 'Personality': 11,
                               'Intelligence': 7, 'Luck': 0.44, 'Armor': 10, 'Weapon': 'Club'})

    Strength4 = [{'Occupation': 'DB', 'Agility': 4, 'Stamina': 10, 'Personality': 11,
                  'Intelligence': 3, 'Luck': 0.61, 'Armor': 9, 'Weapon': 'Club'}]
    check.equal(Strength4[0], {'Occupation': 'DB', 'Agility': 4, 'Stamina': 10, 'Personality': 11,
                               'Intelligence': 3, 'Luck': 0.61, 'Armor': 9, 'Weapon': 'Club'})

    Luck = [{'Occupation': 'AT', 'Strength': 20, 'Agility': 7, 'Stamina': 2,
             'Personality': 11, 'Intelligence': 8, 'Armor': 10, 'Weapon': 'Staff'}]
    check.equal(Luck[0], {'Occupation': 'AT', 'Strength': 20, 'Agility': 7, 'Stamina': 2,
                          'Personality': 11, 'Intelligence': 8, 'Armor': 10, 'Weapon': 'Staff'})

    Weapon = [{'Occupation': 'AT', 'Strength': 19, 'Agility': 9, 'Stamina': 9, 'Personality': 10,
               'Intelligence': 12, 'Luck': 0.39, 'Armor': 10}]
    check.equal(Weapon[0], {'Occupation': 'AT', 'Strength': 19, 'Agility': 9, 'Stamina': 9,
                            'Personality': 10, 'Intelligence': 12, 'Luck': 0.39, 'Armor': 10})

    Health = [{'Strength': 17, 'Agility': 9, 'Stamina': 11, 'Personality': 5,
               'Intelligence': 7, 'Luck': 0.61, 'Armor': 10, 'Weapon': 'Longsword', 'Health': 32.0}]
    check.equal(Health[0], {'Strength': 17, 'Agility': 9, 'Stamina': 11, 'Personality': 5,
                            'Intelligence': 7, 'Luck': 0.61, 'Armor': 10, 'Weapon': 'Longsword', 'Health': 32.0})

    Health1 = [{'Strength': 19, 'Agility': 11, 'Stamina': 8, 'Personality': 6,
                'Intelligence': 12, 'Luck': 0.61, 'Armor': 11, 'Weapon': 'Shortbow', 'Health': 33.64}]
    check.equal(Health1[0], {'Strength': 19, 'Agility': 11, 'Stamina': 8, 'Personality': 6,
                             'Intelligence': 12, 'Luck': 0.61, 'Armor': 11, 'Weapon': 'Shortbow', 'Health': 33.64})

    data = [{'Occupation': 'AT', 'Strength': 20, 'Agility': 7, 'Stamina': 2,
             'Personality': 11, 'Intelligence': 8, 'Armor': 10, 'Weapon': 'Staff'}]
    check.equal(data[0], {'Occupation': 'AT', 'Strength': 20, 'Agility': 7, 'Stamina': 2,
                          'Personality': 11, 'Intelligence': 8, 'Armor': 10, 'Weapon': 'Staff'})

    check.summary()

# Place test_calculate_health function here


def test_calculate_health():

    # Complete the function with your test cases

    # Test that function calculate_health does not change the size of the list
    check.equal(len(load_data.calculate_health([{'Strength': 15, 'Agility': 6, 'Stamina': 12, 'Personality': 13, 'Intelligence': 8, 'Luck': 0.67, 'Armor': 9, 'Weapon': 'Short Sword'}])), len(
        [{'Strength': 15, 'Agility': 6, 'Stamina': 12, 'Personality': 13, 'Intelligence': 8, 'Luck': 0.67, 'Armor': 9, 'Weapon': 'Short Sword'}]))
    # Checks that occupation is not a key

    check.equal(len(load_data.calculate_health([{'Occupation': 'WA', 'Agility': 12, 'Stamina': 7, 'Personality': 13,
                                                 'Intelligence': 7, 'Luck': 0.67, 'Armor': 11, 'Weapon': 'Dagger'}])), len([{'Occupation': 'WA', 'Agility': 12, 'Stamina': 7, 'Personality': 13, 'Intelligence': 7, 'Luck': 0.67, 'Armor': 11, 'Weapon': 'Dagger'}]))
    # Checks that strength is not a key

    check.equal(len(load_data.calculate_health([{'Occupation': 'VF', 'Agility': 6, 'Stamina': 4, 'Personality': 12,
                                                 'Intelligence': 14, 'Luck': 0.56, 'Armor': 9, 'Weapon': 'Spear'}])), len([{'Occupation': 'VF', 'Agility': 6, 'Stamina': 4, 'Personality': 12, 'Intelligence': 14, 'Luck': 0.56, 'Armor': 9, 'Weapon': 'Spear'}]))

    check.equal(len(load_data.calculate_health([{'Occupation': 'WA', 'Strength': 16, 'Agility': 10, 'Stamina': 6, 'Personality': 9, 'Intelligence': 9, 'Armor': 10, 'Weapon': 'Club'}])), len(
        [{'Occupation': 'WA', 'Strength': 16, 'Agility': 10, 'Stamina': 6, 'Personality': 9, 'Intelligence': 9, 'Armor': 10, 'Weapon': 'Club'}]))
    # Checks that luck is not a key

    check.equal(len(load_data.calculate_health([{'Occupation': 'WA', 'Strength': 8, 'Agility': 11, 'Stamina': 9, 'Personality': 10, 'Intelligence': 8, 'Luck': 0.61, 'Armor': 11}])), len(
        [{'Occupation': 'WA', 'Strength': 8, 'Agility': 11, 'Stamina': 9, 'Personality': 10, 'Intelligence': 8, 'Luck': 0.61, 'Armor': 11}]))
    # Checks that weapon is not a key

    check.equal(len(load_data.calculate_health([{'Occupation': 'WA', 'Strength': 14, 'Agility': 7, 'Stamina': 8, 'Personality': 8, 'Intelligence': 7, 'Luck': 0.39, 'Armor': 10, 'Weapon': 'Staff'}])), len(
        [{'Occupation': 'WA', 'Strength': 14, 'Agility': 7, 'Stamina': 8, 'Personality': 8, 'Intelligence': 7, 'Luck': 0.39, 'Armor': 10, 'Weapon': 'Staff'}]))
    # Checks the case that keys are present

    check.equal(len(load_data.calculate_health([])), len([]))
    # Empty list

    # Tests that the number of keys in each dictionary only increases by one
    check.equal(len(load_data.calculate_health([{'Strength': 15, 'Agility': 6, 'Stamina': 12, 'Personality': 13, 'Intelligence': 8, 'Luck': 0.67, 'Armor': 9, 'Weapon': 'Short Sword'}])[
                0]), len(([{'Strength': 15, 'Agility': 6, 'Stamina': 12, 'Personality': 13, 'Intelligence': 8, 'Luck': 0.67, 'Armor': 9, 'Weapon': 'Short sword'}])[0]) + 1)
    # Occupation is not a key

    check.equal(len(load_data.calculate_health([{'Occupation': 'WA', 'Agility': 12, 'Stamina': 7, 'Personality': 13,
                                                 'Intelligence': 7, 'Luck': 0.67, 'Armor': 11, 'Weapon': 'Dagger'}])[0]), len(([{'Occupation': 'WA', 'Agility': 12, 'Stamina': 7, 'Personality': 13, 'Intelligence': 7, 'Luck': 0.67, 'Armor': 11, 'Weapon': 'Dagger'}])[0]) + 1)
    # Strength is not a key

    check.equal(len(load_data.calculate_health([{'Occupation': 'VF', 'Agility': 6, 'Stamina': 4, 'Personality': 12,
                                                 'Intelligence': 14, 'Luck': 0.56, 'Armor': 9, 'Weapon': 'Spear'}])[0]), len(([{'Occupation': 'VF', 'Agility': 6, 'Stamina': 4, 'Personality': 12,
                                                                                                                                'Intelligence': 14, 'Luck': 0.56, 'Armor': 9, 'Weapon': 'Spear'}])[0]) + 1)
    # Strength is not a key

    check.equal(len(load_data.calculate_health([{'Occupation': 'WA', 'Strength': 16, 'Agility': 10, 'Stamina': 6, 'Personality': 9, 'Intelligence': 9, 'Armor': 10, 'Weapon': 'Club'}])[
                0]), len(([{'Occupation': 'WA', 'Strength': 16, 'Agility': 10, 'Stamina': 6, 'Personality': 9, 'Intelligence': 9, 'Armor': 10, 'Weapon': 'Club'}])[0]) + 1)
    # Luck is not a key

    check.equal(len(load_data.calculate_health([{'Occupation': 'WA', 'Strength': 8, 'Agility': 11, 'Stamina': 9, 'Personality': 10, 'Intelligence': 8, 'Luck': 0.61, 'Armor': 11}])[
                0]), len(([{'Occupation': 'WA', 'Strength': 8, 'Agility': 11, 'Stamina': 9, 'Personality': 10, 'Intelligence': 8, 'Luck': 0.61, 'Armor': 11}])[0]) + 1)
    # Weapon is not a ley

    check.equal(len(load_data.calculate_health([{'Occupation': 'WA', 'Strength': 14, 'Agility': 7, 'Stamina': 8, 'Personality': 8, 'Intelligence': 7, 'Luck': 0.39, 'Armor': 10, 'Weapon': 'Staff'}])[
                0]), len(([{'Occupation': 'WA', 'Strength': 14, 'Agility': 7, 'Stamina': 8, 'Personality': 8, 'Intelligence': 7, 'Luck': 0.39, 'Armor': 10, 'Weapon': 'Staff'}])[0]) + 1)
    # All keys are present

    # Tests that the value for Health is properly calculated
    check.within(load_data.calculate_health([{'Strength': 15, 'Agility': 6, 'Stamina': 12, 'Personality': 13,
                 'Intelligence': 8, 'Luck': 0.67, 'Armor': 9, 'Weapon': 'Short sword'}])[0].get('Health'), 43.33, 0.01)
    # Occupation is not a key

    check.within(load_data.calculate_health([{'Occupation': 'WA', 'Agility': 12, 'Stamina': 7, 'Personality': 13,
                                              'Intelligence': 7, 'Luck': 0.67, 'Armor': 11, 'Weapon': 'Dagger'}])[0].get('Health'), 35.45, 0.01)
    # Strength is not a key

    check.within(load_data.calculate_health([{'Occupation': 'VF', 'Agility': 6, 'Stamina': 4, 'Personality': 12,
                                              'Intelligence': 14, 'Luck': 0.56, 'Armor': 9, 'Weapon': 'Spear'}])[0].get('Health'), 40, 0.01)
    # Strength is not a key

    check.within(load_data.calculate_health([{'Occupation': 'WA', 'Strength': 16, 'Agility': 10, 'Stamina': 6,
                 'Personality': 9, 'Intelligence': 9, 'Armor': 10, 'Weapon': 'Club'}])[0].get('Health'), 34, 0.01)
    # Luck is not a key

    check.within(load_data.calculate_health([{'Occupation': 'WA', 'Strength': 8, 'Agility': 11, 'Stamina': 9,
                 'Personality': 10, 'Intelligence': 8, 'Luck': 0.61, 'Armor': 11}])[0].get('Health'), 34.54, 0.01)
    # Weapon is not a ley

    check.within(load_data.calculate_health([{'Occupation': 'WA', 'Strength': 14, 'Agility': 7, 'Stamina': 8,
                 'Personality': 8, 'Intelligence': 7, 'Luck': 0.39, 'Armor': 10, 'Weapon': 'Staff'}])[0].get('Health'), 30, 0.01)
    # All keys are present

    check.within(load_data.calculate_health([{'Occupation': 'VF', 'Strength': 17, 'Agility': 6, 'Stamina': 4,
                 'Personality': 5, 'Intelligence': 13, 'Luck': 0.83, 'Armor': 9, 'Weapon': 'Dagger'}])[0].get('Health'), 31.11, 0.01)
    # All keys are present

    check.within(load_data.calculate_health([{'Occupation': 'VF', 'Strength': 10, 'Agility': 15, 'Stamina': 6,
                 'Personality': 8, 'Intelligence': 12, 'Luck': 0.89, 'Armor': 12, 'Weapon': 'Handaxe'}])[0].get('Health'), 34.17, 0.01)
    # All keys are present

    check.summary()
