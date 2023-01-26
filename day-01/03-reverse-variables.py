# Take an input and reverse the order of the variables
first = input('first: ')
second = input('second: ')

holder = first
first = second
second = holder 

print(first)
print(second)