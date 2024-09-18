import math

#>>1
print(math.lcm(24,30))


#>>2
num1 = 12
num2 = 14

for i in range(max(num1, num2), 1 + (num1 * num2)):
    if i % num1 == i % num2 == 0:
        lcm = i
        break

print("LCM of", num1, "and", num2, "is", lcm)

#>>3
def getHCF(a, b):
    if b == 0:
        return a
    else:
        return getHCF(b, a % b)


num11 = 12
num22 = 14
hcf = getHCF(num11, num22)

# LCM formula
lcm = (num11 * num22) // hcf
print("The hcf is :", lcm)

