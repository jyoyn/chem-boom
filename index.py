def bre(compound:str)->list:
    s=[]
    c=''
    n=0
    for i in compound:
        if i=="(":
            if c:
                s.append((c,n if n else 1))
                c=''
                n=0
            s.append(i)
        elif i==")":
            s.append((c,n if n else 1))
            n=0
            c=[]
            while s[-1]!="(":
                c.insert(0,s.pop())
            c=tuple(c)
            s.pop()
        elif i.isupper():
            if c:
                s.append((c,n if n else 1))
                n=0
            c=i
        elif i.isdigit():
            n=n*10+int(i)
        else:
            c+=i
        print(s,c)
    s.append((c,n if n else 1))
    return s
print(bre("(Al(OH)3)2"))