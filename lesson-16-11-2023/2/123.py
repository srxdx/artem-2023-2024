alph = [0, 1]
print('x','y','z','w', 'F')
for x in alph:
    for y in alph:
        for z in alph:
            for w in alph:
                logic1 = (y <= x) and (z or w)
                logic2 = (x and (not w)) or (y == z)
                if (logic1 <= logic2) == False:
                    print(x,y,z,w)
