def check_prime(number):
    arr = [1]
    if number <= 1:
        return f"{number} is not a prime number"
    for num in range(2, number+1):
        if (number % num == 0):
            arr.append(num)
    
    if len(arr) > 2:
        return f"{number} is not a prime number.\n{arr}"
    else:
        return f"{number} is a prime number."
        
print(check_prime(100))