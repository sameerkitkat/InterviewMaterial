def count_primes(num):
    prime_list =  []
    if num <= 1:
        return 0
    elif num == 2:
        return 1
    elif num == 3:
        return 2 
    prime_list.append(2)
    prime_list.append(3)

    for i in range (4,num):
        is_prime = True
        for p in prime_list:
            m = i%p
            if m == 0:
                is_prime = False
                break
        if is_prime:
            prime_list.append(i)

    return prime_list

if __name__ == "__main__":
    print(count_primes(10))