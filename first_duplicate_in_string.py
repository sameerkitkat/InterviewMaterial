def get_count_array(s):
    count = [0] * 256
    for i in s:
        count[ord(i)]+=1
    return count 

def find_first_duplicate(s):
    count_array = get_count_array(s)
    for i in s:
        if count_array[ord(i)] == 1:
            return i
    return -1


if __name__ == "__main__":
    s = "geeksforgeeks"
    print("First non repeating character is {0}".format(find_first_duplicate(s)))