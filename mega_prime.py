def isprime(n):
    c=0
    for i in range(1,n+1):
        if(n%i==0):
            c=c+1
    if(c==2):
        return True
    else:
        return False
n=int(input())
s=str(n)
l=[]
if isprime(n):
    for i in s:
        if not (isprime(int(i))):
            l.append('0')
        else:
            l.append('1')
    if '0' in l:
        print('Not Mega Prime')
    else:
        print('Mega Prime')
else:
    print('Not Mega Prime')