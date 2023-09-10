# Print the number whose square is present in the List
x = [2,4,3,18,9,16]
emp = []
for i in x:
    if pow(i,2) in x: #i**2 
        emp.append(i)

print(emp)


# Print the number whose square root is present in the List

x = [2,4,3,18,9,16]
f = []
for i in x:
    if i**0.5 in x: # pow(i,0.5) / sqrt(i)
        f.append(i)
print(f)

