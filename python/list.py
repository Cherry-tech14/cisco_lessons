'''
numbers = [10, 5, 7, 2, 1]
del numbers[0]
#print(len(numbers))
print(numbers)


numbers[0] = 111
print(numbers)

numbers[1] = numbers[4]
print(numbers)


numbers = [111, 7, 2, 1]
print(len(numbers))
print(numbers)

# list with .append() and .insert()
numbers.append(4)
print(len(numbers))
print(numbers)

numbers.insert(5, 222)
print(len(numbers))
print(numbers)
'''

#example 2
'''
my_list = []

for i in range(5):
    my_list.append(i + 1)
print(my_list)

my_list = [10, 1, 8, 3, 5]
total = 0

for i in range(len(my_list)):
    total += my_list[i]

print(total)


my_list = [10, 1, 8, 3, 5]
total = 0

for i in my_list:
    total += i

print(total)
'''

# Scenario
beatles = []
print("Step 1:", beatles)

beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("Step 2:", beatles)

for member in ["Stu Sutcliffe", "Pete Best"]:
    new_member = member
    beatles.append(new_member)
print("Step 3:", beatles)

del beatles[-1]
del beatles[-1]
print("Step 4:", beatles)

beatles.insert(0, "Ringo Starr")
print("Step 5:", beatles)

