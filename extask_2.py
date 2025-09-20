num = int(input())


def digital_root(number):
    while number // 10 != 0:
        digital_root = 0
        for sym in str(number):
            digital_root += int(sym)
        number = digital_root
    return number
