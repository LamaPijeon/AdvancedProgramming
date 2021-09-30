import os
os.system('clear')

with open('plainText.txt', 'r') as rf:
    with open('plainTextCopy.txt', 'w') as wf:
        for line in rf:
            wf.write(line)