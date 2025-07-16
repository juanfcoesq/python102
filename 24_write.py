with open ('D:/Python102/text.txt', 'w+') as file:
    for line in file:
        print(line)
    file.write('new stuff in this file\n')
    file.write('another line\n')
    file.write('another stuff in this file\n')