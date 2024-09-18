# input: "hello world"
# output: "d1r1w1o2l3e1h1"

def count_str_rev(string):
    d = {}
    res = ''
    for i in string:
        d[i] = d.get(i,0)+ 1
    for k in d.keys():
        if k != ' ':
            res = k + str(d[k]) + res
    return res

s = "hello world"
print(count_str_rev(s))