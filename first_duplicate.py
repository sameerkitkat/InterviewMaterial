def find_first_duplicate(lst):
    my_set = dict()
    Min = -1
    if len(lst) < 2:
        return -1
    else:
        for i in range(len(lst)-1,-1,-1):
                if lst[i] in my_set.keys():
                    Min = i
                else:
                    my_set[lst[i]] = 1
        return lst[Min]
    return -1

if __name__ == "__main__":
    arr = [10, 5, 3, 4, 3, 5, 6] 
    print("First duplicate number is :",find_first_duplicate(arr))