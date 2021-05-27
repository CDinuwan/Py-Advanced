try:
    f = open('Samefile.txt')
except FileNotFoundError:
    print("You have an error")

try:
    a = 5 / 0
    b = 5 / 'a'
except ZeroDivisionError:
    print("You divided by 5 in 0.")
except TypeError:
    print("There is a Type error in here")
except Exception as e:
    print(e)
else:
    print("Every thing is fine")
finally:
    print("Cleaning up")

x = 5
if x < 0:
    raise Exception('x should be positive')

x = -5
assert (x >= 0), 'X is not positive'


class ValueToHighError(Exception):
    pass


def test_value(x):
    if x > 100:
        raise ValueToHighError('value is too high')


test_value(200)

try:
    test_value(200)
except ValueToHighError as e:
    print(e)

try:
    test_value(500)
except ValueToHighError as e:
    print(e)
