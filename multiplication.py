BASE = 10 #base (binary, octal, base 10)

def multiplication(x, y):
    #find digit number
    digit_number = max(len(str(int(x))) , len(str(int(y))))
        
    if digit_number == 1:
        return x*y
    else:
        m = digit_number//2
        
        x1 = x//(BASE**m)
        x0 = x % (BASE**m)
        y1 = y//(BASE**m)
        y0 = y % (BASE**m)
        
        x1y1 = multiplication(x1, y1)
        x1y0 = multiplication(x1, y0)
        x0y1 = multiplication(x0, y1)
        x0y0 = multiplication(x0, y0)

        return x1y1 * BASE**(2*m) + (x1y0 + x0y1) * BASE**(m) + x0y0

def main():
    print (multiplication(40, 30))
 
    
if __name__ == "__main__":
    main() 