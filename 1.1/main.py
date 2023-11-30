def access(l):
    try:
        if int(l) >= 18:
            print("Добро пожаловать!")
        else:
            print("Доступ запрещён")
        return True
    except ValueError:
        access(input("Введите целое число "))
        return False


def main():
    print("Hello World")
    tmp = input("Введите имя ")
    print("Hello " + tmp)
    i = input("Введите возраст ")
    access(i)


if __name__ == "__main__":
    main()
