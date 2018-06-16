# Translate a string to pig latin


def pig_latin_word(word):
    """ Return word tranlated into pig latin """
    pigLatinWord = word[1:] + '-' + word[0] + 'ay'

    return pigLatinWord

    

print('Welcome to the Pig Latin Translator')
inputStr = input('Please input a phrase to be translated: ')

while (inputStr != ''):
    
    #print(pig_latin_word(inputStr))
    output = ''
    words = inputStr.split()
    for word in words:
        output = output + pig_latin_word(word) + ' '
    print(output)
        
    inputStr = input('Please input a word to be translated: ')
    
    
    
