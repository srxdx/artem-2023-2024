'''
counter = 0
alph = ['1', '2', '3', '4']
for a in alph:
    for b in alph:
        for c in alph:
            for d in alph:
                for e in alph:
                    counterOne = 0
                    word = a + b + c + d + e
                    if a == '1':
                        counterOne += 1
                    if b == '1':
                        counterOne += 1
                    if c == '1':
                        counterOne += 1
                    if d == '1':
                        counterOne += 1
                    if e == '1':
                        counterOne += 1
                    if counterOne == 2:
                        counter += 1
print(counter)
                
'''
'''
counter = 0
alph = ['1', '2', '3', '4']
for a in alph:
    for b in alph:
        for c in alph:
            for d in alph:
                for e in alph:
                    counterOne = 0
                    word = a + b + c + d + e
                    for f in word:
                        if f == '1':
                            counterOne += 1
                    if counterOne == 2:
                        counter += 1
print(counter)
'''



'''
counter = 0
alph = ['1', '2', '3', '4']
for a in alph:
    for b in alph:
        for c in alph:
            for d in alph:
                for e in alph:
                    word = a + b + c + d + e
                    counterOne = word.count('1')
                    if counterOne == 2:
                        counter += 1
print(counter)
'''
'''
counter = 0
alph = 'пятница'
for a in 'пятица':
    for b in alph:
        for c in alph:
            for d in alph:
                for e in alph:
                    word = a + b + c + d + e
                    if word[0] != 'н' and word.count('я') == 1:
                        counter += 1    
print(counter)
'''
'''
counter = 0
alph = 'егэ'
for a in 'еэ':
    for b in alph:
        for c in alph:
            for d in alph:
                for e in alph:
                    counter += 1
print(counter)
'''
'''
counter = 0
alph = 'игорь'
for a in 'игор':
    for b in alph:
        for c in alph:
            for d in alph:
                for e in alph:
                    for f in alph:
                        for g in alph:
                            for h in alph:
                                word = a + b + c + d + e + f + g + h
                                counterO = word.count('о')
                                counterb = word.count('ь')
                                if counterO == 1 and counterb == 1:
                                    counter += 1
print(counter)
'''
counter = 0
alph = 'матвей'
for a in 'матве':
    for b in alph:
        for c in alph:
            for d in alph:
                for e in alph:
                    for f in alph:
                        word = a + b + c + d + e + f
                        no = word.count('ае')
                        m = word.count('м')
                        z = word.count('а')
                        t = word.count('т')
                        v = word.count('в')
                        y = word.count('е')
                        i = word.count('й')
                        if m == 1 and z == 1 and t == 1 and v == 1 and y == 1 and i == 1 and no == 0:
                            counter += 1
print(counter)                
