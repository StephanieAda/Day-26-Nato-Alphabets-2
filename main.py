import pandas

nato_data = pandas.read_csv('nato_phonetic_alphabet.csv')
# print(nato_data)

nato_dict = {row.letter: row.code for (index, row) in nato_data.iterrows()}
# print(nato_dict)

# Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Enter a word? ").upper()
user_input_list = list(user_input)
user_list = [nato_dict[item] for item in user_input_list]

print(user_list)

# ...........OR........ Which is not in order by the way
# user_input_dict = [value for (key, value) in nato_dict.items() if key in user_input_list]
# print(user_input_dict)
