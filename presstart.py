import sys
from count_down import my_count_down as Count_Down
from count_down import whiloop as Count_Up

# Count_Down()

# Count_Up()
# print ('Number of arguments', len(sys.argv), 'arguments.')
# print ('argument list:', str(sys.argv))
# print (sys.argv[0])
my_list = sys.argv
if "up" in my_list:
    Count_Up()
if "down" in my_list:
    Count_Down()