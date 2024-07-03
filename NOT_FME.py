#Functions

#This is the ultra slow, NOT FME function for the MW. Note that a is the number, n is the exponent, and m is the modulus
from re import M


def notFME (a, n ,m):
    result = a ** n
    mod_result = result %  m 
    print(mod_result)
    return mod_result


#This is FME using python's built in pow() function. Note that a is the number, n is the exponent, and m is the modulus
def powFME (a, n, m):
    result = pow(a,n,m)
    print(result)
    return result



z = 2
x = 50011111
y = 6

notFME(z, x, y)

powFME(z, x, y)
