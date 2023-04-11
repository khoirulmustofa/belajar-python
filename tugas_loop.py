# bilangan 1 sampai 100
# Habis di bagi 3 cetak BOOM
# Habis dibagi 5 Cetak DOOR
# Kalo habis dibagi 3 dan 5 cetak JOSS

for number in range(1,101):
    if number % 3 == 0 and number % 5 == 0:
        print(f"{number} JOSS")
    if number % 3 == 0:
        print(f"{number} BOOM")
    elif number % 5 == 0:
        print(f"{number} DOOR")        
    else :
        print(number)