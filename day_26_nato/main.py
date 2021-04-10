# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_alphabet = {row.letter: row.code for (index, row) in data.iterrows()}

def main():
    word = input("Type a word: ").upper()
    try:
        encoded = [nato_alphabet[letter] for letter in word]
    except KeyError:
        print("Letters only, please.")
    else:
        print(encoded)
    finally:
        main()

if __name__ == '__main__':
    main()