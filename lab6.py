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


if __name__ == '__main__':
    print('Menu')
    print('-------------')
    print('1. Encode')
    print('2. Decode')
    print('3. Quit')
    selection = int(input('Please enter an option:'))
    if selection == 1:
        password = (input('Please enter your password to encode:'))
        (encode(password))
