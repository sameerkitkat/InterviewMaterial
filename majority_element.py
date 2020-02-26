def majority_element(arr):
    dct = {}
    for i in range (0,len(arr)):
        if arr[i] in dct.keys():
            dct[arr[i]]+=1
        else:
            dct[arr[i]]=1
    print (dct)
    
    for k,v in dct.items():
        if v > len(arr)//2:
            return k
        else:
            return -1

if __name__ == "__main__":
    arr = [2, 2, 2, 2, 5, 5, 2, 3, 3]
    print("Majority Element is :",majority_element(arr))