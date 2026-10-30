def bre(compound:str)->list[tuple[str,int]]:
    stuf=[]
    curr=''
    count=0
    for i in compound:
        if i.isupper():
            if curr:
                stuf.append((curr,count if count else 1))
            count=0
            curr=i
        elif i.isdigit():
            count=10*count+int(i)
        else:
            curr+=i
    stuf.append((curr,count if count else 1))
    return stuf
print(bre("C6H12O6"))