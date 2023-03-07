def encode(pass_w):
    new_pass = ''
    for i in pass_w:
        if i == str(7):
            digit = int(0)
            new_pass += str(digit)
        elif i == str(8):
            digit = int(1)
            new_pass += str(digit)
        elif i == str(9):
            digit = int(2)
            new_pass += str(digit)
        else:
            digit = int(i) + 3
            new_pass += str(digit)
    return str(str(new_pass))


def decode(password):
    digits = [num for num in password]
    new_pass = []
    for num in digits:
        int(num)
        if int(num) >= 3:
            new_dig = int(num) - 3
        elif int(num) == 2:
            new_dig = 9
        elif int(num) == 1:
            new_dig = 8
        elif int(num) == 0:
            new_dig = 7
        new_pass.append(str(new_dig))
    return ''.join(new_pass)


if __name__ == '__main__':
    while True:
        print('Menu')
        print('-------------')
        print('1. Encode')
        print('2. Decode')
        print('3. Quit')
        selection = int(input('Please enter an option:'))
        if selection == 1:
            password = (input('Please enter your password to encode:'))
            new_pass = (encode(password))
        if selection == 2:
            newer_pass = decode(new_pass)
            print(f'The encoded password is {new_pass}, and the original password is {newer_pass}.')
        if selection == 3:
            break
