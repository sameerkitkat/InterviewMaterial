def remove_duplicates_from_sorted_array(lst):
    j = 0
    for i in range(0,len(lst)-1):
        if lst[i]!=lst[i+1]:
            lst[j]=lst[i]
            j=j+1
    lst[j]=lst[len(lst)-1]
    j=j+1
    return j

if __name__ == "__main__":
    array =  [1,1,2,3,4,5,5]
    length = remove_duplicates_from_sorted_array(array)
    for i in range (0,length):
        print(array[i],end = " ")