string = input('Enter the word you want to check : ').lower()
reversed_string = string[::-1]
if reversed_string == string :
    print('It is a palindrome')
else :
    print('It is not a palindrome')
