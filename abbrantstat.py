from random import randint

def abberant_stat():
    x = randint (1, 6)
    return x

def stateth():
    dice_list = []

    for i in range (1, 5):
        die_roll = abberant_stat()
        if die_roll <= 2:
            die_roll = abberant_stat()
        dice_list.append(die_roll)

    print (dice_list)

    dice_list.remove(min(dice_list))

    print (dice_list)
    return sum(dice_list)


def rollstats():
    another_list = []

    for i in range (1, 7):
        name = stateth()
        another_list.append(name)

    my_dictionary = {
        "stronkth": 0,
        "ducksderety": 0,
        "constipation": 0,
        "intelelijans": 0,
        "wersdum": 0,
        "Krisma": 0
    }

    stat_values  = {}
    stat_list = ["stronkth", "ducksderety", "constipation", "intelelijans", "wersdum", "Krisma"]
    for j in stat_list:
        print (another_list)
        print('Input stat:', j)
        # this_stat = int(input())
        user_input = input()
        this_stat = int(user_input)
        if int(this_stat) in another_list:
            my_dictionary[j] = this_stat
            another_list.remove(this_stat)
        else:
            raise ValueError("Sory dave, that numba is not in our thingee")

    print(my_dictionary)

