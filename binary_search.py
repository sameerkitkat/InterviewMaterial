def binary_search(lst, number):
    left = 0
    right = len(lst)-1

    while(left <= right):
        mid = (left + right)//2
        if number == lst[mid]:
            return mid 
        elif number > lst[mid]:
            left = mid + 1
        else:
            right = mid - 1
    return -1

if __name__ == "__main__":
    array = [1,2,3,4,5]
    number =  3
    index = binary_search(array,number)
    print ("Element found at : {0}".format(index))