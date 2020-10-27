import sys
n = int(sys.argv[1])
e = int(sys.argv[2])
sh = int(sys.argv[3])
print(n,e,sh)
d = 0

def evklid_algo(a,b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
        evklid_list = []
        evklid_list.append(a)
        evklid_list.append(b)
    return evklid_list

def primefactors(n):
    factorlist=[]
    loop=2
    while loop<=n:
        if n % loop == 0:
            n /= loop
            factorlist.append(loop)
        else:
            loop+=1
    return factorlist
p = primefactors(n)[0]
q = primefactors(n)[1]
print(p,q)
fi = (p - 1) * (q - 1)
print(fi)
print(evklid_algo(e,fi))
while True:
    if((((e * d) - 1) % fi) == 0):
        break
    else:
        d = d + 1
print(d)
answer = (sh ** d) % n
print("The encrypted element is ",answer)

