#for printing the lines in a file line by line:

f=open('messages','r')

for i in f:
    print(i,end='')