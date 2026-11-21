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


# Keyword argument passing
def introduction(first_name, last_name):
    print("Hello, my name is", first_name, last_name)
introduction(first_name = "James", last_name = "Bond")
introduction(last_name = "Skywalker", first_name = "Luke")


# returning a result from a function: using return keyword
def boring_function():
    return 123

x = boring_function()

print(x)

def boring_function():
    print("'Boredom Mode' ON.")
    return 123

print("This lesson is interesting!")
boring_function()
print("This lesson is boring...")
'''
