def add_binary_strings(s1,s2):
    carry = 0
    result = ''

    s1 = list(s1)
    s2 = list(s2)

    while s1 or s2 or carry:
        if s1 :
            carry += int(s1.pop())
        if s2 :
            carry += int(s2.pop())
        result += str(carry%2)
        carry //= 2

    return result[::-1]

if __name__ == "__main__":
    s1 = "11"
    s2 = "1"
    print("Adition of binary string is : {0}".format(add_binary_strings(s1,s2)))