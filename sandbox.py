# from PyDictionary import PyDictionary
from nltk.corpus import words
from nltk.corpus import wordnet as wn

########################## ONLY FOR TEST CASES ##############################

# Name suggestion: cipher_list.
original_list = ['a', 'do', 'not', 'thank', 'the', 'moDe', 'words']
length_sorted_list = []
solution_dictionary = {'solution_1': {
    'm': 'c', 'z': 'y'}, 'solution_2': {'d': 'x', 'j': 'z'}}
# Keep in mind the format of nested dictionary.
dictionary_memory = {}
clue_key = 'a'
clue_value = 'I'

#################### REMOVE IT AFTER CODE IS COMPLETED ######################


def sort_list_by_length():
    temp_list = []
    global original_list
    for i in range(0, len(original_list)):
        temp_list.insert(i, sorted(original_list, key=len)[i])
    return temp_list


def dictionary_builder(original, compare):
    for original_element in original:
        for compare_element in compare:
            if compare_element == original_element:
                dictionary_memory[compare.index(
                    compare_element)] = original.index(original_element)
                # original.remove(original_element)


duplicated_list = original_list.copy()
# Duplicating the cipher list (Step 7)


def clue_substitutor():  # (Step 8)
    # global cipher
    # global clue_key
    # global clue_value
    # # Only the above lines will be in final code.
    global duplicated_list  # Delete this.
    for each in duplicated_list:
        if (each == clue_key):
            duplicated_list = [sub.replace(
                each, clue_value.upper()) for sub in duplicated_list]
        else:
            break
    return duplicated_list


#   Below function is not necessary. But I will retain it just to be safe.

# def word_sorter():  # Sort 2.0
#     global dictionary_memory
#     global length_sorted_list
#     global duplicated_list
#     # The original list would have been modified at step 8.
#     # Call the corresponding list from step 8.
#     for value in dictionary_memory.values():
#         length_sorted_list[value] = duplicated_list[value]
#     return length_sorted_list
#     # Assuming the length_sorted_list will be of no use, modified it to be the final list.


def convert_to_string(list):
    # Converting list into a string for output. Thus the name.(*)
    # White spaces brfore and after puntuations needs to be corrected.
    global solution_dictionary
    sentence = ''
    for element in list:
        sentence += element + ' '
    return (sentence)


def make_uppercase(list):
    global duplicated_list
    for letter in list:
        list[list.index(letter)] = list[list.index(letter)].upper()
    return list


def dictionary_lookup(element):
    for eachword in element:
        if eachword not in words.words():
            # print('"' + eachword + '" is not in wordnet') # (1)
            if wn.synsets(eachword):
                # print('But it is in words()\n') # (2)
                # Uncomment (1) and (2) to see how this two level filtering works.
                continue
            else:
                print('Error404: No match found for "' +
                      eachword + '" in dictionary \n')
    # To-do:
    # insert some sort of flag here.
    # Such that those sentances which has incorrect substitution can be excluded from the outputs.
    return convert_to_string(element)


def letter_swapper():   # To substitute the solutions.
    global solution_dictionary
    for solution in solution_dictionary:
        sentence = duplicated_list
        for key in solution_dictionary[solution]:
            # sentence = sentence.replace(key,solution_dictionary[solution][key])
            sentence = [sub.replace(
                key, solution_dictionary[solution][key]) for sub in sentence]
        if dictionary_lookup(sentence):
            print('\nProbable answer: ', convert_to_string(
                make_uppercase(sentence)), '\n\n')
        else:
            break
    return sentence


def main():
    print('\nOriginal list: ', original_list)
    length_sorted_list = sort_list_by_length().copy()
    print('\nSorted list: ', length_sorted_list)
    dictionary_builder(original_list, length_sorted_list)
    print('\nDictionary: ', dictionary_memory)
    print('\nThe list after clue substitution: ', clue_substitutor())
    clue_substitutor()
    print('\n')
    convert_to_string(duplicated_list)
    letter_swapper()


if __name__ == '__main__':
    main()

###############################################################################
# #  Below is the test code for step 9.
###############################################################################
#
# from nltk.corpus import words
#
# word_list = words.words()
# # cipher = ['Just', 'a', 'trial', 'function']
# cipher = ['qwer', 't', 'ryuti', 'owNarusN']
# clue_key = 'p'
# clue_value = 'n'
#
# letter_position = []
# word_position = []
#
#
# def clue_finder(list):
#     global letter_position_pos
#     global word_position
#     for word in list:
#         for letter in range(len(word)):
#             if word[letter].isupper():
#                 # print('The clue: ', letter)
#                 # print('which appears at position: ', letter)
#                 letter_position.append(letter)
#                 word_position.append(cipher.index(word))
#         # return cipher.index(word)
#     print(word_position)
#     print(letter_position)
#
#
# def word_finder():
#     global letter_position
#     global word_position
#     global clue_value
#     solution_words = []
#     # solution_dictionary = dict()
#     for i in range(len(word_position)):
#         for j in range(len(word_list)):
#             if len(cipher[word_position[i]]) == len(word_list[j]):
#                 if word_position[i-1] != word_position[i]:
#                     if word_list[j][letter_position[i]] == clue_value:
#                         print(word_list[j])
#                         solution_words.append(word_list[j])
#                 if word_list[j][letter_position[i-1]] == clue_value and word_list[j][letter_position[i]] == clue_value:
#                     if word_list[j] not in solution_words:
#                         solution_words.append(word_list[j])
#         # for word in solution_words:
#         #     for letter in word:
#         #         print(letter + '\t' +
#         #               cipher[word_position[i]][word.index(letter)])
#         #         solution_dictionary[solution_words.index(word)] = {
#         #             cipher[word_position[i]][word.index(letter)]: letter} # Building a solution dictionary (Not working)
#     print(solution_words)
#     print(len(solution_words))
#     # print(solution_dictionary)
#
#
# def main():
#     clue_finder(cipher)
#     word_finder()
#
#
# if __name__ == '__main__':
#     main()
