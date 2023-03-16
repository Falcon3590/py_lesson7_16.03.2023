from library import *

Q = int(input("0 - изменить номер, 1 - удалить номер: "))
if Q == 0:
    name = input("Введите фамилию или имя: ")
    numb = input("Введите номер телефона: ")
    file = open("telephone.txt", "r+", encoding="utf-8")
    new_file = ""
    for i in file:
        x = changes(name, i, numb)
        new_file += x
        print(x)
    file.close()

elif Q == 1:
    name = input("Введите фамилию или имя: ")
    file = open("telephone.txt", "r+", encoding="utf-8")
    new_file = ""
    for i in file:
        y = delete1(name, i)
        new_file += y
        print(y)
    file.close()
file = open("telephone.txt", "w", encoding="utf-8")
file.write(new_file)
file.close()
