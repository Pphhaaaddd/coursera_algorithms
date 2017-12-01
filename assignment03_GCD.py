#python3
#Find gcd of two numbers

def eucGcd(a,b):
    if(b==0):
        return a
    a_ = a%b
    return eucGcd(b,a_)


#Main
a = int(input())
b = int(input())

print ("GCD: ",eucGcd(a,b))
