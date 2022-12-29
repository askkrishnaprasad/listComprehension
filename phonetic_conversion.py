import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
word = input("Enter the word to be converted: ").upper()
phonetic_dict = {row.letter: row.code for(index, row) in data.iterrows()}
output_list = [phonetic_dict[letter] for letter in word]
print(output_list)

