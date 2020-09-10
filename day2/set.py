my_set = {1, 3}
print(my_set)
my_set.add(2)
print(my_set)
my_set.update([4, 5], {1, 6, 8})
print(my_set)
my_set.remove(6)
print(my_set)
my_set.discard(2)
print(my_set)
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print(A | B)
print(A & B)
print(A - B)
print(B - A)
print(A ^ B)