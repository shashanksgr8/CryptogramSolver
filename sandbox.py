# Sandbox area to test out code snippets before inclusion in cryptogram_solver.py.
# Leave in code under testing, comment out code if needed for later
# reference, or delete code that is no longer wanted.

###############################################################################
###############################################################################
# tkinter GUI test run – leave untouched
###############################################################################
# import re
# import tkinter as tk
# from tkinter import messagebox
#
# cipher: str
# clue_key: str
# clue_value: str
# fields = 'Cryptogram', 'Clue (e.g. w=b)'
# flag_cipher_error: bool
# flag_code_error: bool
#
#
# def clue_checker(clue):
#     # Ask the user to give us x=y type clue for our cipher
#     global clue_key
#     global clue_value
#     # Make sure the clue is not empty
#     if not (clue is None or clue == ''):
#         # Strip all spaces and convert to lowercase
#         clue = re.sub(r'(\s+)', "", clue.rstrip()).lower()  # rstrip() removes trailing spaces
#         # RegEx to check the clue is of the form x=y that we need
#         if re.search(r'^[a-z]+=+[a-z]$', clue):
#             # Split at '=' and save the first part [0] as key and the second part [1] as value
#             clue_key = re.split("=", clue)[0]
#             clue_value = re.split("=", clue)[1]
#         else:
#             # If the clue is not of the format we need
#             alert('Something is wrong with your clue. Please re-enter the clue.', 'OK')
#     else:
#         # If the clue is blank
#         alert('You have not entered a clue. Please retry.', 'OK')
#
#
# def cipher_checker(cryptogram):
#     # The line below tells Python we're going to use the same
#     # global variable called cipher and that we are not creating
#     # a new function-specific one also called cipher
#     global cipher
#     # Check if input follows RegEx for a typical cryptoquip
#     if not re.search(r'^(?!.*\/)[a-zA-Z\s\D.,\-\'\"?!]+$', cryptogram):
#         # If it does not follow RegEx inform the user and restart the function
#         # and give the user an option to quit
#         alert('Invalid cryptogram. Please retry.', 'Retry')
#     else:
#         # If the RegEx is fine, replace double spaces with single spaces and remove trailing spaces
#         cipher = re.sub(r'(\s\s+)', " ", cryptogram.rstrip())  # rstrip() removes trailing spaces
#
#
# def fetch(entries):
#     global cipher, clue_key, clue_value
#     for entry in entries:
#         if entries.index(entry) == 0:  # entries index 0 is the cipher
#             cipher_checker(entry[1].get())  # entry[1] is the value of the cipher
#         if entries.index(entry) == 1:  # entries index 1 is the clue
#             clue_checker(entry[1].get())  # entry[1] is the value of the clue
#         # In both cases above entry[0] is the form field name
#     print('\nCryptogram: ' + cipher + '\nClue: ' + clue_key + '=' + clue_value + '.')
#
#
# def makeform(gui_window, gui_fields):
#     entries = []
#     for field in gui_fields:
#         row = tk.Frame(gui_window)
#         lab = tk.Label(row, width=15, text=field, anchor='w')
#         ent = tk.Entry(row)
#         row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
#         lab.pack(side=tk.LEFT)
#         ent.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
#         entries.append((field, ent))
#     return entries
#
#
# def alert(message, button_text):
#     alert_gui = tk.Tk()
#     messagebox.showerror('Error', message)
#     alert_button = tk.Button(root, text=button_text, command=root.destroy)
#     alert_button.pack(side=tk.LEFT, padx=5, pady=5)
#     quit_button = tk.Button(root, text=button_text, command=root.quit)
#     quit_button.pack(side=tk.LEFT, padx=5, pady=5)
#     alert_gui.mainloop()
#
#
# if __name__ == '__main__':
#     root = tk.Tk()
#     gui_form = makeform(root, fields)
#     root.bind('<Return>', (lambda event, e=gui_form: fetch(e)))
#     b1 = tk.Button(root, text='Solve',
#                    command=(lambda e=gui_form: fetch(e)))
#     b1.pack(side=tk.LEFT, padx=5, pady=5)
#     b2 = tk.Button(root, text='Quit', command=root.quit)
#     b2.pack(side=tk.LEFT, padx=5, pady=5)
#
#     # Bring GUI window to the front
#     root.attributes('-topmost', 1)
#     # Centre GUI window
#     # Give it a size
#     windowWidth = 300
#     windowHeight = 175
#
#     # Compute half the screen width/height and window width/height
#     positionRight = int(root.winfo_screenwidth() / 2 - windowWidth / 2)
#     positionDown = int(root.winfo_screenheight() / 2 - windowHeight / 2)
#
#     # Position the window in the center of the page.
#     root.geometry("+{}+{}".format(positionRight, positionDown))
#
#     # Execute in the main loop
#     root.mainloop()
###############################################################################
# End of tkinter GUI test run
###############################################################################
###############################################################################

########################## ONLY FOR TEST CASES ################################
original_list = ['a','thank','the','mode','works','.']
length_sorted_list = []
solution_dictionary = {'m' : 'c', '.' : '!'}
dictionary_memory = {}
clue_key = 'a'
clue_value = 'i'
#################### REMOVE IT AFTER CODE IS COMPLETED ########################

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
                dictionary_memory[compare.index(compare_element)] = original.index(original_element)
                # original.remove(original_element)


# def dictionary_builder(original, compare):
#     for original_element in original:
#         for compare_element in compare:
#             if original_element == compare_element:
#                 dictionary_memory[original_element] = compare.index(compare_element)
#                 compare.remove(compare_element)
#                 break
#############################################################################
#                                                                                           Sudheendra's part
#############################################################################

duplicated_list = original_list.copy()# Duplicating the list (string or list that I get from thr previous step)

def clue_substitutor():
    #global cipher
    global original_list
    global duplicated_list
    #global clue_key
    #global clue_value # These go in final code
    for each in duplicated_list:
        if (each == clue_key):
            duplicated_list = [sub.replace(each, clue_value.upper()) for sub in duplicated_list]
        else:
            break
    return duplicated_list

############################################################################

def word_sorter(): # Sort 2.0
    global dictionary_memory
    global length_sorted_list
    global duplicated_list
    # The original list would have been modified at step 8.
    # Call the corresponding list from step 8.
    for value in dictionary_memory.values():
        length_sorted_list[value] = duplicated_list[value]
    return length_sorted_list
    #Assuming the length_sorted_list will be of no use, modified it to be the final list.

# Converting list into a string for output (*)
def sentence_maker(list):   # White spaces brfore and after puntuations needs to be corrected
    global solution_dictionary
    sentence = ''
    for element in list:
        sentence+=element+' '
#     return sentence
# def letter_swapper():           # This was originally written as a separate function to substitute solution_dictionary.
    for key in solution_dictionary:
        sentence = sentence.replace(key, solution_dictionary[key])
    return sentence

if __name__ == '__main__':
    print('Original list\t',original_list)
    length_sorted_list = sort_list_by_length().copy()
    print('\n\nSorted list\t',length_sorted_list)
    dictionary_builder(original_list, length_sorted_list)
    print('\n\nDictionary\t',dictionary_memory)
    print('\nThe list after clue substitution \n\t\t', clue_substitutor())
    # print(original_list)
    # print(length_sorted_list)
    clue_substitutor()
    word_sorter()
    print('\n\nFinal list\t',length_sorted_list)  # Change it to the final list name
    print('\n\nThe sentence\t',sentence_maker(length_sorted_list))
    # letter_swapper()
