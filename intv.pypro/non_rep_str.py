str1 = 'hello, world'

for i in str1:
    if i != ' ' and i.isascii():
        c = 0
        for j in str1:
            if i == j :
                c += 1
            if c>1:
                break
        if c == 1:
            print('this is non repeating charcter ',i)