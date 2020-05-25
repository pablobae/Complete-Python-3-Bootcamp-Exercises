def ask_number():
    while True:
        try:
            num = int(input("Please, enter a number greater than 1: "))
        except ValueError:
            print("You must enter a number")
            continue
        else:
            if num <= 1:
                print("You must enter a number greater than 1")
                continue
            else:
                return num


def collatz_conjecture(num):
    if num > 1:
        if num % 2 == 0:
            print("{} / 2 = {}".format(num, num // 2))
            num = num // 2
        else:
            print("{} * 3 + 1 = {}".format(num, num * 3 + 1))
            num = num * 3 + 1

        return 1 + collatz_conjecture(num)
    else:
        return 0


if __name__ == '__main__':
    print('*** Collatz Conjecture ***')

    number = ask_number()
    print("Steps: " + str(collatz_conjecture(number)))
