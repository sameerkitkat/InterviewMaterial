def ugly_number(num):
    if num <= 0:
        return False
    for i in [2,3,5]:
        while num % i == 0:
            num = num // i
    return num == 1  

if __name__ == "__main__":
    print(ugly_number(14))