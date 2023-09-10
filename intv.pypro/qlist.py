# 1
x = [1, 3, 5, 8]
y = [2, 4, 5, 8]

z = [k for k in y if k in x]
print(z)

for i in x:
    if i in y:
        print(i, end=' ')

# 2