# palindrome number

def palindrome(number):
    if number == 0:
        return 0
    temp = number
    res = 0
    while temp > 0:
        res = res*10 + temp%10
        temp //= 10
    return True if res == number else False


if __name__ == "__main__":
    testcases = [10101, 2314321, 11022, 98989, 7007]
    for number in testcases:
        print(palindrome(number))