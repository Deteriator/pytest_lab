def fizzbuzz(num):
    if num == 0:
        return 0
    elif num % 15 == 0:
        return "fizzbuzz"
        
    elif num % 3 == 0: 
        return "fizz"
        
    elif num % 5 == 0:
        return "buzz"
        
    else:
        return num
        

print(fizzbuzz(10))
