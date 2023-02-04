# for i in range(5):
#     print(i)


# loop di mulai dari 1 di stop dibawah 10
# for i in range(2, 10):
#     print(i)


# range(start, max, step)
# for i in range(2, 11, 3):
#     print(i)
# 2
# 5
# 8

# fruits = ['apple', 'banana', 'cherry']
# # print(fruits[1])
# for i in range(len(fruits)):
#     print(i, fruits[i])


# print(5**3)
squares = [x**2 for x in range(1, 11)]
print(squares)

# Output:
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


for i in range(3):
    for j in range(3):
        print("i:", i, "j:", j)

# Output:
# i: 0 j: 0
# i: 0 j: 1
# i: 0 j: 2
# i: 1 j: 0
# i: 1 j: 1
# i: 1 j: 2
# i: 2 j: 0
# i: 2 j: 1
# i: 2 j: 2


# for i in range(1, 101):
#     # kalo bilangan itu ganjil maka cetak tulisan GANJIL
#     # kalo bilangan itu genap maka cetak tulisan GENAP
#     print(i)

for number in range(1, 101):
    if number % 2 == 0:
        print(f"{number} GENAP")
    else:
        print(f"{number} GANJIL")

# 1 GANJIL
# 2 GENAP


# Habis di bagi 3 cetak BOOM
# Habis dibagi 5 Cetak DOOR
# Kalo habis dibagi 3 dan 5 cetak JOSS

