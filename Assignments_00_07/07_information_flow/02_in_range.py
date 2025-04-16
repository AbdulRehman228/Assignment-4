def in_range(n, low, high):
    """Returns True if n is between low and high, inclusive."""
    return low <= n <= high

def main():
    # Example usage
    n = int(input("Enter a number: "))
    low = int(input("Enter the lower bound: "))
    high = int(input("Enter the upper bound: "))
    
    print(in_range(n, low, high))

if __name__ == "__main__":
    main()
    