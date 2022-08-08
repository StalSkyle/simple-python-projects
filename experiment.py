'''
can you guess what will be the output of this code?
python creates recursed infinite list, where m[1] is the same thing as m

(spoiler) the output is m[0], m[1], m[1][0], m[1][1], m[1][2], m[2]
'''
m = [0, [None], 1]
m[1] = m
for i in range(len(m)):
    print(m[i])
    if i==1:
        for j in range(len(m[i])):
            print(m[i][j])
