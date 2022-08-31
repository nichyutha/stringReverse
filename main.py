## Program to reverse a string
def reverseString(string):
    string = string[::-1]
    return string


print(reverseString('Digital Manufacturing'))


## Program to reverse the order of words in a string
def reverseOrder(string):
    string = ' '.join(string.split(' ')[::-1])
    return string


print(reverseOrder('Digital Manufacturing'))


## Program takes input string and flag to perform reverse operation

def userCommands(string, operation):
    if operation.lower() == '-r':
        return string[::-1]
    elif operation.lower() == '-w':
        word_list = string.split()
        # for word in word_list:
        #     return word[::-1]
        return ' '.join([word[::-1] for word in word_list])


userString = input("Enter string: ")
flag = input("Enter '-r' to reverse the string, '-w' to reverse the each word of string: ")
print(userCommands(userString, flag))


## Programme to read input sting from file name
def userCommandsFromFile(string, operation):
    if string.endswith('.txt'):
        with open(string) as f:
            content = f.read()
        string = content
    if operation.lower() == '-r':
        return string[::-1]
    elif operation.lower() == '-w':
        word_list = string.split()
        return ' '.join([word[::-1] for word in word_list])
    else:
        while True:
            operation = input('Please enter valid operation either "-r" or "-w": ')
            if operation == '-r' or operation == '-w':
                break
        return userCommandsFromFile(string, operation)


userInput = input('Enter string or text file name containing the string: ')
flag = input("Enter '-r' to reverse the string, '-w' to reverse the each word of string: ")
print(userCommandsFromFile(userInput, flag))
