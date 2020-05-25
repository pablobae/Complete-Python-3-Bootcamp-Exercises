def ask_number():
    while True:
        try:
            num = int(input("How many happy number do you want?: "))
        except ValueError:
            print("You must enter a number")
            continue
        else:
            if num <= 0:
                print("You must enter a positive number")
                continue
            else:
                return num


def is_happy_number(number):
    if number <= 9:
        if number == 1:
            return True
        else:
            return False
    else:
        sum = 0
        for digit in str(number):
            sum += int(digit)
        return is_happy_number(sum)


if __name__ == '__main__':
    print('*** Happy number checker ***')

    total_numbers = ask_number()

    counter = 0
    num = 1
    while counter <= total_numbers:
        if is_happy_number(num):
            print(str(num) + " is happy!")
            counter += 1
        num += 1

    print("done!")
