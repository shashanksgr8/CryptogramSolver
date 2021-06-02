#_______________________________________________________________________________________________________________#
#                                                                                                               #
# Sandbox area to test out code snippets before inclusion in cryptogram_solver.py.                              #
# Leave in code under testing, comment out code if needed for later                                             #
# reference, or delete code that is no longer wanted.                                                           #
# _______________________________________________________________________________________________________________#
#                                      1 June 2021                                                              #
# _______________________________________________________________________________________________________________#
#                                                                                                               #
#   10. ONCE ALL ARRAY ELEMENTS HAVE BEEN MATCHED COMPARE ELEMENTS TO THE DICTIONARY AND RE-ORDER ARRAY         #
#                                                                                                               #
#   11. CONCATENATE ARRAY INTO A PROPER SENTENCE                                                                #
#_______________________________________________________________________________________________________________#

import re

name : str
name = input('\nWhat shall I call you? \n\n')
if re.search(r'^[a-zA-Z\s\D\.]+$', name):
    print('\nHello' + ' ' + name + '!\n')
else:
    print('\nPlease avoid using any special charecters. \nYour name is special enough.\n\n')
