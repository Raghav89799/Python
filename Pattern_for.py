# Pattern 01

for i in range(1,11):
    for j in range(i):
        print("*",end="")
    print("\n")

# Pattern 02

for i in range(1,11):
    for j in range(1,i+1):
        print(j,end="")
    print("\n")

# Pattern 03

for i in range(1,11):
    for j in range(i):
        print(i,end="")
    print("\n")

# Pattern 04

k = 11
for i in range(1,11):
    a = 10
    for j in range(1,k):
        print(a,end="")
        a -= 1
    k -= 1
    print("\n")

# Patten 05

k = 11
for i in range(1,11):
    a = 10
    for j in range(1,k):
        print("*",end="")
        a -= 1
    k -= 1
    print("\n")

# Pattern 06

b = 0
k = 1
for i in range(1,11):
    a = 10 - b
    for j in range(k,11):
        print(a,end="")
        a -= 1
    b += 1
    k += 1
    print("\n")


