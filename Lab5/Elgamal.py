P = 509
g = 2
sk = a = 279
A = (g ** a) % P
osk = 375
print(A)
pk = (P, g, A)
print(pk)
m = 501
k = A
c1 = (g ** k) % P
c2 = (m * (A ** k) % P)
print(c1,c2)
print(a)
x = (c1 ** a) % P
print(x)

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


print(extEucl(x,P))
lamb = extEucl(x,P)[1]
nyu = extEucl(x,P)[2]

reverse_x = lamb % P
print(reverse_x)

msg = (reverse_x * c2) % P
print(msg)