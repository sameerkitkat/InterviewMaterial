def palindrome_string(s):
    i = 0
    j = len(s)-1
    while (i<=j):
        if s[i] != s[j]:
            return False
        i=i+1
        j=j-1
    return True

if __name__ == "__main__":
    print(palindrome_string('abbacabba'))