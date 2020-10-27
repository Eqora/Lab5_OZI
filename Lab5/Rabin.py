import sys
N = int(sys.argv[1])
B = int(sys.argv[2])
sh = int(sys.argv[3])

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
p = primefactors(N)[0]
q = primefactors(N)[1]
print(p,q)

m1 = (sh ** ((p + 1) // 4)) % p
m2 = (-1 * (sh ** ((p + 1) // 4))) % p
m3 = (sh ** ((q + 1) // 4)) % q
m4 = (-1 * (sh ** ((q + 1) // 4))) % q


print(m1,m2,m3,m4)

def extEucl(m, n):
    (a, b) = (m, n)
    u1 = 1; v1 = 0
    u2 = 0; v2 = 1

    while b != 0:
        assert (a == u1*m + v1*n and b == u2*m + v2*n)

        q = a // b; r = a % b
        assert (a == q*b + r)

        (a, b) = (b, r)
        (u1, u2) = (u2, u1 - q*u2)
        (v1, v2) = (v2, v1 - q*v2)

    if a >= 0:
        itog = []
        itog.append(a)
        itog.append(u1)
        itog.append(v1)
    else:
        itog = []
        itog.append(-a)
        itog.append(-u1)
        itog.append(-v1)
    return itog
print(extEucl(p,q))

yp = extEucl(p,q)[1]
yq = extEucl(p,q)[2]
mp = sh ** ((1/4) * (p + 1)) % p
mq = sh ** ((1/4) * (q + 1)) % q
mp = int(mp)
mq = int(mq)
print(mp,mq,yp,yq)

r = ((yp * p * mq) + (yq * q * mp)) % N
r2 = N - r
s = ((yp * p * mq) - (yq * q * mp)) % N
s2 = N - s
r = int(r)
r2 = int(r2)
s = int(s)
s2 = int(s2)
print(r,r2,s,s2)