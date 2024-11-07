a1 = input()
a2 = int(input())
i = ["", "a", "b", "c", "d", "e", "f", "g", "h"]
if a1 in i:
    if i.index(a1) % 2 == 0 and a2 % 2 == 0:
        print("YES")
    else:
        print("n")
