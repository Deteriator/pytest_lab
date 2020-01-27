def fizzbuzz(num = 100):
    count = 0
    while count <= num:
        if count % 15 == 0:
            return "fizzbuzz"
        
        elif count % 3 == 0: 
            return "fizz"
        
        elif count % 5 == 0:
            return "buzz"
        
        else:
            return count
        
        count += 1

print(fizzbuzz(3))
