# Tuple:ordered,immutable,allows duplicate elements

import timeit
import sys

mytuple = ("Max", 28, "Boston", "Fineland", "Chanuka")
print(type(mytuple))

# mytuple = ("Max")
# print(type(mytuple))

mytuple1 = ("Max", "Jhone")
name, name2 = mytuple1
print(name+name2)

item = mytuple[0]
print(item)

item = mytuple[-1]
print(item)

for i in mytuple:
    print(i)


if "Max" in mytuple:
    print("Yes")
else:
    print("No")

print(len(mytuple))

print(mytuple.count('p'))

print(mytuple.index('Max'))

my_list = list(mytuple)
print(my_list)

my_tuple2 = tuple(mytuple)
print(my_tuple2)

print(mytuple[0:2])

print(mytuple[::2])

mytuple = (1, 2, 3, 4, 5)
i1, *i2, i3 = mytuple
print(i1)
print(i2)
print(i3)


my_list = [0, 1, 2, "hello", True]
my_tuple = (0, 1, 2, "hello", True)
print(sys.getsizeof(my_list), "bytes")
print(sys.getsizeof(my_tuple), "bytes")

print(timeit(stmt="[0,1,2,3,4,5]", number=100000))
print(timeit(stmt="(0,1,2,3,4,5)", number=100000))
