def reverse_integer(number):
    reverse = 0 
    while(number > 0):
        reverse = reverse * 10 + number % 10
        number = number // 10
    return reverse

if __name__ == "__main__":
    number = 123
    print(reverse_integer(number))