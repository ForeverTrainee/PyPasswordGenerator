import random


def main():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = int(input("How many letters would you like in your password? "))
    nr_symbols = int(input("How many symbols would you like? "))
    nr_numbers = int(input("How many numbers would you like? "))
    password = []
    n = 0

    while n < nr_letters:
        n = n+1
        password.append(letters[random.randint(0,len(letters))])

    n = 0

    while n < nr_symbols:
        n = n+1
        password.append(symbols[random.randint(0,len(symbols))])

    n = 0

    while n < nr_numbers:
        n = n + 1
        password.append(numbers[random.randint(0, len(numbers))])

    random.shuffle(password)
    str_password = ''.join(password)
    print(str_password)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
