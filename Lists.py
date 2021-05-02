myList = ["banana", "cherry", "apple"]
print(myList)

item = myList[0]
print(item)

print()
for i in myList:
    print(i)

print()
item1 = myList[-1]
print(item1)

if "banana" in myList:
    print("Yes, Banana in this List.")
else:
    print("no")

print(len(myList))
myList.append("lemon")
print(myList)

myList.insert(1, "blueberry")
print(myList)

item = myList.pop()
print(item)
print(myList)

item = myList.remove("cherry")
print(myList)

item = myList.reverse()
print(item)

item = myList.sort()
print(item)

myList = [0]*5
print(myList)

myList2 = [1, 2, 3, 4, 5]
newList = myList+myList2
print(newList)

item = myList.clear()
print(item)

a = newList[5:10]
print(a)

a = newList[5::10]
print(a)

a = newList[::-1]  # Reverse trick
print(a)

# Copy List
list_org = ["banana", "cherry", "apple"]
list_cpy = list_org  # refer same list
print(list_cpy)

list_cpy.append("lemon")
# In here if we change copy list it also change main list element
print(list_org)
# Can use slicing [:],Can put list keyword to original list

# Lists :mutable,ordered,allows duplicate elements

myList1 = [1, 2, 3, 4, 5]
b = [i*i for i in myList1]
print(b)
