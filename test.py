lst = [4,-2,7,-12,65,33,1,-89,-34,76,-3,2,-1]
x = sorted(lst)
n = []
p = []
for _ in x:
    if _ > 0:
        p.append(_)
    else:
        n.append(_)
res = []
for i,j in zip(n,p):
    res.append(i)
    res.append(j)
print(res)

# [1, 2, 4, 7, 33, 65, 76] [-89, -34, -12, -3, -2, -1]
# [-89,1,-34,2,-12,4]
# [[-89, 1], [-34, 2], [-12, 4], [-3, 7], [-2, 33], [-1, 65]]




# prime number in between 100, 200
li = []
for i in range(100,200):
    for j in range(2,i):
        if i % j == 0:
            break
    else:
        li.append(i)
# print(li) 

# [101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]