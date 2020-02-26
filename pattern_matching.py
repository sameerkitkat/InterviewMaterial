def pattern_matching(string,pattern):
    arr = list(string)
    pat = list(pattern)
    n = len(arr)
    m = len(pat)
    for i in range(0,n-m+1):
        for j in range (0,m):
            if arr[i+j] != pat[j]:
                return False
            if j == m-1 :
                return True

if __name__ == "__main__":
    string = "ABCABCD"
    pattern = "ABCE"
    if pattern_matching(string,pattern):
        print("Pattern matched")
    else:
        print("Pattern did not match")