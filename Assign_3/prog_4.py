def combinations(l):
    for i in range(len(l)-1):
        for j in l[i]:
            for k in l[i+1]:
                print(j+k)

disc={}
# disc= {'1':['a','b','c'], '2':['d','e','f'],'3':['g','h','i']}
key=0
while inp := input('enter comma seperated list of letters(Press Enter to Exit): '):
    key +=1
    disc[key] = inp.split(',')

print(disc)

print("The combiantions are:")
combinations(list(disc.values()))


