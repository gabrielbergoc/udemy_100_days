import random
import json

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
           'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G',
           'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*',]

with open("random_words.json") as file:
    words = json.load(file)

print(len(words))

def password_generator_v2():
    password = [
        random.choice(words).capitalize(),
        random.choice(symbols),
        str(random.randint(1000, 9999))
    ]

    return "".join(password)


def password_generator():
    nr_letters = 20
    nr_symbols = 10
    nr_numbers = 10

    password = [random.choice(letters) for i in range(nr_letters)]\
             + [random.choice(symbols) for j in range(nr_symbols)]\
             + [random.choice(numbers) for k in range(nr_numbers)]

    random.shuffle(password)

    pass_str = "".join(password)

    print(pass_str)

# if __name__ == '__main__':
#     print(password_generator_v2())