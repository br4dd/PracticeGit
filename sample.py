def print_name(name):
    hasdigit = False
    for letter in name:
        if letter.isdigit():
            hasdigit = True
            break
    if not hasdigit:
        print(f'HI THERE, {name.upper()}')
    else:
        print("NAME MUST NOT CONTAIN DIGIT!")


input_name = input("ENTER YOUR NAME: ")
print_name(input_name)
