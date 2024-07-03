def EU (a, b):
    if (a < 0 or b < 0):
        print("invalid input; vales must be greater that or equal to 0")
        return
    
    x = a
    y = b 
    while (y != 0):
        r = x % y
        x = y
        y = r
        
    return x



gcd1 = input("Enter your first value: ") 
integ1 = int(gcd1)
gcd2 = input("Entes yous second value: ")
integ2 = int(gcd2)
mega = EU(integ1, integ2) 
print(mega)
