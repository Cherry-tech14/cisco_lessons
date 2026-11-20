'''
my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:3]
print(new_list)

# Negative slices
my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:-1]
print(new_list)

# del instruction in slices
my_list = [10, 8, 6, 4, 2]
del my_list[1:3]
print(my_list)


# The in and not in operators
my_list = [0, 3, 12, 8, 2]

print(5 in my_list)
print(5 not in my_list)
print(12 in my_list)

#example 2
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
to_find = 5
found = False

for i in range(len(my_list)):
    found = my_list[i] == to_find
    if found:
        break

if found:
    print("Element found at index", i)
else:
    print("absent")
'''

drawn = [5, 11, 9, 42, 3, 49]
bets = [3, 7, 11, 42, 34, 49]
hits = 0

for number in bets:
    if number in drawn:
        hits += 1

print(hits)




