def func():
    f = open('write3.txt', 'r')
    data = f.readline()
    while data != '':
        print(data)
        data = f.readline()      
    f.close()

#func()



f = open('write3.txt', 'r')
data = f.read()
datas = data.split()
print(len(datas))

n = 0
with open('write3.txt', 'r') as f:
    for i in f:
        spl = i.split()
        n = n + 1
print(n)


def fun(x = 'Programs'):
    c = 0
    with open('write3.txt', 'r') as f:
        for i in f.read().split():
            if i == x:
                c = c+1
    return c

print(fun())



def fun2():
    with open('write3.txt','r') as f1:
        with open('writenew24.txt', 'w') as f2:
            f2.writelines(f1.read())

fun2()



l = input("Enter letter to be searched:")
k = 0

with open('write3.txt', 'r') as f:
    for line in f:
        words = line.split()
        for i in words:
            for letter in i:
                if (letter == l):
                    k = k + 1
print("Occurrences of the letter:")
print(k)





def func2():
    with open('writenew2.txt', 'r') as f:
        for i in f:
            words = i.split()
            for j in words:
                for k in j:
                    if k.isdigit():
                        print(k, end=' ')   

func2()




