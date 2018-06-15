# Prompt for a string, reverse it



inputStr = input('Please enter a string to be reversed:   ')

while (inputStr != ''):
    outputStr = ''
    index = len(inputStr) - 1
    while (index >= 0):
        outputStr = outputStr + inputStr[index]
        index = index - 1

    print(outputStr)

    inputStr = input('Please enter a string to be reversed:   ')

    


    
