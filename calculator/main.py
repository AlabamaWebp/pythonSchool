import modules.operations as op


def print_hint():
    print("""Выберите опреацию
1. Сложение
2. Вычитание
3. Умножение
4. Деление
5. История
6. Выход""")

def main():
    print("Операции над X и Y")
    history = list()
    print_hint()
    while True:
        inp = input()
        if inp == "1":
            result = op.addition()
            op.after_operation(result, history)
        elif inp == "2":
            result = op.subtraction()
            op.after_operation(result, history)
        elif inp == "3":
            result = op.multiplication()
            op.after_operation(result, history)
        elif inp == "4":
            result = op.division()
            op.after_operation(result, history)
        elif inp == "5":
            print(history)
        elif inp == "6":
            break
        else:
            print("Неверный ввод")
            print_hint()


if __name__ == "__main__":
    main()
