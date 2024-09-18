# str1 = 'Prasnna interviwing Jagdish, If Jagdish qualify He will be move to final round'


def sort_by_word(sentce):
    spt = sentce.split()
    for i in range(len(spt)):
        for j in range(i, len(spt)):
            if len(spt[i]) > len(spt[j]):
                spt[i], spt[j] = spt[j],spt[i]
    return ' '.join(spt)


str1 = 'Prasnna interviwing Jagdish, If Jagdish qualify He will be move to final round'
print(' '.join(sorted(str1.split(), key=len)))


if __name__ == "__main__":
    print(sort_by_word(str1))

