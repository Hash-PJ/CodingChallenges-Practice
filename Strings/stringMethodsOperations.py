'''This is a python program showing all operations/methods that can be performed /used on strings.'''
# random text
st = "This is a python program for string operations. Strings in Python are arrays of bytes representing unicode characters. However, Python does not have a character data type, a single character is simply a string with a length of 1. Square brackets can be used to access elements of the string."
# slicing: stringVarName[startIndex:endIndex:steps]
print('String:',st)
print('Complete String by slicing: string[:] =',st[:]) 
print('st==st[:] =',st==st[:])
print('String from some index to another index: string[2:17] =',st[2:17])
print('String with steps: string[::2] =',st[::2])
print('String in reverse: string[::-1] =',st[::-1])
