def remove_given_element(lst, element):
    j = 0
    for i in range(0,len(lst)):
        if lst[i] != element:
            lst[j] = lst[i]
            j = j + 1
    return j

if __name__ == "__main__":
    arr = [1,2,3,4,5]
    length = remove_given_element(arr,3)
    for i in range(length):
        print(arr[i], end = " ")