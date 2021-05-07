# Collections: counter,namedtuple,orderedict,defaultdict,deque

from collections import Counter
from collections import namedtuple
from collections import OrderedDict
from collections import defaultdict
from collections import deque

a = "aaaaabbbbccc"
my_counter = Counter(a)
print(my_counter)

print(my_counter.items())
print(my_counter.keys())
print(my_counter.values())
print(my_counter.most_common(1)[0][0])

print(my_counter.elements())
print(list(my_counter.elements()))

Point = namedtuple('Point', 'x,y')
pt = Point(1, -4)
print(pt)
print(pt.x)
print(pt.y)

ordered_dict = OrderedDict()
ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['d'] = 4
print(ordered_dict)

d = defaultdict(float)
d['a'] = 1
d['b'] = 2
print(d)
print(d['c'])

de = deque()

de.append(1)
de.append(2)
de.appendleft(3)
print(de)

de.pop()
print(de)

de.extend([4, 5, 6])
print(de)

de.extendleft((5, 6, 9))

de.rotate(1)
print(de)

de.rotate(-1)

de.clear()
print(de)
