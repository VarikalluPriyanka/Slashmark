import random


def generate_password(pw_lengths):
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    passwords = []

    for length in pw_lengths:

        password = ""
        for _ in range(length):
            next_letter_index = random.randrange(len(alphabet))
            password += alphabet[next_letter_index]

        password = replace_with_number(password)
        password = replace_with_uppercase_letter(password)

        passwords.append(password)

    return passwords


def replace_with_number(p_word):
    for _ in range(random.randrange(1, 3)):
        replace_index = random.randrange(len(p_word) // 2)
        p_word = p_word[:replace_index] + str(random.randrange(10)) + p_word[replace_index + 1:]
    return p_word


def replace_with_uppercase_letter(p_word):
    for _ in range(random.randrange(1, 3)):
        replace_index = random.randrange(len(p_word) // 2, len(p_word))
        p_word = p_word[:replace_index] + p_word[replace_index].upper() + p_word[replace_index + 1:]
    return p_word


def main():
    num_passwords = int(input("How many passwords do you want to generate? "))

    print("Generating " + str(num_passwords) + " passwords")

    password_lengths = []

    print("Minimum length of password should be 3")

    for i in range(num_passwords):
        length = int(input("Enter the length of Password #" + str(i + 1) + " "))
        if length < 3:
            length = 3
        password_lengths.append(length)

    passwords = generate_password(password_lengths)

    for i in range(num_passwords):
        print("Password #" + str(i + 1) + " = " + passwords[i])


main()
