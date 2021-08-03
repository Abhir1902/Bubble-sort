n=int(input())
l=[]
for i in range(n):
    l.append(int(input()))
m=int(input())
a=len(l)
if m==0:
    def bub(l):
        for i in range(0,a-1):
            for j in range(0,a-i-1):
                if l[j]>l[j+1]:
                    l[j],l[j+1]=l[j+1],l[j]
            print(l)
        return(l)
    print(bub(l))
