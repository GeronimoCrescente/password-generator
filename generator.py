import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
           'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
capitalLetters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                  'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
specialCharacters = ['_', '-', '#', '$', '%', '&', '/', '?', '*', '+']

options = [letters, specialCharacters, numbers, capitalLetters]


def generate(large, special_cht, num, cap_letters):
    # This function basically create the password with the preferences of the user,
    # that´s the parameters that receive. includes special characters, numbers and capital letters.
    password = ''
    i = 0
    while i != large:
        i += 1
        # bounded_range is a variable for compare te number that receive and delimit the range of options
        bounded_range = random.randint(0, 3)
        if special_cht and num and cap_letters:
            password += random.choice(options[bounded_range])
        elif special_cht:
            if num:
                password += random.choice(options[random.randint(0, 2)])
            elif cap_letters:
                if bounded_range != 2:
                    password += random.choice(options[bounded_range])
            else:
                password += random.choice(options[random.randint(0, 1)])
        elif num:
            if cap_letters:
                if bounded_range != 1:
                    password += random.choice(options[bounded_range])
            else:
                if bounded_range != 1 and bounded_range != 3:
                    password += random.choice(options[bounded_range])
        elif cap_letters:
            if bounded_range != 1 and bounded_range != 2:
                password += random.choice(options[bounded_range])
        else:
            password += random.choice(options[0])
    return password

