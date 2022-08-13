
def fibonacci_iterative(number) : 
    '''
    Return The calculated position of fibonacci
    
    Parameters
       number (int): position number
    
    Returns
       The calculated position of fibonacci
    '''
    
    current = 1
    previous = 0
    result = 0
    
    for _ in range(number - 1):
        result = current + previous
        previous = current
        current = result
    return result

def main():
    print("Type a number:")
    number = int(input())
    resultado = fibonacci_iterative(number)
    print("Sequence of fibonacci is: " + str(resultado))

if __name__ == "__main__":
    main()