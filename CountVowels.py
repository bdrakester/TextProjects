# Count the number of vowels in a String
# Bonus - report a sum of each vowel

def is_vowel(char):
    if ((char == 'a') or (char == 'e') or (char == 'i') or (char == 'o')
        or (char == 'u')):
        return True
    else:
        return False

vowelCount = 0
vowels = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

inputStr = input('Enter a string... ')
while (inputStr != ''):
    for letter in inputStr:
        if(is_vowel(letter)):
            vowelCount = vowelCount + 1
            vowels[letter] = vowels[letter] + 1

    print('There are {} vowels'.format(vowelCount))
    for vowel in vowels:
        print('There were {} {}'.format(vowels[vowel],vowel))

    inputStr = input('Enter another string... ')
    
