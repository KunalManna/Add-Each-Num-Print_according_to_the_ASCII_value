#Input-1>  6442           Explanation: 6+4+4+2= 16   ASCII value of P is 16
#Output-> P                       Ans: P

#Input-2>  558823         Explanation: 5+5+8+8+2+3= 31  Since 31 > 26, Hence 3+1=4 ASCII value of D is 4
#Output->  D                      Ans: D


def AddEachNum(a):
    p=[int(i) for i in a]
    s1=sum(p)
    if s1>26:
        q=[int(i) for i in str(s1)]
        s2=sum(q)
        return chr(s2+64)
    else:
        return chr(s1+64)


a=input("Enter the number:\n")
ans=AddEachNum(a)
print(ans)
