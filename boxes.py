a = int(input())
s = int(input())
d = int(input())
f = int(input())
g = int(input())
h = int(input())

if (a == h and s == g and d == f) or (a == h and s == f and d == g):
    print("Boxes are equal")
elif (a == f and s == g and d == h) or (a == f and s == h and d == g):
    print("Boxes are equal")
elif (a == g and s == h and d == f) or (a == g and s == f and d == h):
    print("Boxes are equal")
elif (a >= f and s >= g and d >= h) or (a >= f and s >= h and d >= g) \
        or (a >= g and s >= f and d >= h) or (a >= g and s >= h and d >= f):
    print("The first box is larger than the second one")
elif (a >= h and s >= g and d >= f) or (a >= h and s >= f and d >= g):
    print("The first box is larger than the second one")
elif (a <= f and s <= g and d <= h) or (a <= f and s <= h and d <= g) \
        or (a <= g and s <= f and d <= h) or (a <= g and s <= h and d < f):
    print("The first box is smaller than the second one")
elif (a <= h and s <= g and d < f) or (a <= h and s <= f and d <= g):
    print("The first box is smaller than the second one")
else:
    print("Boxes are incomparable")
