############## PROBLEM STATEMENT ##############3
# https://www.codewars.com/kata/544aed4c4a30184e960010f4

def divisors(integer):
    
    divisors = []
    
    divisor = 2
    
    while divisor *2 <= integer:
        if integer % divisor == 0:
            
            divisors.append(divisor)
            
        divisor += 1
        
    if len(divisors):
        
        return divisors
    
    else:
        return f"{integer} is prime"

        

# The logic simple test numbers if the given integer is multiple of them, to make it efficient we are only going up to N/2, as N/2 is the largest divisor of any number N
            
            