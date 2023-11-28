def addition():
    x = input("Введите x: ")
    y = input("Введите y: ")
    return x + " + " + y + " = " + str(float(x) + float(y))


def subtraction():
    x = input("Введите x: ")
    y = input("Введите y: ")
    return x + " - " + y + " = " + str(float(x) - float(y))


def multiplication():
    x = input("Введите x: ")
    y = input("Введите y: ")
    return x + " * " + y + " = " + str(float(x) * float(y))


def division():
    x = input("Введите x: ")
    y = input("Введите y: ")
    return x + " / " + y + " = " + str(float(x) / float(y))


def after_operation(result, history):
    history.append(result)
    print(result)
