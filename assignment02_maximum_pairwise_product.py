#python3
n = int(input())
a = [int(x) for x in input().split()]
assert(len(a) == n)

m1 = 0
m2 = 0

#find maximums
for x in a:
    if x > m2:
        if x >= m1:
            m1, m2 = x, m1
        else:
            m2 = x

print(m1*m2)
