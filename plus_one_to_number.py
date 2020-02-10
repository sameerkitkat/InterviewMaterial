def plus_one(number):
    for i in range(len(number)-1,-1,-1):
        if number[i] < 9:
            number[i] += 1
            return number
        number[i]=0
        n = len(number) + 1
        ans = [0] * n
        ans[0] = 1
    return ans
    
if __name__ == "__main__":
    number = [9,9,9]
    print(plus_one(number))