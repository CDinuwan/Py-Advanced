myset = {1, 2, 3, 4, 5}
print(myset)

myset = set("Hello")
print(myset)

myset = set()
print(type(myset))

myset.add(1)
myset.add(2)
myset.add(3)

myset.remove(3)
print(myset)

myset.discard(3)
print(myset)
# Don't happen key error in here.

item = myset.pop()
print(item)

for i in myset:
    print(i)

if 1 in myset:
    print("Yes")
else:
    print("No")

odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}

union = odds.union(evens)
print(union)

intersection = odds.intersection(primes)
print(intersection)

different = odds.difference(primes)
print(different)

diff = primes.symmetric_difference(evens)
print(diff)

odds.update(evens)
print(odds)

odds.intersection_update(primes)
print(odds)

odds.difference_update(evens)
print(odds)

odds.symmetric_difference_update(evens)
print(odds)

print(primes.issubset(odds))

print(primes.issuperset(odds))

print(primes.isdisjoint(evens))

evens = odds
print(evens)

# Common copy principle work in here

evens = odds.copy()

evens = set(odds)

a = frozenset([1, 2, 3, 4])
print(a)

# In here, Can create immutable set
