#1: Correct the typo and print out the correct word for the user input
''' Suppose the typos are a problem that repeats over and over again
The better way to do it includes (1) a script and save it; (2) using
a function.
A Python function is a block-code unit in while code elements are defined in
different scopes.
The top scope include
1) the keyword def, 2) the name of the function (given by the
programmer), 3) a pair of parentheses, and 4) a colon sign. The top scope can start at any point
from left side. But, the good practice expects starts to type the def keyword
from the 0 position in the editior/ IDLE.

for example, the top level scope 'def correct_typo():' in the parenthese
you may define some parameters (given some names) which do not require
initialization.
In general, after the colon sign, all the code are considered in the 2nd scope
(body),which must be type by an indentation(a space or tab).

A Python module is basically a text/code file with .py extension.
A Python script is a text/code file with .py extension.
Basically, a modele is a script. But, in general, we use the term
'script' to refer a small module.
'''
def correct_typo ():
    '''Correct specific typos that reoccur frequently.''' #a docstring uses to document the purpose of the funtion
                                                          # or a set of Python statements that solve a problem.
    user_input = input("Enter the 1st word: ")
    # if colon operator correctly used inside a pair of square brackets,
    # the colon operator is a slicing operator.
    # user_input[:2] will produce a substring of the user_input string; the
    # string will consist of the first two characters of the original string.
    # For example, Farenheit (original string)
    #        index 0123... (right exclusive- does not include char with index 2)
    # user_input[:2] -> 'Fa'
    corr = user_input[:2] + 'h' + user_input[-7 : ]
    print('Typo : ' + user_input + ' Correction: ' + corr)
    user_input = input('Enter the 2nd word: ')
    corr = user_input[0:3] + user_input[4:7] + user_input[9: ]
    print('Typo: ' + user_input + ' Correction: ' +corr)

correct_typo() #a function call statement which calls the function in a runtime in order to execute the function.

# Way 2: string built-in method, replace()
def correctTypo ():
    user_input = input('enter a word')
    corr = user_input.replace('r', 'hr') #replace() replaces the 1st argument in the string named user_input with the 2nd argument. The important syntax rule for using a method
                                         # is that it must be attatched to a specific object. In this case the object is the str user_input. 'picking' or 'pointing to'
    print('Typo : ' + user_input + ' Correction: ' + corr)
    user_input = input('enter a word')
    corr = user_input.replace('ilical', 'lic')
    print('Typo : ' + user_input + ' Correction: ' + corr)
    
