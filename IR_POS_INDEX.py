# importing libraries
import os
from nltk.tokenize import TweetTokenizer
from natsort import natsorted
import string


fileno = 1
pos_index = {}
file_map = {}


folder_names = [r"C:\Users\youss\OneDrive\Desktop\DocumentCollectiion"]


def read_file(filename):
    with open(filename, 'r') as f:
        stuff = f.read()
    f.close()
    return stuff


def remove_header_footer(final_string):
    new_final_string = ""
    tokens = final_string.split(' ')
    for token in tokens[1:-1]:
        new_final_string += token+" "
    return new_final_string


def preprocessing(final_string):
    tokenizer = TweetTokenizer()
    token_list = tokenizer.tokenize(final_string)
    table = str.maketrans('', '', '\t')
    token_list = [word.translate(table) for word in token_list]
    punctuations = (string.punctuation).replace("'", "")
    trans_table = str.maketrans('', '', punctuations)
    stripped_words = [word.translate(trans_table) for word in token_list]
    token_list = [str for str in stripped_words if str]
    token_list = [word.lower() for word in token_list]
    return token_list


for folder_name in folder_names:

    file_names = natsorted(os.listdir("" + folder_name))
    for file_name in file_names:

        stuff = read_file("" + folder_name + "\\" + file_name)
        token_list = preprocessing(stuff)
        for pos, term in enumerate(token_list):

            if term in pos_index:

                pos_index[term][0] = pos_index[term][0] + 1
                if fileno in pos_index[term][1]:
                    pos_index[term][1][fileno].append(pos)
                else:
                    pos_index[term][1][fileno] = [pos]

            else:

                pos_index[term] = []
                pos_index[term].append(1)
                pos_index[term].append({})
                pos_index[term][1][fileno] = [pos]

        file_map[fileno] =file_name
        fileno += 1


for item in pos_index:
    
    sample_pos_idx = pos_index[item]
    print(item , sample_pos_idx[1])
    file_list = sample_pos_idx[1]
    print("\n")
    for fileno, positions in file_list.items():
        print(file_map[fileno],"\t" , positions)
    print("\n======================================================================\n")
