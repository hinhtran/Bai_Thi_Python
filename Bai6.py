import math
def isPrimeNumber(n):
    if (n < 2):
        return False;
 
    squareRoot = int(math.sqrt(n));
    for i in range(2, squareRoot + 1): # n > 2 
        if (n % i == 0):
            return False;
    return True;
 
print ("All số nguyên tố có 5 chữ số:");
dem = 0;
for i in range(10001, 99999):
    if (isPrimeNumber(i)):
        print(i);
        dem = dem + 1;
print("Sum số nguyên tố có 5 chữ số là:", dem);
