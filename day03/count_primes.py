from is_prime import is_prime

def count_prime_upto(n):
    """Gives the count of primes until the given number"""
    
    ctr = 0
    for number in range(1,n+1):
        if is_prime(number):
            ctr+=1

    return ctr

        
        

if __name__ == "__main__":

    n = int(input("Enter a range to find the no of primes until that range:"))
    print(count_prime_upto(n))

