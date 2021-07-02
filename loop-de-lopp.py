from random import randint

 
def die_of_death():
    x = randint (0, 99)
    # print (x)
    return x

def count_to__ten():
    for x in range(1, 22):
        print ('The for loop value is', x)
    return x

def a_function(x):
    while x > 0:
        x -= 1
        print ('the while loop value is', x)
    return x

# x = count_to__ten()
# print ('the value of x after for loop is ', x)
# x = a_function(x)

# print ('the final value of x is', x)

def roll_a_bunch_of_dice():
    xlist = []

    random_number_of_times = die_of_death()


    while len(xlist) < random_number_of_times:
        r = die_of_death()
        xlist.append(r)

    print (xlist)


def two_random():
    return die_of_death(), die_of_death()

x = two_random()

print (x)
print(x[0])
print(x[1])