import csv

from requests import head
with open('/Users/24nowak_p/Desktop/School/Programming/Programming Class/AdvancedProgramming/Python/Online Games/Wordle/txt/possibleWords.csv', mode = 'r') as inp, open('/Users/24nowak_p/Desktop/School/Programming/Programming Class/AdvancedProgramming/Python/Online Games/Wordle/txt/possibleWordsTeehee.csv', 'w') as out:
     # csv_reader = csv.DictReader(inp)
     writer = csv.writer(out)
     header = ['word', '']
     writer.writerow(header)
     

     for row in csv.reader(inp):
          if row[0] != 'word':
               inWord = 0
               duplicates = False  
               for x in range(5):
                    for y in range(5):
                         if row[0][x] in row[0][y]: inWord += 1
                    if inWord > 1: 
                         duplicates = True
                    inWord = 0     
                    data = ['Afghanistan', 652090, 'AF', 'AFG']
               if duplicates != True: writer.writerow(row)