import sys

def main():
    arguments = sys.argv[1:]  # Get command-line arguments, excluding the script name
    total = 0
    
    for arg in arguments:
        try:
            # Convert the argument to an integer and add it to the total
            num = int(arg)
            total += num
        except ValueError:
            # If the argument is not an integer, skip it
            pass
    
    print("Sum of integers:", total)

if __name__ == "__main__":
    main()
