n = int(input("What number is n: "))
array = []
for i in range(n):
    array.append(i)

print(array)

n_del = int(input("what number you want to delete: "))
array.pop(n_del)
print(array)