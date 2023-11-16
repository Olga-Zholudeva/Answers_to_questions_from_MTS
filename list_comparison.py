a = [0, 1, 2, 3, 4]
b = [4, 5, 6, 7, 8]

count = sum(1 for i in a if i in b)
if count > 0:
    print(f'В списке b {count} элемент/ов из списка a')
else:
    print('В списке b нет ни одного элемента из списка a')
