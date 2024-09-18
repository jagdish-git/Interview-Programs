def count_vowel(strz):
    vowel = ['a','e','i','o','u']
    d = {}
    for i in strz:
        lower = i.lower()
        if lower in vowel:
            d[lower] = d.get(lower,0)+1
        elif lower == ' ':
            continue
        else:
            d[lower] = 0
    print(dict(sorted(d.items())))
    return dict(sorted(d.items(), key=lambda x:x[1], reverse=True))


string1 ='The World War Already On the Ground'
c = count_vowel(string1)
print(c)