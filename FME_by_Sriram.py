#Sriram's version of Fast Modular Exponentiation: a is the exponent, b is the base/modulus, and n is the number 

def FME (a, n ,b):
    result = 1      #note initial value must be a positive int
    sq = a
    while(n > 0):
        k = n % 2
        if k == 1:      #if k is equivalent to 1 (as opposed to 0), then we know the current exponent has an impact 
            result = (result * sq) % b        #...and we update the result with the exoponent 
        sq = (sq * sq) % b        #this line is the "squaring" part of exponentiation by squaring
        n = n // 2      #this line is necessay for n to reach 0
    return result 