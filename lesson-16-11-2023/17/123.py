
maxEl = -1000000
counter = 0
max2 = -1000000000
addNums = []

file = open('17.txt')
for i in file:
    addNums.append(int(i))
#print(addNums)

for i in addNums:
    if abs(i) % 10 == 3 and i > maxEl:
        maxEl = i
        #maxEl = max(maxEl, i)
print('Макс числ на 3',maxEl)
Max2 = maxEl ** 2
print('Максимальный квадрат', Max2)


for x in range(len(addNums)-1):
    countNumber = 0
    if abs(addNums[x]) % 10 == 3:
        countNumber += 1
    if abs(addNums[x+1]) % 10 == 3:
        countNumber += 1
    summ = (addNums[x] ** 2) + (addNums[x+1] ** 2)
    #print(addNums[x], addNums[x+1], summ,countNumber)
    if countNumber == 1 and summ >= Max2:
        counter += 1
        max2 = max(max2, summ)
    
print(counter, max2)

