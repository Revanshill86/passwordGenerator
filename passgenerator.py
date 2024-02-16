import random
import string


def generate_password(num_letters, num_numbers, num_symbols):
    letters = string.ascii_letters
    numbers = string.digits
    symbols = string.punctuation
    password = ''
    for letter in range(0, int(num_letters)):
        password += random.choice(letters)
    for number in range(0, int(num_numbers)):
        password += random.choice(numbers)
    for symbol in range(0, int(num_symbols)):
        password += random.choice(symbols)

    password_list = list(password)
    random.shuffle(password_list)
    password_shuffle = ''.join(password_list)
    return password_shuffle


def main():
    print('Welcome to the password generator')
    num_letters = input('How many letters do you want to use? ')
    num_numbers = input('How many numbers do you want to use? ')
    num_symbols = input('How many symbols do you want to use? ')

    password = generate_password(num_letters, num_numbers, num_symbols)
    print('Your password is ' + password)


if __name__ == "__main__":
    main()
