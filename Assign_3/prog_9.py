inp_str=input("Enter a string: ")

disc={}
for i in inp_str:
    if i not in disc and inp_str.count(i)>=2:
        
        disc[i]=inp_str.count(i)
        # print(f"{inp_str.count(i)} {i}")

disc=dict(sorted(disc.items(),key=lambda elem:elem[1],reverse=True))
for k,v in disc.items():
    print(k,v)