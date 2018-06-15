# Translate a string to pig latin


def pig_latin_word(word):
    """ Return word tranlated into pig latin """
    pigLatinWord = word[1:] + '-' + word[0] + 'ay'

    return pigLatinWord
    

print('Welcome to the Pig Latin Translator')
inputStr = input('Please input a word to be translated: ')

while (inputStr != ''):
    
    print(pig_latin_word(inputStr))

    inputStr = input('Please input a word to be translated: ')
    
    
    
