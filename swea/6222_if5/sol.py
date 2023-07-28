import sys
sys.stdin = open('input.txt')

char = input()

if char.isupper():
    print(f'{char}(ASCII: {ord(char)}) => {char.lower()}(ASCII: {ord(char.lower())})')
else:
    print(f'{char}(ASCII: {ord(char)}) => {char.upper()}(ASCII: {ord(char.upper())})')