file = open('D:/Python102/text.txt')
'''
(file.read())
print(file.readline())
print(file.readline())
print(file.readline())
'''
for line in file:
    print(line)
file.close()

with open ('D:/Python102/text.txt') as file:
    for line in file:
        print(line)