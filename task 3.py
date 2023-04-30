x = list(map(int, list(iput())))
left = sum(x[0:-3])  #с помощью среза получаем от 0 элемента до 3 с конца
right = sum(x[-3:])  #с помощью среза получаем сумму последних трёх чисел
if left == right:
    print("yes")
else:
    print("no")