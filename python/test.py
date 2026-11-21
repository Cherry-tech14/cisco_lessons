'''
for i in range(1):
    print("#")
else:
    print("#")


var = 0
while var < 6:
    var += 1
    if var % 2 == 0:
        continue
    print("#")

var = 1
while var < 10:
    print("#")
    var = var << 1

z = 10
y = 0
x = y < z and z > y or y > z and z < y
print(x)

a = 1
b = 0
c = a & b
d = a | b
e = a ^ b

print(c + d + e)

my_list = [3, 1, -2]
print(my_list[my_list[-1]])

my_list = [1, 2, 3, 4]
print(my_list[-3:-2])

vals = [0, 1, 2]
vals[0], vals[2] = vals[2], vals[0]
print(vals)

vals = [0, 1, 2]
vals.insert(0, 1)
del vals[1]
print(sum(vals))

nums = [1, 2, 3]
vals = nums
del vals[1:2]
print(vals)


my_list_1 = [1, 2, 3]
my_list_2 = []
for v in my_list_1:
    my_list_2.insert(0, v)
print(my_list_2)

my_list = [1, 2, 3]
for v in range(len(my_list)):
    my_list.insert(1, my_list[v])
print(my_list)

t = [[3-i for i in range (3)] for j in range (3)]
s = 0
for i in range(3):
    s += t[i][i]
print(s)

my_list = [[0, 1, 2, 3] for i in range(2)]
print(my_list[2][0])


def f(x):
    if x == 0:
        return 0
    return x + f(x - 1)


print(f(3))

def fun(x):
    x += 1
    return x


x = 2
x = fun(x + 1)
print(x)


dictionary = {}
my_list = ['a', 'b', 'c', 'd']

for i in range(len(my_list) - 1):
    dictionary[my_list[i]] = (my_list[i], )

for i in sorted(dictionary.keys()):
    k = dictionary[i]
    print(k)
    
def func_1(a):
    return a ** a


def func_2(a):
    return func_1(a) * func_1(a)


print(func_2(2))


try:
    value = input("Enter a value: ")
    print(value/value)
except ValueError:
    print("Bad input...")
except ZeroDivisionError:
    print("Very bad input...")
except TypeError:
    print("Very very bad input...")
except:
    print("Booo!")
    
my_list = [1, 2]

for v in range(2):
    my_list.insert(-1, my_list[v])

print(my_list)

print("a", "b", "c", sep="sep")

x = 1 // 5 + 1 / 5
print(x)

dct = {'one': 'two', 'three': 'one', 'two': 'three'}
v = dct['three']

for k in range(len(dct)):
    v = dct[v]

print(v)

def fun(x, y):
    if x == y:
        return x
    else:
        return fun(x, y-1)

print(fun(0, 3))


tup = (1, 2, 4, 8)
tup = tup[-2:-1]
tup = tup[-1]
print(tup)

dct = {}
dct['1'] = (1, 2)
dct['2'] = (2, 1)

for x in dct.keys():
    print(dct[x][1], end="")


def fun(inp=2, out=3):
    return inp * out


print(fun(out=2))

lst = [[x for x in range(3)] for y in range(3)]

for r in range(3):
    for c in range(3):
        if lst[r][c] % 2 != 0:
            print("#")

'''



