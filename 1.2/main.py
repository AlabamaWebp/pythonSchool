print("y=ax^2+bx+c")
a = int(input("Введите a = "))
b = int(input("Введите b = "))
c = int(input("Введите c = "))
x = int(input("Введите x = "))
print("Ответ " + str(a*(x*x)+b*x+c))

print("Остаток от деления")
x = int(input("Введите x = "))
y = int(input("Введите y = "))
if y == 0:
    print("Делитель равен нулю")
else:
    print("Ответ " + str(x // y))

