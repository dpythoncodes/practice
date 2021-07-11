import sys

def add(a, b):
    return a+b

def subtract(a, b):
    return a-b

def multiply(a, b):
    return a*b

def divide(a, b):
    return a/b

def modulo(a, b):
    return a%b

first_number = 8
second_number = 67


symbol_list = ["+", "-", "*", "%"]
op_list = [
    add(first_number, second_number),
    subtract(first_number, second_number),
    multiply(first_number, second_number),
    divide(first_number, second_number)
    ]

for i in range(0, 4):
    print(first_number, symbol_list[i], second_number, "=", op_list[i])
variable = """
try:
    print("Arguments as an integer:")
    print (int(first_number), "+", int(second_number), "=", add(int(first_number), int(second_number)))
    print (int(first_number), "-", int(second_number), "=", subtract(int(first_number), int(second_number)))
    print (int(first_number), "*", int(second_number), "=", multiply(int(first_number), int(second_number)))
    print (int(first_number), "/", int(second_number), "=", divide(int(first_number), int(second_number)))
    print (int(first_number), "%", int(second_number), "=", modulo(int(first_number), int(second_number)))
    print("as a string:")
except TypeError:
    pass
try:
    print("Aruments a string:")
    # print (first_number, "/", second_number, "=", divide(first_number, second_number))
    # print (first_number, "%", second_number, "=", modulo(first_number, second_number))
    print (first_number, "+", second_number, "=", add(first_number, second_number))
    # print (first_number, "%", second_number, "=", subtract(first_number, second_number))
    print (first_number, "x", second_number, "=", multiply(first_number, second_number))
except TypeError:
    pass

"""
print("thanks")

multi_line_text = """this will keep 
returns and you can
do as many lines as
you want in one string."""

other_m_line_string = '''
it can be single x 3 quotes too
like this
'''
