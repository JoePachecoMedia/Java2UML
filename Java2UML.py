import os

# extending for loop capabilities
from itertools import tee, islice, chain


def previous_and_next(some_iterable):
    prevs, items, nexts, nnexts = tee(some_iterable, 4)
    prevs = chain([None], prevs)
    nexts = chain(islice(nexts, 1, None), [None])
    nnexts = chain(islice(nnexts, 2, None), [None])
    return zip(prevs, items, nexts, nnexts)


global methodFinderVar
methodFinderVar = 0


def methodFinder(initialparen):  # ( ) then { found? Method!
    # print('calling methodFinder' + initialparen)
    if initialparen == '(':
        global methodFinderVar
        methodFinderVar = 1
        # print(methodFinderVar)
    elif initialparen == ')' and methodFinderVar == 1:
        methodFinderVar = 2
        # print(methodFinderVar)
    elif initialparen == '}':  # no method
        methodFinderVar = 0
        # print(methodFinderVar)
    elif initialparen == '{' and methodFinderVar == 2:
        f.writelines('()\n')
        methodFinderVar = 0
        # print(methodFinderVar)


# list that python will populate with method names
methodList = []

# load  keyword library
access_mod_list = ['public', 'private', 'protected', 'default']
void_list_id = ['void', 'double', 'int', 'String', 'boolean', 'float', 'byte', 'short', 'long', 'char']
bracket_list = ['{', '}', '(', ')']


def access_mod_func(mod):
    if mod == 'public'.casefold():
        return '+'
    elif mod == 'private'.casefold():
        return '-'
    elif mod == 'protected'.casefold():
        return '#'


java_file = open(str(input("enter file name: ")), 'r')  # This file will be in the same directory
code_string = java_file.read()
# code_string = ''
# 'class HelloWorld { public static void main( String[] args ) { System.out.println("Hello, World!"); } }'


mod_string = code_string.replace(
    '(', ' ( ').replace(')', ' ) ').replace(
    '}', ' } ').replace('{', ' { ').replace(
    '\n', '').replace(';', ' ; ').replace(
    '/', ' / ').replace('while', '').replace(
    '(i', ''
                        )

code_list = mod_string.split(' ')
code_list = list(filter(None, code_list))

print(code_list)

codeInitialize = 0
bracketsOpen = 0

# begin writing file
f = open("sourceCode.txt", "x")  # output same directory

# format for planttext
f.writelines('@startuml\n\n')
f.writelines('title Class Diagram\n\n')

for prevToken, token, nextToken, farToken in previous_and_next(code_list):
    # identify classes
    # case for new class
    if token == 'class'.casefold() and codeInitialize == 0:  # case for new class
        codeInitialize = 1
        bracketsOpen = 1
        f.writelines('class ' + nextToken + '{\n')
    elif token in access_mod_list:  # determine access modifier
        f.writelines(access_mod_func(token))
    elif token == 'static'.casefold():  # is it static?
        f.writelines('{static}')
    elif prevToken in void_list_id and nextToken == '(':  # determine method
        f.writelines('' + prevToken + ' ' + token + '')
    elif prevToken in void_list_id:  # determine variables
        f.writelines('' + prevToken + ' ' + token + '\n')
        # methodList.append(nextToken)    # add the nextToken to the method list
    # elif token in methodList and (nextToken == '=' or nextToken == ';'): # its a var!
    # methodList.pop()
    elif token in bracket_list:  # ( ) then { found? Method!
        methodFinder(token)
    else:
        print(token)

# print(methodList)

if bracketsOpen == 1:
    f.writelines('\n}\n\n')
    bracketsOpen = 0
f.writelines('@enduml')
f.close()

# for token in code_list:
#   if token in access_mod_list or token == 'class'.casefold():
#      f.writelines('class or method found --> ')
#  elif token in bracket_list:
#      f.writelines('*bracket*\n')
#  elif token in void_list_id:
#      f.writelines('-> ')
#  else:
#      f.writelines(token.title() + '\n')
