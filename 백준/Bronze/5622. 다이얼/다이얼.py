list1 = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
word = input()

time = 0
for unit in list1 :
    for i in unit: 
        for x in word:
            if i == x:
                time += list1.index(unit)+3
print(time)