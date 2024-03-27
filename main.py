N = int(input(""))
for i in range(0,N):
    T = int(input())
    X = int(input())


list = []
list.append(abs(X))
list.sort(reverse=True)
return list[0] - list["N"]