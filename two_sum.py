def two_sum(target, lst):
    dct = {}
    for i in range(len(lst)):
        if lst[i] in dct:
            return [dct[lst[i]],i]
        else:
            dct[target-lst[i]]=i
    return -1
    
if __name__ == "__main__":
    lst = [1,2,3,4,5]
    target = 3
    print(two_sum(target,lst))
    