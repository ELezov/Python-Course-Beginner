# Дано целое число, не меньшее 2.
# Выведите его наименьший натуральный делитель, отличный от 1.
a = int(input())
i = 2
s = 1
while s != 0:
    s = a % i
    if s != 0:
        i = i + 1
print(i)
