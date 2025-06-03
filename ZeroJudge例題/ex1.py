num = input().split()
list.sort(num)
a = int(num[0])
b = int(num[1])
c = int(num[2])
if a+b <= c:
    print("NO")
if a**2+b**2 < c**2 :
    print("Obtuse")
if a**2+b**2 == c**2 :
    print("Right")
if a**2+b**2 > c**2 :
    print("Acute")