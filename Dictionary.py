# Dictionary: key-Value pairs,Unordered,Mutable

myDic = {"name": "Chanuka", "age": 21, "City": "New York"}
print(myDic)

myDict2 = dict(name="Dinuwan", age=27, city="Boston")
print(myDict2)

value = myDic["age"]
print(value)

myDic["email"] = "hecdinuwan@gmail.com"
print(myDic)

myDic["email"] = "chanukadinuwan35@gmail.com"
print(myDic)

del myDict2["name"]
print(myDict2)

myDict2.popitem()
print(myDict2)

try:
    print(myDic["name"])
except:
    print("Error")

for key in myDic:
    print(key)

for key in myDic.keys():
    print(key)

# for key, value in myDic.values():
#     print(key+value)

for value in myDic:
    print(value)

# mydict_cpy = myDic
# print(mydict_cpy)

# When we update copy dictionary also update original dictionary.
# In here these two variable pointed to same container.

# myDic.update(myDict2)
# print(myDic)

my_dict = {3: 9, 6: 36, 9: 81}
print(my_dict)

value = my_dict[3]
print(value)

mytuple = (8, 7)
mydict = {mytuple: 15}

print(mydict)
