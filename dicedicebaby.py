from random import randint

def roll_the_dice():
    x = randint(1, 20)
    if x == 20:
        print ("nat 20!")
    elif x == 1:
        print ("natural 1... uh oh")
    else:
        print (x)

def a_bunch_of_dice():
    dicelist = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20']
    # print (len(dicelist))
    print("deans dice list is: ", dicelist)
    print("the first element is of type: ", type(dicelist[0]))
    dads_dice_list = []
    for i in range(1, 21):
        dads_dice_list.append(i)
    print("\ndads dice list is: ", dads_dice_list)
    print("the first element is of type:", type(dads_dice_list[0]) )

def roll_a_number_of_dice(how_many_dice, what_kind_of_dice):
    list_of_dice_rolls = []

    for i in range(1, int(how_many_dice)+1):
        x = randint(1, int(what_kind_of_dice))
        list_of_dice_rolls.append(x)
        print("you rolled a", x)
    print("here are your die rolls:" )
    print(list_of_dice_rolls)


# roll_the_dice()
print("how many dice would you like to roll? ")
input_dice_number = input()
print("what kind of dice would you like to roll (how many sides)? ")
input_die_type = input()
roll_a_number_of_dice(input_dice_number,input_die_type)

