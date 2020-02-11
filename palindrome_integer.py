def palindrome_integer(number):
    temp = number 
    reverse = 0
    while (number > 0):
        reverse = reverse * 10 + number % 10
        number = number // 10
    if temp == reverse:
        return True 
    return False

if __name__ == "__main__":
    print (palindrome_integer(121))