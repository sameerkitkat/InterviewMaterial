def shift_zeros_to_end(lst):
    j = 0
    for i in range(0,len(lst)):
        if lst[i] != 0:
            lst[j] = lst[i]
            j = j + 1
    while (j < len(arr)):
        arr[j] = 0
        j = j + 1
    return j

if __name__ == "__main__":
    arr = [1,1,0,0,2,2,0,0,3,3,0,0]
    length = shift_zeros_to_end(arr)
    for i in range(length):
        print(arr[i])