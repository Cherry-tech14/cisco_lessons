'''
def message():
    print("Enter a value: ")

message()
a = int(input())
message()
b = int(input())
message()
c = int(input())

# parameterized functions
def message(number):
    print ("Enter a number:", number)

message(1)


def message(number):
    print(number)
number = 1234
message(1)
print(number)
'''

def message(what, number):
    print("Enter", what, "number", number)

message("telephone", 11)
message("price", 5)

# Positional parameter passing

def introduction(first_name, last_name):
    print("Hello, my name is", first_name, last_name)

introduction("Luke", "Skywalker")
introduction("Jesse", "Quick")
introduction("Clark", "Kent")



