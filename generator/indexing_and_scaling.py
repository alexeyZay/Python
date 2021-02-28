greeting='Hello Python!'
string_length=len(greeting)
print(string_length)
char_13 = greeting[12]
print(char_13)
print(greeting[0])
# indexing from the end of the string
print(greeting[-1]) # the last symb will be dispalyed

# Slicing getting the part of the sting starting from specified char and ends with specified char,
# also step between chars can be defined as a third param

print(greeting[1:5])#char with index 5 won't be included
print(greeting[1:5:3])
# to revert the string we can use -1 as a step param and other empty then string wil be printed from the end
print(greeting[::-1])
print(greeting[1::2])

greeting='Hello Python!'
print(greeting[3])

print('Hello Python!'[:2])
s='Hello Python!'
print(s[0]+s[1])
new_line='Hello Python!'[6]+'a'+'Hello Python!'[8:-3]
print(new_line)
