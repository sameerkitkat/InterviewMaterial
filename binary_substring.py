def binary_substring(string):
    count = 0
    for i in range (0,len(string)):
        if string[i] == '1':
            count= count + 1
    return count* (count- 1) // 2

if __name__ == "__main__":
    string = '110111'
    print("Number of substrings :",binary_substring(string))