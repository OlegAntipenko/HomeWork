class FormulaError(Exception):
    pass


def calc():
    st = input().split()
    if len(st) != 3:
        raise FormulaError("Не верный формат ввода")
    try:
        v1 = float(st[0])
        v2 = float(st[2])
    except ValueError:
        print("Не верные данные")

    if st[1] == '+':
        res = v1 + v2
        return print(res)
    elif st[1] == '-':
        res = v1 - v2
        return print(res)
    elif st[1] == '*':
        res = v1 * v2
        return print(res)
    elif st[1] == '/':
        if v2 != 0:
            res = v1 / v2
            return print(res)
        else:
            raise ZeroDivisionError("На ноль делить нельзя")
    else:
        raise FormulaError("Не верный формат ввода")


calc()
