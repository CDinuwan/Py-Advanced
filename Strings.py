# Strings:ordered,immutable,text representation
import timeit

my_string = "Hello World"
print(my_string)

my_string = "I'm programmer"
print(my_string)

my_string = """I'm
    programmer"""
print(my_string)

char = my_string[0]
print(char)

substring = my_string[1:5]
print(substring)

substring = my_string[::2]
print(substring)

substring = my_string[::-1]
print(substring)

greeting = "Hello"
name = "Chanuka"

print(greeting+" "+name)  # String concatenation

for i in greeting:
    print(i)

if 'e' in greeting:
    print("Yes")
else:
    print("No")

# my_string = '          Hello World           '
print(my_string)

print(my_string.strip())

# Didn't change original

print(my_string.upper())
print(my_string.lower())

print(my_string.startswith('Hello'))
print(my_string.endswith('World'))
print(my_string.find('o'))
print(my_string.find('lo'))

print(my_string.count('p'))
print(my_string.replace('world', 'universe'))

my_string = "How are you doing"
my_list = my_string.split()
print(my_list)

new_string = ' '.join(my_list)
print(new_string)

my_list = ['a']*6
print(my_list)

start = timeit.default_timer()
my_string = ''
for i in my_list:
    my_string += i

# print(my_string)
# stop = timeit.default_timer()
# print(stop-start)

# start = timeit.default_timer()
# my_string = ''.join(my_list)
# print(my_string)
# stop = timeit.default_timer()
# print(stop-start)

# Formatting letters: %,format(),f-Strings

var = "Tom"
my_string = "The variable is %s" % var
print(my_string)

var = 3
my_string = "The variable is %d" % var
print(my_string)

var = 3.178
my_string = "The variable is %.2f" % var
print(my_string)

var = "Tom"
my_string = "The variable is {}".format(var)
print(my_string)

var = 3.178
my_string = "The variable is {:.2f}".format(var)
print(my_string)

var = 3.178
my_string = f"The variable is {var*2}"
print(my_string)
