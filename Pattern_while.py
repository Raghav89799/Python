# Pattern 01

i = 2
while i < 11:
    j = 1
    while j < i:
        print("*",end="")
        j += 1
    i += 1
    print("\n")

# # Pattern 02

i = 2
while i < 12:
    j = 1
    while j < i:
        print(j,end="")
        j += 1
    i += 1
    print("\n")

# # Pattern 03

i = 1
while i < 11:
    j = 0
    while j < i:
        print(i,end="")
        j += 1
    i += 1
    print("\n")

# # Pattern 04
i = 2
k = 11
while i < 12:
    a = 10
    j = 1
    while j < k:
        print(a,end="")
        a -= 1
        j += 1
    k -= 1
    i += 1
    print("\n")

# # Patten 05

i = 2
k = 11
while i < 12:
    a = 10
    j = 1
    while j < k:
        print("*",end="")
        a -= 1
        j += 1
    k -= 1
    i += 1
    print("\n")

# # Pattern 06

n = 0
b = 0
i = 2
while i < 12:
    a = 10 - b
    k = 1 + n
    while k < 11:
        print(a,end="")
        a -= 1
        k += 1
    i += 1
    b += 1
    n += 1
    print("\n")


