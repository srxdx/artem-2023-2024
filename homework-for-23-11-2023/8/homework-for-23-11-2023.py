'''
counter = 0
letters = ['Б', 'О', 'Р', 'И', 'С']
for a in letters:
    for b in letters:
        for c in letters:
            for d in letters:
                for e in letters:
                    for f in letters:
                        word = a + b + c + d + e + f
                        i = word.count('Б')
                        w = word.count('Р')
                        s = word.count('С')
                        if i == 1 and w == 1 and (s == 1 or s == 0):
                            counter += 1
print(counter)
'''

'''
counter = 0
letters = ['Я', 'Р', 'О', 'С', 'Л', 'А', 'В']
for a in letters:
    for b in letters:
        for c in letters:
            for d in letters:
                for e in letters:
                    word = a + b + c + d + e
                    m = word.count('Я')
                    z = word.count('Р')
                    t = word.count('О')
                    v = word.count('С')
                    y = word.count('Л')
                    i = word.count('А')
                    w = word.count('В')
                    if m <= 1 and z <= 1 and t <= 1 and v <= 1 and y <= 1 and i <= 1 and w <= 1 and (z + v + y + w > m + t + i):
                        counter += 1
print(counter)
'''


counter = 0
maximum = 0
addNums = []
file = open('17.txt')
for i in file:
    addNums.append(int(i))

for z in addNums:
    for x in addNums:
        if (z + x) % 80 == 0 and (z % 50 == 0 or x % 50 ==0) and z != x:
            counter += 1
            summ = z + x
            if summ > maximum:
                maximum = summ
print(counter, maximum)

'''
for i in range(174457, 174506):
    x = 1
    x = x + 1
    counter = 0
    if i % x == 0:
        counter += 1
        if counter == 2:
            print(i)
            print(x)
'''        
