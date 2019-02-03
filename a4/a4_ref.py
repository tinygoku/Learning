def second_letter(word):
	return word[1]  # the [1] means the character in index/position 1. Programming is very weird and everything starts at 0
					# so word[1] is actually the second letter.

# This is called a FUNCTION
def no_spaces(word):  # each function must have a "definition" (this line)
	return word.replace(" ", "")  # and most have a return value (sometimes you don't need to return anything) 


# it's important to make sure that your function definitions are placed above the code that calls them.
input = input("Type some words pls. ")
input_second_letter = second_letter(input)
input_no_spaces = no_spaces(input)

# a fancy way to format a string in python, could be of use.
print(str.format("The second letter of the word is '{word_letter}'. \nThe word stripped of spaces is '{word_spaces}'", word_letter=input_second_letter, word_spaces=input_no_spaces))