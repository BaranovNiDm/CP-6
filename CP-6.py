def CHODN(a):
    ab=[]
    for i in range(len(a)):
        if a[i] in b and a[i] not in ab:
            ab.append(int(a[i]))
    print(*ab)
print("введите длину первого массива")
lena=int(input())
print("введите длину второго массива")
lenb=int(input())
print("введите элементы первого массива через пробел")
a=[float(i) for i in input().split()]
print("введите элементы второго массива через пробел")
b=[float(i) for i in input().split()]
CHODN(a)
